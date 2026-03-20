# Section 3 — Network Infrastructure Complete Reference

> **Nameless Flow's Master Notes** | Port Forwarding · Firewalls · VPNs · Routers · Switches · VLANs
> _"Understand the infrastructure. Own the infrastructure."_

---

# PART 1 — PORT FORWARDING

## The Core Problem

Every device on a home/office network has a **private IP address** (`192.168.x.x`) — not routable on the public internet. Your router has **one public IP** (`82.62.51.70`). Without port forwarding, services on internal devices are completely unreachable from outside.

**Port forwarding** is a rule on the router that says:

> _"Any traffic arriving on my public IP at port X — forward it to internal device Y on port Z."_

## Private IP Ranges — Memorize These

```
10.0.0.0    – 10.255.255.255      (10.x.x.x)
172.16.0.0  – 172.31.255.255      (172.16-31.x.x)
192.168.0.0 – 192.168.255.255     (192.168.x.x)
```

These ranges are reused by every network in the world. They never appear on the public internet. NAT on each router translates them.

## The Full Packet Journey (Port Forwarding)

```
Step 1: External user types public IP
        http://82.62.51.70:80

Step 2: Packet arrives at router's public interface
        Dst: 82.62.51.70:80 → router checks forwarding table

Step 3: Router applies forwarding rule
        82.62.51.70:80 → rewritten to → 192.168.1.10:80

Step 4: Packet reaches internal web server
        192.168.1.10:80 receives and processes request

Step 5: Router rewrites return path (NAT)
        Response: 192.168.1.10 → rewritten to → 82.62.51.70 → external user
        Private network completely invisible to external user
```

## What Port Forwarding Rules Look Like

```
# Basic web server
External port 80 → Internal IP 192.168.1.10 → Internal port 80 → TCP

# Port remapping (external ≠ internal port)
External port 8080 → Internal IP 192.168.1.10 → Internal port 80

# SSH access to internal server
External port 2222 → Internal IP 192.168.1.50 → Internal port 22

# Without a rule:
82.62.51.70:80 → no rule → DROPPED / RST sent back
```

## Intranet vs Internet

- **Intranet** = private internal network. Only reachable by devices within it. All `192.168.x.x` devices are intranet by default.
- **Internet** = public-facing. Only deliberately forwarded ports are accessible.
- **Why internal pentesting matters** = once inside a network (via phishing, physical access, VPN), you reach all intranet services the public internet can never see. The valuable targets are always inside.

## NAT — The Hidden Mechanism

**Network Address Translation** solves IPv4 exhaustion. IPv4 has ~4.3 billion addresses. Not enough for 8+ billion people and tens of billions of devices. NAT lets private IP ranges be reused by every network simultaneously.

Port forwarding = NAT working in reverse. Instead of hiding internal devices, it deliberately exposes one specific port on one specific device.

## Port Forwarding vs Firewall

|          | Port Forwarding                                  | Firewall                                            |
| -------- | ------------------------------------------------ | --------------------------------------------------- |
| Job      | Opens doors — creates path into network          | Guards doors — decides who walks through            |
| Function | Routes specific external port to internal device | Inspects source, destination, port, protocol, state |
| Default  | Off — ports blocked by default                   | On — filters all traffic                            |
| Analogy  | Unlocking a specific door                        | Security guard checking IDs at the door             |

**Both work together.** Port forwarding alone with no firewall = dangerous. You need both.

## Attack Surface

**Misconfigured port forwarding = direct path into your network.**

| Attack                      | Description                                                                                                                                                           |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Shodan scanning**         | Shodan indexes every open port on the internet. `port:3389` returns millions of RDP-exposed machines. Attackers don't need to scan — Shodan already did it            |
| **Exposed SSH (22)**        | Port-forwarded SSH with weak credentials = brute-forced within hours of exposure                                                                                      |
| **Exposed RDP (3389)**      | Every ransomware gang's scanner finds these. Compromised within hours                                                                                                 |
| **Reverse port forwarding** | After compromising internal machine, attacker tunnels traffic OUT through firewall via reverse connection. Persistent backdoor that bypasses inbound firewall rules   |
| **UPnP abuse**              | Many routers have Universal Plug and Play enabled. Malware calls UPnP API to automatically create forwarding rules — punches holes in firewall without admin approval |

