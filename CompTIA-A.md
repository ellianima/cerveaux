# CompTIA A+ V15 — Complete Master Checklist

> **Exams:** 220-1201 (Core 1) · 220-1202 (Core 2) **Version:** V15 — Launched March 25, 2025 · Retires ~2028 **Passing Score:** Core 1 = 675/900 · Core 2 = 700/900 **Questions:** Max 90 per exam (MCQ + Performance-Based) · 90 minutes each **Format:** ✅ = Already in your notes | 🆕 = NEW — gap added from official objectives

---

---

# PHASE 1 — CompTIA A+ Core 1 (220-1201)

> **Exam Weight: Mobile 13% | Networking 23% | Hardware 25% | Virtualization/Cloud 11% | Hardware & Network Troubleshooting 28%**

---

## 1.0 Mobile Devices (13%)

### Objective 1.1 — Mobile Device Hardware & Replacement

- [x] Why laptop parts are non-interchangeable — proprietary form factors to save space and power
- [x] Display types and their tradeoffs: IPS / TN / OLED / VA
- [x] 🆕 **Mini-LED displays** — backlighting with thousands of tiny LEDs; better local dimming than standard LED; appears in high-end laptops (Apple MacBook Pro, Dell XPS)
- [x] Internal display connector: **eDP** (Embedded DisplayPort) — soldered, cannot be swapped
- [x] **Inverter board** — converts DC to high-voltage AC for CCFL backlights
- [x] CCFL backlight (older) vs LED backlight (modern)
- [x] 🆕 **Touch screen / digitizer** — digitizer is a separate layer that senses touch; if display works but touch doesn't, replace digitizer only
- [x] 🆕 **Pixel density (PPI)** — pixels per inch; higher = sharper image (Retina display = 220+ PPI)
- [x] 🆕 **Refresh rate** — how many times per second the image refreshes; 60 Hz standard, 120/144 Hz gaming; affects battery life
- [x] 🆕 **Color gamut** — range of colors a display can reproduce; sRGB (standard), DCI-P3 (wide, for video/photo work)
- [x] **SO-DIMM** — laptop RAM form factor
- [x] DDR4 SO-DIMM vs DDR5 SO-DIMM — different notch positions, not cross-compatible
- [x] Laptop storage options: 2.5" SATA, M.2 SATA, M.2 NVMe
- [x] **M.2 key types**: B-key (SATA), M-key (NVMe), B+M key (both)
- [x] ZIF (Zero Insertion Force) socket for keyboard ribbon cable
- [x] DC jack / power connector — intermittent charging = DC jack issue
- [x] Heat pipe + fan cooling; thermal paste
- [x] Webcam, fingerprint reader, smart card reader — connected internally via USB or ribbon cables
- [x] 🆕 **Wi-Fi antenna connector/placement** — antennas routed inside the lid frame; break when hinge fails; antenna connector is MHF4 (tiny push-fit)
- [x] 🆕 **Biometrics** — fingerprint reader (capacitive sensor), facial recognition (IR camera); used for device unlock and Windows Hello
- [x] 🆕 **Near-field scanner** — NFC coil embedded near back cover; used for mobile payments and pairing
- [x] 🆕 **Physical privacy components** — webcam kill switch (hardware), privacy screen filter (blocks side-angle viewing), microphone mute switch

### Objective 1.2 — Mobile Accessories & Connectivity Options

- [x] USB versions and bandwidths: 2.0 (480 Mbps), 3.0/3.1 Gen 1 (5 Gbps), 3.1 Gen 2 (10 Gbps), 3.2 (20 Gbps), USB4 (40 Gbps)
- [x] USB-C is a **connector shape only** — capabilities depend on the controller
- [x] **Thunderbolt 4** — 40 Gbps, two 4K displays, 100W charging, PCIe tunneling; uses USB-C connector
- [x] Lightning (Apple, older) vs USB-C (modern standard)
- [x] 🆕 **microUSB** — older Android standard (Micro-B); still found on budget devices and accessories
- [x] 🆕 **miniUSB** — legacy; used in older cameras, GPS units; rarely seen now
- [x] **NFC** — 13.56 MHz, 4 cm range, contactless payments, pairing
- [x] Bluetooth profiles: HFP/HSP, A2DP, HID, AVRCP, PAN
- [x] Bluetooth pairing process
- [x] TRRS connector (4-pole 3.5mm) — has mic channel; TRS = audio-only
- [x] 🆕 **Stylus** — active (requires Bluetooth pairing and battery, e.g. Apple Pencil) vs passive (rubber tip, works anywhere)
- [x] 🆕 **Docking station** — replicates laptop ports into a desk hub; connects via USB-C/Thunderbolt; adds monitor, LAN, USB-A, audio
- [x] 🆕 **Port replicator** — simpler version of a dock; only replicates ports, no added functionality
- [x] 🆕 **Trackpad / drawing pad / track points** — trackpad uses capacitive sensing; drawing pads use digitizer; TrackPoint (Lenovo red nub) = pointing stick that moves cursor with pressure

### Objective 1.3 — Mobile Network Connectivity & App Support

- [x] Wi-Fi generations: 802.11n (Wi-Fi 4), 802.11ac (Wi-Fi 5), 802.11ax (Wi-Fi 6/6E)
- [x] Cellular: 2G → 3G → 4G LTE → 5G NR
- [x] Sub-6 GHz 5G vs mmWave 5G
- [x] SIM card sizes: Standard → Micro → Nano → eSIM
- [x] **eSIM** — programmable, OTA provisioning, no physical card
- [x] Hotspot/tethering — shares cellular data via Wi-Fi, USB, or Bluetooth
- [x] IMEI — 15-digit unique identifier per cellular device
- [x] GPS vs A-GPS
- [x] **Exchange ActiveSync (EAS)** — syncing corporate email, contacts, calendar; enforces MDM policies
- [x] **MDM (Mobile Device Management)** — enforce encryption, passcode, app restrictions, remote wipe
- [x] **MAM (Mobile Application Management)** — controls only corporate apps
- [x] Remote wipe vs selective wipe
- [x] 🆕 **BYOD (Bring Your Own Device)** — employee uses personal device for work; requires MAM policy, not full MDM
- [x] 🆕 **Corporate device configuration** — company-owned; full MDM control; GPS tracking, full wipe permitted
- [x] 🆕 **Recognizing data caps** — mobile hotspot has data limits; apps can consume data in background; MDM can set data usage alerts
- [x] 🆕 **Mobile device synchronization targets** — Calendar, Contacts, Mail, Cloud storage (OneDrive, iCloud, Google Drive)
- [x] 🆕 **Location services** — GPS (hardware chip), cellular (tower triangulation), Wi-Fi (known SSID positions); privacy concern; MDM can restrict

### Mobile Troubleshooting (Objective 5.4)

- [x] 169.254.x.x IP → DHCP failure (APIPA)
- [x] Battery drain — screen brightness, background apps, location services
- [x] Overheating — CPU throttling, swollen battery
- [x] No SIM detected — SIM tray seating, carrier lock
- [x] App crashes — clear cache → clear data → reinstall
- [x] Slow performance — storage space, background processes
- [x] 🆕 **Poor battery health** — check battery cycle count; iOS: Settings > Battery; Android: third-party apps or `*#*#4636#*#*`
- [x] 🆕 **Swollen battery** — fire hazard; do NOT puncture; use plastic tools only; dispose as hazardous waste
- [x] 🆕 **Broken screen / digitizer** — crack in glass vs digitizer failure (touch not responding); glass-only vs full assembly replacement
- [x] 🆕 **Improper charging** — debris in USB-C port; check with magnifying glass; clean with non-conductive tool
- [x] 🆕 **Liquid damage** — corrosion on logic board; do NOT charge; place in bag of desiccant; professional repair required
- [x] 🆕 **Cursor drift / touch calibration** — screen registering ghost touches; common after glass replacement (adhesive issue)
- [x] 🆕 **Unable to install new apps** — storage full; incompatible OS version; enterprise restriction via MDM
- [x] 🆕 **Digitizer issues** — ghost touches, unresponsive areas; check for screen protector interference, recalibrate, replace digitizer
- [x] 🆕 **Stylus does not work** — active stylus: check battery/Bluetooth; passive: check screen protector thickness
- [x] 🆕 **Physically damaged ports** — bent pins in USB-C; use magnifying glass; micro-soldering or dock replacement
- [x] 🆕 **Malware on mobile** — unexpected ads, battery drain, high data usage; run AV app; factory reset if persistent
- [x] 🆕 **Degraded performance** — low storage, outdated OS, too many background apps; factory reset as last resort

---

## 2.0 Networking (23%)

### Objective 2.1 — TCP vs UDP / Ports & Protocols

- [x] Full ports table (FTP, SSH, Telnet, SMTP, DNS, DHCP, HTTP, POP3, IMAP, SNMP, LDAP, HTTPS, SMB, Syslog, LDAPS, IMAPS, POP3S, RADIUS, RDP, TACACS+)
- [x] 🆕 **NetBIOS / NetBT — ports 137–139** — legacy Windows name resolution; NBT over TCP/IP; required by very old applications
- [x] 🆕 **TCP vs UDP comparison**:
    - TCP — connection-oriented, 3-way handshake (SYN/SYN-ACK/ACK), reliable, ordered, error-checked; use for data integrity
    - UDP — connectionless, no handshake, no guaranteed delivery, faster; use for streaming, VoIP, DNS queries
- [x] 🆕 **TFTP — port 69** — UDP; no authentication; used for PXE boot images and IOS firmware updates
- [x] 🆕 **SNMP — ports 161/162** — 161 = agent listens; 162 = trap receiver; monitors network devices; SNMPv3 adds encryption
- [x] 🆕 **Syslog — port 514** — centralized logging; UDP; sends device logs to a syslog server
- [x] 🆕 **NTP — port 123** — UDP; synchronizes time across all network devices; critical for Kerberos (must be within 5 min)
- [x] 🆕 **SFTP — port 22** — SSH File Transfer Protocol; NOT the same as FTPS; runs over SSH tunnel

### Objective 2.2 — Wireless Networking Technologies

