# 💻 Computer Hardware & The Boot Process

> **Source:** TryHackMe — Pre-Security / How Computers Work Module
> **Purpose:** Foundational OS & hardware knowledge for cybersecurity
> **Covers:** Core components, analogies, boot sequence, UEFI/BIOS

---

## 🧒 Feynman Explanation — What Is a Computer?

A computer is just a very fast, very obedient robot that can only
do exactly what it's told. It has:

- A **brain** that thinks (CPU)
- **Short-term memory** for what it's working on right now (RAM)
- **Long-term memory** for storing everything permanently (HDD/SSD)
- A **skeleton and nerves** connecting everything (Motherboard)
- A **heart and lungs** giving it power (PSU)
- **Eyes** that turn math into pictures (GPU)

Every computer — from your phone to a NASA supercomputer —
has these same six things. The only difference is how fast
and how big each component is.

---

## 🔷 1. Core Hardware Components

### Component Overview Table

| Component       | Analogy           | Function                       | Security Relevance                |
| --------------- | ----------------- | ------------------------------ | --------------------------------- |
| **CPU**         | The Brain         | Executes all instructions      | Spectre/Meltdown CPU attacks      |
| **RAM**         | Short-term memory | Stores active data temporarily | RAM forensics, cold boot attacks  |
| **HDD/SSD**     | Long-term memory  | Permanent storage              | Disk forensics, data recovery     |
| **Motherboard** | Skeleton + nerves | Connects all components        | Firmware attacks, BIOS malware    |
| **GPU**         | Visual cortex     | Renders graphics               | GPU-accelerated password cracking |
| **PSU**         | Heart + lungs     | Supplies power to all parts    | Physical security                 |

---

### 🧠 CPU — The Brain

```
The CPU (Central Processing Unit) executes instructions.
Every program, every click, every calculation = CPU work.

Key concepts:
  Clock Speed   — how many instructions per second (GHz)
  Cores         — parallel brains (quad-core = 4 CPUs in one)
  Architecture  — x86 (32-bit), x64 (64-bit), ARM (mobile)
  Cache         — tiny ultra-fast memory built into the CPU
                  (L1 > L2 > L3, in speed and size)
```

> ⚠️ **Security note:** Spectre and Meltdown (2018) were
> CPU-level vulnerabilities allowing programs to read
> memory they shouldn't access — including passwords and
> encryption keys — by exploiting how CPUs predict and
> speculatively execute instructions. A hardware-level
> attack that patching software couldn't fully fix.

---

### 🧠 RAM — Short-Term Memory

```
RAM (Random Access Memory) holds data the CPU is actively using.

Characteristics:
  ✅ Extremely fast (nanosecond access)
  ❌ Volatile — loses ALL data when power is off
  ✅ Everything currently running lives here:
     - Open browser tabs
     - Running processes
     - Decrypted files being edited
     - Passwords and encryption keys in use
```

> ⚠️ **Security (Cold Boot Attack):** Because RAM loses
> data when powered off, attackers can freeze RAM chips
> (literally with cold spray) to slow data decay, then
> read the memory for encryption keys, passwords, and
> session tokens. This is why full disk encryption alone
> doesn't protect a running machine.

```bash
# Linux: View RAM usage
free -h

# View running processes and their RAM usage
top
htop

# Forensics: dump RAM for analysis (requires root)
sudo dd if=/dev/mem of=/tmp/ram_dump.raw
# Then analyze with Volatility (memory forensics tool)
volatility -f ram_dump.raw imageinfo
```

---

### 💾 HDD / SSD — Long-Term Memory

| Type                        | Speed       | Durability          | How It Works               |
| --------------------------- | ----------- | ------------------- | -------------------------- |
| **HDD** (Hard Disk Drive)   | Slower      | Mechanical, fragile | Spinning magnetic platters |
| **SSD** (Solid State Drive) | Much faster | No moving parts     | Flash memory chips         |
| **NVMe SSD**                | Fastest     | No moving parts     | Direct PCIe connection     |

> ⚠️ **Security/Forensics note:** Deleted files are NOT
> immediately gone from HDD/SSD. The OS just marks the
> space as "available to overwrite." Until overwritten,
> the data is recoverable with forensic tools.
> This is how digital forensics investigators recover
> "deleted" evidence.

```bash
# Forensics: recover deleted files
sudo apt install testdisk photorec

# List all storage devices
lsblk
fdisk -l

# Create forensic disk image (preserves original)
sudo dd if=/dev/sdb of=/forensics/disk_image.raw bs=4M
md5sum /forensics/disk_image.raw  # hash for chain of custody

# Analyze with Autopsy (GUI forensics tool)
autopsy
```

---

### 🖥️ Motherboard — The Skeleton and Nerves