## Reverse Shells — The Direction of Connection Matters

```
Firewall blocks all INBOUND connections.
But OUTBOUND is allowed (browsing works).

Normal shell (blocked by firewall):
Attacker → [INBOUND BLOCKED] → Victim

Reverse shell (bypasses firewall):
Victim → [OUTBOUND ALLOWED] → Attacker
Attacker receives the connection — gets shell
Direction = everything
```

---

# PART 2 — FIREWALLS

## The Core Idea

A firewall is a border checkpoint. Every packet entering or leaving goes through it. The firewall reads the packet's "passport" — source IP, destination IP, port, protocol, connection state — and decides: **permit or deny**.

**Four questions every firewall asks:**

1. Where is the traffic coming from? (source IP/network)
2. Where is it going? (destination IP/network)
3. What port is it for? (port number)
4. What protocol is it using? (TCP, UDP, ICMP, both?)

## Stateless vs Stateful — The Critical Distinction

### Stateless Firewall

- Examines each packet **in complete isolation**
- No memory. No context. No connection tracking.
- Checks: source IP, dest IP, port, protocol against a static rule list
- First match = permit or deny. Done.
- **Fast, low resource, dumb**
- Cannot handle return traffic intelligently
- Great for absorbing DDoS floods at the edge

**The return traffic problem with stateless:**

```
You browse google.com → your machine sends to port 443
Google responds → sends back to your ephemeral port 54321
Stateless firewall sees: inbound packet from Google to port 54321
No rule exists for this → BLOCKED → web browsing breaks
Fix required: allow all inbound on ports 1024+ (huge security hole)
```

### Stateful Firewall

- Tracks the **entire connection** in a connection table
- Remembers: did this connection start legitimately? Was handshake valid? Is this response expected?
- Automatically allows return traffic for established connections
- More resource-intensive but intelligent
- **Standard for modern networks**

**Connection tracking table:**

```
Protocol | Src IP        | Src Port | Dst IP        | Dst Port | State
TCP      | 192.168.1.5   | 54321    | 142.250.1.46  | 443      | ESTABLISHED
TCP      | 192.168.1.5   | 54987    | 8.8.8.8       | 53       | ESTABLISHED
UDP      | 192.168.1.5   | 51234    | 8.8.8.8       | 53       | NEW
```

Return traffic is automatically permitted if it matches an established connection entry. No rule needed.

**Where stateless wins:** DDoS absorption. A stateful firewall under a 10M packets/sec DDoS must check each against its connection table — memory and CPU collapse. A stateless firewall just checks: "Blocked IP? Drop. Blocked protocol? Drop." Handles flood trivially. Real-world architecture: stateless at the edge, stateful behind it.

## All Firewall Types

| Type                               | Layer     | How it works                                                   | Strength            | Weakness                               |
| ---------------------------------- | --------- | -------------------------------------------------------------- | ------------------- | -------------------------------------- |
| **Packet Filter**                  | L3-4      | Stateless. IP/port/protocol per packet vs static rules         | Fast, low resource  | No context, easily bypassed            |
| **Stateful Inspection**            | L3-4      | Tracks connection state. Allows return traffic automatically   | Smart, handles NAT  | Resource heavy, blind to L7            |
| **WAF (Web Application Firewall)** | L7        | Inspects HTTP content. Detects SQLi, XSS, traversal in payload | Catches app attacks | Expensive, bypassable with encoding    |
| **NGFW (Next-Gen Firewall)**       | All       | Stateful + app + IDS/IPS + TLS inspection + threat intel       | Most complete       | Very expensive, complex                |
| **Host-based Firewall**            | On device | Software on endpoint (Windows Defender, iptables)              | Defense in depth    | Disabled by attacker with admin access |

### Snort — The Tool TryHackMe Mentions

Open-source IDS/IPS. Doesn't just filter by IP/port — reads packet payloads and matches against attack signatures. "Does this contain a SQL injection pattern? A known exploit payload?" Used on Kali. Free, powerful, industry-recognized.

## How Firewall Rules Work

Rules are processed **top to bottom**. First match wins. Order is critical.

