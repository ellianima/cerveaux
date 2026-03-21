# 🌐 Putting It All Together — The Complete Web Request Journey

> **Source:** TryHackMe — How The Web Works Module
> **Purpose:** Full-stack web infrastructure for cybersecurity & pentesting
> **Covers:** DNS, Load Balancers, CDN, WAF, Web Servers, Static vs Dynamic,
> Backend Languages, Virtual Hosts

---

## 🧒 Feynman Explanation — What Happens When You Visit a Website?

Imagine you want a pizza from a famous restaurant chain.

1. You look up their address in a phonebook (**DNS**)
2. Your request goes through a security guard at the door (**WAF**)
3. The guard directs you to the least busy counter (**Load Balancer**)
4. The counter staff take your order (**Web Server**)
5. They go to the kitchen's ingredients storage (**Database**)
6. They cook your pizza and hand it back (**Response**)
7. You eat it (**Browser renders HTML**)

The whole trip — from typing a URL to seeing a webpage —
takes less than **300 milliseconds**. That is the internet.

---

## 🔷 1. The Full Web Request Journey (End-to-End)

```
STEP 1  → You type tryhackme.com in your browser

STEP 2  → Check LOCAL CACHE (do I already know the IP?)
            └─ Yes → skip to Step 5
            └─ No  → continue

STEP 3  → Ask your RECURSIVE DNS SERVER (your ISP's DNS)
            └─ Knows it → returns IP, skip to Step 5
            └─ Doesn't know → continue

STEP 4  → Recursive DNS queries ROOT DNS SERVER
            └─ Root says "ask the .com authoritative server"
            └─ Authoritative DNS server returns the IP address
            └─ IP cached locally for next time

STEP 5  → Request passes through WAF
            (Web Application Firewall — is this a legit request?)

STEP 6  → Request passes through LOAD BALANCER
            (which server is least busy right now?)

STEP 7  → Connect to WEB SERVER on port 80 (HTTP) or 443 (HTTPS)

STEP 8  → Web server receives the GET request
            (Apache/Nginx/IIS processes it)

STEP 9  → Web Application talks to DATABASE if needed
            (MySQL/PostgreSQL/MongoDB returns data)

STEP 10 → Server sends back HTML/CSS/JS response

STEP 11 → Your browser RENDERS the HTML into a visible webpage
```

### 💻 See This Happening Live (Terminal Commands)

```bash
# Step 1-4: Trace the full DNS resolution path
dig tryhackme.com +trace

# See which DNS server your system uses
cat /etc/resolv.conf

# Check if IP is in local DNS cache (Windows)
ipconfig /displaydns

# Steps 5-8: Make a raw HTTP request and see the server response
curl -v http://tryhackme.com

# See the full headers (reveals server software, WAF presence)
curl -I https://tryhackme.com

# Trace the network path to the server
traceroute tryhackme.com      # Linux/Mac
tracert tryhackme.com         # Windows

# See the TCP connection being made
netstat -an | grep :443
```

---

## 🔷 2. DNS — The Internet's Phonebook

### 🧒 Feynman Explanation

You don't memorize every phone number — you look names up in your
contacts. DNS is the internet's contacts app. You type
`tryhackme.com` (the name) and DNS translates it to
`104.26.10.229` (the phone number / IP address).

### DNS Resolution Chain

```
Your Browser
     │
     ▼
Local Cache ──── found? ──────────────────────────────▶ Use IP
     │
     │ not found
     ▼
Recursive DNS Server (your ISP)
     │
     │ not found
     ▼
Root DNS Server (.)
     │ "ask .com TLD server"
     ▼
TLD DNS Server (.com)
     │ "ask tryhackme's authoritative server"
     ▼
Authoritative DNS Server
     │ "the IP is 104.26.10.229"
     ▼
IP returned to browser → connection made
```

### DNS Record Types (Know All of These)

