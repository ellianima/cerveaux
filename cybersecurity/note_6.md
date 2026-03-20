# Complete Networking Mastery Reference

> **Nameless Flow's Master Notes** | Networks, Protocols, TCP/IP, Ports & Attack Surfaces
> _"Know the layer. Find the attack. Know all layers. Find every attack."_

---

# PART 1 — THE OSI MODEL

## The Big Picture

The **OSI Model (Open Systems Interconnection)** is a 7-layer framework standardizing how all networked devices send, receive, and interpret data. It is the mental map every attacker and defender thinks in.

- **Attacker:** Which layer is weakest? Which layer hides my attack?
- **Defender:** Which layer is this anomaly at? Where do I block it?
- **Engineer:** Which layer is broken? Where do I start debugging?

### Mnemonics

| Direction          | Phrase                                                              |
| ------------------ | ------------------------------------------------------------------- |
| Top → Bottom (7→1) | **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing |
| Bottom → Top (1→7) | **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way  |

---

## Encapsulation & Decapsulation

As data travels **down** the layers on the sender's side, each layer wraps data with its own header — envelopes inside envelopes. This is **encapsulation**. Going **up** on the receiver's side, each layer unwraps its envelope. This is **decapsulation**.

```
Sender                              Receiver
Layer 7 → [DATA]                    [DATA]       ← Layer 7
Layer 6 → [L6][DATA]                [DATA]       ← Layer 6
Layer 5 → [L5][L6][DATA]            [DATA]       ← Layer 5
Layer 4 → [L4][L5][L6][DATA]        [DATA]       ← Layer 4
Layer 3 → [L3][L4]...[DATA]         [DATA]       ← Layer 3
Layer 2 → [L2][L3]...[DATA]         [DATA]       ← Layer 2
Layer 1 → 10110101011010...         10110101...  ← Layer 1
```

---

## Layer 7 — Application

> _"The layer you see and touch every day"_

**What it does:** Interface between user/application and the network. Provides protocols and rules for how applications communicate. NOT the application itself — the protocol it uses.

**PDU:** Data

**Key protocols & ports:**
| Protocol | Port | Use | Risk |
|---|---|---|---|
| HTTP | 80 | Web browsing | Plaintext — fully sniffable |
| HTTPS | 443 | Encrypted web | Safe if TLS implemented correctly |
| FTP | 21 | File transfer | Plaintext credentials |
| SFTP | 22 | Secure file transfer | Encrypted via SSH |
| SSH | 22 | Secure remote shell | Industry standard |
| Telnet | 23 | Remote shell (legacy) | Never use — plaintext |
| SMTP | 25/587 | Sending email | Often misconfigured |
| DNS | 53 | Domain → IP | Frequently attacked |
| DHCP | 67/68 | Assigns IPs | Spoofable |

**Attack vectors:**

- **Phishing** — fake application impersonating legitimate service
- **SQL Injection** — malformed input executes attacker DB commands
- **XSS** — injected JavaScript steals session tokens
- **DNS Spoofing** — poison cache, redirect victims to attacker servers
- **Directory Traversal** — `../../../etc/passwd` reads files outside web root
- **Anonymous FTP abuse** — no auth = full file system access
- **API abuse** — exploit poorly secured API endpoints

**Tools:** Burp Suite, OWASP ZAP, sqlmap, Nikto, dnsrecon, dig, nslookup

**Key insight:** Layer 7 is where human behavior meets application logic. Most creative and devastating attacks live here.

---

## Layer 6 — Presentation

> _"The universal translator"_

**What it does:** Translates data between formats so different systems understand each other. Three jobs: Translation, Compression, Encryption.

**PDU:** Data

**Three jobs:**

**1. Translation/Encoding** — converts between character sets (ASCII, UTF-8, UTF-16, Unicode). Mismatch = garbled text (ever seen `â€™` instead of `'`? Layer 6 failure).