```
# Example ruleset — order matters enormously:
ALLOW  | src: ANY        | dst: 192.168.1.10 | port: 80   | TCP → PERMIT (web)
ALLOW  | src: ANY        | dst: 192.168.1.10 | port: 443  | TCP → PERMIT (HTTPS)
ALLOW  | src: 10.0.0.0/8 | dst: ANY          | port: 22   | TCP → PERMIT (SSH internal only)
DENY   | src: ANY        | dst: ANY          | port: 23   | TCP → BLOCK (Telnet)
DENY   | src: ANY        | dst: ANY          | port: 445  | TCP → BLOCK (SMB from internet)
DENY   | src: ANY        | dst: ANY          | port: ANY  | ANY → BLOCK (implicit deny all)
```

**The Implicit Deny** — the most important rule that isn't written. Everything not explicitly permitted is blocked. This is correct security posture:

- **Default deny, explicit allow** ✓ — block everything, allow only what's needed
- **Default allow, explicit deny** ✗ — catastrophic. You can never enumerate all bad things.

## iptables — Linux Firewall on Kali

```bash
# View current rules
sudo iptables -L -v -n

# Allow established connections (stateful return traffic)
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow inbound HTTP
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Allow SSH only from specific IP
sudo iptables -A INPUT -p tcp -s 192.168.1.0/24 --dport 22 -j ACCEPT

# Block specific IP entirely
sudo iptables -A INPUT -s 10.10.10.5 -j DROP

# Implicit deny — drop everything else
sudo iptables -A INPUT -j DROP

# View connection tracking table
sudo conntrack -L
```

## Firewall Bypass Techniques

| Technique            | How it works                                                                                                                     |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Port tunneling**   | Tunnel C2 traffic inside HTTP/HTTPS on allowed ports 80/443. Looks like web traffic to packet-filter firewall                    |
| **DNS tunneling**    | DNS is almost never blocked. Encode data inside DNS queries/responses. Bypasses all port-based filtering. Tools: iodine, dnscat2 |
| **ICMP tunneling**   | Ping (ICMP) often allowed for diagnostics. Encode data inside ICMP echo packets. Tools: ptunnel, icmptunnel                      |
| **Reverse shell**    | Make victim connect OUT to attacker. Outbound connection passes firewall. Attacker receives shell                                |
| **WAF bypass**       | Encode SQLi: `%53%45%4C%45%43%54` or use comments: `SEL/**/ECT`. Signature doesn't match. Bypassed                               |
| **IP fragmentation** | Older stateless FWs only inspect fragment 1 (has port info). Put payload in fragment 2+. Fragments reassemble after firewall     |

---

# PART 3 — VPNs (VIRTUAL PRIVATE NETWORKS)

## The Core Idea

A VPN creates an encrypted tunnel through the public internet connecting two endpoints. Traffic inside the tunnel is invisible to everyone between the endpoints — ISP, routers, anyone sniffing.

**The tunnel analogy:**

- Without VPN: carry documents through a public street — anyone can read them
- With VPN: walk through a private underground tunnel — nobody on the street sees you or the documents

## How VPN Works Technically

```
Step 1: Cryptographic handshake
Your device → VPN server: negotiate encryption keys
Shared secret established — only you and VPN server have it

Step 2: Virtual network interface created
Linux: tun0 or tap0 created
All traffic routed through this interface gets encrypted automatically

Step 3: Packet encapsulation
Without VPN: [ IP Header: you → destination ] [ plaintext data ]
With VPN:    [ IP Header: you → VPN server ] [ ENCRYPTED: IP Header + destination + data ]

Step 4: VPN server decrypts and routes
VPN server receives outer packet
Decrypts inner payload
Sees original destination
Forwards on internal network

Step 5: Return path reversed
Response → VPN server → encrypted → you → decrypted
ISP sees only: you ↔ VPN server (encrypted noise)
```

## VPN Protocols — The Full Picture

| Protocol      | Year       | Security    | Speed   | Notes                                                                                                                    |
| ------------- | ---------- | ----------- | ------- | ------------------------------------------------------------------------------------------------------------------------ |
| **PPP**       | Foundation | Basic       | —       | Authentication + encryption base layer. Not routable alone. Used by PPTP                                                 |
| **PPTP**      | 1999       | **BROKEN**  | Fast    | MS-CHAPv2 defeated. MPPE encryption weak. NSA-accessible. Never use. Port TCP 1723                                       |
| **IPSec**     | Standard   | Strong      | Good    | Encrypts at IP layer. Transport mode (payload only) or Tunnel mode (full packet). Hard to set up. UDP 500/4500           |
| **OpenVPN**   | 2001       | Very strong | Good    | Open source, TLS-based. Runs on TCP or UDP. Can tunnel on port 443 (looks like HTTPS). What TryHackMe uses. UDP 1194     |
| **WireGuard** | 2019       | Best        | Fastest | Only ~4,000 lines of code vs OpenVPN's 70,000+. Modern crypto (ChaCha20, Curve25519). Built into Linux kernel. UDP 51820 |