- [x] 802.11 standards comparison table (a/b/g/n/ac/ax)
- [x] 2.4 GHz vs 5 GHz characteristics
- [x] 🆕 **6 GHz band** — Wi-Fi 6E only; least congested; best speeds; very short range; no interference from legacy devices
- [x] Non-overlapping channels: 2.4 GHz = 1, 6, 11; 5 GHz = 25+ non-overlapping
- [x] 🆕 **Channel width** — 20 MHz (standard), 40 MHz (HT), 80 MHz (VHT), 160 MHz (HE); wider = faster but more overlap with neighbors
- [x] 🆕 **Channel regulations** — some channels restricted by country (FCC in US, ETSI in EU); know that channels vary by region
- [x] SSID — human-readable Wi-Fi name; BSSID — MAC of AP radio
- [x] WEP / WPA / WPA2 / WPA3 hierarchy
- [x] WPA2 Personal (PSK) vs WPA2 Enterprise (802.1X)
- [x] 🆕 **Bluetooth** — 2.4 GHz ISM band; 1 Mbps (Classic) to 2 Mbps (BLE); Class 1 (100m), Class 2 (10m), Class 3 (1m)
- [x] 🆕 **NFC** — 13.56 MHz; max 4 cm; passive (tag reads by powered device) vs active (two powered devices)
- [x] 🆕 **RFID (Radio-Frequency Identification)** — uses electromagnetic fields to ID tags; low freq (125 kHz, HID badges) vs high freq (13.56 MHz, NFC); used for asset tracking, access cards, inventory
- [x] 🆕 **Long-range fixed wireless / WISP** — point-to-point or point-to-multipoint; used in rural areas without cable/fiber

### Objective 2.3 — Services Provided by Networked Hosts

- [x] DHCP server, DNS server, file share, print server, mail server, Syslog, web server
- [x] 🆕 **AAA (Authentication, Authorization, Accounting)** — who are you / what can you do / what did you do; implemented by RADIUS (port 1812/1813) or TACACS+ (port 49)
- [x] 🆕 **Database servers** — host SQL databases (MySQL, MS SQL, PostgreSQL); accessed on port 1433 (MS SQL), 3306 (MySQL)
- [x] 🆕 **NTP server** — provides authoritative time to all devices; stratum 0 = atomic clock; stratum 1 = directly connected to stratum 0
- [x] 🆕 **Spam gateways** — filter inbound email before reaching mail server; examples: Proofpoint, Mimecast
- [x] 🆕 **UTM (Unified Threat Management)** — all-in-one appliance: firewall + IPS + AV + VPN + content filtering
- [x] 🆕 **Load balancers** — distributes traffic across multiple servers; prevents single server overload; Layer 4 (TCP) or Layer 7 (HTTP)
- [x] 🆕 **Proxy servers** — sits between client and internet; caches content; can filter/block URLs; forward proxy (internal users) vs reverse proxy (protects servers)
- [x] 🆕 **SCADA / ICS** — Supervisory Control and Data Acquisition; controls physical industrial systems (power plants, water treatment); legacy = vulnerable to cyberattacks; air-gapped when possible
- [x] 🆕 **IoT devices** — smart TVs, cameras, thermostats; often use proprietary firmware; segment onto guest/IoT VLAN; disable default creds

### Objective 2.4 — Network Configuration Concepts

- [x] DNS record types: A, AAAA, CNAME, MX, TXT
- [x] DKIM, SPF, DMARC — email authentication (TXT records)
- [x] DHCP: Leases, Reservations, Scope, Exclusions
- [x] 🆕 **DNS AAAA record** — IPv6 equivalent of A record; maps hostname to 128-bit IPv6 address
- [x] 🆕 **CNAME record** — alias; points one hostname to another (e.g., www → webserver1)
- [x] 🆕 **VLAN (Virtual LAN)** — logically segments a physical switch into separate broadcast domains; controlled by switch port tagging (802.1Q); Layer 2 feature; requires routing to communicate between VLANs
- [x] 🆕 **VPN (Virtual Private Network)** — encrypted tunnel over public internet; types: site-to-site (branch offices), remote access (individual users); protocols: IPsec, SSL/TLS, OpenVPN, WireGuard

### Objective 2.5 — Common Networking Hardware

- [x] Routers, switches (managed vs unmanaged), access points, patch panel, firewall
- [x] 🆕 **Managed switch** — configurable via CLI or web; supports VLANs, port mirroring, SNMP, STP, QoS
- [x] 🆕 **Unmanaged switch** — plug-and-play; no config interface; no VLANs; for simple home/small office use
- [x] 🆕 **PoE (Power over Ethernet)** — delivers power over Cat5e/Cat6 cable to devices (IP phones, APs, cameras)
    - PoE (802.3af) — up to 15.4W
    - PoE+ (802.3at) — up to 30W
    - PoE++ (802.3bt) — up to 60W or 100W
    - PoE injector — adds PoE to a non-PoE port; inline device
- [x] 🆕 **Cable modem** — converts coaxial (DOCSIS) to Ethernet for cable internet
- [x] 🆕 **DSL modem** — converts phone line (POTS) to Ethernet; slower than cable/fiber
- [x] 🆕 **ONT (Optical Network Terminal)** — fiber-to-the-home device; converts fiber signal to Ethernet; used with FTTP/GPON
- [x] 🆕 **NIC (Network Interface Card)** — Layer 2 device; every NIC has a burned-in **MAC address** (48-bit, 6 hex pairs); first 3 pairs = OUI (manufacturer ID)
- [x] 🆕 **Patch panel** — terminates structured cabling in a rack; allows flexible patching; 568A/568B wiring standards

### Objective 2.6 — SOHO Network Configuration

- [x] IPv4 structure; subnet mask; default gateway; DHCP; APIPA
- [x] Private IP ranges (RFC 1918): 10.x, 172.16-31.x, 192.168.x
- [x] Loopback: 127.0.0.1
- [x] IPv4 vs IPv6
- [x] DHCP reservation; port forwarding; DMZ; NAT/PAT; guest network
- [x] First steps after getting new router (7 security steps)
- [x] 🆕 **IPv6 addressing** — 128-bit, 8 groups of 4 hex (e.g., 2001:0db8::1); link-local (fe80::/10); global unicast (2000::/3); no broadcast; uses NDP (Neighbor Discovery Protocol) instead of ARP
- [x] 🆕 **Static vs dynamic IP** — static = manually configured; dynamic = assigned by DHCP; hybrid = DHCP reservation gives same IP every time
- [x] 🆕 **Subnet mask** — e.g., /24 = 255.255.255.0 = 254 usable hosts; CIDR notation; determines network boundary
- [x] 🆕 **UPnP (Universal Plug and Play)** — allows devices to auto-configure port forwarding; security risk; **always disable**

### Objective 2.7 — Internet Connection Types & Network Types

- [x] 🆕 **Satellite internet** — high latency (500–700 ms); used in rural/remote areas; Starlink (LEO) has lower latency (~20–60 ms)
- [x] 🆕 **Fiber (FTTH/FTTP)** — fastest; symmetric up/down; requires ONT; most reliable
- [x] 🆕 **Cable** — DOCSIS standard; coaxial; fast download, asymmetric; shared neighborhood bandwidth
- [x] 🆕 **DSL (Digital Subscriber Line)** — runs on existing phone lines; distance-limited; ADSL (asymmetric) vs SDSL (symmetric)
- [x] 🆕 **Cellular** — LTE/5G data; used for mobile hotspot and fixed wireless; available anywhere with cell coverage
- [x] 🆕 **WISP (Wireless Internet Service Provider)** — fixed wireless; uses directional antenna to tower; rural alternative
- [x] 🆕 **Network type definitions**:
    - LAN — Local Area Network (single building/campus)
    - WAN — Wide Area Network (spans cities/countries; internet is the largest WAN)
    - PAN — Personal Area Network (Bluetooth, NFC; <10m)
    - MAN — Metropolitan Area Network (city-wide; fiber rings)
    - SAN — Storage Area Network (dedicated high-speed storage network; Fibre Channel or iSCSI)
    - WLAN — Wireless LAN (Wi-Fi within a building)

### Objective 2.8 — Networking Tools

- [x] Crimping tool; cable tester; cable certifier; toner probe; Wi-Fi analyzer; loopback plug; multimeter
- [x] 🆕 **Cable stripper** — removes outer jacket of UTP cable before termination; don't nick the inner conductors
- [x] 🆕 **Punchdown tool** — seats wire conductors into 110-block or keystone jack; 110 punch = most common; use correct blade
- [x] 🆕 **Network tap** — passive device that copies traffic for monitoring/analysis without disrupting the network; used by security tools and packet analyzers
- [x] 🆕 **T568A vs T568B wiring standards** — 568B is most common in North America; 568A used in government/residential; NEVER mix standards on same cable (unless making crossover cable)

---

## 3.0 Hardware (25%)

### Objective 3.1 — Display Components & Attributes

- [x] IPS / TN / VA / OLED display types
- [x] Inverter board for CCFL
- [x] eDP internal connector
- [x] 🆕 **Mini-LED** — backlighting technology; thousands of tiny LEDs grouped in zones for local dimming; better HDR than standard LED; found in MacBook Pro, iPad Pro
- [x] 🆕 **Pixel density (PPI)** — dots per inch; 1080p on 15" laptop ≈ 141 PPI; Retina = 220+ PPI; affects readability and UI scaling
- [x] 🆕 **Screen resolution** — common: 1920×1080 (FHD), 2560×1440 (QHD), 3840×2160 (4K UHD)
- [x] 🆕 **Refresh rate** — Hz; 60 = standard; 120/144 = gaming; 240 = competitive; higher Hz = smoother motion
- [x] 🆕 **Color gamut** — sRGB (standard web), DCI-P3 (video production), Adobe RGB (photo editing); wider gamut = more colors rendered
- [x] 🆕 **Touch screen / digitizer** — capacitive (most phones/tablets) vs resistive (old devices/medical); digitizer is a separate replaceable layer

### Objective 3.2 — Cable Types & Connectors