**2. Compression** — reduces data size before transmission. gzip, deflate, Brotli. A 2MB webpage travels as 400KB.

**3. Encryption/Decryption** — TLS/HTTPS lives here conceptually. Scrambles data so only the recipient can read it.

**Key formats handled:**
| Category | Formats |
|---|---|
| Text encoding | ASCII, UTF-8, UTF-16, Unicode |
| Images | JPEG, PNG, GIF, WebP |
| Video | MP4, H.264, H.265 |
| Encryption | TLS, AES, RSA |
| Compression | gzip, Brotli, zstd |
| Serialization | JSON, XML, Protocol Buffers |

**Attack vectors:**

- **SSL Stripping** — attacker downgrades HTTPS → HTTP. Victim thinks encrypted, they're not
- **Certificate Spoofing** — fake TLS cert fools browser into trusting attacker's server
- **CRIME Attack** — exploits TLS compression to steal session tokens by measuring compressed packet sizes
- **Downgrade Attack** — force negotiation to broken cipher suite (SSLv2)

**Tools:** mitmproxy, sslstrip, Wireshark, testssl.sh

**Critical misconception:** A padlock (HTTPS) proves the _connection_ is encrypted. It does NOT prove the website is safe or legitimate. Phishing sites use HTTPS too.

---

## Layer 5 — Session

> _"The conversation manager"_

**What it does:** Creates, maintains, and terminates sessions between applications. Manages the dialogue — not the data itself.

**PDU:** Data

**Three jobs:**

**1. Session Establishment** — negotiates and opens session before data flows. Authentication often happens here.

**2. Session Maintenance** — keeps conversation alive. Manages timeouts — why your bank logs you out after 10 minutes of inactivity.

**3. Checkpoints & Recovery** — places checkpoints during transfer. If connection drops at 9.5GB into a 10GB download, resume from last checkpoint — not from zero.

**Sessions are unique:** Data is bound to a specific session ID. Your YouTube session and bank session cannot cross-contaminate.

**Key protocols:** NetBIOS, RPC, SMB (critical — EternalBlue/WannaCry), SIP, SQL sessions

**Attack vectors:**

- **Session Hijacking** — steal valid session token → impersonate user without password
- **Session Fixation** — send victim a pre-known session ID via crafted link → they log in → attacker uses that known ID
- **Pass-the-Hash** — steal hashed credentials, replay without cracking
- **Cookie Theft via XSS** — JavaScript extracts session cookie
- **SMB Exploitation** — EternalBlue targets SMB sessions

**Session Fixation flow:**

```
1. Attacker visits site → gets SESSION_ID=abc123
2. Attacker sends victim: https://bank.com/login?session_id=abc123
3. Victim logs in with real credentials
4. Server authenticates victim using session abc123
5. Attacker uses abc123 → they're in as victim
```

**Defenses:**

- Regenerate session token after every login (kills fixation)
- `HttpOnly` flag — JavaScript can't read cookies
- `Secure` flag — cookie only travels over HTTPS
- Short timeout + inactivity logout
- `SameSite` attribute — prevents CSRF

**Key insight:** The server can only see the token. Whoever holds the token IS the user.

---

## Layer 4 — Transport

> _"The heart of reliable communication"_

**What it does:** End-to-end delivery between applications. Handles segmentation, port numbers, ordering, and reliability (TCP) or speed (UDP).

**PDU:** Segment (TCP) / Datagram (UDP)

### TCP — Transmission Control Protocol

_Stateful. The phone call. Reliable, ordered, confirmed._

**Advantages:** Guarantees accuracy, error checking, retransmission, flow control, ordered delivery
**Disadvantages:** Slower than UDP, requires stable connection, overhead

**Used for:** File downloads, HTTP/HTTPS, email, SSH, databases — anything where missing data breaks the result.

#### The Three-Way Handshake

