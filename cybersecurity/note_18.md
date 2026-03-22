# 🖥️ Operating Systems — The Invisible Manager

> **Source:** TryHackMe — Pre-Security / Operating Systems Module
> **Purpose:** OS fundamentals for cybersecurity
> **Covers:** What an OS is, kernel/user space, OS duties, security,
> GUI vs CLI, OS landscape, real-world OS families

---

## 🧒 Feynman Explanation — The Airport Analogy

A computer without an OS is like an airport with no air traffic
control tower. Planes (apps) would taxi onto runways randomly,
crash into each other, fight over fuel, and nobody would know
who lands where. Chaos.

The OS is the **air traffic control system**:

| Airport Component                | Computer Component            |
| -------------------------------- | ----------------------------- |
| **Runways, radar, fuel systems** | Hardware (CPU, RAM, storage)  |
| **Airlines and passengers**      | Applications (browser, games) |
| **Air traffic control tower**    | Operating System              |
| **Radio communications**         | System calls                  |
| **Flight schedules**             | Process scheduling            |

The tower doesn't fly planes — it **coordinates** everything
so planes can operate safely without crashing into each other.

---

## 🔷 1. What Is an Operating System?

```
The OS sits between the user and the hardware:

    ┌─────────────────────┐
    │        USER         │  ← you, clicking and typing
    ├─────────────────────┤
    │    APPLICATIONS     │  ← browser, games, Word
    ├─────────────────────┤
    │  OPERATING SYSTEM   │  ← Windows, Linux, macOS
    ├─────────────────────┤
    │      HARDWARE       │  ← CPU, RAM, SSD, GPU
    └─────────────────────┘

Without the OS:
  Every app would need to directly control the CPU, memory,
  storage, and every device — writing custom drivers for
  every possible hardware combination. Impossible.

With the OS:
  Apps just ask "save this file" or "play this sound"
  The OS handles all the hardware complexity beneath
```

---

## 🔷 2. System Privilege Layers — Kernel vs User Space

### 🧒 Feynman Explanation

The airport control tower has two zones:

**Inside the tower** (kernel space) = only certified air traffic
controllers work here. They have direct access to the runways,
radar, weather systems. Full power. Fully trusted.

**Outside the tower** (user space) = airlines, passengers, ground
crew. They can't walk into the tower. Instead they radio requests
("Gate 7 is ready") and the tower acts on their behalf.

### Kernel Space vs User Space

| Feature             | Kernel Space                 | User Space                          |
| ------------------- | ---------------------------- | ----------------------------------- |
| **Who lives here**  | OS kernel                    | All applications                    |
| **Hardware access** | Direct, unrestricted         | None — must request via system call |
| **Privilege level** | Ring 0 (highest)             | Ring 3 (lowest)                     |
| **If it crashes**   | Entire system crashes        | Just that one app crashes           |
| **Examples**        | Linux kernel, device drivers | Chrome, Spotify, Python scripts     |

```
SYSTEM CALL FLOW:
  App wants to open a file
    ↓
  "open('/etc/passwd', 'r')"  ← system call
    ↓
  Kernel validates: does this user have permission?
    ↓ YES                        ↓ NO
  Returns file handle        Returns error: Permission denied
    ↓
  App reads file
```

> ⚠️ **Security relevance:** Privilege escalation attacks try
> to move code FROM user space INTO kernel space — gaining
> unrestricted hardware access. Kernel exploits (dirty pipe,
> dirty cow) are some of the most severe CVEs possible because
> they break the fundamental security boundary of the OS.

### 💻 Seeing Privilege Levels in Linux

```bash
# See your current user and privileges
whoami
id

# System calls made by a program (strace traces kernel calls)
strace ls /tmp 2>&1 | head -30

# See running processes and their privilege levels
ps aux
# UID 0 = root = kernel-level privilege
# Other UIDs = regular user space processes

# Check what a process is doing at kernel level
sudo cat /proc/<PID>/status
```

---

## 🔷 3. Operating System Duties

### The Five Core Responsibilities

| OS Responsibility          | What It Does                                                                                                      | Real Example                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Process Management**     | Creates, schedules, prioritizes, terminates programs. Decides how much CPU time each process gets                 | Opening browser + music + game simultaneously without freezing   |
| **Memory Management**      | Allocates RAM to processes, protects each app's memory from others, uses virtual memory when RAM is full          | Chrome using 2GB RAM without touching Firefox's memory           |
| **File System Management** | Organizes files into directories, handles paths, permissions, metadata (name, size, timestamps)                   | Saving a photo, creating a folder, setting a file to "read only" |
| **User Management**        | Handles multiple user accounts, authentication, permissions for who can access what                               | Your password keeping your files private from other accounts     |
| **Device Management**      | Loads drivers, provides hardware abstraction layer so apps can say "print this" without knowing the printer model | Plugging in any mouse and it just works                          |