**PPTP is broken and must never be used:**

```
MS-CHAPv2 broken in 2012
Captured PPTP handshake → offline crack → plaintext password
Tool chain: chapcrack + CloudCracker = under 24 hours
Pentest: nmap -p 1723 target → found PPTP → capture handshake → crack
```

## How TryHackMe's VPN Works

```bash
# 1. Download .ovpn config from TryHackMe
# 2. Connect
sudo openvpn your_username.ovpn

# 3. Check VPN interface
ip addr show tun0
# You get a 10.x.x.x IP — you're inside THM's internal network

# 4. Verify routing
ping 10.10.x.x      # target machine — now reachable

# 5. What your ISP sees:
# You → THM VPN server (encrypted)
# NOT: you → vulnerable machine

# 6. Split tunneling (THM uses this)
# 10.10.0.0/8 → via tun0 (VPN tunnel)
# Everything else → direct to internet
```

**Why THM uses VPN:**

- Vulnerable machines can't be public — they'd be attacked by everyone
- Your ISP doesn't flag you for "attacking" machines
- You get real internal network experience — exactly like real pentests
- THM controls who can reach the vulnerable machines

## VPN Benefits

| Benefit                    | Detail                                                                                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Geographic connection**  | Two offices in different cities connected as one private network. Resources accessible from either location                           |
| **Privacy**                | Traffic encrypted from your device. ISP sees only VPN server address. Can't read content or see DNS queries (if configured correctly) |
| **Anonymity**              | Traffic attributed to VPN server's IP, not yours. **Only as strong as VPN provider's logging policy**                                 |
| **Public WiFi protection** | Coffee shop WiFi: attacker runs Wireshark, captures all HTTP traffic. With VPN: sees only encrypted noise to one IP                   |

## The Critical Anonymity Misconception

> _"The level of anonymity a VPN provides is only as much as how other devices on the network respect privacy. A VPN that logs all your data is essentially the same as not using a VPN."_

Trust chain shifts — not eliminated:

- Without VPN: trust your ISP
- With VPN: trust VPN provider instead
- "No-log" claims only meaningful if independently audited

**Anonymity spectrum:**

```
Commercial VPN → hides from ISP, not from VPN provider
Tor            → routes through multiple relays, no single point knows both source + destination
VPN over Tor   → maximum separation, used by journalists in hostile countries
OPSEC          → full discipline of not leaking identity through ANY channel
```

## DNS Leaks — The Hidden VPN Failure

VPN encrypts traffic but DNS queries leak outside the tunnel. Your ISP still sees every domain you visit even though they can't read the content.

```bash
# Test for DNS leak
curl https://dnsleaktest.com/api

# Fix: configure VPN to route DNS through tunnel
# In OpenVPN config:
dhcp-option DNS 10.10.10.1   # use VPN's DNS server
```

## VPN Attack Surface

| Attack                    | Description                                                                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Credential attacks**    | VPN endpoints = highest-value targets. Credentials = direct internal network access, bypassing all perimeter firewalls. REvil and Conti targeted Pulse Secure VPN specifically |
| **CVE-2019-11510**        | Pulse Secure VPN: unauthenticated file read → leaked credentials → internal network access                                                                                     |
| **VPN as attacker infra** | Attackers route through VPNs across multiple countries. Attribution becomes impossible. Nation-state actors always use layered VPN infrastructure                              |
| **Split tunneling abuse** | Employee's malware pivots through their VPN connection to reach internal corporate resources. Corporate monitoring never sees the traffic                                      |

---

# PART 4 — ROUTERS

## What a Router Does

Connects different networks and routes packets between them. Operates at **Layer 3**. Reads **IP addresses**. Maintains a **routing table** — a map of which networks are reachable via which interfaces and paths.

**At the packet level, every hop a router makes:**