```
Client  →  SYN        →  Server   "I want to connect" (seq=100)
Client  ←  SYN-ACK    ←  Server   "Ready, here's my ISN" (seq=5000, ack=101)
Client  →  ACK        →  Server   "Connection open" (ack=5001)
              [CONNECTION ESTABLISHED]
```

#### TCP Flags

| Flag | Meaning                        | Used in               |
| ---- | ------------------------------ | --------------------- |
| SYN  | Synchronize — start connection | Handshake steps 1 & 2 |
| ACK  | Acknowledge — confirm receipt  | Almost every packet   |
| FIN  | Finish — close cleanly         | Closing handshake     |
| RST  | Reset — abort immediately      | Error or forced close |
| PSH  | Push — deliver immediately     | Real-time data        |
| URG  | Urgent — prioritize            | Rarely used           |

#### TCP Connection Closing (Four-Way)

```
Alice  →  FIN  →  Bob    "I'm done sending"
Alice  ←  ACK  ←  Bob    "Got your FIN"
Alice  ←  FIN  ←  Bob    "I'm also done"
Alice  →  ACK  →  Bob    "Connection fully closed"
```

**FIN vs RST:**

- **FIN** = polite goodbye. Both sides confirm. No data lost. Four packets.
- **RST** = emergency brake. Immediate termination. No confirmation. Data may be lost. One packet. Indicates crash, firewall block, or attacker injection.

#### TCP Sequence Numbers

Every byte gets a sequence number. Starts random (ISN) to prevent prediction attacks.

- **ACK number = last byte received + 1** — always. Tells sender exactly where to continue.
- If packet lost → ACK freezes → sender detects and retransmits from exactly that byte.

```
ISN random because: if seq started at 0 every time,
attackers predict and inject forged packets mid-connection.
```

#### TCP Header Fields

| Field                 | Purpose                        | Attack relevance              |
| --------------------- | ------------------------------ | ----------------------------- |
| Source Port           | Randomly chosen ephemeral port | Port scanning, fingerprinting |
| Destination Port      | Well-known service port        | Targeting specific services   |
| Sequence Number       | Tracks byte order              | Session hijacking, injection  |
| Acknowledgment Number | Next expected byte             | Detects packet loss           |
| Flags                 | Control connection behavior    | SYN flood, RST injection      |
| Checksum              | Integrity verification         | Detects modification          |
| Window Size           | Flow control                   | DoS via window manipulation   |

---

### UDP — User Datagram Protocol

_Stateless. The megaphone. Fast, fire-and-forget._

**Advantages:** Much faster, no reserved connection, application controls pacing
**Disadvantages:** No delivery guarantee, no ordering, no error recovery

**Used for:** Video streaming, voice calls, gaming, DNS, live telemetry — speed > perfection.

**UDP is stateless:** Each datagram is completely independent. No tracking, no memory, no contract.

**UDP header — only 8 bytes:**

```
Source Port  | Destination Port
Length       | Checksum
DATA
```

vs TCP's 20+ bytes minimum.

#### UDP Header Fields

| Field               | Purpose                          |
| ------------------- | -------------------------------- |
| Time to Live        | Prevents packets looping forever |
| Source Address      | Where to return replies          |
| Destination Address | Where to deliver                 |
| Source Port         | Random ephemeral port            |
| Destination Port    | Target service port              |
| Data                | The actual payload               |

**Why UDP enables amplification attacks:** No handshake = source IP unverified = spoofing trivially effective.

```
DNS Amplification:
Attacker → spoofed source IP = victim
Attacker → tiny DNS query (60 bytes) to open resolver
Resolver → huge response (3000 bytes) → victim
Amplification: 50x with minimal attacker bandwidth
```

---

### TCP vs UDP Decision Framework

| Question                            | Protocol     |
| ----------------------------------- | ------------ |
| Missing data breaks everything?     | TCP          |
| Speed matters more than perfection? | UDP          |
| File, email, web page, SSH?         | TCP          |
| Video, voice, gaming?               | UDP          |
| DNS query (tiny)?                   | UDP          |
| DNS response over 512 bytes?        | TCP fallback |