| Record    | Purpose                       | Example                              |
| --------- | ----------------------------- | ------------------------------------ |
| **A**     | Domain → IPv4 address         | `tryhackme.com → 104.26.10.229`      |
| **AAAA**  | Domain → IPv6 address         | `tryhackme.com → 2606:4700::...`     |
| **CNAME** | Domain → another domain       | `www.tryhackme.com → tryhackme.com`  |
| **MX**    | Mail server for domain        | `tryhackme.com → mail.tryhackme.com` |
| **TXT**   | Text info (SPF, verification) | `"v=spf1 include:..."`               |
| **NS**    | Name servers for domain       | `ns1.cloudflare.com`                 |
| **PTR**   | IP → domain (reverse DNS)     | `104.26.10.229 → tryhackme.com`      |

### 💻 DNS Recon (Pentester Must-Know)

```bash
# Basic lookup
nslookup tryhackme.com
dig tryhackme.com

# Get ALL record types
dig tryhackme.com ANY

# Reverse DNS lookup (IP → domain)
dig -x 104.26.10.229

# Find mail servers
dig tryhackme.com MX

# Find name servers
dig tryhackme.com NS

# Zone transfer attempt (misconfig = gold for attacker)
dig axfr @ns1.tryhackme.com tryhackme.com
# If successful → dumps ALL DNS records → massive recon win

# Subdomain brute force
gobuster dns -d tryhackme.com -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```

> ⚠️ **Security note:** DNS Zone Transfers (`AXFR`) that are
> publicly accessible leak your entire internal DNS map to
> attackers. This is a critical misconfiguration — always test for it.

---

## 🔷 3. Load Balancers

### 🧒 Feynman Explanation

Imagine a supermarket with 10 checkout counters but only one
entrance. A staff member at the door (the **load balancer**)
looks at which counter has the shortest queue and sends you there.
If one counter breaks down, they stop sending people to it.
Everyone still gets served — nobody notices the broken counter.

### How Load Balancers Work

```
Client Request
      │
      ▼
┌─────────────────┐
│  LOAD BALANCER  │  ← receives ALL requests first
└────────┬────────┘
         │
    ┌────┴─────┐
    │ Algorithm│
    └────┬─────┘
    ┌────┴──────────────┐
    │                   │
    ▼                   ▼
Server 1           Server 2           Server 3
(handling          (least busy        (on health
 5 requests)        → gets next)       check fail
                                       → skipped)
```

### Load Balancing Algorithms

| Algorithm             | How It Works                                      | Best For            |
| --------------------- | ------------------------------------------------- | ------------------- |
| **Round-Robin**       | Sends each request to the next server in rotation | Equal-spec servers  |
| **Weighted**          | Sends more traffic to more powerful servers       | Mixed-spec servers  |
| **Least Connections** | Sends to server with fewest active connections    | Long-lived sessions |
| **IP Hash**           | Same client IP always goes to same server         | Session persistence |

### Health Checks

```
Load balancer pings each server every N seconds:
  ✅ Server responds correctly → continues receiving traffic
  ❌ Server doesn't respond    → removed from rotation
  ✅ Server recovers           → added back automatically

This is how Netflix/Google/Facebook achieve 99.99% uptime.
```

> ⚠️ **Security/Pentest note:** Load balancers can cause
> inconsistent pentesting results — you might hit server A
> on one request and server B on the next. One server may be
> patched, the other not. Always test multiple times and
> note if responses differ between requests.

---

## 🔷 4. CDN — Content Delivery Network

### 🧒 Feynman Explanation

If a pizza shop in New York wants to serve customers in Manila,
the pizza takes forever to arrive. So instead, they set up
mini-kitchens all over the world that store pre-made pizza
(static content). When you order, you get served from the
nearest mini-kitchen — not New York. That's a CDN.

### What a CDN Does

```
WITHOUT CDN:                     WITH CDN:
User in Manila                   User in Manila
      │                                │
      │ (request)                      │ (request)
      ▼                                ▼
Server in USA                  CDN Server in Singapore
(high latency,                 (low latency, 20ms vs 300ms)
 slow load time)               (same file served from nearby)
```

### What CDNs Cache (Static Content)

