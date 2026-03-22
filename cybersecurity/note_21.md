# 🪟 Windows CLI Fundamentals — Navigation, Files & System Recon

> **Source:** TryHackMe — Pre-Security / Windows Command Line Module
> **Purpose:** Windows terminal mastery for cybersecurity
> **Covers:** cd, dir, dir /a, dir /s, type, whoami, hostname,
> systeminfo, ipconfig, hidden files, filesystem navigation

---

## 🧒 Feynman Explanation — The Command Prompt as a Flashlight

Imagine you're in a dark building (Windows system). The GUI is
like turning on all the lights — you see everything nicely but
it takes time and some rooms stay locked. The CLI is like having
a powerful flashlight: you point it exactly where you need, it
shows you things the lights don't, and you move 10x faster.

The best part? **You can find things the GUI deliberately hides.**

---

## 🔷 The Parallel — Linux vs Windows CLI

| Action           | Linux                   | Windows CMD       |
| ---------------- | ----------------------- | ----------------- |
| Where am I?      | `pwd`                   | `cd` (no args)    |
| List files       | `ls`                    | `dir`             |
| List + hidden    | `ls -al`                | `dir /a`          |
| Change directory | `cd Documents`          | `cd Documents`    |
| Go up one level  | `cd ..`                 | `cd ..`           |
| Find a file      | `find ~ -name file.txt` | `dir /s file.txt` |
| Read a file      | `cat file.txt`          | `type file.txt`   |
| Who am I?        | `whoami`                | `whoami`          |
| System info      | `uname -a`              | `systeminfo`      |
| Network info     | `ip a`                  | `ipconfig`        |
| Machine name     | `hostname`              | `hostname`        |

> 💡 Many commands are the same (`whoami`, `hostname`, `cd`).
> Windows and Linux share more CLI DNA than most people realize.

---

## 🔷 1. Step 1 — "Where Am I?" → `cd` (no arguments)

```cmd
C:\Users\Administrator> cd
C:\Users\Administrator
```

**On Linux:** `pwd` prints the directory.
**On Windows:** `cd` with NO arguments prints current location.

```cmd
# Reading a Windows path:
C:\Users\Administrator\Desktop
│  │     │             └── subfolder
│  │     └── folder (username)
│  └── folder (Users — all accounts live here)
└── Drive letter (C: = main hard drive)

Common drive letters:
  C:\  → main system drive (Windows installed here)
  D:\  → second drive or DVD
  E:\  → external drive or USB
```

> 💡 **Windows paths use backslash `\`**
> **Linux paths use forward slash `/`**
> This trips up beginners constantly. Muscle memory takes time.

---

## 🔷 2. Step 2 — "What's Around Me?" → `dir`

```cmd
C:\Users\Administrator> dir
 Volume in drive C has no label.
 Volume Serial Number is XXXX-XXXX

 Directory of C:\Users\Administrator

02/27/2022  12:00 PM    <DIR>          Desktop
12/11/2023  12:45 PM    <DIR>          Documents
02/16/2024  10:00 AM    <DIR>          Downloads
...
              16 Dir(s)
```

**`dir` = directory listing** (equivalent to Linux `ls`)

```cmd
# dir output columns:
Date/Time    → last modified
<DIR>        → it's a directory (folder)
Size         → file size in bytes (blank for dirs)
Name         → file or folder name
```

### `dir` Flags Cheat Sheet

```cmd
dir              # basic listing
dir /a           # ALL files including hidden
dir /s           # search subfolders recursively
dir /s file.txt  # FIND a file anywhere below current dir
dir /b           # bare format (names only, no details)
dir /o           # sorted alphabetically
dir /od          # sorted by date (oldest first)
dir /o-d         # sorted by date (newest first)
dir /w           # wide format (more names per line)
dir /p           # pause after each screen (like less)
dir *.txt        # list only .txt files
dir *.log        # list only .log files
dir /s *.log     # find ALL .log files in subdirs
```

---

## 🔷 3. Step 3 — "Show Hidden Files" → `dir /a`

```cmd
C:\Users\Administrator> dir /a
 Directory of C:\Users\Administrator

02/27/2022  .
02/27/2022  ..
09/12/2024  .ssh                    ← HIDDEN folder!
02/10/2022  AppData                 ← HIDDEN folder!
03/11/2021  NTUSER.DAT              ← HIDDEN file!
...
```

**Hidden doesn't mean secret — it means Windows hides it by default.**

```
Why files are hidden:
  System files    → Windows hides to prevent accidental deletion
  AppData folder  → App settings/data hidden to reduce clutter
  Dotfiles        → config files hidden for cleanliness
  NTUSER.DAT      → your user registry hive (important!)