```
The motherboard is the main circuit board that connects
EVERYTHING together. Every component plugs into it:

  CPU    → CPU socket
  RAM    → DIMM slots
  GPU    → PCIe slot
  HDD    → SATA port
  SSD    → M.2 slot or SATA
  PSU    → 24-pin ATX connector
  USB    → USB headers

Also contains:
  UEFI/BIOS chip → firmware that starts the computer
  CMOS battery   → keeps time/settings when powered off
  Chipset        → manages data flow between components
```

> ⚠️ **Security note:** BIOS/UEFI malware (bootkit/rootkit)
> is the most persistent malware possible — it survives
> OS reinstallation, hard drive replacement, and even some
> factory resets. It lives in the firmware chip on the
> motherboard itself. Very difficult to detect and remove.

---

### 🎮 GPU — The Visual Cortex

```
GPU (Graphics Processing Unit) — originally for rendering
graphics, now also used for:

  ✅ Gaming and video
  ✅ Machine learning / AI training
  ✅ Password cracking (HUGE in cybersecurity!)
  ✅ Cryptocurrency mining
  ✅ Scientific simulation
```

> ⚠️ **Security (Password Cracking):** A modern GPU can
> try **billions** of password hashes per second.
> Hashcat (the industry standard cracking tool) uses
> your GPU to crack leaked password hashes at insane speeds.

```bash
# GPU-accelerated password cracking with Hashcat
# Crack MD5 hashes with rockyou wordlist
hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt

# Benchmark your GPU's cracking speed
hashcat -b

# Speed comparison (approximate, RTX 3080):
# MD5:    68 BILLION hashes/second
# SHA1:   22 BILLION hashes/second
# bcrypt: 100,000 hashes/second (slow by design!)
# → This is why bcrypt is used for passwords, not MD5
```

---

### ⚡ PSU — Heart and Lungs

```
PSU (Power Supply Unit) converts AC power from the wall
outlet into DC power that computer components use.

Outputs:
  +12V  — CPU, GPU, storage drives
  +5V   — motherboard, USB
  +3.3V — RAM, some motherboard components

Wattage matters:
  Gaming PC    → 650–850W
  Server       → 500W–2000W+ per unit
  Data center  → megawatts total
```

---

## 🔷 2. The Boot Process

### 🧒 Feynman Explanation

Booting a computer is like waking up in the morning:

1. **Alarm goes off** → You press power (signal to PSU)
2. **Body wakes up** → Firmware (UEFI) starts
3. **Check you're OK** → POST tests all hardware
4. **Find your brain** → Select which device has the OS
5. **Become conscious** → Bootloader loads the OS into RAM

---

### The 5-Step Boot Sequence

```
Power Button → Firmware → POST → Select Boot Device → Bootloader
```

### Step-by-Step Breakdown

**Step 1 — Press the Power Button**

```
Signal sent to PSU → PSU provides power to all components
→ Motherboard receives power → CPU receives first instruction
→ That instruction is hardcoded: "go find UEFI firmware"
```

**Step 2 — Firmware Starts (UEFI/BIOS)**

```
UEFI = Unified Extensible Firmware Interface (modern)
BIOS = Basic Input/Output System (legacy, largely replaced)

UEFI is a small program stored on a chip ON the motherboard.
It is the FIRST software that runs — before the OS.
It initializes all hardware so components can communicate.

BIOS vs UEFI:
┌────────────┬──────────────────┬──────────────────────────┐
│ Feature    │ BIOS (legacy)    │ UEFI (modern)            │
├────────────┼──────────────────┼──────────────────────────┤
│ Interface  │ Text only        │ GUI with mouse support   │
│ Drive size │ Max 2TB          │ 9.4 ZB (no limit)        │
│ Security   │ None             │ Secure Boot              │
│ Speed      │ Slower           │ Faster POST              │
│ Partitions │ MBR (max 4)      │ GPT (128 partitions)     │
└────────────┴──────────────────┴──────────────────────────┘
```

**Step 3 — POST (Power-On Self Test)**

```
UEFI tests every required component:
  ✅ CPU present and functional?
  ✅ RAM installed and readable?
  ✅ Storage devices detected?
  ✅ GPU detected?
  ✅ Keyboard/mouse connected?

PASS → continues to Step 4
FAIL → beep codes or error message displayed
       (different beep patterns = different hardware failures)
```

**Step 4 — Select Boot Device**

```
UEFI has a Boot Order list — e.g.:
  1st: USB Drive
  2nd: DVD Drive
  3rd: SSD (Windows)
  4th: HDD (Linux)

Checks each in order until it finds a bootable device.
The boot device contains the bootloader program.

You can access this list:
  Press DEL or F2 or F12 during POST (varies by manufacturer)
  → UEFI Setup menu appears
```