1. Receives packet — reads destination IP
2. Looks up destination in routing table
3. Picks best next hop
4. Decrements TTL by 1
5. Recalculates IP checksum
6. Strips old Layer 2 frame
7. Wraps new frame with next hop's MAC address
8. Forwards out the correct interface

## Routing Table

```
Destination      Subnet Mask      Gateway         Interface  Metric
0.0.0.0          0.0.0.0          82.62.51.1      eth0       100   ← default (internet)
192.168.1.0      255.255.255.0    0.0.0.0         eth1       0     ← local network direct
10.0.0.0         255.0.0.0        192.168.1.5     eth1       20    ← via another router
172.16.0.0       255.255.0.0      82.62.51.4      eth0       30    ← remote office VPN
```

**Default route (0.0.0.0/0)** = catch-all. "If no specific route matches, send it here." Points to your ISP's router. Gateway of last resort. Without it, packets to unknown destinations are dropped.

## Routing Decision Factors

| Factor        | Description                                                                            |
| ------------- | -------------------------------------------------------------------------------------- |
| Shortest path | Fewest hops (router-to-router jumps)                                                   |
| Reliability   | Has this path dropped packets recently?                                                |
| Speed         | Fiber (light, ~200,000 km/s) >> Copper (electrical, ~200,000 km/s but degrades faster) |

These combine into a **metric** — lowest metric = best path.

## Routing Protocols

| Protocol   | Type    | How it works                                                                                    | Used where              |
| ---------- | ------- | ----------------------------------------------------------------------------------------------- | ----------------------- |
| **RIP**    | Dynamic | Counts hops only. Simple, naive — ignores speed                                                 | Legacy/small networks   |
| **OSPF**   | Dynamic | Builds complete network map, considers all factors. Recalculates within seconds of link failure | Enterprise standard     |
| **BGP**    | Dynamic | Routes between entire ISPs and countries. The internet's backbone protocol                      | ISPs, large enterprises |
| **Static** | Manual  | Admin enters each route by hand. Predictable, no overhead, doesn't adapt                        | Small/simple networks   |

## Kali Commands

```bash
# View routing table
ip route show
route -n

# Add static route
sudo ip route add 10.10.0.0/16 via 192.168.1.1

# Check default gateway
ip route | grep default

# Trace the path to a destination
traceroute google.com
tracepath google.com
```

## Router Attack Surface

| Attack                       | Description                                                                                  |
| ---------------------------- | -------------------------------------------------------------------------------------------- |
| **Default credentials**      | Admin/admin, admin/password on millions of routers. Shodan finds them. Full network control  |
| **Route manipulation**       | Inject false routes → redirect traffic through attacker-controlled path                      |
| **BGP hijacking**            | Corrupt routing between ISPs → redirect national internet traffic                            |
| **DNS hijacking via router** | Change router's DNS settings → all clients get attacker-controlled DNS → redirect any domain |
| **Firmware vulnerabilities** | Unpatched router firmware = persistent compromise. Most routers never updated                |

---

# PART 5 — SWITCHES

## What a Switch Does

Connects multiple devices **within the same network**. Operates at **Layer 2** (or Layer 3). Reads **MAC addresses**. Maintains a **MAC address table** mapping MACs to ports. Forwards frames only to the correct port — not every port.

**Layer 2 Switch:** MAC addresses only. Forwards within one subnet. Cannot route between different IP subnets.
**Layer 3 Switch:** MAC + IP addresses. Can route between VLANs internally. Replaces "router on a stick" design. Enterprise standard.

## The MAC Address Table

```
MAC Address         Port    VLAN    Age (sec)
AA:BB:CC:DD:EE:01   Port 1  1       45
AA:BB:CC:DD:EE:02   Port 2  1       12
AA:BB:CC:DD:EE:03   Port 3  2       89
AA:BB:CC:DD:EE:04   Port 4  2       3
```

Switch learns by observing traffic. Frame arrives on Port 3 from MAC AA:BB → records "MAC AA:BB lives on Port 3." Future frames to AA:BB go only to Port 3.

## Unknown MAC — Flooding

Frame arrives for an unknown MAC. Switch floods out every port except the source port. Every device receives it. Only correct device responds. Switch records response's MAC and port. Never floods that MAC again.

**This flooding behavior is the target of MAC flooding attacks.**