Why YOU need to see them:
  Malware hides in AppData\Roaming
  Credentials stored in hidden config files
  SSH keys in hidden .ssh folder
  Registry hives contain persistence mechanisms
  Forensics: you must see EVERYTHING
```

> ⚠️ **Security note:** `dir /a` is one of the first commands
> run during incident response and forensics on a Windows machine.
> Malware frequently uses hidden files and folders to avoid
> detection by casual users browsing File Explorer.

---

## 🔷 4. Step 4 — "Move Around" → `cd <folder>`

```cmd
# Go INTO a folder
C:\Users\Administrator> cd Documents
C:\Users\Administrator\Documents>

# Go BACK one level
C:\Users\Administrator\Documents> cd ..
C:\Users\Administrator>

# Go to root of drive
cd \

# Go using absolute path (from anywhere)
cd C:\Users\Administrator\Desktop

# Go to a path with spaces (use quotes)
cd "C:\Program Files\Important Folder"

# Change drive entirely (cd doesn't switch drives!)
D:          ← just type the drive letter with colon
cd D:\data  ← then navigate

# Go back multiple levels at once
cd ..\..    ← goes up TWO levels
```

### Windows Filesystem Structure

```
C:\
├── Windows\              ← OS system files
│   ├── System32\         ← Core executables and DLLs
│   │   ├── drivers\      ← Hardware drivers
│   │   └── config\       ← Registry hives (SAM!)
│   └── SysWOW64\         ← 32-bit compatibility
├── Program Files\        ← 64-bit installed apps
├── Program Files (x86)\  ← 32-bit installed apps
├── Users\
│   ├── Administrator\    ← Admin's home folder
│   │   ├── Desktop\
│   │   ├── Documents\
│   │   ├── Downloads\
│   │   └── AppData\      ← HIDDEN — app data + malware hides here
│   │       ├── Local\
│   │       ├── LocalLow\
│   │       └── Roaming\  ← Most malware targets this!
│   └── Public\           ← Shared by all users
├── ProgramData\          ← HIDDEN — system-wide app data
└── Temp\                 ← Temporary files
```

---

## 🔷 5. Step 5 — "Find a File" → `dir /s filename`

```cmd
C:\Users\Administrator> dir /s task_brief.txt

 Volume in drive C has no label.

 Directory of C:\Users\Administrator\Documents\Onboarding

03/15/2024  09:30 AM               512 task_brief.txt

       1 File(s)            512 bytes
       0 Dir(s)  45,678,901,248 bytes free
```

**`/s` = search all SUBfolders recursively**

```cmd
# Find any file starting from current directory
dir /s filename.txt

# Find from root (search ENTIRE C: drive)
cd \
dir /s passwords.txt

# Find files by extension anywhere
dir /s *.txt         # all text files
dir /s *.log         # all log files
dir /s *.config      # all config files (goldmine!)
dir /s *.bak         # backup files (often contain old passwords!)
dir /s *.sql         # database files
dir /s *.kdbx        # KeePass databases!
dir /s *.pfx         # certificates with private keys!
```

> ⚠️ **Pentesting recon:** `dir /s *.txt`, `dir /s *.config`,
> and `dir /s *.kdbx` run from the Users directory reveals
> sensitive documents, config files, and password managers.
> Always run these when doing post-exploitation file recon.

---

## 🔷 6. Step 6 & 7 — Navigate and Read → `cd` + `type`

```cmd
# Navigate to the file's location
C:\> cd C:\Users\Administrator\Documents\Onboarding

# Confirm the file is there
C:\Users\...\Onboarding> dir
task_brief.txt

# Read the file
C:\Users\...\Onboarding> type task_brief.txt
Great job finding your way around the terminal.

Your next assignment is to collect a system report:
- Who you're logged in as
- The computer name
- Windows version
- Network configuration
```

### File Reading Commands on Windows

```cmd
# type — print entire file (equivalent to Linux cat)
type file.txt
type C:\Windows\System32\drivers\etc\hosts

# more — scroll through large files (space = next page, q = quit)
more bigfile.txt
more C:\Windows\System32\drivers\etc\hosts

# Combine with find (like grep on Linux)
type file.txt | find "password"
type auth.log | find "Failed"
type file.txt | findstr /i "secret"   # case insensitive

# Read multiple files
type file1.txt file2.txt

# Read and save output
type file.txt > output.txt
```

---

## 🔷 7. System Recon Commands

### `whoami` — Who Are You?

```cmd
C:\Users\Administrator> whoami
desktop-abc123\administrator
```

```cmd
# More detailed — show all privileges
whoami /priv

# Show group memberships
whoami /groups