**Step 5 — Start Bootloader**

```
Bootloader is a small program on the boot device.
Its ONLY job: load the OS from storage into RAM.

Common bootloaders:
  Windows  → Windows Boot Manager (bootmgr)
  Linux    → GRUB2 (Grand Unified Bootloader)
  macOS    → iBoot

Process:
  Bootloader reads OS files from disk
  → Loads OS kernel into RAM
  → Transfers control to OS kernel
  → OS initializes drivers and services
  → Login screen appears
```

### Full Boot Flow Diagram

```
[POWER BUTTON]
      │
      ▼
[PSU powers components]
      │
      ▼
[UEFI/BIOS firmware starts]
  ├─ Initializes CPU, RAM, storage
  └─ Prepares hardware for OS
      │
      ▼
[POST — Power-On Self Test]
  ├─ PASS → continue
  └─ FAIL → beep codes, halt
      │
      ▼
[UEFI reads Boot Order list]
  ├─ USB? → check
  ├─ SSD?  → check → FOUND bootloader
  └─ Loads bootloader into memory
      │
      ▼
[Bootloader runs]
  └─ Loads OS kernel from disk into RAM
      │
      ▼
[OS Kernel initializes]
  ├─ Loads device drivers
  ├─ Starts system services
  └─ Presents login screen
      │
      ▼
[YOU ARE IN CONTROL]
```

---

## 🔗 Security Attack Map — Hardware & Boot

| Component/Stage | Attack             | Technique                               | Tool                        |
| --------------- | ------------------ | --------------------------------------- | --------------------------- |
| **RAM**         | Cold Boot Attack   | Freeze RAM, extract encryption keys     | msramdmp, Inception         |
| **RAM**         | Memory forensics   | Dump running process memory             | Volatility, dd              |
| **HDD/SSD**     | Data recovery      | Recover "deleted" files                 | Autopsy, TestDisk, PhotoRec |
| **UEFI/BIOS**   | Bootkit/Rootkit    | Persist malware below OS                | LoJax, MosaicRegressor      |
| **Boot Order**  | Evil Maid Attack   | Boot from USB, bypass OS auth           | Kon-Boot, offline tools     |
| **GPU**         | Password cracking  | Brute force password hashes             | Hashcat                     |
| **POST**        | Hardware keylogger | Physical device between keyboard and PC | Physical access             |
| **Bootloader**  | GRUB bypass        | Boot to single-user mode, reset root pw | Physical access             |

---

## ⚡ Enriched Insights (Beyond the Source Material)

### Secure Boot — UEFI's Security Feature

```
Secure Boot (UEFI feature) verifies that bootloader code
is SIGNED by a trusted authority before running it.

Purpose: Prevent malicious bootloaders/bootkits from loading

How it works:
  UEFI has a database of trusted signing keys
  → Bootloader must be signed with a trusted key
  → If unsigned or unknown → REFUSED to run
  → Protects against Evil Maid attacks

Pentest relevance:
  Kali Linux and many live USB tools require
  Secure Boot to be DISABLED to boot from USB
  (This is why pentesters often disable it in BIOS)
```

### The Volatile Memory Hierarchy

```
Speed (fastest → slowest):
CPU Registers → L1 Cache → L2 Cache → L3 Cache → RAM → SSD → HDD

Size (smallest → largest):
CPU Registers → L1 Cache → L2 Cache → L3 Cache → RAM → SSD → HDD

Everything above RAM loses data when power is off (volatile).
Everything from SSD/HDD down keeps data (non-volatile).
```

### Linux Boot Forensics Commands

```bash
# See boot messages (great for troubleshooting)
dmesg | head -50
journalctl -b

# See what services started at boot
systemctl list-units --type=service

# See boot time breakdown
systemd-analyze
systemd-analyze blame    # which service took longest?

# Check UEFI variables
efibootmgr -v           # show boot order and entries

# See hardware summary
lshw -short             # all hardware
lscpu                   # CPU details
free -h                 # RAM details
lsblk                   # storage devices
lspci                   # PCI devices (GPU, network cards)
```

### Why This Matters for Cybersecurity

```
SOC Analyst:
  → Malware can persist in UEFI (survives reinstall)
  → Memory forensics reveals running malware
  → Boot logs show unauthorized USB boots (Evil Maid)

Pentester:
  → Disable Secure Boot to boot Kali from USB
  → Cold boot attacks on encrypted laptops
  → Physical access = game over for most systems

Forensics:
  → RAM dump captures passwords, keys, running code
  → Disk forensics recovers deleted evidence
  → Boot logs preserved in Windows Event Log
```

---

_Notes compiled from TryHackMe — How Computers Work Module_
_Enriched with security context, forensics tools, and Feynman explanations_
