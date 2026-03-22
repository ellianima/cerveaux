# OSI Model — Complete Reference & Attack Map

> **Nameless Flow's Cybersecurity Notes** | Networking Fundamentals
> _"Every attack lives at a layer. Know the layer, own the problem."_

---

## The Big Picture

The **OSI Model (Open Systems Interconnection)** is a 7-layer framework that standardizes how all networked devices send, receive, and interpret data. It's not just a memorization exercise — it's the **mental map every attacker and defender thinks in**.

- **Attacker mindset:** Which layer is weakest? Which layer hides my attack?
- **Defender mindset:** Which layer is this anomaly coming from? Where do I block it?
- **Engineer mindset:** Which layer is broken? Where do I start debugging?

### The Mnemonic

| Direction          | Phrase                                                              |
| ------------------ | ------------------------------------------------------------------- |
| Top → Bottom (7→1) | **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing |
| Bottom → Top (1→7) | **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way  |

---

## Encapsulation & Decapsulation

As data travels **down** the layers on the sender's side, each layer **wraps** the data with its own header — like envelopes inside envelopes. This is **encapsulation**.

As data travels **up** the layers on the receiver's side, each layer **unwraps** its envelope. This is **decapsulation**.

```
<img width="3999" height="2074" alt="image" src="https://github.com/user-attachments/assets/8e109c75-93d0-47b1-a2fb-7aefd5a31080" />

Sender                          Receiver
Layer 7 → [DATA]                [DATA]          ← Layer 7
Layer 6 → [L6][DATA]            [DATA]          ← Layer 6
Layer 5 → [L5][L6][DATA]        [DATA]          ← Layer 5
Layer 4 → [L4][L5][L6][DATA]    [DATA]          ← Layer 4
Layer 3 → [L3][L4]...[DATA]     [DATA]          ← Layer 3
Layer 2 → [L2][L3]...[DATA]     [DATA]          ← Layer 2
Layer 1 → 10110101011010...     10110101011010  ← Layer 1
```

---

## Layer 7 — Application

> _"The layer you see and touch every day"_

### What It Does

The interface between the user/application and the network. Provides protocols and rules that define how applications communicate. **Not** the application itself — the protocol the application uses.

### Key Protocols & Ports

| Protocol | Port   | Use                    | Security Risk                       |
| -------- | ------ | ---------------------- | ----------------------------------- |
| HTTP     | 80     | Web browsing           | Plaintext — fully sniffable         |
| HTTPS    | 443    | Encrypted web          | Safe (if TLS implemented correctly) |
| FTP      | 21     | File transfer          | Plaintext credentials               |
| SFTP     | 22     | Secure file transfer   | Encrypted via SSH                   |
| SSH      | 22     | Secure remote shell    | Strong — industry standard          |
| Telnet   | 23     | Remote shell (legacy)  | Plaintext — never use               |
| SMTP     | 25/587 | Sending email          | Often misconfigured                 |
| DNS      | 53     | Domain → IP resolution | Frequently attacked                 |
| DHCP     | 67/68  | Assigns IP addresses   | Spoofable                           |

### PDU (Protocol Data Unit)

**Data**

### Real-World Example

Typing `https://google.com` — HTTP/HTTPS protocol handles how that request is structured and sent.

### Attack Vectors

| Attack                         | Description                                                                        |
| ------------------------------ | ---------------------------------------------------------------------------------- |
| **Phishing**                   | Fake application layer (website/email) impersonating legitimate service            |
| **SQL Injection**              | Malformed input breaks out of intended database query — executes attacker commands |
| **Cross-Site Scripting (XSS)** | Inject malicious JavaScript into a web app — steals session tokens                 |
| **DNS Spoofing**               | Poison DNS cache — redirect victims to attacker-controlled servers                 |
| **Directory Traversal**        | Request `../../../etc/passwd` to read files outside web root                       |
| **Anonymous FTP abuse**        | Misconfigured FTP with no authentication — full file system access                 |
| **API abuse**                  | Exploit poorly secured APIs — unauthorized data access or commands                 |

### Tools (Kali Linux)

- `Burp Suite` — intercept/modify HTTP requests
- `OWASP ZAP` — automated web vulnerability scanning
- `sqlmap` — automated SQL injection
- `Nikto` — web server vulnerability scanner
- `dnsrecon` / `dig` / `nslookup` — DNS enumeration
- `ftp` — manual FTP connection and exploration