# Show everything
whoami /all

# Sample output analysis:
# BUILTIN\Administrators    → you ARE an admin
# NT AUTHORITY\SYSTEM       → highest Windows privilege
# SeDebugPrivilege Enabled  → can debug any process → Mimikatz!
# SeImpersonatePrivilege    → potato attacks for SYSTEM!
```

> ⚠️ **Pentesting:** After getting a shell, immediately run
> `whoami /priv` and `whoami /groups`. Enabled privileges like
> `SeImpersonatePrivilege`, `SeDebugPrivilege`, and
> `SeBackupPrivilege` all lead to privilege escalation paths.

### `hostname` — Machine Name

```cmd
C:\Users\Administrator> hostname
DESKTOP-ABC123
```

```cmd
# In corporate environments, hostnames reveal roles:
# WEB-PROD-01    → production web server
# DC-01          → domain controller (highest value target!)
# FILESERVER-02  → file server
# WORKSTATION-05 → employee workstation
```

### `systeminfo` — Full System Details

```cmd
C:\Users\Administrator> systeminfo

Host Name:                 DESKTOP-ABC123
OS Name:                   Microsoft Windows 11 Pro
OS Version:                10.0.22621 Build 22621
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Workstation
OS Build Type:             Multiprocessor Free
Registered Owner:          Administrator
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
Total Physical Memory:     8,192 MB
Available Physical Memory: 4,096 MB
Domain:                    WORKGROUP
Hotfix(s):                 25 Hotfix(s) Installed.
                           [01]: KB5031455
                           [02]: KB5027397
                           ...
Network Card(s):           1 NIC(s) Installed.
```

**Key fields to focus on:**

```
OS Name        → Windows version (search CVEs for this!)
OS Version     → Build number (find unpatched vulnerabilities!)
System Type    → x64-based or x86 (32-bit vs 64-bit)
Hotfix(s)      → installed patches (MISSING patches = exploitable!)
Domain         → WORKGROUP=standalone, domain name=corporate network
```

> ⚠️ **Security:** Cross-reference `OS Version` and `Hotfix(s)`
> with known CVEs. If a critical patch (like MS17-010 for
> EternalBlue) is NOT in the hotfix list → that vulnerability
> is still exploitable. This is exactly what attackers check.

```cmd
# Extract just the key fields
systeminfo | findstr /i "OS Name"
systeminfo | findstr /i "OS Version"
systeminfo | findstr /i "System Type"
systeminfo | findstr /i "Hotfix"
systeminfo | findstr /i "Domain"
```

### `ipconfig` — Network Information

```cmd
C:\Users\Administrator> ipconfig

Windows IP Configuration

Ethernet adapter Ethernet:
   Connection-specific DNS Suffix  :
   IPv4 Address. . . . . . . . . . : 192.168.1.105
   Subnet Mask . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . : 192.168.1.1

Wireless LAN adapter Wi-Fi:
   Media State . . . . . . . . . . : Media disconnected
```

```cmd
# More detail (DNS servers, MAC addresses, lease info)
ipconfig /all

# Key fields:
# IPv4 Address    → this machine's IP on the network
# Subnet Mask     → network range (255.255.255.0 = /24 = 254 hosts)
# Default Gateway → router IP (this is how traffic exits the network)
# DNS Servers     → who resolves domain names
# MAC Address     → physical hardware identifier
# DHCP Server     → who assigned this IP
```

> 💡 **Analyst workflow:** `ipconfig /all` reveals the full
> network picture. The Default Gateway IP often points to the
> router — which is usually the next pivot target in network
> pentesting. DNS server IP often reveals if this machine is
> part of an Active Directory domain (AD's DNS is on the DC).

---

## 🔷 8. Complete Windows CMD Cheat Sheet

```cmd
── NAVIGATION ────────────────────────────────────────────────────
cd                   # show current directory (like pwd)
cd Documents         # go into Documents folder
cd ..                # go up one level
cd \                 # go to drive root
cd C:\Windows\System32  # absolute path navigation
D:                   # switch to D: drive

── FILE LISTING ──────────────────────────────────────────────────
dir                  # list visible files
dir /a               # list ALL files including hidden
dir /s               # list files in all subfolders
dir /s file.txt      # FIND a file recursively
dir /b               # bare names only
dir *.log            # only .log files
dir /a /s *.txt      # ALL (hidden included) .txt files everywhere

── FILE READING ──────────────────────────────────────────────────
type file.txt        # print file content (like cat)
more file.txt        # paginate large files
type file | find "keyword"     # search in file (like grep)
type file | findstr /i "key"   # case-insensitive search