### 💻 Seeing OS Duties in Action (Linux)

```bash
# ── PROCESS MANAGEMENT ────────────────────────────────────────────
# List all running processes
ps aux

# Real-time process monitor with CPU/RAM usage
top
htop  # more visual version (install: apt install htop)

# Kill a process
kill <PID>
kill -9 <PID>    # force kill (unresponsive processes)

# ── MEMORY MANAGEMENT ─────────────────────────────────────────────
# See RAM usage
free -h

# See virtual memory stats
vmstat

# See which process is using most RAM
ps aux --sort=-%mem | head -10

# ── FILE SYSTEM MANAGEMENT ────────────────────────────────────────
# Navigate filesystem
ls -la /etc         # list files with permissions
ls -la /home        # user home directories

# File permissions (rwxrwxrwx = owner/group/other)
chmod 644 file.txt  # rw-r--r--  (owner read/write, others read)
chmod 755 script.sh # rwxr-xr-x  (owner all, others read+execute)

# File metadata
stat file.txt       # size, permissions, timestamps, inode

# ── USER MANAGEMENT ───────────────────────────────────────────────
# Show all users
cat /etc/passwd

# Show all groups
cat /etc/groups

# Show password hashes (root only!)
sudo cat /etc/shadow

# Current user info
id
whoami

# ── DEVICE MANAGEMENT ─────────────────────────────────────────────
# List all hardware devices
lshw -short
lspci          # PCI devices (GPU, network)
lsusb          # USB devices
lsblk          # storage devices
```

---

## 🔷 4. Operating System Security

### The OS as the First Security Layer

```
BEFORE antivirus, firewalls, or any security tools run —
the OS is ALREADY enforcing security:

Authentication  → Verifies who you are (password, biometrics)
Permissions     → Controls what each user/app can read/write/execute
Isolation       → Keeps every process in its own protected space
System Protection → Protects critical system files from changes
```

### Linux File Permissions Deep Dive

```
Permission string: -rwxr-xr--
                   │└┬┘└┬┘└┬┘
                   │ │  │  └── Other users: r-- = read only
                   │ │  └───── Group:       r-x = read + execute
                   │ └──────── Owner:       rwx = full access
                   └────────── File type:   - = file, d = directory

Numeric representation:
  r = 4, w = 2, x = 1
  rwx = 4+2+1 = 7
  r-x = 4+0+1 = 5
  r-- = 4+0+0 = 4

Common permission sets:
  644 → rw-r--r-- (normal files)
  755 → rwxr-xr-x (executable scripts)
  600 → rw------- (private files, SSH keys)
  700 → rwx------ (private scripts)
  777 → rwxrwxrwx (⚠️ dangerous — anyone can do anything)
```

> ⚠️ **Security note:** Finding files with `777` permissions or
> SUID bit set (`chmod +s`) is a critical pentesting finding.
> SUID files run with the OWNER's privileges (often root) even
> when run by a regular user — a classic privilege escalation path.

```bash
# Find SUID files (pentesting must-know!)
find / -perm -4000 2>/dev/null

# Find world-writable files (security risk)
find / -perm -o+w -type f 2>/dev/null

# Find files owned by root with SUID
find / -user root -perm -4000 2>/dev/null

# Check GTFObins for any SUID binary you find
# https://gtfobins.github.io/
```

---

## 🔷 5. OS Interfaces — GUI vs CLI

### 🧒 Feynman Explanation

**GUI** = tap an icon on Google Maps and it navigates for you.
Point and click. Easy, but limited precision.

**CLI** = type the exact GPS coordinates of your destination.
Takes knowledge, but gets you exactly where you want with
complete control and speed.

For cybersecurity — you need to be **fluent in CLI**. The terminal
is where the real power lives.

### GUI vs CLI Comparison

| Feature              | GUI                           | CLI                           |
| -------------------- | ----------------------------- | ----------------------------- |
| **How you interact** | Click icons, menus, windows   | Type text commands            |
| **Learning curve**   | Low — intuitive               | Higher — must learn syntax    |
| **Speed**            | Slower for repetitive tasks   | Much faster once learned      |
| **Precision**        | Limited to what buttons exist | Unlimited control             |
| **Automation**       | Hard to script                | Easy — write scripts          |
| **Remote access**    | Requires GUI (heavy)          | SSH works over any connection |
| **Resource use**     | High (renders graphics)       | Minimal                       |
| **Security work**    | Limited                       | Essential                     |

