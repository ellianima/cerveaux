# 💻 Types of Computers — From Servers to Embedded Systems

> **Source:** TryHackMe — Pre-Security / How Computers Work Module
> **Purpose:** Computer classification for cybersecurity context
> **Covers:** Laptop, Desktop, Workstation, Server, Smartphone,
> Tablet, IoT, Embedded Systems

---

## 🧒 Feynman Explanation — Not All Computers Look Like Computers

When most people hear "computer" they picture a laptop or desktop.
But a computer is really just **anything that takes input,
processes it, and gives output**. By that definition:

- Your **phone** is a computer
- Your **smart thermostat** is a computer
- The **chip in your car's engine** is a computer
- The **automatic door sensor** at a mall is a computer

They're everywhere. They just don't all have screens.

---

## 🔷 1. The Four Computers You Sit In Front Of

### Comparison Table

| Computer Type   | Screen & Keyboard | Main Purpose                                    | Analogy                                                   |
| --------------- | ----------------- | ----------------------------------------------- | --------------------------------------------------------- |
| **Laptop**      | ✅ Yes            | Portable everyday computing                     | A backpack — light, mobile, limited                       |
| **Desktop**     | ✅ Yes            | Sustained performance at fixed location         | A gym — powerful, stationary                              |
| **Workstation** | ✅ Yes            | Precision & reliability for professional tasks  | A surgeon's operating room — specialized, reliable        |
| **Server**      | ❌ No             | Providing services to many users over a network | A restaurant kitchen — works nonstop, invisible to diners |

---

### 🖥️ Laptop

```
Built for: Portability
Trade-off: Performance limited by battery + heat constraints
           (small chassis = hard to cool = throttles under load)

Hardware characteristics:
  - Mobile CPU (lower power, lower heat)
  - Integrated or low-power GPU
  - Limited upgrade options
  - Battery-powered

Common OS: Windows, macOS, Linux
```

> 💡 **Security relevance:** Laptops are prime targets for
> physical theft and Evil Maid attacks (boot from USB, bypass
> login). Full disk encryption (BitLocker, VeraCrypt) is
> critical for laptops used in security work.

---

### 🖥️ Desktop

```
Built for: Consistent sustained performance
Trade-off: Not portable, requires wall power

Hardware characteristics:
  - Full-size CPU (higher performance)
  - Dedicated GPU option
  - Easily upgradeable (RAM, storage, GPU)
  - Better cooling = sustained speeds under load

Common OS: Windows, Linux
```

> 💡 **Security relevance:** Desktops are common in
> corporate offices. Physical security matters —
> an unlocked desktop = instant compromise.

---

### 🖥️ Workstation

```
Built for: Precision, reliability, professional computation
Examples: 3D rendering, scientific simulation, video editing,
          CAD design, ML model training

Hardware characteristics:
  - ECC RAM (Error-Correcting Code — catches memory bit flips)
  - XEON or Threadripper CPUs (high core count)
  - Professional GPU (NVIDIA Quadro/A-series)
  - RAID storage for redundancy
  - Often runs 24/7

Why ECC RAM matters:
  Regular RAM has occasional bit-flip errors (0→1 or 1→0)
  In normal use: unnoticeable
  In scientific simulation: wrong answer
  In financial calculation: wrong number
  ECC RAM detects and corrects these errors automatically
```

> ⚠️ **Security relevance:** Workstations hold extremely
> valuable data (research, financial models, design IP).
> High-value targets for APTs (Advanced Persistent Threats)
> and corporate espionage.

---

### 🖥️ Server

```
Built for: Serving many users simultaneously, 24/7 uptime
Key difference: NO screen, NO keyboard (headless)
Managed remotely via SSH (Linux) or RDP (Windows)

Hardware characteristics:
  - Rack-mounted form factor (sits in data center racks)
  - Redundant PSUs (if one fails, server keeps running)
  - Hot-swappable drives (replace without shutting down)
  - ECC RAM
  - Multiple network interfaces
  - Often many CPU cores and hundreds of GB RAM

Types of servers:
  Web Server    — serves websites (Apache, Nginx, IIS)
  Database      — stores/retrieves data (MySQL, PostgreSQL)
  File Server   — stores shared files (Samba, NFS)
  Mail Server   — handles email (Postfix, Exchange)
  DNS Server    — resolves domain names
  Auth Server   — handles login/identity (Active Directory, LDAP)
```