── SYSTEM RECON ──────────────────────────────────────────────────
whoami               # current username
whoami /priv         # user privileges
whoami /groups       # group memberships
whoami /all          # everything
hostname             # computer name
systeminfo           # full system information
systeminfo | findstr "OS"     # extract OS info only
ipconfig             # basic network config
ipconfig /all        # full network details including MAC, DNS

── PROCESS INFO ──────────────────────────────────────────────────
tasklist             # all running processes
tasklist | findstr "malware"  # search for specific process
taskkill /F /IM process.exe   # kill process by name
taskkill /F /PID 1234         # kill process by PID

── NETWORK ───────────────────────────────────────────────────────
netstat -ano         # all connections with PIDs
netstat -an | findstr "ESTABLISHED"  # active connections
ping 8.8.8.8         # test connectivity
nslookup google.com  # DNS lookup
tracert google.com   # trace network path

── USER MANAGEMENT ───────────────────────────────────────────────
net user             # list all users
net user username    # details about specific user
net localgroup administrators  # who has admin?
```

---

## 🔷 9. PowerShell Equivalents (Modern Windows CLI)

```powershell
# PowerShell vs CMD — same tasks, more power
cd              → Get-Location (or pwd)
dir             → Get-ChildItem (or ls, dir)
dir /a          → Get-ChildItem -Force
dir /s file     → Get-ChildItem -Recurse -Filter "file.txt"
type file       → Get-Content file.txt
whoami          → $env:USERNAME
hostname        → $env:COMPUTERNAME
systeminfo      → Get-ComputerInfo
ipconfig        → Get-NetIPAddress

# PowerShell exclusive power
Get-Process                          # running processes
Get-Service                          # Windows services
Get-EventLog -LogName Security -Newest 50  # event logs
Get-NetFirewallRule                  # firewall rules
Get-LocalUser                        # local users
Get-LocalGroupMember Administrators  # admin group members
```

---

## 🔗 Security Attack Map — Windows CMD

| Command                                  | Attack Scenario                                       |
| ---------------------------------------- | ----------------------------------------------------- |
| `dir /a /s *.txt`                        | Find password files left by admins                    |
| `dir /a /s *.kdbx`                       | Find KeePass password databases                       |
| `dir /a /s *.config`                     | Find app config files with credentials                |
| `type %USERPROFILE%\AppData\Roaming\...` | Read app credential files                             |
| `whoami /priv`                           | Check for exploitable privileges (SeImpersonate etc.) |
| `whoami /groups`                         | Check group memberships for lateral movement          |
| `systeminfo`                             | Find unpatched CVEs (missing Hotfix entries)          |
| `ipconfig /all`                          | Map network, find domain controller via DNS           |
| `netstat -ano`                           | Find C2 connections (unusual outbound traffic)        |
| `tasklist`                               | Find malicious processes running                      |

---

## ⚡ Enriched Insights (Beyond the Source Material)

### The Real Power — Combining Commands

```cmd
# Search entire C: drive for password files
cd C:\
dir /a /s *password* 2>nul
dir /a /s *credential* 2>nul
dir /a /s *secret* 2>nul

# Find all config files (web app credentials often here)
dir /s /b *.config 2>nul
dir /s /b web.config 2>nul
dir /s /b *.ini 2>nul

# Search INSIDE files for the word "password"
findstr /si password *.txt *.xml *.config *.ini

# Find recently modified files (incident response)
forfiles /m *.* /d -1 /c "cmd /c echo @path @fdate @ftime"
```

### Why CMD Still Matters When PowerShell Exists

```
PowerShell is more powerful, BUT:
  → PowerShell execution may be restricted (ExecutionPolicy)
  → CMD is always available on every Windows version
  → Some legacy scripts and malware only use CMD
  → CMD commands work in batch files (.bat) — still widely used
  → Forensics often involves reading CMD history artifacts

Pro move: Know BOTH.
  Use CMD for quick navigation and basic recon.
  Use PowerShell for deep investigation and automation.
```

### Windows CLI vs Linux CLI — The Mental Model

```
Both are just languages for talking to the OS.

The concepts are identical:
  Navigate filesystem    ✅ Both
  List files             ✅ Both
  Find hidden files      ✅ Both
  Search for files       ✅ Both
  Read file contents     ✅ Both
  Get system info        ✅ Both
  Network configuration  ✅ Both

The syntax differs, the logic is the same.
Learn one well → learning the other is 50% faster.

The most important skill is NOT memorizing commands.
It's developing the MINDSET:
  "What do I need to know? What command gives me that?"
```

---

_Notes compiled from TryHackMe — Windows Command Line Module_
_Enriched with security use cases, PowerShell equivalents, and pentest context_