## Hub vs Switch

| Hub                                              | Switch                                       |
| ------------------------------------------------ | -------------------------------------------- |
| Dumb — sends every frame out every port          | Smart — sends frames only to correct port    |
| Every device sees every frame                    | Privacy — devices only see their own traffic |
| Massive collisions                               | No collisions (full duplex)                  |
| Obsolete                                         | Current standard                             |
| Attacker's dream — Wireshark captures everything | Requires exploitation (MAC flood) to sniff   |

## Switch Attack Surface

| Attack                 | Description                                                                                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MAC Flooding**       | Tool: macof. Flood switch with thousands of fake MACs/sec. MAC table fills. Switch enters flooding mode — broadcasts everything to every port. Run Wireshark. Capture all traffic |
| **ARP Poisoning**      | No MAC flooding needed. Send gratuitous ARPs claiming to be the router. Traffic flows through you first. MITM on a switched network                                               |
| **CAM table overflow** | Same as MAC flooding — CAM = Content Addressable Memory = the MAC table                                                                                                           |

```bash
# MAC flooding
sudo macof -i eth0

# ARP poisoning with Bettercap
sudo bettercap -iface eth0
» net.probe on
» arp.spoof on
» net.sniff on
```

---

# PART 6 — VLANs (VIRTUAL LOCAL AREA NETWORKS)

## The Core Idea

**One physical switch → multiple logical switches.**

VLANs logically divide a switch into isolated segments. Devices in different VLANs cannot communicate directly at Layer 2 — even if they're plugged into the same physical switch. Traffic between VLANs must go up to Layer 3 (router) and back down.

**Without VLANs — flat network:**

```
Every device on the same switch = same broadcast domain
Sales can see Accounting traffic
Compromised Sales machine = access to everything
Ransomware on one machine = spreads to entire network
```

**With VLANs — segmented network:**

```
VLAN 1: Sales (192.168.1.x) — isolated
VLAN 2: Accounting (192.168.2.x) — isolated
VLAN 3: Servers (10.0.0.x) — isolated
VLAN 4: IT/Management — isolated

Ransomware on Sales machine:
→ Spreads only within VLAN 1
→ CANNOT reach Accounting (Layer 2 blocked)
→ CANNOT reach Servers (different VLAN)
→ Damage contained — organization survives
```

## Port Types

| Port Type       | Description                                                         | Used for                                 |
| --------------- | ------------------------------------------------------------------- | ---------------------------------------- |
| **Access port** | Untagged. Carries one VLAN only. Device doesn't know it's in a VLAN | End devices: PCs, printers, IP phones    |
| **Trunk port**  | 802.1Q tagged. Carries multiple VLANs simultaneously                | Switch-to-switch, switch-to-router links |

## Inter-VLAN Routing

VLANs are separate networks. To communicate between them, traffic must travel through a router (Layer 3) where firewall rules control what's allowed.

```
Sales (192.168.1.x)
    → VLAN 1
        → trunk port
            → router (applies ACLs/firewall rules between VLANs)
                → VLAN 2
                    → Accounting (192.168.2.x)

Direct Sales → Accounting = BLOCKED at Layer 2. Must traverse router.
Router can permit or deny based on rules.
```

## Router on a Stick

One physical router port carries all VLAN traffic on a trunk. Router creates sub-interfaces for each VLAN and routes between them.

```
[VLAN 1 Sales]    ──┐
[VLAN 2 Accounting] ├── Trunk Port ── Router sub-interfaces ── Internet
[VLAN 3 Servers]  ──┘
```

## VLAN and Ransomware — Why This Matters

**WannaCry (2017)** — 200,000+ machines infected globally. Used EternalBlue on SMB port 445 to spread laterally. Organizations with flat networks: destroyed. Organizations with proper VLAN segmentation: barely noticed it. SMB could not cross VLAN boundaries.

**This is the single most effective architectural control against lateral movement.**

## VLAN Attack Surface

### VLAN Hopping — Escaping Your VLAN

**Technique 1: Switch Spoofing (DTP abuse)**

```
DTP (Dynamic Trunking Protocol) often enabled by default on switch ports
Attacker's machine sends DTP packets pretending to be a switch
Real switch negotiates trunk with attacker
Attacker now receives ALL VLAN traffic
Completely escaped VLAN isolation
Tool: yersinia
```