```
✅ JavaScript files (.js)
✅ CSS stylesheets (.css)
✅ Images (.jpg, .png, .gif, .webp)
✅ Videos (.mp4, .webm)
✅ Fonts (.woff, .ttf)
✅ Static HTML pages
❌ Dynamic content (database results, user-specific pages)
```

### Popular CDNs

```
Cloudflare    — most common, also acts as WAF
AWS CloudFront
Akamai
Fastly
Azure CDN
```

> ⚠️ **Pentest note:** CDNs hide the real server IP address.
> If you're doing recon and only get a Cloudflare IP, the
> actual origin server is hidden. Techniques to bypass:
> historical DNS records (SecurityTrails), direct IP scanning,
> misconfigured subdomains that bypass CDN.

---

## 🔷 5. WAF — Web Application Firewall

### 🧒 Feynman Explanation

A bouncer at a nightclub checks everyone at the door:
"Are you on the guest list? Do you have a weapon?
Are you drunk and going to cause trouble?"
A WAF does the same for web requests — it checks every HTTP
request before it reaches the server and blocks anything
that looks like an attack.

### What a WAF Does

```
Client Request
      │
      ▼
┌───────────────────────────────────────┐
│           W  A  F                     │
│                                       │
│  Checks for:                          │
│  ├── SQL injection patterns           │
│  ├── XSS payloads                     │
│  ├── Bot signatures                   │
│  ├── Rate limiting (too many requests)│
│  ├── Known malicious IPs              │
│  └── Abnormal request patterns        │
│                                       │
│  ALLOW → passes to web server         │
│  BLOCK → dropped, 403/429 returned    │
└───────────────────────────────────────┘
      │
      ▼ (only clean requests reach here)
   Web Server
```

### WAF vs Firewall vs IDS

| Device       | Operates At            | Inspects              | Blocks                   |
| ------------ | ---------------------- | --------------------- | ------------------------ |
| **Firewall** | Network layer (L3/L4)  | IPs, ports, protocols | IP/port-based traffic    |
| **IDS**      | Network/host layer     | Packet patterns       | Alerts only (no block)   |
| **IPS**      | Network/host layer     | Packet patterns       | Blocks malicious traffic |
| **WAF**      | Application layer (L7) | HTTP request content  | Web attack payloads      |

> ⚠️ **Pentest note:** WAF bypass is a real skill.
> Common techniques: encoding payloads (URL, base64, hex),
> case variation (`SeLeCt` instead of `SELECT`),
> adding comments (`SEL/**/ECT`), using less common
> HTTP methods, or finding paths that bypass the WAF entirely.

---

## 🔷 6. Web Servers

### 🧒 Feynman Explanation

A web server is like a librarian. When you ask for book
"index.html", it goes to the shelf (file system), finds the
file, and hands it to you. Simple. It also knows the
library's floor plan — where each section (directory) is.

### Most Common Web Servers

| Server     | Usage          | Default Root (Linux) | Default Root (Windows) |
| ---------- | -------------- | -------------------- | ---------------------- |
| **Apache** | ~31% of web    | `/var/www/html`      | N/A                    |
| **Nginx**  | ~34% of web    | `/var/www/html`      | N/A                    |
| **IIS**    | ~8% of web     | N/A                  | `C:\inetpub\wwwroot`   |
| **NodeJS** | Developer apps | Configured in code   | Configured in code     |

### Virtual Hosts — One Server, Many Websites

```
One physical server → many websites via virtual hosts

HTTP Header: "Host: one.com"   → serves /var/www/website_one
HTTP Header: "Host: two.com"   → serves /var/www/website_two
HTTP Header: "Host: ???"       → serves default site

Config example (Nginx):
server {
    listen 80;
    server_name one.com;
    root /var/www/website_one;
}

server {
    listen 80;
    server_name two.com;
    root /var/www/website_two;
}
```

> ⚠️ **Pentest note:** Virtual host discovery is a critical
> recon technique. A server at IP `10.10.10.1` might host
> `admin.company.com` that doesn't appear in public DNS.
> Always enumerate virtual hosts during pentests.