---

### Key Ports — Memorize These Cold

| Port  | Protocol | Transport | Category        | Key Risk                           |
| ----- | -------- | --------- | --------------- | ---------------------------------- |
| 21    | FTP      | TCP       | File transfer   | Plaintext creds, anonymous login   |
| 22    | SSH/SFTP | TCP       | Remote access   | Brute force, key attacks           |
| 23    | Telnet   | TCP       | Remote (legacy) | Everything plaintext — never use   |
| 25    | SMTP     | TCP       | Email           | Open relay, user enumeration       |
| 53    | DNS      | UDP/TCP   | Name resolution | Spoofing, tunneling, zone transfer |
| 80    | HTTP     | TCP       | Web             | SQLi, XSS, traversal, sniffing     |
| 110   | POP3     | TCP       | Email           | Credential brute force             |
| 139   | NetBIOS  | TCP       | Windows legacy  | Null sessions, enumeration         |
| 143   | IMAP     | TCP       | Email           | Credential brute force             |
| 443   | HTTPS    | TCP       | Web (encrypted) | SSL strip, cert spoof, web attacks |
| 445   | SMB      | TCP       | File sharing    | EternalBlue, WannaCry, ransomware  |
| 1433  | MSSQL    | TCP       | Database        | xp_cmdshell, data exfiltration     |
| 3306  | MySQL    | TCP       | Database        | Brute force, SQLi                  |
| 3389  | RDP      | TCP       | Remote desktop  | BlueKeep, brute force              |
| 5900  | VNC      | TCP       | Remote desktop  | Weak/no auth, brute force          |
| 6379  | Redis    | TCP       | Database        | Unauthenticated RCE                |
| 8080  | HTTP-Alt | TCP       | Web (dev)       | Same as 80, often less secured     |
| 27017 | MongoDB  | TCP       | Database        | Unauthenticated access             |

**Port ranges:**

- **0–1023** — Well-known ports. Standard services. Requires root to bind.
- **1024–49151** — Registered ports. Specific applications.
- **49152–65535** — Ephemeral ports. Randomly assigned for outgoing connections.

---

## Layer 3 — Network

> _"The postal system of the internet"_

**What it does:** Logical addressing and routing of packets across multiple networks. Determines best path from source to destination across the entire internet.

**PDU:** Packet

**IP Addressing:** Logical addresses assigned by software. Globally organized. Changeable. IPv4 = 32-bit (4.3 billion addresses). IPv6 = 128-bit (virtually unlimited).

**How routing decisions are made:**
| Factor | Description |
|---|---|
| Shortest path | Fewest hops (routers) between source and destination |
| Reliability | Has this path dropped packets before? Avoid flaky routes |
| Speed | Fiber (light) >> Copper (electrical). Routers factor in link speed |

**Routing protocols:**
| Protocol | How it works |
|---|---|
| RIP | Counts hops only. Simple but naive — ignores speed |
| OSPF | Builds complete network map, considers all factors. Real enterprise standard |
| BGP | Routes between entire ISPs and countries — the internet's backbone |

**Layer 3 devices:** Router — reads IP addresses, makes routing decisions, connects different networks.

### IP Packet Header Fields