**Technique 2: Double Tagging**

```
Attacker crafts frame with TWO 802.1Q VLAN tags:
  Outer tag: VLAN 1 (attacker's own VLAN)
  Inner tag: VLAN 2 (target VLAN)

First switch strips outer tag (sees VLAN 1 = attacker's port, valid)
Forwards frame on trunk with inner tag still intact
Second switch reads inner tag = VLAN 2
Delivers frame to VLAN 2 device

Limitation: ONE-WAY ONLY
Response goes back via normal routing — attacker can't receive it
Because response is tagged for VLAN 2, not forwarded to attacker's VLAN 1 port
Attack is injection-only, not full bidirectional communication
```

**Defenses against VLAN hopping:**

```
# Disable DTP on all access ports
switchport mode access           # forces access mode, no trunk negotiation
switchport nonegotiate           # disables DTP entirely

# Assign unused ports to a dead VLAN
switchport access vlan 999       # isolated dead VLAN

# Change native VLAN from default (1) to unused VLAN
# Double tagging requires attacker to be on native VLAN
switchport trunk native vlan 999
```

---

# PART 7 — HOW EVERYTHING CONNECTS

## The Full Network Stack in One View

```
INTERNET
    │
    ▼
[ROUTER] ← Layer 3. Public IP ↔ Private network. Routing table. Firewall rules.
    │         Handles NAT, port forwarding, VPN endpoints, inter-VLAN routing
    │
    ▼
[LAYER 3 SWITCH] ← Optional. Routes between VLANs internally.
    │              Replaces router-on-a-stick for inter-VLAN traffic.
    │
    ├──────────────────────────────────┐
    ▼                                  ▼
[VLAN 1 - Sales]              [VLAN 2 - Accounting]
[Layer 2 Switch]              [Layer 2 Switch]
192.168.1.x                   192.168.2.x
PC, laptops                   Finance servers
    │                                  │
    └──────────── ISOLATED ────────────┘
    Layer 2 boundary — no direct communication
    All inter-VLAN traffic must traverse router
```

## The Attacker's Journey Through This Infrastructure

```
Step 1 — External recon (internet)
Shodan → find public IP with open ports
nmap -p- 82.62.51.70 → discover forwarded ports

Step 2 — Exploit exposed service
Port 443 forward → web app → SQLi → RCE
Port 22 forward → SSH brute force → credential access
Port 3389 forward → RDP exploit → system access

Step 3 — Internal recon (inside network)
Now inside VLAN X
arp-scan → discover local hosts
nmap → discover services on local VLAN

Step 4 — Lateral movement attempts
Try to reach other VLANs
VLAN hopping if DTP enabled
ARP poisoning within VLAN
Pivot through shared servers (DMZ)

Step 5 — Escalation
Compromise router → own entire network
Compromise VPN endpoint → persistent access
Dump credentials → access all services
```

## The Defender's Checklist

```
Router:
☐ Change default credentials immediately
☐ Disable unnecessary services (Telnet, UPnP, unused ports)
☐ Enable firewall, configure default deny
☐ Keep firmware updated
☐ Restrict admin access to management VLAN only
☐ Enable logging

Switch:
☐ Disable unused ports, assign to dead VLAN
☐ Disable DTP on all access ports (switchport nonegotiate)
☐ Change native VLAN from default 1
☐ Port security — limit MACs per port
☐ Enable Dynamic ARP Inspection (DAI) — blocks ARP spoofing
☐ Enable DHCP snooping — prevents rogue DHCP servers

VLANs:
☐ Segment network by function (IT, HR, Finance, Servers, Guest)
☐ Block all inter-VLAN traffic by default at router
☐ Explicitly allow only required inter-VLAN flows
☐ Put servers in dedicated VLAN with strict ACLs
☐ Isolate IoT devices in their own VLAN

Firewall:
☐ Default deny inbound
☐ Allow only required ports
☐ Log all denied traffic
☐ Review rules regularly — remove stale rules
☐ Layer stateless (edge) + stateful + WAF (web apps)

VPN:
☐ Use WireGuard or OpenVPN — never PPTP
☐ Require MFA on VPN authentication
☐ Log all VPN connections
☐ Disable split tunneling for sensitive environments
☐ Audit VPN firmware/software for CVEs regularly
☐ Revoke credentials immediately when employee leaves

Port Forwarding:
☐ Only forward ports that are absolutely required
☐ Restrict forwarded ports to specific source IPs where possible
☐ Disable UPnP on all routers
☐ Regularly audit all forwarding rules
☐ Use VPN instead of direct port forwarding where possible
```