> ⚠️ **Security relevance:** Servers are THE primary
> target in cyberattacks. Compromising one server can
> affect thousands of users simultaneously. This is why
> server hardening, patch management, and monitoring
> are core cybersecurity disciplines.

```bash
# Connecting to a Linux server remotely (SSH)
ssh username@192.168.1.100
ssh -p 2222 username@server.company.com  # custom port

# Connecting to a Windows server (RDP)
rdesktop 192.168.1.100           # Linux client
# Or use Windows Remote Desktop (mstsc.exe)

# Check what services are running on a server
nmap -sV 192.168.1.100

# Pentest: find exposed servers on a network
nmap -sV -p 80,443,22,3389,21,25 192.168.1.0/24
```

---

## 🔷 2. Computers You Never Sit In Front Of

### The Hidden Computer World

| Type                  | What It Is                                                 | Examples                                    | Network Connected? |
| --------------------- | ---------------------------------------------------------- | ------------------------------------------- | ------------------ |
| **Smartphone**        | Pocket-sized computer optimized for battery & connectivity | iPhone, Android                             | ✅ Always          |
| **Tablet**            | Touch-first computer with larger screen                    | iPad, drawing tablet                        | ✅ Usually         |
| **IoT Device**        | Network-connected device with a single purpose             | Smart thermostat, doorbell, fitness tracker | ✅ By definition   |
| **Embedded Computer** | Computer built INTO another device                         | Coffee maker chip, door sensor, car ECU     | ❌ Often not       |

---

### 📱 Smartphone

```
Architecture: ARM CPU (power-efficient)
OS: iOS (Apple) or Android (Linux-based)
Always connected: cellular, Wi-Fi, Bluetooth, GPS, NFC

Security surface:
  - Camera and microphone (always present)
  - Location tracking (GPS + cell towers + Wi-Fi triangulation)
  - App permissions (contacts, SMS, files)
  - Biometric authentication (fingerprint, face ID)
  - Encrypted storage (usually on by default)
```

> ⚠️ **Security note:** Smartphones are the richest source
> of personal data. Mobile malware, spyware (Pegasus),
> SIM swapping, and malicious apps are major attack vectors.
> Mobile pentesting is a growing specialization.

---

### 🌐 IoT Devices — The Internet of (Insecure) Things

```
IoT = Internet of Things
Definition: Physical devices connected to a network,
            collecting and exchanging data

Examples:
  Smart home:   thermostats, doorbells, bulbs, locks
  Industrial:   SCADA systems, factory sensors, PLCs
  Healthcare:   connected medical devices, monitors
  City:         traffic lights, parking sensors
  Wearables:    fitness trackers, smartwatches
```

> ⚠️ **HUGE security issue:** IoT devices are notorious
> for terrible security:

```
Common IoT Security Problems:
  ❌ Default credentials never changed (admin:admin)
  ❌ No patch/update mechanism
  ❌ Unencrypted communications
  ❌ No authentication on local network
  ❌ Running outdated Linux kernels
  ❌ Exposed management interfaces

Real attack: Mirai Botnet (2016)
  → Malware scanned internet for IoT devices
  → Tried default credentials (admin:admin etc.)
  → Infected 600,000+ cameras, DVRs, routers
  → Used them to launch 1.1 Tbps DDoS attack
  → Took down Twitter, Netflix, Reddit, GitHub
  → All from insecure security cameras

Pentest tools for IoT:
  shodan.io  — search engine for exposed IoT devices
  nmap       — discover IoT on local networks
  hydra      — brute force default credentials
```

```bash
# Find IoT devices on your network
nmap -sn 192.168.1.0/24           # host discovery
nmap -sV --script=banner 192.168.1.0/24  # grab banners

# Search Shodan for exposed devices (from browser or API)
# shodan.io → search: "default password" port:23
# shodan.io → search: webcam country:PH

# Python: Shodan API example
import shodan
api = shodan.Shodan("YOUR_API_KEY")
results = api.search("default password port:23")
for result in results['matches']:
    print(result['ip_str'], result['data'][:100])
```

---

### 🔧 Embedded Computers