### 💻 Virtual Host Discovery

```bash
# Brute force virtual hosts with gobuster
gobuster vhost -u http://10.10.10.1 \
  -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt

# Manually test a specific vhost
curl -H "Host: admin.target.com" http://10.10.10.1

# With ffuf
ffuf -w subdomains.txt -u http://10.10.10.1 \
  -H "Host: FUZZ.target.com" -fs 0
```

---

## 🔷 7. Databases

### Common Databases in Web Apps

| Database       | Type              | Common In          | Attack Vector       |
| -------------- | ----------------- | ------------------ | ------------------- |
| **MySQL**      | Relational (SQL)  | PHP/WordPress apps | SQL Injection       |
| **MSSQL**      | Relational (SQL)  | .NET/Windows apps  | SQL Injection       |
| **PostgreSQL** | Relational (SQL)  | Python/Django apps | SQL Injection       |
| **MongoDB**    | NoSQL (document)  | Node.js apps       | NoSQL Injection     |
| **SQLite**     | Relational (file) | Small apps, mobile | SQL Injection       |
| **Redis**      | Key-value (cache) | Session storage    | Unauthorized access |

> ⚠️ **SQL Injection is the #1 database attack.** It occurs
> when user input is directly inserted into SQL queries.
> Every database in the table above is vulnerable if the
> developer doesn't use parameterized queries.

### SQL Injection Preview

```sql
-- Vulnerable PHP query
$query = "SELECT * FROM users WHERE username='$username'";

-- Normal input:  username = "admin"
SELECT * FROM users WHERE username='admin'

-- Attack input:  username = "' OR '1'='1'--"
SELECT * FROM users WHERE username='' OR '1'='1'--'
-- Result: returns ALL users → authentication bypass!

-- Attack input (data extraction):
username = "' UNION SELECT username,password FROM users--"
SELECT * FROM users WHERE username=''
UNION SELECT username,password FROM users--'
-- Result: dumps username + password from users table!
```

---

## 🔷 8. Static vs Dynamic Content

### Comparison

| Type        | Content               | Changes?                         | Processed By        | Examples                               |
| ----------- | --------------------- | -------------------------------- | ------------------- | -------------------------------------- |
| **Static**  | Fixed files           | Never (until manually updated)   | Web server directly | Images, CSS, JS, fixed HTML            |
| **Dynamic** | Generated per request | Yes — changes based on user/data | Backend language    | Blog feeds, search results, dashboards |

### Static vs Dynamic — What You Can See

```
STATIC:
  Client sees: <html><body>Hello World</body></html>
  Source shows: exactly what's on disk — nothing hidden

DYNAMIC (PHP example):
  URL: http://example.com/index.php?name=adam

  Server-side PHP (YOU CANNOT SEE THIS):
  <html><body>Hello <?php echo $_GET["name"]; ?></body></html>

  Client receives (what YOU see in source):
  <html><body>Hello adam</body></html>

  The PHP code is gone — executed on the server
  Only its OUTPUT reaches the client
```

> ⚠️ **Security insight:** Dynamic content creates security
> risks because user input interacts with server-side code.
> `$_GET["name"]` takes input directly from the URL — if
> that input isn't sanitized, it opens the door to injection
> attacks. The client never sees the backend code — which is
> why backend bugs are harder to find but far more damaging.

### Backend Languages & Their Attack Surfaces

| Language   | Common Framework   | Common Vuln                 | Attack Tool    |
| ---------- | ------------------ | --------------------------- | -------------- |
| **PHP**    | WordPress, Laravel | LFI, RFI, SQLi, RCE         | sqlmap, Burp   |
| **Python** | Django, Flask      | SSTI, SQLi, Deserialization | tplmap, sqlmap |
| **Ruby**   | Rails              | SSTI, Mass Assignment       | Metasploit     |
| **NodeJS** | Express            | Prototype Pollution, SSRF   | Burp Suite     |
| **Java**   | Spring             | Deserialization, SSRF       | ysoserial      |
| **Perl**   | Legacy CGI         | RCE, injection              | Manual         |