- [x] 🆕 **Network cables — copper**:
    - Cat5e — up to 1 Gbps, 100m
    - Cat6 — up to 10 Gbps at 55m; 1 Gbps at 100m
    - Cat6a — 10 Gbps at 100m; augmented; used for PoE++ and 10G runs
    - Cat8 — 40 Gbps, max 30m; data centers
    - **T568A / T568B** — wiring standards; 568B most common; must match both ends of straight-through cable
    - **UTP** — Unshielded Twisted Pair; most common
    - **STP / ScTP** — Shielded; reduces EMI; required in industrial environments
    - **Direct burial cable** — outdoor-rated, gel-filled jacket; resists moisture underground
    - **Plenum-rated** — fire-retardant jacket; required in ceiling/floor airspaces (plenum)
    - **Coaxial** — RG6 (cable TV/internet); RG59 (older video); F-type connector
- [x] 🆕 **Network cables — optical fiber**:
    - **Single-mode (SMF)** — 9 µm core; laser light; long distances (km); yellow jacket
    - **Multimode (MMF)** — 50 or 62.5 µm core; LED light; up to 550m; orange or aqua jacket
    - Connectors: **LC** (small form factor, most common in data centers), **SC** (push-pull, square), **ST** (bayonet, twist-lock, older)
- [x] 🆕 **Video cables**:
    - HDMI — digital audio+video; versions: 1.4 (4K@30), 2.0 (4K@60), 2.1 (8K@60)
    - DisplayPort — higher bandwidth than HDMI; daisy-chaining via MST; Mini-DP on older MacBooks
    - DVI — digital (DVI-D), analog (DVI-A), both (DVI-I); older; no audio
    - VGA — analog; 15-pin DB15; no audio; legacy; lowest quality
    - USB-C/Thunderbolt — carries video (DP Alt Mode or TB3/4)
- [x] 🆕 **Peripheral cables**: Serial (DB9 / RS-232), USB 2.0, USB 3.0
- [x] 🆕 **Storage cables**: SATA data + SATA power (15-pin), eSATA (external SATA, no power), Molex (older 4-pin power connector)
- [x] 🆕 **Connector types to recognize**: RJ11 (phone, 6P2C/6P4C), RJ45 (network, 8P8C), F-type (coax, TV/cable), ST/SC/LC (fiber), MicroUSB, MiniUSB, USB-C, Molex, Lightning, DB9 (serial), Punchdown block (110-type)

### Objective 3.3 — RAM Characteristics

- [x] DIMM (288-pin desktop) vs SO-DIMM (260-pin laptop)
- [x] DDR4 vs DDR5 (bandwidth, voltage, slot notch)
- [x] Dual-channel — matched pairs in correct slots
- [x] ECC RAM — detects/corrects single-bit errors; required in servers
- [x] RAM troubleshooting: memtest86+, one stick at a time
- [x] 🆕 **DDR iterations**:
    - DDR3 — 1.5V, 1600–2133 MHz; still found in older systems
    - DDR4 — 1.2V, 2133–3200+ MHz; current mainstream
    - DDR5 — 1.1V, 4800–7200+ MHz; on-die ECC; higher performance; requires new platform
- [x] 🆕 **CAS Latency (CL)** — Column Address Strobe; how many cycles RAM takes to respond; lower = faster; tradeoff with speed
- [x] 🆕 **Channel configurations** — single (1 stick), dual (2 matching sticks), quad (4 sticks); dual channel effectively doubles bandwidth

### Objective 3.4 — Storage Devices

- [x] HDD (spinning magnetic) vs SSD (NAND flash)
- [x] SATA III — 6 Gbps max (~550 MB/s real world)
- [x] NVMe over PCIe — 3,500–7,000+ MB/s
- [x] M.2 form factor sizes — 2280 most common
- [x] RAID levels: 0, 1, 5, 6, 10 table
- [x] Software RAID vs hardware RAID
- [x] 🆕 **HDD spindle speeds** — 5400 RPM (laptop, quiet, lower power), 7200 RPM (desktop/performance), 10K/15K RPM (server SAS drives)
- [x] 🆕 **HDD form factors** — 2.5" (laptop/portable) vs 3.5" (desktop/NAS)
- [x] 🆕 **SAS (Serial Attached SCSI)** — enterprise storage; hot-swappable; up to 12 Gbps; used in servers and RAID arrays
- [x] 🆕 **mSATA** — older small form factor SSD; pre-M.2; uses mini-PCIe slot; max SATA speeds; mostly obsolete
- [x] 🆕 **PCIe SSD (add-in card)** — full-size PCIe card SSD; used in workstations; extremely fast
- [x] 🆕 **SMART (Self-Monitoring, Analysis and Reporting Technology)** — drive monitors its own health; key attributes: Reallocated Sector Count, Spin Retry Count, Uncorrectable Sector Count, Power-On Hours; tools: CrystalDiskInfo (Windows), `smartctl` (Linux)
- [x] 🆕 **Removable storage** — Flash drives (USB thumb drives); SD / microSD / SDHC / SDXC cards; used in cameras, Raspberry Pi, phone expansion
- [x] 🆕 **Optical drives** — CD (700 MB), DVD (4.7–8.5 GB), Blu-ray (25–50 GB); mostly legacy; still used for media and software

### Objective 3.5 — Motherboards, CPUs & Add-on Cards

- [x] ATX / Micro-ATX / Mini-ITX form factors
- [x] Intel LGA vs AMD AM4/AM5 socket types
- [x] Chipset; PCIe slots x1/x4/x8/x16; PCIe Gen 3/4/5
- [x] CMOS battery (CR2032); POST; beep codes
- [x] BIOS vs UEFI (MBR/GPT, Secure Boot, mouse, faster POST)
- [x] TPM; Secure Boot; front panel connectors
- [x] CPU cores, threads, HyperThreading/SMT
- [x] CPU cache L1/L2/L3; TDP; thermal paste application
- [x] Turbo Boost / Precision Boost; VT-x / AMD-V
- [x] 🆕 **CPU architecture**:
    - x86/x64 — dominant desktop/server; Intel and AMD; 64-bit = addressable memory >4 GB
    - ARM — Reduced Instruction Set (RISC); low power; used in phones, tablets, Apple M-series; Windows on ARM (Surface Pro X)
- [x] 🆕 **Core configurations** — physical cores vs virtual (SMT/HT); big.LITTLE / hybrid architecture (Intel P-cores + E-cores); NUMA for multi-socket servers
- [x] 🆕 **Boot password / BIOS password** — two types: supervisor (prevents BIOS changes) and user/power-on (prevents booting); can be reset by clearing CMOS (remove CMOS battery or jumper)
- [x] 🆕 **USB permissions in UEFI** — enable/disable USB ports in firmware; used to prevent USB boot or data theft
- [x] 🆕 **Fan considerations in UEFI** — PWM fan curves; temperature thresholds; helps control noise vs cooling
- [x] 🆕 **Temperature monitoring** — UEFI shows CPU/system temps; tools: HWiNFO64, Core Temp; alert thresholds typically 90-95°C for CPU
- [x] 🆕 **HSM (Hardware Security Module)** — dedicated hardware for cryptographic operations; stronger than TPM; used in enterprises for key storage, PKI, code signing
- [x] 🆕 **Expansion cards**: Sound card, Video/GPU card, Capture card (records HDMI/game video), NIC (add wired or wireless)
- [x] 🆕 **Liquid cooling** — AIO (All-In-One) liquid cooler; pump + radiator + fans; better for overclocking than air; pump failure = catastrophic
- [x] 🆕 **Multisocket motherboards** — two or more CPU sockets; used in servers/workstations; NUMA architecture

### Objective 3.6 — Power Supplies

- [x] ATX form factor; modular vs semi-modular vs non-modular
- [x] 80 Plus efficiency ratings
- [x] Voltage rails: +3.3V, +5V, +12V, -12V, +5VSB
- [x] Paperclip test (PS_ON to ground); UPS types
- [x] 🆕 **Input voltage** — 110-120 VAC (North America) vs 220-240 VAC (Europe/Asia/PH uses 220V); PSU must match local voltage or have auto-switching
- [x] 🆕 **20+4 pin motherboard connector** — main power; 20-pin for older boards; 24-pin modern; "+4" can detach for older compatibility
- [x] 🆕 **Redundant power supply** — two PSUs in server; one fails, other takes over; common in rackmount servers
- [x] 🆕 **Wattage rating** — choose PSU at 50-70% load capacity for efficiency and headroom; GPU is the biggest load (RTX 4090 = 450W TDP alone)
- [x] 🆕 **Line-interactive UPS** — most common; battery during outages; AVR for brownouts
- [x] 🆕 **Online/double-conversion UPS** — always on battery; best protection; for servers

### Objective 3.7 & 3.8 — Printers & Maintenance

- [x] **Laser printer process** (7 steps: Processing → Charging → Exposing → Developing → Transferring → Fusing → Cleaning) ⚡ MEMORIZE
- [x] Fuser — most common failure; smearing/unfused toner
- [x] Inkjet — piezoelectric or thermal; better color; higher cost per page
- [x] Thermal printer — heat-sensitive paper; no ink; receipts/labels
- [x] Impact / dot matrix — pins strike ribbon; carbon forms
- [x] Print spooler (SPOOLSV.EXE) — fix stuck: stop spooler → delete `C:\Windows\System32\spool\PRINTERS\*` → start spooler
- [x] PCL vs PostScript
- [x] Network printer port 9100 (RAW)
- [x] 🆕 **Printer security settings**:
    - User authentication — require login at printer panel
    - Badging — smart card / NFC tap to release print jobs
    - Audit logs — track who printed what and when
    - Secured/held prints — job waits in queue until authenticated at printer
- [x] 🆕 **Printer device connectivity options** — USB, Ethernet (static IP + driver install), Wireless (802.11 + WPA2 config), Bluetooth (short range, personal)
- [x] 🆕 **Network scan services** — scan-to-email (SMTP), scan-to-SMB (network folder), scan-to-cloud (OneDrive, SharePoint)
- [x] 🆕 **ADF (Automatic Document Feeder)** — feeds pages automatically; flatbed requires manual placement; duplex ADF scans both sides
- [x] 🆕 **Printer configuration settings** — Duplex (double-sided), Orientation (portrait/landscape), Tray settings (paper size/type per tray), Quality (draft/normal/best = DPI)
- [x] 🆕 **Inkjet maintenance** — clean printheads (auto-clean wastes ink), replace cartridges, roller/feeder cleaning, clear jams (open access covers in sequence)
- [x] 🆕 **Thermal printer maintenance** — replace thermal paper (right side up!), clean heating element, remove debris from platen roller
- [x] 🆕 **Impact printer maintenance** — replace ribbon (ink-soaked cloth), printhead pins, tractor-feed paper
- [x] 🆕 **Laser printer maintenance kit** — fuser, rollers, transfer components; replace on schedule (every 200K-300K pages); calibrate color after maintenance