---

# PART 8 — QUICK REFERENCE

## Device Comparison Table

| Device       | Layer | Reads           | Connects                | Key attack                          |
| ------------ | ----- | --------------- | ----------------------- | ----------------------------------- |
| Hub          | L1    | Nothing         | Devices (obsolete)      | Passive sniffing — sees all traffic |
| Switch (L2)  | L2    | MAC             | Devices in same network | MAC flooding, ARP spoofing          |
| Switch (L3)  | L2+L3 | MAC + IP        | Devices + VLANs         | VLAN hopping, ARP spoofing          |
| Router       | L3    | IP              | Different networks      | Default creds, route injection      |
| Firewall     | L3-L7 | IP/port/payload | Filters all             | Bypass via tunneling, encoding      |
| VPN endpoint | L3-L7 | IP + encryption | Private tunnels         | Credential attack, CVE exploitation |

## Key Commands Cheat Sheet

```bash
# Network discovery
nmap -sn 192.168.1.0/24        # ping sweep — discover hosts
nmap -p- --min-rate 5000 IP    # fast full port scan
nmap -sV -sC -p PORTS IP       # service version + default scripts
arp-scan --localnet             # ARP-based host discovery

# Routing
ip route show                   # view routing table
traceroute TARGET               # map hops to destination
ip addr show tun0               # view VPN tunnel interface

# ARP
arp -a                          # view ARP cache
sudo arp-scan --localnet        # discover hosts via ARP

# Firewall (iptables)
sudo iptables -L -v -n          # view all rules
sudo conntrack -L               # view connection tracking table

# VPN
sudo openvpn config.ovpn        # connect to VPN
ip addr show tun0               # verify VPN interface

# Switch attacks (ethical/lab use only)
sudo macof -i eth0              # MAC flooding
sudo bettercap -iface eth0      # ARP spoofing framework
sudo yersinia -I                # VLAN hopping toolkit

# Wireshark filters for infrastructure analysis
arp                             # ARP traffic — look for poisoning
icmp                            # ICMP — ping sweeps, tunneling
tcp.flags.syn==1 && tcp.flags.ack==0  # SYN scan detection
vlan                            # 802.1Q VLAN tagged traffic
```

---

# PART 9 — CRITICAL CONCEPTS & MISCONCEPTIONS

## Things That Never Change

- Port forwarding opens paths INTO your network — always a security decision
- Stateful firewalls are the standard — stateless alone is not enough for modern networks
- Default deny is always the correct posture — never default allow
- PPTP is cryptographically broken — never use it in 2026
- VLANs are Layer 2 isolation — they cannot be treated as security boundaries without router ACLs enforcing them
- A VPN's anonymity is only as strong as its provider's logging policy
- The direction of a network connection (inbound vs outbound) determines whether a firewall blocks it

## Security Architecture Principles

- **Defense in depth** — layer multiple controls. No single control is sufficient.
- **Least privilege** — only allow the minimum access required. Default deny everywhere.
- **Segmentation** — isolate systems by function. Contain blast radius when breach occurs.
- **Assume breach** — design assuming an attacker is already inside. VLAN segmentation, internal firewalls, monitoring.
- **Log everything** — you can't investigate what you didn't record.

## The Human Factor

Organizations are slow to replace broken technology (like PPTP) because:

1. **Cost and complexity** — replacing infrastructure is expensive and disruptive
2. **Legacy dependencies** — old systems may only support old protocols
3. **Risk aversion** — "if it ain't broke" mentality even when it IS broken
4. **Awareness gap** — IT staff may not know PPTP is broken

**This gap between theoretical security and real-world security is where most real attacks happen.** Perfect knowledge of exploits matters less than understanding WHY organizations remain vulnerable.

---

_Notes compiled from TryHackMe Pre-Security Path — Section 3 + extended deep dives with Claude_
_Nameless Flow | Cybersecurity & Networks Engineer Roadmap — Phase 1_
_Port Forwarding · NAT · Firewalls · VPNs · Routers · Switches · VLANs · Network Segmentation_