### Same Task — GUI vs CLI

```
TASK: List files in /home/ubuntu

GUI:
  1. Open Files app
  2. Navigate to home folder
  3. Navigate to ubuntu folder
  4. Look at files
  (4 steps, mouse required)

CLI:
  ls /home/ubuntu
  (1 command, anywhere, scriptable)
```

### Essential CLI Commands for Security Work

```bash
# ── NAVIGATION ────────────────────────────────────────────────────
pwd                    # where am I right now?
ls -la                 # list all files with permissions
cd /path/to/dir        # change directory
cd ..                  # go up one level
cd ~                   # go to home directory

# ── FILE OPERATIONS ───────────────────────────────────────────────
cat file.txt           # read file contents
less file.txt          # read large files (scroll)
head -20 file.txt      # first 20 lines
tail -20 file.txt      # last 20 lines
tail -f logfile.log    # live log monitoring (SOC essential!)
grep "error" file.txt  # search for text in file
grep -r "password" /   # search recursively

# ── FILE MANAGEMENT ───────────────────────────────────────────────
cp source dest         # copy file
mv source dest         # move/rename file
rm file.txt            # delete file
mkdir newdir           # create directory
touch newfile.txt      # create empty file

# ── SYSTEM INFO ───────────────────────────────────────────────────
uname -a               # OS and kernel version
hostname               # machine name
uptime                 # how long system has been running
df -h                  # disk space usage
free -h                # RAM usage
env                    # environment variables

# ── NETWORK ───────────────────────────────────────────────────────
ip a                   # network interfaces and IPs
ss -tulnp              # open ports and services
netstat -tulnp         # same (older command)
ping google.com        # test connectivity
curl -I https://google.com  # HTTP headers
```

---

## 🔷 6. The OS Landscape — Five Types

| OS Type           | Primary Use                      | Key Characteristics                       | Examples                               |
| ----------------- | -------------------------------- | ----------------------------------------- | -------------------------------------- |
| **Desktop**       | Personal computers, work, gaming | Rich GUI, multitasking, user-focused      | Windows 11, macOS, Ubuntu              |
| **Server**        | Web hosting, databases, cloud    | Headless (no GUI), max uptime, multi-user | Ubuntu Server, Red Hat, Windows Server |
| **Mobile**        | Smartphones, tablets             | Touch UI, power-efficient, app sandboxing | Android, iOS                           |
| **Embedded**      | Cars, IoT, appliances, routers   | Tiny footprint, limited hardware          | OpenWrt, FreeRTOS, VxWorks             |
| **Virtual/Cloud** | VMs, containers, cloud instances | Lightweight, scalable, rapid deployment   | Alpine Linux, Amazon Linux             |

---

## 🔷 7. Real-World Operating Systems

### Desktop OS

```
Windows
  Most widely used desktop OS globally
  Versions: Windows 10 (EOL), Windows 11
  Used in: Offices, gaming, everyday computing

macOS
  Apple's desktop OS — polished GUI, Apple ecosystem
  Versions: Sonoma (14), Sequoia (15), Tahoe (26)
  Used in: Creative work, development, Apple users

Linux (Desktop)
  Not one OS — a FAMILY of distributions (distros)
  All share the Linux kernel, differ in packaging and GUI
  Versions: Ubuntu, Debian, Fedora, Mint, Arch, Kali
  Used in: Development, security, power users
```

### Server OS

```
Linux (Server) ← THE dominant server OS
  ~96% of the top 1 million web servers run Linux
  Ubuntu Server, Debian, CentOS, Red Hat Enterprise Linux (RHEL)
  Why: Free, stable, secure, massive community, SSH-friendly

Windows Server
  Used in large corporate networks with Active Directory
  Versions: 2016, 2019, 2022, 2025
  Why: Integration with Microsoft ecosystem (AD, Exchange)

Unix
  Used in: Finance, telecom, government, large enterprises
  Examples: IBM AIX, Oracle Solaris
  Why: Extreme stability, decades of proven reliability
```

### Mobile OS

```
Android
  Most used mobile OS globally (~72% market share)
  Open source (based on Linux), manufacturer customizable
  Versions: Android 14, 15, 16

iOS
  Apple's mobile OS — iPhones, iPads
  Closed ecosystem, known for strong security model
  Versions: iOS 17, 18, 26
```

### Embedded & IoT

```
Embedded Linux
  Stripped-down Linux for specific devices
  Examples: OpenWrt (routers), Yocto Project

Real-Time OS (RTOS)
  Guarantees response times for time-critical systems
  Aircraft controls, medical devices, factory equipment
  Examples: FreeRTOS, VxWorks, QNX
```