---

## 4.0 Virtualization & Cloud Computing (11%)

### Objective 4.1 — Virtualization Concepts

- [x] Type 1 (bare-metal) vs Type 2 (hosted) hypervisors
- [x] Guest OS vs host OS; VM resource allocation (vCPU, vRAM, vDisk)
- [x] Snapshots — point-in-time capture; for testing NOT backup
- [x] Network modes: Bridged / NAT / Host-only
- [x] Intel VT-x / AMD-V; Containers vs VMs
- [x] 🆕 **Purpose of virtual machines**:
    - Sandbox — isolated environment to test malware or untrusted software
    - Test/development — spin up and destroy without affecting production
    - Application virtualization — run legacy apps (XP-era software) on modern OS
    - Cross-platform virtualization — run macOS apps on Windows, etc.
- [x] 🆕 **VDI (Virtual Desktop Infrastructure)** — centralized virtual desktops served to thin clients; all processing on server; benefits: easier management, patch once, secure (no data on endpoint)
- [x] 🆕 **Containers** — OS-level virtualization; share host kernel; Docker is most common; lightweight (MB not GB); faster start; less isolation than VM; great for microservices
- [x] 🆕 **VM security requirements** — network isolation (separate VLANs); resource limits (prevent VM escapes using CPU/RAM exhaustion); encrypted virtual disks; snapshot policies
- [x] 🆕 **Community cloud** — shared between organizations with similar requirements (e.g., government agencies, healthcare orgs); hybrid of public and private
- [x] 🆕 **FaaS (Function as a Service)** — serverless computing; run code in response to events without managing servers; AWS Lambda, Azure Functions

### Objective 4.2 — Cloud Computing Concepts

- [x] IaaS / PaaS / SaaS definitions and examples
- [x] Shared responsibility model
- [x] Public / Private / Hybrid cloud
- [x] Rapid elasticity; metered billing; CDN
- [x] 🆕 **Community cloud** — multi-tenant but restricted to specific organizations with shared concerns
- [x] 🆕 **Multitenancy** — multiple customers share same physical infrastructure; isolated logically; cost efficiency
- [x] 🆕 **Shared vs dedicated resources** — shared = multitenant (cheaper); dedicated = single tenant (more expensive, more control)
- [x] 🆕 **Metered utilization — ingress/egress** — data INTO cloud often free; data OUT (egress) costs money; important for cloud cost management
- [x] 🆕 **File synchronization** — OneDrive, Google Drive, Dropbox sync files between devices and cloud; conflict resolution when same file edited simultaneously
- [x] 🆕 **XaaS (Anything as a Service)** — umbrella term covering all cloud service models including IaaS, PaaS, SaaS, FaaS, DaaS, etc.

---

## 5.0 Hardware & Network Troubleshooting (28%)

### Objective 5.1 — Troubleshoot Motherboards, RAM, CPUs, Power

- [x] No POST → check power → reseat RAM → remove expansion cards
- [x] BSOD — read stop code; check Event Viewer
- [x] CPU overheating → reapply thermal paste → clean fans
- [x] Capacitor bulge → replace motherboard
- [x] System powers off randomly → PSU failing or overheating
- [x] 🆕 **POST beeps** — AMI BIOS specific codes:
    - 1 short = POST passed OK
    - 1 long + 2 short = Video card failure
    - 2 short = Memory parity error
    - Continuous = Power or stuck key
    - 3 short = RAM failure (base 64K)
- [x] 🆕 **Proprietary crash screens** — Windows BSOD; macOS Kernel Panic (dark screen + restart); Linux Kernel Oops/Panic
- [x] 🆕 **Blank screen on POST** — check monitor cable and input source FIRST before assuming motherboard failure; test with known-good monitor
- [x] 🆕 **Unusual noise** — HDD clicking = head failure (back up NOW); fan grinding = bearing failure; coil whine = PSU/GPU electrical noise
- [x] 🆕 **Inaccurate system date/time** — CMOS battery dead; replace CR2032; re-enter BIOS settings
- [x] 🆕 **Burning smell** — capacitors; PSU failure; electrolytic capacitor overheating; immediately power off

### Objective 5.2 — Troubleshoot Drives & RAID

- [x] SMART failure → back up immediately
- [x] HDD clicking → mechanical failure → back up immediately
- [x] 🆕 **LED status indicators** — solid green = OK; flashing amber = RAID degraded; red = drive failed (depends on controller)
- [x] 🆕 **Grinding noises** — HDD mechanical failure; NOT a normal sound; imminent failure
- [x] 🆕 **Bootable device not found** — check boot order in UEFI; check SATA cable; check if drive appears in BIOS; try different SATA port
- [x] 🆕 **Data loss / corruption** — can be hardware (bad sectors) or software (filesystem corruption); run `chkdsk /f /r`
- [x] 🆕 **RAID failure scenarios**:
    - RAID 0 — any drive fails = total data loss
    - RAID 1 — one drive fails = still operational; replace drive, array rebuilds
    - RAID 5 — one drive fails = degraded mode; replace drive, rebuild from parity
    - RAID 6 — two drives can fail simultaneously; more rebuild time
- [x] 🆕 **Extended read/write times** — drive is struggling; increased seek time; early failure indicator; back up immediately
- [x] 🆕 **Low IOPS** — Input/Output Operations Per Second; HDD = ~100-200 IOPS; SSD = 10K-500K IOPS; if SSD shows HDD-level IOPS, check for thermal throttling or dying NAND
- [x] 🆕 **Missing drives in OS / array missing** — check SATA/power cable; check RAID controller BIOS; may need to re-import foreign array

### Objective 5.3 — Troubleshoot Video, Projector & Display

- [x] 🆕 **Incorrect input source** — monitor set to HDMI but PC using DisplayPort; use monitor's OSD menu to change input
- [x] 🆕 **Physical cabling issues** — loose HDMI; bent pins on VGA; cable longer than spec
- [x] 🆕 **Burnt-out bulb** — projector lamp; symptoms: dim image, warning light on projector; replace lamp module
- [x] 🆕 **Fuzzy / distorted image** — wrong resolution for native display; check display scaling; set to native resolution
- [x] 🆕 **Display burn-in** — permanent ghost image on OLED/plasma; use screensavers; avoid static images; pixel refresh feature
- [x] 🆕 **Dead pixels** — permanently off (black) or stuck (fixed color); single dead pixel = warranty claim; cluster = replace panel
- [x] 🆕 **Flashing / flickering screen** — refresh rate mismatch; loose cable; failing backlight; driver issue
- [x] 🆕 **Incorrect color display** — wrong color profile; calibrate with DisplayCAL; check GPU color settings
- [x] 🆕 **Dim image** — failing backlight (laptop inverter or LED); BIOS brightness setting; adaptive brightness enabled
- [x] 🆕 **Intermittent projector shutdown** — overheating (blocked vents); lamp life exceeded; thermal protection triggering

### Objective 5.5 — Troubleshoot Network Issues

- [x] Full "no internet" troubleshooting flow (5 ping steps)
- [x] ipconfig / ip addr / ping / tracert / nslookup / netstat / arp / route print
- [x] 🆕 **Intermittent wireless connectivity** — check for interference (2.4 GHz congestion); driver updates; distance from AP; check event logs for disconnect reason
- [x] 🆕 **Slow network speeds** — run `iperf3` to test actual throughput; check duplex mismatch (auto-negotiate vs forced full-duplex); check for packet loss with `ping -t`
- [x] 🆕 **Limited connectivity** — IP address obtained but no internet; check gateway, DNS; try pinging gateway IP
- [x] 🆕 **Jitter** — variation in packet delay; affects VoIP and video calls; caused by congestion or poor Wi-Fi; QoS can prioritize VoIP traffic
- [x] 🆕 **Poor VoIP quality** — jitter, packet loss, latency; configure QoS to prioritize UDP voice packets; use wired connection
- [x] 🆕 **Port flapping** — switch port repeatedly going up/down; causes: bad cable, NIC failure, STP loop; check switch logs
- [x] 🆕 **High latency** — run `tracert`; identify which hop is slow; latency >150ms causes noticeable delay in VoIP
- [x] 🆕 **External interference** — 2.4 GHz: microwaves, cordless phones, Bluetooth, neighboring Wi-Fi; use Wi-Fi analyzer to identify; move to 5 GHz
- [x] 🆕 **Authentication failures** — wrong WPA2 PSK; RADIUS server unreachable; certificate mismatch; check client logs
- [x] 🆕 **Intermittent internet connectivity** — ISP issue; check modem logs; test with direct ethernet from modem; ping ISP gateway

### Objective 5.6 — Troubleshoot Printers

- [x] 🆕 **Lines down printed pages** — laser: dirty drum or contaminated transfer roller; inkjet: clogged nozzle; run cleaning cycle
- [x] 🆕 **Garbled print** — driver mismatch; PCL vs PostScript conflict; corrupt print job; update/reinstall driver
- [x] 🆕 **Paper jams** — clear in direction of paper travel; never yank backwards; check feed rollers for wear; use correct paper weight 
- [x] 🆕 **Faded prints** — laser: low toner (gently shake cartridge); inkjet: low ink; wrong paper type
- [x] 🆕 **Paper not feeding** — dirty/worn feed rollers; wrong paper size in tray setting; paper not fanned properly
- [x] 🆕 **Multipage misfeed** — static electricity in paper stack; fan pages before loading; check humidity
- [x] 🆕 **Multiple prints pending in queue** — clear spooler: stop Print Spooler service → delete queue files → restart service
- [x] 🆕 **Speckling / toner scatter** — laser: damaged drum; replace drum unit (separate from toner cartridge)
- [x] 🆕 **Double/echo images (ghosting)** — laser: residual toner from previous page; replace drum unit or clean transfer roller
- [x] 🆕 **Grinding noise** — laser: worn rollers or foreign object in paper path; open all access covers and inspect
- [x] 🆕 **Finishing issues** — staple jams (clear staple cartridge), hole punch (empty punch waste box), binding errors
- [x] 🆕 **Incorrect page orientation** — check application print settings vs printer default; override in Print dialog
- [x] 🆕 **Tray not recognized** — reseat tray fully; check tray sensor; update firmware
- [x] 🆕 **Connectivity issues** — USB: try different port; network: verify IP, ping printer; wireless: check SSID and credentials
- [x] 🆕 **Frozen print queue** — spooler service hung; restart it via `services.msc`