```
Definition: A computer built INTO a device to control it.
            It IS the device's brain.

Key difference from IoT:
  IoT      = connected to a network, reports data remotely
  Embedded = may have NO network connection at all
             does its job silently inside the machine

Examples:
  Automatic door sensor   ← detects motion, opens door
  Coffee machine          ← controls brew temperature/timing
  Car ABS system          ← controls anti-lock braking
  Microwave timer         ← controls magnetron cycles
  Elevator controller     ← manages floors, doors, motors
  Medical pacemaker       ← controls heart rhythm timing
  Aircraft autopilot      ← controls flight surfaces

Architecture: Usually microcontrollers (Arduino, ARM Cortex-M)
OS: Often none, or a tiny RTOS (Real-Time Operating System)
```

> ⚠️ **Security relevance:** Embedded systems in critical
> infrastructure (power grids, hospitals, factories) are
> called **OT (Operational Technology)**. Attacking them
> can cause physical harm. Stuxnet (2010) was malware that
> targeted embedded PLCs in Iranian nuclear centrifuges —
> it physically destroyed equipment by sending wrong
> commands while displaying normal readings.

---

## 🔷 IoT vs Embedded — Key Distinction

```
                    IoT Device              Embedded Computer
                    ──────────              ─────────────────
Network connected?  ✅ Always               ❌ Often no
Reports data?       ✅ Yes (to cloud)        ❌ Works internally
Can be hacked       ✅ Remotely via          Only via physical
 remotely?           network                 access (usually)
Updates?            Sometimes               Rarely/never
Examples            Smart thermostat        Car brake controller
                    Smart doorbell          Coffee machine chip
                    Fitness tracker         Elevator motor board
```

---

## 🔗 Security Attack Map — All Computer Types

| Computer Type   | Primary Attack Vector                            | Real Example                            |
| --------------- | ------------------------------------------------ | --------------------------------------- |
| **Laptop**      | Physical theft, Evil Maid, unencrypted disk      | Stolen laptop with unencrypted drive    |
| **Desktop**     | Unattended workstation, malware, USB drop        | USB rubber ducky left in parking lot    |
| **Workstation** | APT targeting, insider threat                    | Operation Aurora (Google, 2010)         |
| **Server**      | Remote exploitation, misconfiguration, weak auth | Log4Shell, EternalBlue                  |
| **Smartphone**  | Malicious apps, spyware, SIM swap                | Pegasus spyware (journalists/activists) |
| **IoT Device**  | Default credentials, unpatched firmware          | Mirai botnet (2016)                     |
| **Embedded**    | Physical access, firmware tampering              | Stuxnet (Iranian centrifuges, 2010)     |

---

## ⚡ Enriched Insights (Beyond the Source Material)

### The Attack Surface Is EVERYWHERE

```
2025 reality:
  33+ billion IoT devices connected worldwide
  Average home: 10+ connected devices
  Average hospital: 10-15 connected devices PER BED
  Average factory: hundreds of embedded controllers

Most of these:
  ❌ Never updated
  ❌ Default credentials unchanged
  ❌ No monitoring
  ❌ No encryption
  ❌ No one even knows they're there

This is why IoT/OT security is one of the
fastest-growing cybersecurity specializations.
```

### For Pentesters: The Attack Surface Beyond Computers

```
Traditional pentest targets:
  Web servers, databases, Windows AD, VPNs

Modern pentest targets also include:
  Smart TVs in conference rooms          → camera/mic access
  VoIP phones                            → call interception
  Building management systems            → HVAC, door locks
  Printers (networked)                   → stored documents, pivot
  IP cameras                             → surveillance bypass
  Industrial control systems (ICS/SCADA) → physical damage

Tools:
  Shodan    — find exposed devices globally
  Nessus    — vulnerability scanning incl. IoT
  Firmwalker — analyze extracted IoT firmware
  Binwalk   — extract/analyze firmware images
```

### Nmap for Device Discovery

```bash
# Discover ALL devices on your network
sudo nmap -sn 192.168.1.0/24

# Identify device type by OS fingerprint
sudo nmap -O 192.168.1.0/24

# Find common IoT ports
nmap -p 23,80,443,8080,8443,554,1883,5683 192.168.1.0/24
# port 23   = Telnet (IoT default management, often open!)
# port 554  = RTSP (IP cameras video stream)
# port 1883 = MQTT (IoT messaging protocol, often no auth)
# port 5683 = CoAP (IoT protocol)

# Check for default Telnet credentials manually
telnet 192.168.1.X
# try: admin/admin, root/root, admin/1234, admin/(blank)
```

---

_Notes compiled from TryHackMe — How Computers Work Module_
_Enriched with security context, IoT attack examples, and real-world incidents_