### Virtual & Cloud

```
Cloud-optimized Linux
  Stripped down for fast boot and minimal footprint
  Ubuntu LTS, Amazon Linux, Rocky Linux

Container-optimized
  Even lighter — just enough to run containers
  Alpine Linux (5MB!), Bottlerocket (AWS), Flatcar Linux
```

---

## 🔷 8. Key Terminology — Quick Reference

| Term                      | Definition                                                          |
| ------------------------- | ------------------------------------------------------------------- |
| **Operating System (OS)** | Core software managing hardware, applications, and system resources |
| **Kernel**                | The OS's core — directly manages hardware, runs in kernel space     |
| **Kernel Space**          | OS's privileged area with direct hardware access                    |
| **User Space**            | Where regular applications run with limited permissions             |
| **System Call**           | How user-space apps request kernel services                         |
| **GUI**                   | Graphical User Interface — visual interaction via clicks            |
| **CLI**                   | Command-Line Interface — text-based, precise control                |
| **Process**               | A running program being managed by the OS                           |
| **SUID**                  | Set User ID — file runs with owner's privileges (security risk!)    |
| **Driver**                | Software that lets the OS communicate with hardware                 |

---

## 🔗 Security Attack Map — OS Level

| OS Component             | Attack                     | Technique                                 |
| ------------------------ | -------------------------- | ----------------------------------------- |
| **User/Kernel boundary** | Privilege escalation       | Kernel exploit (DirtyPipe, DirtyCow)      |
| **SUID binaries**        | Local privilege escalation | Find SUID → GTFObins exploit              |
| **File permissions**     | Unauthorized access        | World-writable files, misconfigured perms |
| **User accounts**        | Lateral movement           | Weak passwords, reused credentials        |
| **/etc/shadow**          | Password cracking          | Read hash → crack offline with hashcat    |
| **Process injection**    | Malware persistence        | Inject into legitimate process            |
| **Device drivers**       | Rootkit installation       | Malicious kernel module                   |
| **System calls**         | Sandbox escape             | Exploit kernel syscall handler            |

---

## ⚡ Enriched Insights (Beyond the Source Material)

### Why Linux Dominates Security Work

```
Linux is THE operating system of cybersecurity because:
  ✅ Open source — you can read and modify EVERYTHING
  ✅ CLI-first — automation and scripting is native
  ✅ Transparent — see every process, file, connection
  ✅ Flexible — Kali, Parrot, BlackArch = security distros
  ✅ Server reality — 96% of servers run Linux → you must know it
  ✅ Free — no licensing costs for home labs

The most important Linux directories for security:
  /etc/passwd     → user account information
  /etc/shadow     → password hashes (root only)
  /etc/hosts      → local DNS overrides
  /var/log/       → ALL system logs (SOC gold mine)
  /tmp/           → temp files, often writable by any user
  /home/          → user home directories
  /root/          → root's home directory
  /bin/ /usr/bin/ → executable programs
  /etc/cron*      → scheduled tasks (persistence location!)
```

### Windows vs Linux for Security

```
Windows:
  Event Logs     → C:\Windows\System32\winevt\Logs\
  Registry       → HKLM, HKCU (persistence locations!)
  SAM database   → password hashes stored here
  Active Directory → user management for corporate networks
  PowerShell     → the CLI for Windows automation

Linux:
  /var/log/      → auth.log, syslog, kern.log
  /etc/passwd    → user accounts
  /etc/shadow    → password hashes
  Crontab        → scheduled tasks
  Bash           → the CLI for Linux automation

SOC analysts need to know BOTH.
Pentesters need to know BOTH.
Linux is more common on servers, Windows is more common in offices.
```

### The Linux Filesystem Hierarchy

```
/           ← root of everything
├── bin/    ← essential user binaries (ls, cp, cat)
├── sbin/   ← system admin binaries (fdisk, iptables)
├── etc/    ← system configuration files
├── home/   ← user home directories
├── root/   ← root user's home
├── var/    ← variable data (logs, databases, mail)
│   └── log/ ← system logs (SOC analyst's home!)
├── tmp/    ← temporary files (world-writable, risky!)
├── usr/    ← user programs and libraries
├── proc/   ← virtual filesystem — running process info
├── sys/    ← virtual filesystem — hardware info
├── dev/    ← device files (/dev/sda = first hard drive)
└── opt/    ← optional/third-party software
```

---

_Notes compiled from TryHackMe — Operating Systems Introduction Module_
_Enriched with Linux commands, security context, and Feynman explanations_