---

---

# PHASE 2 — CompTIA A+ Core 2 (220-1202)

> **Exam Weight: OS 28% | Security 28% | Software Troubleshooting 23% | Operational Procedures 21%**

---

## 1.0 Operating Systems (28%)

### Objective 1.1 — OS Types & Purposes

- [ ] Windows editions: Home / Pro / Enterprise/Education
- [ ] Windows 11 minimum requirements (TPM 2.0, Secure Boot, 64-bit CPU, 4GB RAM, 64GB storage)
- [ ] macOS: APFS, Finder, Activity Monitor, Disk Utility, FileVault, Time Machine, DMG files, Terminal (zsh)
- [ ] Linux: open-source, case-sensitive, file-based; common distros
- [ ] Linux file system hierarchy: /, /home, /etc, /var, /tmp, /usr, /bin, /sbin, /dev, /proc
- [ ] 🆕 **Chrome OS** — Google's OS; Linux-based; runs web apps and Android apps; Chromebook is the hardware; very limited local storage; cloud-centric; popular in education
- [ ] 🆕 **Various filesystem types**:
    - NTFS — Windows standard; ACL permissions, EFS encryption, journaling, large files
    - ReFS (Resilient File System) — Windows Server; self-healing; better for large storage arrays; no bootable (can't be C:)
    - FAT32 — max 4 GB file size, max 8 TB volume; used on USB drives for compatibility
    - exFAT — extended FAT; no 4 GB file limit; cross-platform (Windows+Mac); for flash storage
    - ext4 — Linux standard; journaling; large file support; most common Linux filesystem
    - XFS — Linux high-performance; great for large files; used in RHEL/CentOS
    - APFS — Apple File System; default macOS/iOS; snapshots, encryption, space sharing
- [ ] 🆕 **Vendor life cycle limitations**:
    - EOL (End of Life) — vendor stops patches and support; security risk; upgrade or isolate
    - End of Mainstream Support — no new features, only security patches
    - Windows 10 EOL: October 2025; Windows 11 is current

### Objective 1.2 — OS Installation & Upgrades

- [ ] Clean install vs upgrade
- [ ] Windows Media Creation Tool; boot order in UEFI
- [ ] Sysprep — generalizes image for deployment
- [ ] 🆕 **Boot methods**:
    - USB — most common; requires bootable USB (Rufus, Ventoy, WMC Tool)
    - Network (PXE) — Preboot eXecution Environment; boots from network server; used for imaging many PCs
    - External/hot-swappable drive — eSATA or USB external drive
    - Internal partition — recovery partition on same drive; Windows RE lives here
    - Internet-based — Windows 10/11 can install directly from Microsoft servers (cloud reset)
    - Solid-state/flash — boot from NVMe/SSD external enclosure
- [ ] 🆕 **Types of installations**:
    - Clean install — wipes drive; fresh OS; recommended for major upgrades
    - Upgrade — keeps files, apps, settings; risk of carrying over issues
    - Repair install — repairs system files while keeping user data (Windows: run setup.exe from within OS)
    - Unattended installation — answer file (autounattend.xml) automates all prompts; used for mass deployment
    - Remote network installation — PXE boot pulls image from WDS/MDT server
    - Image deployment — Sysprep + WIM image + DISM/MDT; clone to multiple machines
    - Multiboot — multiple OSes on same machine; bootloader menu; must install Windows LAST (or repair BCD)
- [ ] 🆕 **Partition methods**:
    - MBR — legacy; max 2 TB; max 4 primary; required for legacy BIOS
    - GPT — modern; max 9.4 ZB; 128 partitions; required for UEFI Secure Boot; has protective MBR
- [ ] 🆕 **Drive format considerations** — during install, format as NTFS; decide partition scheme before starting

### Objective 1.3 — Microsoft Windows Features & Tools

- [ ] Full Windows Administration Tools table (Task Manager, Resource Monitor, Event Viewer, Device Manager, Disk Management, Services, Task Scheduler, Group Policy Editor, Computer Management, System Config, System Info, Performance Monitor, Registry Editor, Local Security Policy)
- [ ] 🆕 **Certificate Manager (certmgr.msc)** — manage digital certificates for the current user; personal, trusted roots, intermediate CAs; critical for troubleshooting SSL/TLS issues and smart card auth
- [ ] 🆕 **Local Users and Groups (lusrmgr.msc)** — manage local user accounts and groups; available in Pro/Enterprise (not Home); create local accounts, set passwords, manage group membership
- [ ] 🆕 **Disk Cleanup (cleanmgr)** — removes temp files, Recycle Bin, Windows Update cache; safe for routine maintenance; "Clean up system files" = more aggressive cleanup
- [ ] 🆕 **Disk Defragment (dfrgui)** — defragments HDDs; SSDs should NOT be defragmented (trimmed instead); Windows auto-schedules for HDDs
- [ ] 🆕 **Windows Settings vs Control Panel** — Settings (modern, tablet-friendly, Win 10/11); Control Panel (legacy, disappearing); some features only in one or the other; know both paths

### Objective 1.4 — Windows Command-Line Tools

- [ ] cd, dir, mkdir, rmdir, copy, xcopy, robocopy, del, sfc, DISM, chkdsk, diskpart, shutdown, tasklist, taskkill, net user, net localgroup, gpupdate, gpresult, netsh
- [ ] PowerShell equivalents
- [ ] 🆕 **`format`** — formats a volume; `format C: /fs:NTFS /q` (quick format); used inside `diskpart` workflow
- [ ] 🆕 **`bootrec`** — repairs Windows boot record; WinRE only:
    - `/fixmbr` — rewrites MBR
    - `/fixboot` — rewrites boot sector
    - `/rebuildbcd` — scans drives and rebuilds BCD store (most useful)
- [ ] 🆕 **`bcdedit`** — Boot Configuration Data editor; modify boot menu entries; change boot timeout; `bcdedit /enum` shows all entries
- [ ] 🆕 **`winver`** — shows Windows version in a GUI popup; quick way to check exact build number
- [ ] 🆕 **`dxdiag`** — DirectX Diagnostic Tool; shows GPU, DirectX version, display driver; used for gaming support
- [ ] 🆕 **`mmc`** — Microsoft Management Console; framework for snap-ins; custom consoles by adding specific snap-ins

### Objective 1.5 — Configure Windows Settings

- [ ] 🆕 **Display settings** — resolution, refresh rate, scale (125%, 150%); multiple monitors (extend/mirror/second screen only); HDR toggle
- [ ] 🆕 **Power settings** — Sleep, Hibernate, Fast Startup; Balanced vs High Performance vs Power Saver; wake timers; `powercfg /batteryreport`; `powercfg /sleepstudy`
- [ ] 🆕 **Network settings** — adapter settings; static IP config; metered connection toggle (prevents background downloads)
- [ ] 🆕 **User account settings** — change account type (Standard/Admin); password settings; picture/PIN; sign-in options (Hello PIN, fingerprint, password)
- [ ] 🆕 **App settings** — default apps; startup apps (Settings > Apps > Startup); optional features (add RSAT tools, Hyper-V)
- [ ] 🆕 **Accessibility settings** — Magnifier, Narrator, High Contrast, Sticky Keys, Filter Keys; important for ADA compliance in enterprise

### Objective 1.6 — Linux Client/Desktop OS

- [ ] File management: ls, pwd, mv, cp, rm, chmod, chown, grep, find
- [ ] sudo; package managers (apt, yum/dnf, pacman)
- [ ] File permissions: rwxr-xr-x notation; chmod 755; chown
- [ ] 🆕 **Common Linux configuration files**:
    - `/etc/passwd` — user account info (username, UID, GID, home dir, shell); NOT passwords (that's shadow)
    - `/etc/shadow` — hashed passwords; only root can read
    - `/etc/hosts` — local DNS override; maps hostnames to IPs; checked before DNS
    - `/etc/fstab` — filesystem mount table; defines what mounts at boot
    - `/etc/resolv.conf` — DNS server configuration
- [ ] 🆕 **Linux OS components**:
    - **Kernel** — core OS; manages hardware, processes, memory; `uname -r` shows kernel version
    - **systemd** — init system and service manager; replaced SysVinit; `systemctl start/stop/enable/disable`
    - **Bootloader** — GRUB2 most common; loads kernel; edit `/etc/default/grub`
- [ ] 🆕 **Additional Linux commands**:
    - `ps aux` — list all running processes
    - `top` / `htop` — real-time process monitor
    - `kill -9 PID` — force-kill process by PID
    - `df -h` — disk space usage
    - `du -sh /path` — directory size
    - `tar -czvf archive.tar.gz /path` — compress files
    - `ssh user@host` — remote shell
    - `scp file user@host:/path` — secure file copy
    - `systemctl status sshd` — check SSH service status
    - `journalctl -xe` — view system logs (systemd)
    - `ip addr` / `ip route` — network configuration

### Objective 1.7 — macOS Features (Expanded)

- [ ] APFS, Finder, Activity Monitor, Disk Utility, FileVault, Time Machine, DMG files, Terminal (zsh)
- [ ] 🆕 **macOS Spotlight** — `Cmd+Space`; universal search; find files, apps, calculations, web; faster than File Explorer search
- [ ] 🆕 **macOS Mission Control** — `F3` or swipe up with 3 fingers; shows all open windows and Spaces (virtual desktops)
- [ ] 🆕 **Force Quit (Cmd+Option+Esc)** — equivalent of Task Manager for ending hung apps
- [ ] 🆕 **macOS keychain** — stores passwords, certificates, secure notes; auto-fills passwords; can unlock with Touch ID; equivalent to Windows Credential Manager
- [ ] 🆕 **Xcode Command Line Tools** — provides `git`, `make`, `clang`; needed for developer tools on Mac
- [ ] 🆕 **macOS System Preferences / System Settings** — control panel equivalent; General, Security & Privacy, Network, Users & Groups, Sharing
- [ ] 🆕 **macOS Remote Desktop / Screen Sharing** — VNC-based; enable in System Settings > Sharing; or use Apple Remote Desktop (enterprise tool)
- [ ] 🆕 **AirDrop** — wireless file transfer between Apple devices; uses Wi-Fi + Bluetooth; no internet required
- [ ] 🆕 **Homebrew** — third-party package manager for macOS; `brew install` for CLI tools; equivalent to `apt` on Ubuntu

### Objective 1.8 — Application Installation & Requirements

- [ ] 🆕 **System requirements for applications**:
    - 32-bit vs 64-bit apps — 32-bit apps run on 64-bit Windows (WOW64 layer); 64-bit apps cannot run on 32-bit OS; 32-bit apps max 4 GB RAM
    - Dedicated vs integrated GPU — games/video editing require discrete GPU; check VRAM (GPU RAM) requirements
    - VRAM requirements — 4 GB minimum for 1080p gaming; 8 GB+ for 4K; 16 GB+ for AI/ML workloads
    - RAM requirements — check minimum and recommended; leave headroom for OS
    - CPU requirements — clock speed and core count; some apps are single-threaded (clock speed matters); others multi-threaded (core count matters)
    - Storage requirements — installation size + working space; SSD strongly recommended for productivity apps
    - External hardware tokens — USB dongle license keys (iLok, HASP); enterprise software anti-piracy; if lost, license lost
    - OS compatibility — 32-bit vs 64-bit; minimum OS version; Windows 10 vs 11 differences
- [ ] 🆕 **Distribution methods**:
    - Physical media (optical disc, USB) — legacy; decreasing
    - Downloadable / internet-based — most common; EXE/MSI/DMG/PKG
    - ISO image — disk image; mount with Windows or burn to USB
    - App stores — Microsoft Store, Mac App Store, Google Play; managed, sandboxed
    - Enterprise deployment — SCCM / Intune / GPO; push to endpoints silently
- [ ] 🆕 **Cloud-based productivity tools** — Microsoft 365, Google Workspace; install companion apps; configure account sync; Teams, OneDrive, Drive desktop clients

---

## 2.0 Security (28%)

### Objective 2.1 — Security Measures & Their Purposes

- [ ] CIA Triad (Confidentiality / Integrity / Availability)
- [ ] Least Privilege; Zero Trust; Defense in Depth; MFA; Separation of duties
- [ ] 🆕 **Physical security measures**:
    - Cable locks — Kensington lock; secure laptops in public spaces
    - Server rack locks — secure access to server hardware
    - Badge readers — access control to data centers/server rooms; log entry/exit
    - Biometric door locks — fingerprint/retina for server rooms
    - Visitor logs — sign in/out; escort policy for non-staff
    - Camera systems — CCTV for surveillance; motion-triggered
    - Faraday cage — blocks all wireless signals; used in sensitive compartmented info facilities (SCIF)
- [ ] 🆕 **Logical security measures**:
    - Principle of least privilege — minimum access to do the job; review and revoke excess access
    - Access control lists (ACL) — define who can access what on network devices and filesystems
    - IAM (Identity and Access Management) — centralized control of identities and their access
    - SSO (Single Sign-On) — one login grants access to multiple apps; SAML 2.0, OAuth, OpenID Connect
    - Password managers — LastPass, Bitwarden, 1Password; store complex unique passwords
- [ ] 🆕 **Encryption concepts**:
    - Symmetric encryption — same key encrypts and decrypts; fast; AES-256 standard; key sharing is the problem
    - Asymmetric encryption — public key encrypts, private key decrypts; RSA, ECC; used in TLS, SSH, PGP
    - End-to-end encryption (E2EE) — only sender and recipient can decrypt; Signal, WhatsApp
    - Encryption in transit — TLS/HTTPS; protects data moving over network
    - Encryption at rest — BitLocker, FileVault, EFS; protects stored data if drive is stolen
- [ ] 🆕 **Active Directory security** — already covered in your notes above

### Objective 2.2 — Windows OS Security Settings

- [ ] UAC; Windows Defender; Windows Firewall; BitLocker; EFS; AppLocker; Credential Manager
- [ ] Password policy settings; account lockout policy
- [ ] 🆕 **Users and Groups security**:
    - Standard user vs. Administrator — standard user cannot install software or change system settings without UAC prompt
    - Local vs. domain accounts — local = only on that PC; domain = authenticated by AD DC
    - Guest account — disabled by default; NEVER enable
    - Built-in Administrator account — rename and disable; create separate named admin account
- [ ] 🆕 **NTFS permissions** — read, read & execute, list folder contents, write, modify, full control; inherited vs explicit; deny overrides allow
- [ ] 🆕 **Shared folder permissions** — full control, change, read; combined with NTFS (most restrictive wins)
- [ ] 🆕 **Windows Defender Firewall with Advanced Security** — inbound/outbound rules; create rules by program, port, or protocol; domain/private/public profiles
- [ ] 🆕 **Run as administrator** — right-click > Run as administrator; launches with elevated privileges; triggers UAC

### Objective 2.3 — Wireless Security Protocols & Authentication

- [ ] WEP (broken) / WPA (TKIP) / WPA2 (AES/CCMP) / WPA3 (SAE)
- [ ] WPA2 Personal (PSK) vs WPA2 Enterprise (802.1X/RADIUS)
- [ ] Evil twin attack; disable WPS
- [ ] 🆕 **WPA3 — SAE (Simultaneous Authentication of Equals)** — replaces PSK; resistant to offline dictionary attacks; forward secrecy (past traffic cannot be decrypted if key later compromised)
- [ ] 🆕 **RADIUS for wireless** — clients authenticate with individual credentials; RADIUS server validates against AD; each user has unique session keys
- [ ] 🆕 **WPS vulnerabilities** — 8-digit PIN brute-forceable in hours (Pixie Dust attack); always disable WPS
- [ ] 🆕 **TKIP vs AES/CCMP** — TKIP (used in WPA) is deprecated/broken; AES-CCMP (used in WPA2/3) is current standard
- [ ] 🆕 **Open network / captive portal** — no encryption; used in hotels/coffee shops; anything transmitted is readable; always use VPN on open networks
- [ ] 🆕 **Certificate-based authentication (EAP-TLS)** — strongest wireless auth; each device has a certificate; requires PKI; immune to credential theft

### Objective 2.4 — Malware Types & Detection/Removal

- [ ] Virus / Worm / Trojan / Ransomware / Spyware / Adware / Rootkit / Bootkit / Fileless malware / Cryptominer / Botnet
- [ ] Malware removal 7-step procedure
- [ ] 🆕 **PUP (Potentially Unwanted Program)** — not technically malware but unwanted; browser toolbars, bundled freeware; detected by Windows Defender; remove via Programs and Features
- [ ] 🆕 **Keylogger** — type of spyware; records every keystroke; captures passwords and sensitive data; can be hardware (USB dongle between keyboard and PC) or software
- [ ] 🆕 **Man-in-the-browser (MitB)** — malware modifies browser transactions in real-time; targets online banking; bypasses HTTPS; defeated by out-of-band authentication
- [ ] 🆕 **Malware tools/methods for detection and removal**:
    - Windows Defender (built-in, real-time)
    - Malwarebytes (second-opinion scanner; free for manual scan)
    - ESET, Sophos, Trend Micro (enterprise AV)
    - VirusTotal (upload file to check against 70+ AV engines)
    - Process Explorer / Autoruns (Sysinternals) — identify malicious processes and startup entries
    - Offline scanning — boot from AV rescue disk; scan without OS running (bypasses rootkits)
    - Safe Mode scan — disables most malware auto-start
- [ ] 🆕 **Quarantine** — isolate infected file without deleting; preserves for analysis; AV quarantine folder

### Objective 2.5 — Social Engineering Attacks, Threats & Vulnerabilities

- [ ] Phishing / Spear phishing / Whaling / Vishing / Smishing / Tailgating / Shoulder surfing / Dumpster diving / Pretexting / Impersonation
- [ ] 🆕 **BEC (Business Email Compromise)** — attacker impersonates executive (CEO, CFO) via email; tricks finance into wire transfer; most costly cybercrime by dollar amount
- [ ] 🆕 **Watering hole attack** — attacker compromises a website the target frequently visits; victim's browser is exploited when visiting
- [ ] 🆕 **Credential harvesting** — fake login pages capture username/password; check URL carefully; use password managers (won't autofill on wrong domain)
- [ ] 🆕 **Insider threat** — malicious or negligent employee; has legitimate access; hardest to detect; mitigated by least privilege, DLP, behavior analytics
- [ ] 🆕 **Zero-day vulnerability** — exploit for which no patch exists yet; vendor has zero days to fix; extremely dangerous; mitigated by defense-in-depth
- [ ] 🆕 **Unpatched software vulnerabilities** — most breaches exploit known, patchable vulnerabilities; patch management is critical
- [ ] 🆕 **Weak password / default credentials** — default admin/admin or admin/password; must change all defaults immediately on every device

### Objective 2.6 — SOHO Malware Prevention & Security

- [ ] First steps for new router; WPA3/WPA2; disable WPS; disable UPnP; guest VLAN
- [ ] 🆕 **SOHO malware prevention**:
    - Keep all firmware/software updated (routers, devices, OS)
    - Enable Windows Defender real-time protection
    - Email filtering — use spam filtering (Google/Microsoft built-in or third-party)
    - DNS filtering — use OpenDNS or NextDNS to block malicious domains
    - Browser extensions — uBlock Origin (ad/malware blocker)
    - Train users — don't click links; verify before downloading; report suspicious emails
- [ ] 🆕 **Home router security hardening**:
    - Change default admin credentials (web UI login, NOT Wi-Fi password)
    - Update firmware regularly
    - Use WPA3 or WPA2-AES (never TKIP or WEP)
    - Disable WPS (all variants)
    - Disable remote management (SSH/telnet from WAN)
    - Disable UPnP
    - Enable DoS protection if available
    - Check connected devices list regularly for unknown devices

### Objective 2.7 — Browser Security Settings

- [ ] 🆕 **Browser security configuration**:
    - Trusted vs untrusted sites — add to IE/Edge trusted zones for SSO intranet sites
    - Certificate errors — expired/self-signed cert; DO NOT proceed on corporate systems without investigation
    - Pop-up blockers — enable; disable only for known-good sites
    - Private/incognito browsing — no local history/cookies saved; NOT truly anonymous; useful for testing auth issues
    - Ad blockers — reduce malvertising risk; uBlock Origin recommended
    - Password manager integration — built-in (Chrome/Edge) or third-party; use unique passwords for every site
    - Extensions/add-ons — audit and remove unnecessary; each extension has access to your browsing data
    - Clear browsing data — cache, cookies, history; fixes many loading/auth issues
    - HTTPS-only mode — available in Firefox/Chrome; forces HTTPS or warns; enable for better security
    - Site permissions — camera, microphone, location, notifications; review and restrict per-site

---

## 3.0 Software Troubleshooting (23%)

### Objective 3.1 — Troubleshoot Windows OS Issues

- [ ] System won't boot → Safe Mode → WinRE → Startup Repair
- [ ] BSOD — stop codes; Event Viewer
- [ ] SFC → DISM → SFC again workflow
- [ ] Profile corruption
- [ ] DLL missing error
- [ ] 🆕 **Safe Mode types**:
    - Safe Mode — minimal drivers; no network
    - Safe Mode with Networking — adds network drivers; can download tools
    - Safe Mode with Command Prompt — no Explorer GUI; command line only; for heavy repairs
- [ ] 🆕 **Common Windows OS issues**:
    - Slow boot — check startup programs (Task Manager > Startup); disable unnecessary; check Event Viewer for boot delays
    - Slow performance — check RAM (is it maxed?), CPU (thermal throttling?), disk (SSD vs HDD, SMART status)
    - Application crashes — Event Viewer > Windows Logs > Application; look for crash reports and DLL faults
    - Windows Update failures — error codes; run Windows Update Troubleshooter; DISM to repair WU component store
    - Failed login — check Caps Lock; reset password; check if account is locked; check if profile is corrupt (loads TEMP profile)
    - Service not starting — Services.msc; check dependencies; check log for specific error; check permissions on service account

### Objective 3.2 — Troubleshoot Mobile OS & App Issues

- [ ] Battery drain; overheating; no SIM detected; app crashes; slow performance
- [ ] 🆕 **Mobile OS update failures** — insufficient storage; poor Wi-Fi; try update via USB to computer (iTunes/Finder for iOS; ADB for Android)
- [ ] 🆕 **App not updating** — clear Play Store / App Store cache; check payment method on account; check storage
- [ ] 🆕 **Mobile device sync issues** — check account credentials; check MDM enrollment status; re-enroll if needed
- [ ] 🆕 **High data usage** — identify culprit app in Settings > Data Usage; background data restriction; set data warnings/limits

### Objective 3.3 — Troubleshoot Mobile OS Security Issues

- [ ] 🆕 **Mobile device locked out** — Android: Google account recovery, Factory Reset Protection; iOS: iCloud recovery, Apple ID reset
- [ ] 🆕 **Unauthorized account access** — enable 2FA on all mobile accounts; check sign-in logs; change all passwords; revoke sessions
- [ ] 🆕 **Leaked corporate data from mobile** — remote selective wipe via MDM; review MAM policies; enable conditional access
- [ ] 🆕 **Profile issues** — MDM configuration profile not installing; check enrollment status; re-enroll device; ensure correct Apple/Android enterprise account

### Objective 3.4 — Troubleshoot PC Security Issues

- [ ] Malware removal 7-step procedure
- [ ] Ransomware — offline backups; patching; email filtering
- [ ] 🆕 **Common PC security symptoms**:
    - Pop-ups / browser redirects — adware or browser hijacker; check extensions; reset browser settings
    - Renamed/encrypted files — ransomware; disconnect from network immediately; restore from backup
    - Certificate warnings — malware intercepting TLS; check proxy settings; run AV scan
    - Spam sent from your email — account compromised; change password + enable MFA; check email forwarding rules
    - Unusual network activity — unknown connections in `netstat -an`; check firewall logs; run malware scan
    - Disabled security tools — malware often kills AV/Defender; boot offline AV disc
    - Missing/changed files — check Recycle Bin; check Previous Versions; check backup; may indicate ransomware
    - High resource usage — check Task Manager; research unknown processes; may be cryptominer

---

## 4.0 Operational Procedures (21%)

### Objective 4.1 — Documentation & Support Systems

- [ ] Change management; CAB; rollback plan; asset inventory; network diagrams; knowledge base; SOP; incident documentation
- [ ] 🆕 **CMDB (Configuration Management Database)** — tracks all IT assets and their relationships; know what's connected to what; used for change impact analysis; ServiceNow is the most popular CMDB
- [ ] 🆕 **Ticketing system** — IT service management (ITSM); ServiceNow, Jira Service Management, Zendesk, Freshdesk; record all incidents, requests, changes; assigned severity/priority
- [ ] 🆕 **Regulatory and business compliance requirements** — HIPAA (healthcare), PCI-DSS (credit card), GDPR (EU data), RA-ITRIP (PH Data Privacy Act 2012); compliance affects how data is stored, accessed, and destroyed
- [ ] 🆕 **Splash screens** — used by organizations to display legal notices/acceptable use policy before login; required for compliance in many regulated industries

### Objective 4.2 — Change Management Procedures

- [ ] Change management flow; CAB; rollback plan
- [ ] 🆕 **Change management key concepts**:
    - RFC (Request for Change) — formal document submitted for review
    - Standard change — pre-approved, low-risk, routine (e.g., password reset)
    - Normal change — must go through CAB review
    - Emergency change — expedited; done first, documented after; only for critical outages
    - Backout plan — same as rollback plan; must exist BEFORE making any change
    - Change freeze — periods (holidays, year-end) where no changes are allowed

### Objective 4.3 — Backup & Recovery Methods

- [ ] 3-2-1 rule; Full / Incremental / Differential; RPO / RTO; testing backups; Windows Backup options
- [ ] 🆕 **GFS (Grandfather-Father-Son) backup rotation** — daily (son), weekly (father), monthly (grandfather); tape rotation strategy; minimizes media wear
- [ ] 🆕 **Onsite vs offsite backup** — onsite: fast restore; offsite: disaster recovery; cloud backup = offsite by definition
- [ ] 🆕 **Synthetic full backup** — server-side full backup created from previous full + incrementals; no need to re-send all data from client; storage-efficient
- [ ] 🆕 **Backup verification** — after backup, verify checksum/hash; test restore periodically; backup without restore test = not trustworthy
- [ ] 🆕 **Windows File History** — backs up user libraries continuously to external drive or network; easy self-service restore; NOT a full system backup

### Objective 4.4 — Safety Procedures

- [ ] ESD; anti-static wrist strap; anti-static mat; anti-static bags; SDS; toner vacuum; battery disposal; CRT disposal; Class C fire; lifting technique
- [ ] 🆕 **Proper component handling**:
    - Hold PCBs by edges; never touch traces or chips
    - Store components on anti-static mat or in anti-static bag
    - Ground yourself before opening case; touch metal chassis
- [ ] 🆕 **Toner handling** — toner particles are carcinogenic if inhaled; use NIOSH-rated mask for toner spills; use toner vacuum or damp cloth only
- [ ] 🆕 **MSDS / SDS** — Safety Data Sheet; required for all chemicals; lists hazards, first aid, disposal; OSHA requires on-site
- [ ] 🆕 **Equipment disposal / recycling**:
    - CRT monitors — lead and high-voltage capacitors; hazardous waste facility
    - Toner cartridges — many manufacturers have return/recycle programs
    - Mobile devices — battery recycling programs; Call2Recycle
    - Batteries (non-Li-Ion) — alkaline can go in trash in most US states; other types are hazardous
    - Electronics (WEEE) — E-waste recycling centers; data destruction first

### Objective 4.5 — Environmental Impacts & Controls

- [ ] 🆕 **Temperature and humidity controls** — data centers: 64-80°F (18-27°C), 45-55% relative humidity; humidity too low = ESD; too high = condensation
- [ ] 🆕 **Proper ventilation** — hot aisle / cold aisle containment in data centers; airflow from front to back of rack; blanking panels in unused rack slots
- [ ] 🆕 **Power protection**:
    - Surge suppressor — protects from voltage spikes; use on all equipment
    - UPS — battery backup; VA rating must exceed connected load; runtime varies by battery capacity
    - Line conditioner — smooths voltage fluctuations; often built into line-interactive UPS
- [ ] 🆕 **Green IT** — ENERGY STAR ratings; power-saving modes; virtualization reduces physical hardware; responsible e-waste disposal

### Objective 4.6 — Incident Response & Forensics

- [ ] 🆕 **Incident response basics**:
    - **Chain of custody** — documented record of who handled evidence and when; required for legal admissibility
    - **Informing management / law enforcement** — when required; data breach notification laws; HIPAA breach = notify within 60 days; PCI DSS breach = notify immediately
    - **Copy of drive (data integrity)** — create forensic image (bit-for-bit copy) before analysis; use `dd` (Linux) or FTK Imager; never analyze original
    - **Write blockers** — hardware device that prevents writes to forensic drive; preserves evidence integrity
    - **Order of volatility** — collect most volatile first:
        1. CPU registers and cache
        2. RAM
        3. Swap/page file
        4. Open network connections/routing table
        5. Running processes
        6. Disk storage
        7. Remote logging / monitoring
        8. Physical configuration / network topology
        9. Archival media (backups, tapes)
    - **Incident documentation** — timeline of events, actions taken, evidence collected, escalations

### Objective 4.7 — Licensing, Regulatory Compliance & Data

- [ ] Data destruction & disposal: Overwriting, Zero-fill, Degaussing, Physical destruction, NIST 800-88
- [ ] 🆕 **Licensing types**:
    - Valid license — must have for all software; audit-ready
    - Perpetual license — one-time purchase; use forever; no subscription; e.g., Office 2021
    - Subscription license — pay monthly/annually; stops working if subscription lapses; e.g., Microsoft 365
    - Personal-use license — for one person on limited devices
    - Corporate/enterprise license — volume licensing; per seat or per device; must track installs
    - Open-source license — free to use/modify; GPL requires derivative works to also be open-source; MIT/Apache = more permissive
- [ ] 🆕 **DRM (Digital Rights Management)** — prevents unauthorized copying; built into e-books, streaming services, some software
- [ ] 🆕 **EULA (End-User License Agreement)** — legal contract for software use; agreeing to install = agreeing to EULA
- [ ] 🆕 **NDA / MNDA** — Non-Disclosure Agreement; protects company confidential info; employees sign on hire; third parties sign before receiving sensitive data
- [ ] 🆕 **Regulated data types**:
    - PII (Personally Identifiable Information) — name, SSN, address, birthdate; Protected by GDPR, Privacy Act
    - PHI (Protected Health Information) — medical records; governed by HIPAA
    - PCI data — credit card numbers; governed by PCI-DSS
    - Government-issued IDs — passports, driver's licenses; handle with strict controls
    - Data retention requirements — how long must you keep certain data? Varies by regulation and country
- [ ] 🆕 **AUP (Acceptable Use Policy)** — defines allowed and prohibited use of company IT resources; must be signed by all employees; splash screen at login as reminder

### Objective 4.8 — Communication Techniques & Professionalism

- [ ] 🆕 **Professional appearance and conduct**:
    - Present appropriate attire for environment (formal vs business casual)
    - Be punctual; if late, notify customer
    - Avoid personal interruptions (calls, texting, social media) during customer interaction
    - Use proper language; avoid jargon and acronyms with non-technical users
    - Maintain positive attitude; do not argue with customer or become defensive
- [ ] 🆕 **Effective communication**:
    - Active listening — don't interrupt; confirm understanding by repeating back ("So what I'm hearing is...")
    - Open-ended questions — "Can you describe what happens when...?" (gets more info than yes/no)
    - Clarifying questions — "When did this start?" "What changed recently?"
    - Avoid assumptions — don't assume user caused the problem; never blame the user
    - Set expectations — tell user what you're doing and how long it will take; provide updates
    - Follow up — contact user after repair to confirm satisfaction
- [ ] 🆕 **Difficult customers**:
    - Stay calm; do not escalate emotion; use empathy ("I understand how frustrating this must be")
    - Document everything said during interaction
    - Know when to escalate — to supervisor if situation cannot be resolved professionally
- [ ] 🆕 **Confidentiality**:
    - Do not share customer/company information with unauthorized parties
    - Do not discuss other users' data or IT incidents
    - Discretion when working at customer's workstation (may see sensitive data)
    - Clean desk policy — do not leave paperwork or screens visible when leaving

### Objective 4.9 — Scripting Basics

- [ ] PowerShell: Get-Process, Stop-Process, Get-Service, Get-EventLog, Set-ExecutionPolicy, Test-NetConnection
- [ ] 🆕 **Script file types**:
    - `.bat` — Windows batch file; legacy; CMD shell commands; `@echo off` suppresses output; basic automation
    - `.ps1` — PowerShell script; more powerful than batch; can interact with WMI, AD, registry, APIs
    - `.vbs` — VBScript; legacy Windows automation; still found in old enterprise environments
    - `.sh` — Bash/shell script; Linux/macOS; start with shebang (`#!/bin/bash`); `chmod +x` to make executable
    - `.js` — JavaScript; can be run as Windows Script Host (wscript/cscript) or Node.js
    - `.py` — Python; cross-platform; powerful for automation, data processing, network scripting
- [ ] 🆕 **Scripting concepts**:
    - Variables — `$name = "John"` (PS), `name="John"` (bash)
    - Loops — `for`, `while`, `foreach`
    - Conditionals — `if/else`, `switch`
    - Comments — `#` (PS/bash/Python), `REM` (batch)
    - Input/output — `Read-Host` (PS), `read` (bash), `input()` (Python)
    - Error handling — `try/catch` (PS/Python); `set -e` (bash)
- [ ] 🆕 **Common admin scripts to know**:
    - List all users in AD group (PowerShell)
    - Map network drives at logon (batch/PS)
    - Bulk reset user passwords (PS + AD module)
    - Check disk space on remote servers
    - Automate log cleanup

### Objective 4.10 — Remote Access Technologies

- [ ] RDP (port 3389); TeamViewer; AnyDesk; Quick Assist; Chrome Remote Desktop; Zoom/Teams screen sharing
- [ ] Cisco AnyConnect; Palo Alto GlobalProtect; VPN protocols; split tunneling; full tunnel
- [ ] VPN troubleshooting workflow
- [ ] 🆕 **Remote access security considerations**:
    - Never expose RDP directly to internet; use VPN + RDP or RD Gateway
    - Enable Network Level Authentication (NLA) for RDP — requires authentication before full connection
    - Use non-default port for RDP (security through obscurity — not a replacement for proper security)
    - TeamViewer/AnyDesk — review authorized access list; revoke unattended access for terminated employees
    - Least privilege for remote accounts — dedicated service accounts for RMM tools
- [ ] 🆕 **SPICE (Simple Protocol for Independent Computing Environments)** — remote display protocol for VMs; used in KVM/QEMU virtual machines; better video performance than VNC
- [ ] 🆕 **VNC (Virtual Network Computing)** — cross-platform remote desktop; port 5900; no authentication by default; use with SSH tunnel or password
- [ ] 🆕 **WinRM (Windows Remote Management)** — Microsoft's implementation of WS-Management; allows PowerShell remoting; `Enable-PSRemoting`; port 5985 (HTTP) / 5986 (HTTPS)
- [ ] 🆕 **RMM (Remote Monitoring and Management)** — tools used by MSPs; ConnectWise, NinjaRMM, Datto, Kaseya; monitors endpoints, pushes scripts, remote access

### Objective 4.11 — Artificial Intelligence (AI) Basics 🆕 NEW IN V15

> This is an entirely new section added to V15. It was not in the previous (1101/1102) version.

- [ ] 🆕 **AI application integration** — AI features built into OS/apps: Windows Copilot, Microsoft 365 Copilot, macOS Siri; used for drafting emails, summarizing documents, troubleshooting suggestions
- [ ] 🆕 **AI in IT support** — AI chatbots for Tier 0/1 support; automated ticket categorization; predictive failure analysis; SIEM anomaly detection
- [ ] 🆕 **AI policy considerations**:
    - Appropriate use — company policies on using AI tools for work; what data can be submitted to AI?
    - Plagiarism — AI-generated content must be reviewed; academic/professional integrity concerns
- [ ] 🆕 **AI limitations**:
    - Bias — AI trained on biased data produces biased outputs; important for hiring tools, security scoring
    - Hallucinations — AI confidently states incorrect information; never trust AI output without verification
    - Accuracy — AI knowledge has cutoff dates; not always current; fact-check critical information
    - Privacy risk — do not submit PII, PHI, or confidential company data to external AI tools

---

---

# 🔬 LAB LIST — Hands-On Practice (Do Every Single One)

## Core 1 Labs

- [ ] Crimp an RJ-45 connector onto Cat6 cable using T568B wiring
- [ ] Use a cable tester to verify all 8 pins pass
- [ ] Use a Wi-Fi analyzer app (Android: WiFiAnalyzer; Windows: inSSIDer) to identify channels and signal strength
- [ ] Build a PC from scratch in a VM — add vCPU, vRAM, attach ISO, install OS
- [ ] Configure bridged / NAT / host-only networking in VirtualBox or VMware Workstation
- [ ] Take a snapshot, make changes, revert snapshot
- [ ] Replace thermal paste on a CPU (or practice on an old PC)
- [ ] Access router admin page — change SSID, enable WPA3, disable WPS, set DHCP reservation

## Core 2 Labs

- [ ] Install Windows 11 from scratch in a VM (VirtualBox or VMware)
- [ ] Run all Windows admin tools: Event Viewer, Device Manager, Disk Management, Services, gpedit
- [ ] Create a local user, add to Administrators group via net user and lusrmgr
- [ ] Set password policy in Local Security Policy (secpol.msc)
- [ ] Enable and configure BitLocker on a VM drive
- [ ] Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth`
- [ ] Boot a VM into Safe Mode (all 3 types)
- [ ] Install Ubuntu in a VM; practice: ls, pwd, chmod, chown, apt install, systemctl
- [ ] Enable SSH on Ubuntu; connect via Windows Terminal SSH
- [ ] Write a batch script to map a network drive on login
- [ ] Write a PowerShell script to list all running services
- [ ] Create a forensic image of a VM's disk using FTK Imager (free) or `dd`
- [ ] Set up Quick Assist and remote-control another machine on your LAN

---

# 📚 Official & Trusted Resources

|Resource|Type|Notes|
|---|---|---|
|[CompTIA Official Exam Objectives (220-1201)](https://www.examcompass.com/comptia-certifications/a-plus/core-1/comptia-a-plus-220-1201-exam-objectives.pdf)|PDF|**Start here. The Bible of this exam.**|
|[Professor Messer A+ 220-1201/1202](https://www.professormesser.com)|Free Video Course|Best free resource; structured by objective|
|[CompTIA CertMaster Learn](https://www.comptia.org/training/certmaster-learn)|Paid|Official adaptive learning; PBQ practice|
|[Jason Dion - Udemy A+ Courses](https://www.udemy.com)|Paid|Excellent paid video; practice exams|
|[ExamCompass Free Practice Tests](https://www.examcompass.com)|Free|Good for knowledge testing|
|[r/CompTIA subreddit](https://www.reddit.com/r/CompTIA)|Community|Real exam experiences; study tips|
|[TryHackMe - Pre-Security Path](https://tryhackme.com)|Interactive|Hands-on labs; connects A+ to Cybersecurity|
|[Professor Messer Study Groups](https://www.professormesser.com/category/220-1201/)|Community|Discord + weekly study groups|

---

# 🎯 Exam Day Reminders

- [ ] Max 90 questions, 90 minutes — pace yourself (1 min/question average)
- [ ] Performance-Based Questions (PBQs) come FIRST — take your time; they are worth more
- [ ] You CAN skip and come back — flag any question you're unsure of
- [ ] No penalty for guessing — ALWAYS answer every question
- [ ] Pass Core 1 = 675/900; Pass Core 2 = 700/900
- [ ] Must pass BOTH for A+ certification; can take in any order
- [ ] Bring valid government ID; no notes; no phones
- [ ] Testing via Pearson VUE — in-person or online proctored
- [ ] V15 launches March 2025 — make sure you're studying correct version objectives