### Key Insight

> Layer 7 is where human behavior meets application logic — and humans make mistakes. The most creative and devastating attacks live here.

---

## Layer 6 — Presentation

> _"The universal translator"_

### What It Does

Translates data between the application layer and the network. Ensures data from one system can be understood by a completely different system, regardless of internal format differences.

### Three Core Jobs

**1. Translation / Encoding**
Converts between character sets and data formats so systems speaking different internal languages understand each other.

- ASCII, UTF-8, UTF-16, Unicode
- Encoding mismatch = garbled text (ever seen `â€™` instead of `'`? That's a Layer 6 failure)

**2. Compression**
Reduces data size before transmission to save bandwidth and increase speed.

- gzip, deflate, Brotli, zstd
- A 2MB webpage can travel as 400KB after compression

**3. Encryption / Decryption**
Encrypts data before sending, decrypts on arrival. This is where **TLS/HTTPS** conceptually lives.

### Key Formats Handled

| Category      | Formats                       |
| ------------- | ----------------------------- |
| Text encoding | ASCII, UTF-8, UTF-16, Unicode |
| Images        | JPEG, PNG, GIF, WebP          |
| Video         | MP4, H.264, H.265             |
| Audio         | MP3, AAC, FLAC                |
| Encryption    | TLS, AES, RSA                 |
| Compression   | gzip, Brotli, zstd            |
| Serialization | JSON, XML, Protocol Buffers   |

### PDU

**Data**

### Attack Vectors

| Attack                   | Description                                                                                    |
| ------------------------ | ---------------------------------------------------------------------------------------------- |
| **SSL Stripping**        | Attacker downgrades HTTPS → HTTP mid-connection. Victim thinks they're encrypted — they're not |
| **Certificate Spoofing** | Fake TLS certificate fools browser into trusting attacker's server                             |
| **CRIME Attack**         | Exploits TLS compression to deduce session tokens by measuring compressed size changes         |
| **Downgrade Attack**     | Force negotiation to weaker, broken cipher suite (e.g. SSLv2)                                  |

### Tools

- `mitmproxy` — intercept and modify TLS traffic
- `sslstrip` — strip HTTPS to HTTP
- `Wireshark` — observe encryption negotiation

### Key Insight

> A padlock icon (HTTPS) proves the _connection_ is encrypted — it does **not** prove the website is legitimate or safe. Phishing sites use HTTPS too. TLS proves identity of the server via certificates, but only if you verify the certificate chain.

---

## Layer 5 — Session

> _"The conversation manager"_

### What It Does

Creates, maintains, and terminates sessions (conversations) between applications on different devices. Manages the _dialogue_ — not the data itself.

### Three Core Jobs

**1. Session Establishment**
Negotiates and opens a session before data flows. Authentication often happens here.

**2. Session Maintenance**
Keeps the conversation alive. Manages session timeouts — why your bank logs you out after 10 minutes of inactivity.

**3. Checkpoints & Recovery**
Places checkpoints throughout a transfer. If connection drops, only data after the last checkpoint needs to be resent. A 10GB transfer dropping at 9.5GB resumes from the last checkpoint — not from 0.

### Sessions Are Unique

Data is bound to a specific session ID. Your YouTube session and your bank session cannot cross-contaminate. Each session is a completely isolated conversation.

### Key Protocols

- NetBIOS — Windows file sharing
- RPC — Remote Procedure Calls
- **SMB** — Windows network file system (critical for hacking — EternalBlue/WannaCry)
- SIP — Voice/video call sessions
- SQL sessions — database connections

### PDU

**Data**

### Attack Vectors

| Attack                   | Description                                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------------------- |
| **Session Hijacking**    | Steal a valid session token → impersonate the user without needing their password               |
| **Session Fixation**     | Send victim a pre-known session ID via crafted link → they log in → attacker uses that known ID |
| **Pass-the-Hash**        | Steal hashed credentials from a session → replay them without cracking                          |
| **Cookie Theft via XSS** | JavaScript extracts session cookie → attacker takes over session                                |
| **SMB Exploitation**     | EternalBlue targets SMB sessions → used by WannaCry ransomware                                  |

### Session Token Attack Flow (Fixation)

```
1. Attacker visits site → receives SESSION_ID=abc123 (pre-auth)
2. Attacker sends victim: https://bank.com/login?session_id=abc123
3. Victim logs in normally with real credentials
4. Server authenticates victim using session abc123
5. Attacker uses abc123 in their own browser
6. Server sees valid authenticated session → attacker is in
```

### Defenses

- Regenerate session token after every login (kills fixation)
- `HttpOnly` cookie flag — JavaScript cannot read cookies (kills XSS theft)
- `Secure` cookie flag — cookie only travels over HTTPS
- Short timeout + inactivity logout
- `SameSite` cookie attribute — prevents cross-site request forgery

### Key Insight

> The server cannot see who is on the other side of a connection. It can only see the token. **Whoever holds the token IS the user** — as far as the server is concerned.

---

## Layer 4 — Transport

> _"The heart of reliable communication"_

### What It Does

End-to-end delivery of data between applications. Handles segmentation, port numbers, ordering, and either reliability (TCP) or speed (UDP).

### PDU

- **Segment** (TCP)
- **Datagram** (UDP)

---

### TCP — Transmission Control Protocol

_The phone call. Reliable, ordered, confirmed._

**Advantages**

- Guarantees data accuracy and delivery order
- Error checking and retransmission of lost packets
- Flow control — prevents flooding the receiver
- Synchronizes both devices before transfer

**Disadvantages**

- Slower than UDP (more overhead)
- Requires stable connection throughout
- One missing chunk blocks everything after it

**Used for:** File downloads, web browsing (HTTP/HTTPS), email, SSH — anything where missing data breaks the result.

#### The Three-Way Handshake

```
Client  →  SYN        →  Server   "I want to connect" (seq=100)
Client  ←  SYN-ACK    ←  Server   "Ready, here's my seq" (seq=300, ack=101)
Client  →  ACK        →  Server   "Great, let's go" (ack=301)
         [CONNECTION ESTABLISHED]
```

- **SYN** = Synchronize sequence numbers
- **ACK** = Acknowledge receipt
- Both sides must confirm before any data flows

---

### UDP — User Datagram Protocol

_The megaphone. Fast, unreliable, fire-and-forget._

**Advantages**

- Much faster than TCP (no handshake, no acknowledgment)
- No reserved connection — doesn't block other operations
- Application layer controls pacing

**Disadvantages**

- No guarantee of delivery
- No ordering — packets may arrive scrambled
- No error recovery

**Used for:** Video streaming, voice calls, online gaming, DNS lookups — anything where speed matters more than perfection, and a little loss is acceptable.

---

### TCP vs UDP Decision Framework

| Question                                  | Answer → Protocol  |
| ----------------------------------------- | ------------------ |
| Does missing data break everything?       | → **TCP**          |
| Is speed more important than perfection?  | → **UDP**          |
| Is this a file, email, or web page?       | → **TCP**          |
| Is this video, voice, or gaming?          | → **UDP**          |
| Is this a DNS lookup (tiny request)?      | → **UDP**          |
| Does large DNS response exceed 512 bytes? | → **TCP** fallback |

---

### Key Ports to Memorize

| Port  | Protocol | Service                      |
| ----- | -------- | ---------------------------- |
| 20/21 | TCP      | FTP                          |
| 22    | TCP      | SSH / SFTP                   |
| 23    | TCP      | Telnet                       |
| 25    | TCP      | SMTP                         |
| 53    | UDP/TCP  | DNS                          |
| 80    | TCP      | HTTP                         |
| 443   | TCP      | HTTPS                        |
| 3389  | TCP      | RDP (Windows Remote Desktop) |
| 445   | TCP      | SMB                          |

### Attack Vectors

| Attack                    | Protocol | Description                                                                                          |
| ------------------------- | -------- | ---------------------------------------------------------------------------------------------------- |
| **SYN Flood**             | TCP      | Millions of SYN packets, never complete handshake. Server queues fill, memory exhausted. Classic DoS |
| **UDP Flood**             | UDP      | Spam random ports — server wastes CPU checking each one                                              |
| **DNS Amplification**     | UDP      | Spoof victim's IP in DNS request → server sends huge response to victim. 50x amplification           |
| **TCP Session Hijacking** | TCP      | Predict sequence numbers → inject malicious packets mid-connection                                   |
| **Port Scanning**         | TCP/UDP  | Send SYN → SYN-ACK means open, RST means closed. Map all services                                    |
| **RST Injection**         | TCP      | Forge TCP Reset packet → forcibly terminate someone's connection                                     |

### Tools

- `nmap` — port scanning, service detection
- `hping3` — craft custom TCP/UDP packets
- `netcat` — raw TCP/UDP connections
- `Wireshark` — capture and analyze traffic

### Key Insight

> Ports are doors. Protocols are languages. Nmap knocks on every door and listens to what answers. Your entire reconnaissance phase at Layer 4 happens before you touch a single vulnerability.

---

## Layer 3 — Network

> _"The postal system of the internet"_

### What It Does

Logical addressing and routing of packets across multiple networks. Determines the best path from source to destination across the entire internet.

### PDU

**Packet**

### IP Addressing

Every device gets a logical IP address. Unlike MAC addresses (Layer 2), IP addresses are:

- **Logical** — assigned by software, not burned in hardware
- **Globally organized** — structured so every router can make sensible routing decisions
- **Changeable** — can be reassigned, spoofed, or dynamically allocated

Example: `192.168.1.100` (IPv4) or `2001:0db8::1` (IPv6)

### How Routing Decisions Are Made

Routers calculate the optimal path using three factors:

| Factor            | Description                                                                |
| ----------------- | -------------------------------------------------------------------------- |
| **Shortest path** | Fewest hops (routers) between source and destination                       |
| **Reliability**   | Has this path dropped packets before? Avoid flaky routes                   |
| **Speed**         | Fiber (light) >> Copper (electrical signal) — routers factor in link speed |

These combine into a **metric** — lowest metric wins.

### Routing Protocols

| Protocol | Full Name                    | How It Works                                                                         |
| -------- | ---------------------------- | ------------------------------------------------------------------------------------ |
| **RIP**  | Routing Information Protocol | Counts hops only. Simple but naive — ignores speed                                   |
| **OSPF** | Open Shortest Path First     | Builds complete network map, considers all factors. Used in real enterprise networks |
| **BGP**  | Border Gateway Protocol      | Routes between entire ISPs and countries — the internet's backbone protocol          |

### Layer 3 Devices

- **Router** — reads IP addresses, makes routing decisions, connects different networks
- A switch is Layer 2 (reads MACs only) — a router is Layer 3 (reads IPs)

### Attack Vectors

| Attack                         | Description                                                                       |
| ------------------------------ | --------------------------------------------------------------------------------- |
| **IP Spoofing**                | Forge source IP address — victim thinks packet came from trusted source           |
| **ICMP Flood (Ping of Death)** | Flood target with ICMP packets — overwhelm CPU/bandwidth                          |
| **BGP Hijacking**              | Corrupt routing tables between ISPs — redirect internet traffic at national scale |
| **Route Poisoning**            | Inject false routing information — send traffic through attacker-controlled path  |
| **Traceroute Recon**           | Map every hop between you and a target — build network topology picture           |

### Tools

- `nmap` — IP-level scanning
- `traceroute` / `tracepath` — map network hops
- `scapy` — craft custom Layer 3 packets
- `Wireshark` — analyze IP headers

### Key Insight

> IP addresses stay the same from source to destination across the entire internet. MAC addresses change at every single hop. The router strips the Layer 2 frame, reads the Layer 3 destination IP, wraps a new frame with new MACs for the next hop, and forwards it.

---

## Layer 2 — Data Link

> _"The neighborhood delivery system"_

### What It Does

Node-to-node transfer within the same local network segment. Uses physical MAC addresses to deliver frames to the correct device on a local network. The "last mile" delivery after Layer 3 gets the packet to the right network.

### PDU

**Frame**

### MAC Addresses

**Media Access Control address** — the physical hardware address of a network interface card (NIC).

Structure: `A4:C3:F0:85:AC:2D`

- **First 3 pairs** (`A4:C3:F0`) = OUI — manufacturer identifier (Apple, Intel, Cisco, etc.)
- **Last 3 pairs** (`85:AC:2D`) = unique device ID assigned by manufacturer
- 48 bits total, expressed in hexadecimal
- Burned into hardware — cannot be changed
- **Can be spoofed** — OS sends whatever MAC it's told to send

### MAC Spoofing on Kali

```bash
sudo ip link set dev eth0 address AA:BB:CC:DD:EE:FF
```

Hardware MAC unchanged. Every packet now claims to be from the spoofed address.

### Layer 2 Devices

- **Switch** — maintains a MAC address table, forwards frames only to the correct port
- **NIC (Network Interface Card)** — the hardware that converts digital data to physical signals

### ARP — The Bridge Between Layer 2 and Layer 3

**Address Resolution Protocol** — answers the question: _"I have an IP address — what's the MAC address?"_

```
Device broadcasts: "Who has 192.168.1.50? Tell me your MAC!"
Target replies:    "I'm 192.168.1.50 — my MAC is A4:C3:F0:85:AC:2D"
Sender caches:     192.168.1.50 → A4:C3:F0:85:AC:2D
```

**Critical flaw:** ARP has zero authentication. Anyone can reply to an ARP request with any MAC address. This is the root cause of ARP-based attacks.

### Attack Vectors

| Attack                       | Description                                                                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **ARP Poisoning / Spoofing** | Broadcast fake ARP replies — "I'm the router." All traffic flows through attacker first. Classic Man-in-the-Middle                     |
| **MAC Flooding**             | Flood switch with fake MACs — fill MAC address table — switch panics and broadcasts everything to every port (you can see all traffic) |
| **MAC Spoofing**             | Impersonate a trusted device, bypass MAC-based access controls                                                                         |
| **VLAN Hopping**             | Exploit switch trunk port misconfiguration — access VLANs you shouldn't see                                                            |
| **Evil Twin AP**             | Fake wireless access point with same name as legitimate one — victims connect to attacker                                              |

### Tools

- `arpspoof` — ARP poisoning
- `Ettercap` — comprehensive MITM framework
- `Bettercap` — modern MITM, ARP spoofing, network recon
- `macof` — MAC flooding
- `Wireshark` — capture frames, observe ARP traffic

### Key Insight

> MAC address logs are not reliable evidence of who was on a network. Any access control system based purely on MAC filtering is fundamentally weak — any attacker can spoof a MAC in seconds.

---

## Layer 1 — Physical

> _"Pure physics — the real world"_

### What It Does

Transmission of raw bits (1s and 0s) as physical signals. No logic, no addresses, no error checking — just converting digital data into the physical medium and back.

### PDU

**Bit**

### Physical Media Types

| Medium                | Signal Type          | Speed                    | Notes                                 |
| --------------------- | -------------------- | ------------------------ | ------------------------------------- |
| **Cat5e/Cat6 copper** | Electrical (voltage) | Up to 10Gbps             | Most common office/home wiring        |
| **Fiber optic**       | Light pulses         | Up to 400Gbps+           | Backbone of the internet              |
| **Wi-Fi (802.11)**    | Radio waves          | Up to ~9.6Gbps (Wi-Fi 6) | Broadcast — anyone nearby can receive |
| **Bluetooth**         | Radio waves          | ~3Mbps                   | Short range                           |
| **Coaxial**           | Electrical           | Varies                   | Cable TV/internet                     |

### What Layer 1 Defines

- Voltage levels representing 1 and 0
- Cable specifications and connector types (RJ45, SFP, etc.)
- Radio frequencies and modulation for wireless
- Transmission distances before signal degrades

### Attack Vectors

| Attack                 | Description                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------------------- |
| **Physical cable tap** | Physically splice into a copper cable — intercept signals                                       |
| **RF Jamming**         | Broadcast noise on Wi-Fi frequency — disrupt all wireless communication                         |
| **Rogue Access Point** | Plug in unauthorized hardware — create backdoor network entry point                             |
| **Hardware keylogger** | Physical device between keyboard and computer — captures every keystroke                        |
| **USB Rubber Ducky**   | Looks like a USB drive — acts as a keyboard — executes pre-programmed attack payloads instantly |
| **LAN tap**            | Passive hardware device — silently copies all traffic on a network cable                        |

### Tools

- **HackRF** — software-defined radio — transmit/receive any radio frequency
- **USB Rubber Ducky** — automated physical keyboard attack
- **LAN Tap** — passive network interception hardware
- **Alfa Wi-Fi adapter** — monitor mode for capturing all nearby Wi-Fi traffic on Kali

### Key Insight

> You can have perfect security at Layers 2-7 and lose everything to a Layer 1 attack. Physical security IS cybersecurity. A server room with an unlocked door is a compromised server.

---

## Complete Attack Map — All 7 Layers

```
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 7 — APPLICATION                                          │
│  Attacks: Phishing, SQLi, XSS, DNS spoofing, FTP abuse         │
│  Tools:   Burp Suite, sqlmap, Nikto, dnsrecon                  │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 6 — PRESENTATION                                         │
│  Attacks: SSL stripping, cert spoofing, CRIME, downgrade        │
│  Tools:   mitmproxy, sslstrip, Wireshark                       │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 5 — SESSION                                              │
│  Attacks: Session hijacking, fixation, pass-the-hash           │
│  Tools:   Burp Suite, Ettercap, Bettercap                      │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 4 — TRANSPORT                                            │
│  Attacks: SYN flood, UDP flood, DNS amplification, port scan   │
│  Tools:   nmap, hping3, netcat, Wireshark                      │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 3 — NETWORK                                              │
│  Attacks: IP spoofing, ICMP flood, BGP hijacking, traceroute   │
│  Tools:   nmap, traceroute, scapy, Wireshark                   │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 2 — DATA LINK                                            │
│  Attacks: ARP poisoning, MAC flooding, VLAN hopping            │
│  Tools:   arpspoof, Ettercap, Bettercap, macof                 │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 1 — PHYSICAL                                             │
│  Attacks: Cable tap, RF jamming, Rubber Ducky, LAN tap         │
│  Tools:   HackRF, LAN tap hardware, Rubber Ducky               │
└─────────────────────────────────────────────────────────────────┘
```

---

## Quick Reference Cheat Sheet

### Layer Summary Table

| #   | Layer        | PDU              | Address     | Device     | Key Protocols                    |
| --- | ------------ | ---------------- | ----------- | ---------- | -------------------------------- |
| 7   | Application  | Data             | —           | —          | HTTP, HTTPS, DNS, FTP, SSH, SMTP |
| 6   | Presentation | Data             | —           | —          | TLS/SSL, JPEG, UTF-8, gzip       |
| 5   | Session      | Data             | Session ID  | —          | NetBIOS, RPC, SMB, SIP           |
| 4   | Transport    | Segment/Datagram | Port number | —          | TCP, UDP                         |
| 3   | Network      | Packet           | IP address  | Router     | IP, ICMP, OSPF, BGP              |
| 2   | Data Link    | Frame            | MAC address | Switch     | Ethernet, Wi-Fi, ARP             |
| 1   | Physical     | Bit              | —           | Hub, Cable | Electrical/Light/Radio           |

### Debugging with OSI (The Engineer's Method)

```
Problem: "I can't connect to the website"

Layer 1: Is the cable plugged in? Is Wi-Fi on?
Layer 2: Is the MAC address resolving? (arp -a)
Layer 3: Is the IP route correct? (ping, traceroute)
Layer 4: Is the port open? (nmap, telnet to port)
Layer 5: Is the session being established?
Layer 6: Is there an encryption/certificate error?
Layer 7: Is the application/service running correctly?
```

Work bottom-up. Most problems live at Layer 1, 3, or 7.

---

## Key Concepts to Never Forget

**Encapsulation** — data gets wrapped in headers as it goes down the layers (sender side).

**Decapsulation** — headers get stripped as data goes up the layers (receiver side).

**IP addresses change** — FALSE. IP stays constant source → destination.

**MAC addresses change** — TRUE. New MAC at every router hop.

**HTTPS padlock = safe website** — FALSE. It means the _connection_ is encrypted. The site can still be malicious.

**MAC filtering is strong security** — FALSE. MACs are spoofable in one command.

**UDP is useless** — FALSE. UDP is essential where speed > reliability (video, DNS, gaming).

**Physical security doesn't matter if software is secure** — FALSE. Layer 1 attacks bypass everything above.

---

## The Philosophy

> _"The OSI model isn't a description of what happens. It's a map of where problems can happen — and where attackers operate. Every attack in existence targets a specific layer. Know the layer, find the attack. Know all layers, find every attack."_

---

_Notes compiled from TryHackMe Pre-Security Path + extended deep dives_
_Nameless Flow | Cybersecurity & Networks Engineer Roadmap — Phase 1_