### 💻 Identifying the Backend Technology (Recon)

```bash
# Check response headers for server/language clues
curl -I https://target.com

# Common header giveaways:
# X-Powered-By: PHP/7.4.3    ← PHP version exposed!
# Server: Apache/2.4.41      ← Apache version exposed!
# Set-Cookie: PHPSESSID=...  ← PHP session → it's PHP
# Set-Cookie: JSESSIONID=... ← Java session → it's Java

# Wappalyzer (browser extension) — identifies entire tech stack
# Also: builtwith.com for passive recon

# File extension recon
curl http://target.com/index.php   # PHP
curl http://target.com/index.asp   # Classic ASP
curl http://target.com/index.aspx  # ASP.NET
```

---

## 🔗 Full Security Attack Map

| Component       | What Attackers Target                      | Attack Technique                                 |
| --------------- | ------------------------------------------ | ------------------------------------------------ |
| DNS             | Zone transfers, DNS hijacking              | `dig axfr`, subdomain takeover                   |
| Load Balancer   | Inconsistent patching across servers       | Test multiple times, look for version diff       |
| CDN             | Bypass to find real server IP              | Historical DNS, misconfigured subdomains         |
| WAF             | Bypass to reach vulnerable server          | Payload encoding, case variation, HTTP smuggling |
| Web Server      | Default files, misconfig, version exploits | Nikto, Metasploit, searchsploit                  |
| Virtual Hosts   | Hidden admin panels, internal apps         | gobuster vhost, ffuf                             |
| Database        | SQL/NoSQL injection                        | sqlmap, manual SQLi                              |
| Static Files    | Sensitive data in JS/CSS                   | Manual source review, grep                       |
| Dynamic Backend | Injection, SSTI, LFI, RCE                  | Burp Suite, tplmap, sqlmap                       |

---

## ⚡ Enriched Insights (Beyond the Source Material)

### The Full Request in One Diagram

```
Browser types: https://tryhackme.com/login
       │
       ├─1─ DNS lookup → 104.26.10.229
       ├─2─ TLS handshake (HTTPS certificate verified)
       ├─3─ TCP connection → port 443
       ├─4─ HTTP GET /login sent
       ├─5─ Passes WAF (Cloudflare checks request)
       ├─6─ Load Balancer routes to Server #2
       ├─7─ Nginx receives GET /login
       ├─8─ Backend (Node.js) processes request
       ├─9─ Database query: SELECT page WHERE url='/login'
       ├─10─ HTML response generated
       ├─11─ Static assets (CSS/JS) served from CDN
       └─12─ Browser renders login page
                Total time: ~200-400ms
```

### HTTP Response Headers That Reveal the Stack

```http
HTTP/1.1 200 OK
Server: nginx/1.18.0           ← web server + version
X-Powered-By: PHP/8.0.3        ← backend language + version
Set-Cookie: PHPSESSID=abc123   ← session type → PHP confirmed
CF-Ray: 123abc-SIN             ← Cloudflare WAF/CDN in use
Via: 1.1 varnish               ← caching layer (Varnish)
X-Cache: HIT                   ← CDN cache hit
```

> 💡 **Pro tip:** The first thing a pentester does after
> finding a target is fingerprint the entire stack from
> these headers. **Server version + language version =**
> searchable CVEs in `searchsploit` or ExploitDB.

### Security Headers You Should Know (Defense)

```http
Strict-Transport-Security: max-age=31536000  ← force HTTPS
X-Frame-Options: DENY                         ← prevent clickjacking
X-Content-Type-Options: nosniff              ← prevent MIME sniffing
Content-Security-Policy: default-src 'self'  ← prevent XSS
X-XSS-Protection: 1; mode=block             ← legacy XSS filter
Referrer-Policy: no-referrer                 ← control referrer data
```

---

_Notes compiled from TryHackMe — How The Web Works Module_
_Enriched with Feynman explanations, pentest techniques, and code examples_