| Field               | Purpose                                                          | Attack relevance                                             |
| ------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------ |
| TTL                 | Countdown timer. Decrements at each hop. At 0, packet discarded. | OS fingerprinting (Win=128, Linux=64, Cisco=255), traceroute |
| Checksum            | Mathematical integrity fingerprint                               | Detects tampering — attacker must recalculate                |
| Source Address      | Sender's IP                                                      | IP spoofing — forge to hide origin or impersonate            |
| Destination Address | Recipient's IP                                                   | BGP hijacking redirects traffic                              |
| Version             | IPv4 or IPv6                                                     | IPv6 often unmonitored — attacker blind spot                 |
| Protocol            | TCP=6, UDP=17, ICMP=1                                            | ICMP tunneling bypasses firewalls                            |
| Fragment Offset     | Reassembly position for fragmented packets                       | Fragmentation attacks bypass IDS inspection                  |
| Flags               | DF (Don't Fragment), MF (More Fragments)                         | Ping of Death used malformed fragment flags                  |

**TTL fingerprinting:**

```
Receive packet with TTL=119:
Default Windows TTL = 128
128 - 119 = 9 hops traveled
→ Sender is likely Windows, ~9 routers away
```

**Traceroute abuses TTL:**

```
Send TTL=1 → first router discards, reveals itself
Send TTL=2 → second router discards, reveals itself
...continues until destination
= complete map of every router to target
```

**Attack vectors:**

- **IP Spoofing** — forge source IP to impersonate or hide
- **ICMP Flood** — overwhelm target with ping packets
- **BGP Hijacking** — corrupt routing between ISPs — national-scale traffic redirection
- **Route Poisoning** — inject false routing info — send traffic through attacker path
- **Traceroute Recon** — map entire network topology silently

**Tools:** nmap, traceroute, scapy, Wireshark

**Key insight:** IP stays constant source → destination. MAC changes at every single hop.

---

## Layer 2 — Data Link

> _"The neighborhood delivery system"_

**What it does:** Node-to-node transfer within local network. Uses MAC addresses to deliver frames to the correct device. The "last mile" after Layer 3 reaches the right network.

**PDU:** Frame

### MAC Addresses

Physical hardware address burned into every NIC.

**Structure:** `A4:C3:F0:85:AC:2D`

- First 3 pairs = OUI (manufacturer identifier — Apple, Intel, Cisco)
- Last 3 pairs = unique device ID
- 48 bits total, hexadecimal
- Burned into hardware but **can be spoofed**

**MAC spoofing on Kali:**

```bash
sudo ip link set dev eth0 address AA:BB:CC:DD:EE:FF
```

**Layer 2 devices:** Switch — maintains MAC address table, forwards frames only to correct port.

### ARP — The Bridge Between Layer 2 and Layer 3

Address Resolution Protocol. Answers: _"I have an IP — what's the MAC?"_

```
Device broadcasts: "Who has 192.168.1.50? Tell me your MAC!"
Target replies:    "I'm 192.168.1.50 — MAC is A4:C3:F0:85:AC:2D"
Sender caches:     192.168.1.50 → A4:C3:F0:85:AC:2D
```

**Critical flaw:** ARP has zero authentication. Anyone can reply with any MAC address. Root cause of ARP-based attacks.

**Attack vectors:**

- **ARP Poisoning/Spoofing** — broadcast fake ARP replies "I'm the router" → all traffic flows through attacker first → MITM
- **MAC Flooding** — flood switch with fake MACs → fill MAC table → switch broadcasts everything to every port → see all traffic
- **MAC Spoofing** — impersonate trusted device, bypass MAC-based access controls
- **VLAN Hopping** — exploit switch trunk port misconfiguration
- **Evil Twin AP** — fake wireless AP with same name — victims connect to attacker

**Tools:** arpspoof, Ettercap, Bettercap, macof, Wireshark

**Key insight:** MAC address logs are unreliable evidence. MAC filtering is fundamentally weak security.

---

## Layer 1 — Physical

> _"Pure physics — the real world"_

**What it does:** Transmission of raw bits as physical signals. No logic, no addresses — just physics.

**PDU:** Bit

**Physical media:**
| Medium | Signal | Speed | Notes |
|---|---|---|---|
| Cat5e/Cat6 copper | Electrical | Up to 10Gbps | Common office/home wiring |
| Fiber optic | Light | Up to 400Gbps+ | Internet backbone |
| Wi-Fi (802.11) | Radio waves | Up to ~9.6Gbps (Wi-Fi 6) | Broadcast — anyone nearby can receive |
| Bluetooth | Radio waves | ~3Mbps | Short range |

**Attack vectors:**

- **Physical cable tap** — splice into copper cable — intercept signals
- **RF Jamming** — broadcast noise on Wi-Fi frequency — disrupt wireless
- **Rogue Access Point** — plug in unauthorized hardware — backdoor entry
- **Hardware Keylogger** — physical device between keyboard and computer
- **USB Rubber Ducky** — looks like USB drive, acts as keyboard, executes attacks instantly
- **LAN Tap** — passive hardware — silently copies all network traffic

**Tools:** HackRF (software-defined radio), USB Rubber Ducky, LAN Tap hardware, Alfa Wi-Fi adapter

**Key insight:** Perfect software security loses to Layer 1 attack. Physical security IS cybersecurity.

---

## Layer Summary Table

| #   | Layer        | PDU              | Address     | Device     | Key Protocols                    |
| --- | ------------ | ---------------- | ----------- | ---------- | -------------------------------- |
| 7   | Application  | Data             | —           | —          | HTTP, HTTPS, DNS, FTP, SSH, SMTP |
| 6   | Presentation | Data             | —           | —          | TLS/SSL, JPEG, UTF-8, gzip       |
| 5   | Session      | Data             | Session ID  | —          | NetBIOS, RPC, SMB, SIP           |
| 4   | Transport    | Segment/Datagram | Port number | —          | TCP, UDP                         |
| 3   | Network      | Packet           | IP address  | Router     | IP, ICMP, OSPF, BGP              |
| 2   | Data Link    | Frame            | MAC address | Switch     | Ethernet, Wi-Fi, ARP             |
| 1   | Physical     | Bit              | —           | Hub, Cable | Electrical/Light/Radio           |

---

# PART 2 — TCP/IP MODEL

## OSI vs TCP/IP

The internet actually runs on TCP/IP — a 4-layer simplification of OSI.

| TCP/IP Layer      | OSI Equivalent | Contains                              |
| ----------------- | -------------- | ------------------------------------- |
| Application       | Layers 5, 6, 7 | Sessions + Presentation + Application |
| Transport         | Layer 4        | TCP / UDP                             |
| Internet          | Layer 3        | IP, ICMP, routing                     |
| Network Interface | Layers 1 & 2   | Physical + Data Link                  |

**OSI** = anatomy textbook. **TCP/IP** = the living body. Study OSI to understand deeply. The internet runs TCP/IP.

---

# PART 3 — PACKETS & FRAMES IN DEPTH

## Packet vs Frame

- **Packet** = Layer 3 concept. Carries IP addresses. Thinks about journey across entire internet.
- **Frame** = Layer 2 concept. Carries MAC addresses. Thinks about the next single hop only.

```
[ Frame: MAC src + MAC dst ]
  [ Packet: IP src + IP dst ]
    [ TCP/UDP header: ports ]
      [ Your actual data ]
  [ /Packet ]
[ /Frame ]
```

**The envelope analogy:** Frame = envelope. Packet = letter inside. At each router (post office): envelope torn open, letter read, new envelope addressed to next hop.

## Why Packets Exist

- **Efficiency** — one corrupt packet = resend that packet only, not the entire file
- **Sharing** — packets from thousands of users interleave on same wire (statistical multiplexing)
- **Resilience** — different packets take different routes, network survives partial failure

---

# PART 4 — PORTS IN DEPTH

## The Harbour Analogy

IP address = building's street address. Port = specific door in that building.

- Port 80 = front door for web traffic
- Port 22 = staff entrance for admin
- Port 443 = secured front door with lock

## Non-Standard Ports

Services can run on non-standard ports (web server on 8080 instead of 80). "Security through obscurity" — **completely ineffective** against proper scanning.

```bash
# Default scan — only ~1000 common ports
nmap 192.168.1.1

# Full scan — all 65,535 ports
nmap -p- 192.168.1.1

# Service version detection — identifies service regardless of port
nmap -sV -p- 192.168.1.1
```

## The Pentester's Port Workflow

```
Step 1 — Discover open ports:
nmap -p- --min-rate 5000 <target>

Step 2 — Identify services and versions:
nmap -sV -sC -p <open ports> <target>

Step 3 — Research each service for CVEs and misconfigs:
FTP 21  → check anonymous login
SSH 22  → check weak credentials
SMB 445 → check EternalBlue (MS17-010)
HTTP 80 → run Nikto and Gobuster

Step 4 — Every open port = a question:
"Is this service vulnerable? Misconfigured? Default credentials?"
```

## Why SMB Port 445 Is the Most Dangerous Port in History

- **WannaCry (2017)** — 200,000+ computers, 150 countries, hours. Used EternalBlue on port 445.
- **NotPetya** — ~$10 billion damages. Also EternalBlue on port 445.
- **Every modern ransomware** uses SMB for lateral movement after initial infection.

---

# PART 5 — COMPLETE ATTACK MAP

```
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 7 — APPLICATION                                              │
│  Attacks: Phishing, SQLi, XSS, DNS spoofing, FTP abuse, API abuse  │
│  Tools:   Burp Suite, sqlmap, Nikto, dnsrecon, Gobuster            │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 6 — PRESENTATION                                             │
│  Attacks: SSL stripping, cert spoofing, CRIME, downgrade attacks   │
│  Tools:   mitmproxy, sslstrip, Wireshark, testssl.sh               │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 5 — SESSION                                                  │
│  Attacks: Session hijacking, fixation, pass-the-hash, SMB exploit  │
│  Tools:   Burp Suite, Ettercap, Bettercap, CrackMapExec            │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 4 — TRANSPORT                                                │
│  Attacks: SYN flood, UDP flood, DNS amplification, port scan       │
│  Tools:   nmap, hping3, netcat, Wireshark                          │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 3 — NETWORK                                                  │
│  Attacks: IP spoofing, ICMP flood, BGP hijacking, traceroute recon │
│  Tools:   nmap, traceroute, scapy, Wireshark                       │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 2 — DATA LINK                                                │
│  Attacks: ARP poisoning, MAC flooding, VLAN hopping, Evil Twin AP  │
│  Tools:   arpspoof, Ettercap, Bettercap, macof                     │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 1 — PHYSICAL                                                 │
│  Attacks: Cable tap, RF jamming, Rubber Ducky, LAN tap, rogue AP   │
│  Tools:   HackRF, LAN Tap hardware, USB Rubber Ducky               │
└─────────────────────────────────────────────────────────────────────┘
```

---

# PART 6 — ENGINEER'S DEBUGGING METHOD

When something breaks, walk the layers bottom-up:

```
"I can't connect to the website"

Layer 1: Is the cable plugged in? Is Wi-Fi on?
Layer 2: Is MAC resolving? (arp -a)
Layer 3: Is the IP route correct? (ping, traceroute)
Layer 4: Is the port open? (nmap, telnet to port)
Layer 5: Is the session being established?
Layer 6: Is there an encryption/certificate error?
Layer 7: Is the application/service running correctly?
```

Most problems live at Layer 1, 3, or 7.

---

# PART 7 — CRITICAL CONCEPTS & COMMON MISCONCEPTIONS

## Things That Never Change

- IP address stays constant source → destination across the entire internet
- MAC address changes at every single router hop
- UDP source IP is trivially spoofable — TCP's handshake makes spoofing much harder
- Ports 0–1023 require root/admin to bind
- Every byte in a TCP stream has a sequence number — not just packets

## Things Most People Get Wrong

| Misconception                                   | Truth                                                                                         |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------- |
| HTTPS padlock = safe website                    | HTTPS = encrypted connection only. The site can still be malicious. Phishing sites use HTTPS. |
| MAC filtering is strong security                | MACs are spoofable in one command. Useless as sole access control.                            |
| Services on non-standard ports are hidden       | `nmap -sV -p-` finds everything regardless of port.                                           |
| UDP is useless                                  | YouTube uses UDP (HTTP/3/QUIC). DNS uses UDP. Gaming uses UDP.                                |
| Physical security doesn't matter                | Layer 1 attacks bypass all software security.                                                 |
| Session tokens are secrets stored on the server | Tokens travel with every request. Steal the token = steal the identity.                       |
| A firewall is enough                            | Firewalls work at Layers 3-4. Application attacks (Layer 7) bypass most firewalls.            |

## Checksum vs Encryption

- **Checksum** → proves data wasn't modified. Doesn't hide content. Anyone can read and recalculate.
- **Encryption** → hides content. Doesn't prove non-modification alone.
- **Authenticated encryption (AES-GCM in TLS 1.3)** → does both simultaneously.

## TCP Stateful vs UDP Stateless

- **Stateful (TCP)** = remembers. Tracks what was sent, received, missing, order. Shared contract.
- **Stateless (UDP)** = forgets instantly. Each datagram independent. No tracking, no memory.

## QUIC / HTTP/3

Modern internet (YouTube, Google) runs HTTP/3 over QUIC — which is built on UDP. Google engineers needed TCP-like reliability with UDP-like speed and flexibility, so they built their own protocol on top of UDP. UDP + custom reliability layer = better than TCP for modern high-speed applications.

---

# PART 8 — QUICK REFERENCE CHEAT SHEETS

## TCP Handshake in 10 Seconds

```
SYN → SYN-ACK → ACK = connection open
FIN → ACK → FIN → ACK = connection closed (clean)
RST = connection aborted (emergency/error)
```

## ARP in 10 Seconds

```
"Who has IP X? Tell me your MAC"
→ Reply: "I have IP X, my MAC is Y"
→ Cache: IP X = MAC Y
→ No authentication = spoofable
```

## DNS in 10 Seconds

```
Browser: "What IP is google.com?"
DNS resolver: "142.250.185.46"
Browser: connects to that IP
Attack: poison resolver → victim goes to attacker's IP
```

## Nmap Cheat Sheet

```bash
nmap <target>                    # Default scan, top 1000 ports
nmap -p- <target>                # All 65,535 ports
nmap -sV <target>                # Service version detection
nmap -sS <target>                # Stealth SYN scan (half-open)
nmap -sC <target>                # Default scripts
nmap -O <target>                 # OS fingerprinting
nmap -A <target>                 # Aggressive (sV + sC + O + traceroute)
nmap -p 80,443,22 <target>       # Specific ports only
nmap --min-rate 5000 -p- <target> # Fast full scan
```

## Wireshark Filters Cheat Sheet

```
ip.addr == 192.168.1.1           # Filter by IP
tcp.port == 80                   # Filter by port
http                             # HTTP traffic only
dns                              # DNS traffic only
tcp.flags.syn == 1               # SYN packets only
tcp.flags.rst == 1               # RST packets (terminated connections)
arp                              # ARP traffic (look for poisoning)
!(arp or dns or icmp)            # Remove noise
```

---

# PART 9 — THE PHILOSOPHY

> _"The OSI model isn't a description of what happens. It's a map of where problems can happen — and where attackers operate. Every attack in existence targets a specific layer. Know the layer, find the attack. Know all layers, find every attack."_

> _"Attacks don't respect layer boundaries. But defenders must understand every layer to find them."_

> _"The server cannot see who is on the other side of a connection. It can only see the token. Whoever holds the token IS the user."_

> _"Physical security IS cybersecurity. A server room with an unlocked door is a compromised server."_

---

_Notes compiled from TryHackMe Pre-Security Path + extended deep dives with Claude_
_Nameless Flow | Cybersecurity & Networks Engineer Roadmap — Phase 1_
_OSI Model · TCP/IP · Packets & Frames · TCP · UDP · Ports · Attack Surfaces_
