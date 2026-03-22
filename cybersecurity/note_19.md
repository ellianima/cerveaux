# 🪟 Windows OS — Fundamentals for Cybersecurity

> **Source:** TryHackMe — Pre-Security / Windows Fundamentals Module
> **Purpose:** Windows knowledge for SOC analysts and pentesters
> **Covers:** History, authentication, desktop, file system, apps,
> updates, settings, Task Manager, Windows Security, Defender Firewall

---

## 🧒 Feynman Explanation — Windows as an Airport Terminal

You've already logged in through security (authentication).
Now you're inside the terminal (the Desktop). Everything branches
out from here — gates (apps), directories (File Explorer),
departures board (Start Menu), airport services (built-in tools).

The OS manages everything happening behind the scenes so you
can focus on your journey (getting work done).

---

## 🔷 1. Brief History of Windows

```
1981  MS-DOS         Black screen, type commands, no mouse
1985  Windows 1.0    First GUI — windows, menus, mouse support
2000  Windows ME     Consumer-focused, still unstable
2001  Windows XP     Hugely successful, still seen in legacy systems
2009  Windows 7      Stable, beloved, finally replaced XP
2015  Windows 10     Most adopted modern Windows
2021  Windows 11     Current flagship desktop OS

Key insight: Windows started as a shell ON TOP of DOS.
Over decades, it became a complete OS in its own right.

Security note: Legacy Windows (XP, 7) still runs on ATMs,
hospitals, industrial systems — STILL being attacked today.
EternalBlue (WannaCry, 2017) exploited Windows 7 vulnerabilities.
```

---

## 🔷 2. Authentication & User Account Types

### 🧒 Feynman Explanation

The login screen is the airport security checkpoint. Before you
enter the terminal (desktop), you must prove who you are. Your
boarding pass (password/PIN) determines which areas you can
access — economy lounge or executive VIP suite.

### Windows Account Types

| Account Type      | Privilege Level | What They Can Do                                       |
| ----------------- | --------------- | ------------------------------------------------------ |
| **Guest**         | Lowest          | Temporary access, no system settings changes           |
| **Standard**      | Medium          | Daily tasks, personal settings, run apps               |
| **Administrator** | Highest         | Install software, change system settings, manage users |

```
In a corporate environment (Active Directory):
  Domain User    → standard user across the network
  Domain Admin   → administrator across ALL machines on domain
  Local Admin    → admin only on that specific machine
  SYSTEM         → highest privilege — the OS itself

Pentest importance:
  Goal of most attacks: escalate from Guest/Standard → Admin → SYSTEM
  SYSTEM = complete control, unrestricted access to everything
```

> ⚠️ **Security note:** Running as Administrator by default
> is a major security risk. UAC (User Account Control) exists
> to prompt you before Administrator-level actions execute.
> Many malware samples specifically target Administrator
> accounts because they immediately have full system control.

### 💻 Windows User Management (PowerShell)

```powershell
# List all local user accounts
Get-LocalUser

# List all local groups
Get-LocalGroup

# List members of Administrators group
Get-LocalGroupMember -Group "Administrators"

# Create a new user (admin task)
New-LocalUser -Name "testuser" -Password (ConvertTo-SecureString
  "P@ssw0rd!" -AsPlainText -Force)

# Add user to Administrators group
Add-LocalGroupMember -Group "Administrators" -Member "testuser"

# Check current user's privileges
whoami
whoami /priv         # all privileges
whoami /groups       # all group memberships
net user             # list all users (CMD)
net localgroup administrators  # who has admin?
```

---

## 🔷 3. The Windows Desktop

### Desktop Components

| Component         | What It Is                                    | Security Relevance                                    |
| ----------------- | --------------------------------------------- | ----------------------------------------------------- |
| **Desktop**       | Main workspace — files, folders, shortcuts    | Sensitive files left here are accessible to all users |
| **Taskbar**       | Control strip — apps, tools, notifications    | Shows running processes, network status               |
| **Start Menu**    | Quick access to apps, settings, power options | Attackers use it to find installed software           |
| **Search**        | Find apps, files, settings quickly            | Can search registry and system files                  |
| **Task View**     | See all open windows, switch between them     | Shows what user was doing                             |
| **Pinned Apps**   | Frequently used apps in taskbar               |                                                       |
| **Network/Audio** | Network status and audio settings             | SOC: Network icon shows connected/disconnected        |
| **Date/Time**     | System clock and calendar                     | Forensics: timestamps matter                          |
| **Notifications** | System and app alerts                         | Security alerts appear here                           |

### Windows File System Structure

```
Windows uses a hierarchical folder structure:

C:\                          ← Root drive
├── Windows\                 ← OS system files (DO NOT TOUCH)
│   ├── System32\            ← Core Windows DLLs and executables
│   │   ├── drivers\         ← Hardware drivers
│   │   └── config\          ← Registry hives (SAM, SYSTEM, etc.)
│   └── SysWOW64\            ← 32-bit compatibility files
├── Program Files\           ← 64-bit installed applications
├── Program Files (x86)\     ← 32-bit installed applications
├── Users\                   ← All user home directories
│   ├── Administrator\
│   │   ├── Desktop\         ← C:\Users\Administrator\Desktop
│   │   ├── Documents\
│   │   ├── Downloads\
│   │   ├── AppData\         ← Hidden — app settings, often malware hides here!
│   │   │   ├── Local\
│   │   │   ├── LocalLow\
│   │   │   └── Roaming\
│   └── Public\              ← Shared between ALL users
├── ProgramData\             ← Hidden — app data for all users
└── Temp\                    ← Temporary files
```

> ⚠️ **Security note — AppData:** The `AppData\Roaming` and
> `AppData\Local` folders are hidden by default and are
> prime malware hiding spots. Many RATs, stealers, and
> persistence mechanisms drop files here because most users
> never look. Always check these during incident response.

### 💻 File System Navigation (CMD + PowerShell)

```powershell
# ── CMD COMMANDS ──────────────────────────────────────────────────
dir                          # list files in current directory
dir /a                       # list ALL including hidden files
cd C:\Users\Administrator    # change directory
cd ..                        # go up one level
type file.txt                # read file contents
copy source dest             # copy file
move source dest             # move file
del file.txt                 # delete file
mkdir NewFolder              # create directory
tree C:\Users /F             # show full directory tree with files

# ── POWERSHELL COMMANDS ───────────────────────────────────────────
Get-ChildItem                # ls equivalent
Get-ChildItem -Force         # show hidden files
Get-Content file.txt         # cat equivalent
Get-ChildItem -Recurse -Filter "*.log"  # find all .log files
Copy-Item source dest        # copy
Move-Item source dest        # move
Remove-Item file.txt         # delete

# Find sensitive files (pentesting recon)
Get-ChildItem -Path C:\ -Recurse -Filter "*.txt" 2>$null |
  Select-String -Pattern "password"

dir /s /b C:\*.config 2>nul  # find all config files
```

---

## 🔷 4. Built-In Windows Tools

### Essential Built-In Apps

| Tool                | Purpose                                  | Security Use                               |
| ------------------- | ---------------------------------------- | ------------------------------------------ |
| **File Explorer**   | Browse and manage files/folders          | Navigate to investigate suspicious files   |
| **Notepad**         | Edit text files                          | Read config files, scripts, logs           |
| **Calculator**      | Math operations                          | Convert hex/decimal (IP addresses, hashes) |
| **Paint**           | Basic image editing                      | Screenshot evidence                        |
| **Task Manager**    | Monitor processes, performance, services | Detect malicious processes                 |
| **CMD**             | Command-line interface                   | Run commands, scripts                      |
| **PowerShell**      | Advanced CLI + scripting                 | Automation, admin tasks, forensics         |
| **Registry Editor** | Edit Windows registry                    | Find persistence, malware keys             |
| **Event Viewer**    | View Windows event logs                  | SOC investigation, forensics               |
| **Services**        | Manage Windows services                  | Find malicious services                    |
| **msconfig**        | System configuration                     | Boot options, startup programs             |

### Getting System Information

```powershell
# About Your PC info (PowerShell)
Get-ComputerInfo

# Key fields:
# WindowsProductName   → Windows version
# OsArchitecture       → 64-bit / 32-bit
# CsName               → computer name
# TotalPhysicalMemory  → RAM

# CMD equivalent
systeminfo

# Quick system info
$env:COMPUTERNAME    # hostname
$env:USERNAME        # current user
$env:OS              # OS version
[Environment]::OSVersion   # detailed version
```

---

## 🔷 5. Task Manager — Real-Time System Monitor

### The Five Tabs

| Tab             | What It Shows                                          | Security Use                                |
| --------------- | ------------------------------------------------------ | ------------------------------------------- |
| **Processes**   | Running apps and background processes + resource usage | Spot unusual processes (malware)            |
| **Performance** | CPU, memory, disk, network graphs                      | Detect crypto miners (100% CPU)             |
| **Users**       | Currently logged-in users and their resource use       | Detect unauthorized sessions                |
| **Details**     | Technical view with PIDs, CPU, memory per process      | Match PID to suspicious network connections |
| **Services**    | Windows services and their status                      | Find malicious services                     |

### 💻 Task Manager from CLI

```powershell
# List all running processes
Get-Process
tasklist                     # CMD version

# Find specific process
Get-Process -Name "chrome"
tasklist | findstr "malware"

# Kill a process by name
Stop-Process -Name "suspicious.exe" -Force
taskkill /F /IM suspicious.exe   # CMD version

# Kill by PID
Stop-Process -Id 1234 -Force
taskkill /F /PID 1234

# Show processes with their file paths (find malware location!)
Get-Process | Select-Object Name, Id, Path

# Check what network connections a PID has
netstat -ano | findstr "ESTABLISHED"
# Then match the PID from tasklist

# Find processes with no path (suspicious — injected?)
Get-Process | Where-Object {$_.Path -eq $null}
```

> ⚠️ **SOC/Pentest note:** Malware often disguises itself
> with names similar to legitimate processes:
> `svchost.exe` vs `svch0st.exe`, `explorer.exe` running
> from the wrong directory, or `lsass.exe` with unusual
> CPU usage. Always check the full PATH of suspicious processes.

---

## 🔷 6. Updating Applications & Windows

### Why Updates Are Critical for Security

```
Every update contains:
  ✅ Security patches   → fixes vulnerabilities attackers exploit
  ✅ Bug fixes          → stability improvements
  ✅ Performance updates → speed improvements

Without updates:
  ❌ Known CVEs remain exploitable
  ❌ WannaCry (2017) spread via unpatched MS17-010 (EternalBlue)
  ❌ NotPetya used same unpatched vulnerability
  ❌ Millions of unpatched systems still compromised today

Rule: An unpatched vulnerability + internet exposure = eventual compromise
```

### Windows Update

```
Access via: Settings → Update & Security → Windows Update

Updates include:
  - Cumulative updates (OS patches, labeled KB + number)
  - Security Intelligence Updates (Defender definitions)
  - .NET Framework updates
  - Feature updates (major version changes)

From PowerShell (check + force update):
  # Check for updates (requires PSWindowsUpdate module)
  Install-Module PSWindowsUpdate
  Get-WindowsUpdate
  Install-WindowsUpdate -AcceptAll -AutoReboot
```

### Installing Applications

```
Method 1: Microsoft Store
  Safe, curated, automatic updates
  Not available on Windows Server by default

Method 2: Installer (.exe or .msi)
  Download from vendor website
  .exe = executable installer (runs setup wizard)
  .msi = Microsoft Installer package (more controlled)
  ⚠️ ONLY download from official vendor sites!

Method 3: winget (Windows Package Manager — modern)
  winget install 7zip.7zip
  winget install Mozilla.Firefox
  winget upgrade --all   ← update everything at once

Method 4: Chocolatey (third-party package manager)
  choco install nmap
  choco install wireshark
  choco upgrade all
```

### Uninstalling Applications

```
4 Methods:
  1. Settings → Apps → Apps & features → Uninstall
  2. Control Panel → Programs → Uninstall a program
  3. App's own built-in uninstaller
  4. Microsoft Store (for Store apps)

PowerShell uninstall:
  Get-Package | Where-Object {$_.Name -like "*7-Zip*"} |
    Uninstall-Package
```

---

## 🔷 7. Windows Settings & Control Panel

### Two Ways to Configure Windows

| Tool                 | Type                | Use For                                                      |
| -------------------- | ------------------- | ------------------------------------------------------------ |
| **Windows Settings** | Modern, centralized | Daily settings — display, audio, accounts, network, security |
| **Control Panel**    | Legacy interface    | Older/advanced config — still needed for some admin tasks    |

### Key Settings Locations for Security

```
Windows Settings:
  Accounts → Manage users, login options, sign-in requirements
  Privacy → What data apps can access (camera, mic, location)
  Update & Security → Windows Update, Windows Security, Backup
  Network & Internet → Firewall status, VPN, proxy settings

Control Panel:
  System and Security → Windows Firewall, Event Viewer, BitLocker
  User Accounts → Manage credentials and account types
  Programs → Add/Remove programs (uninstall)
  Network and Internet → Advanced network adapter settings
```

---

## 🔷 8. Native Windows Security

### Windows Security Dashboard

The central security control panel — four sections:

| Section                           | Protects Against            | Key Feature                                |
| --------------------------------- | --------------------------- | ------------------------------------------ |
| **Virus & Threat Protection**     | Malware, ransomware         | Real-time protection, custom scans         |
| **Firewall & Network Protection** | Unauthorized network access | Inbound/outbound rules per network profile |
| **App & Browser Control**         | Unsafe apps, websites       | SmartScreen, reputation-based protection   |
| **Device Security**               | Hardware-level threats      | Secure Boot, TPM, memory integrity         |

### Windows Defender Antivirus

```
Real-time protection:
  Scans every file as it's created, modified, or accessed
  Blocks known malware signatures and suspicious behavior

Scan types:
  Quick Scan    → checks most likely infection locations
  Full Scan     → scans entire hard drive (slow but thorough)
  Custom Scan   → you pick which folders to scan
  Offline Scan  → runs before Windows boots (catches rootkits)

Definitions:
  "Security Intelligence" = malware signature database
  Updated multiple times daily via Windows Update
  Must stay current — outdated definitions = blind spots
```

### Windows Defender Firewall

```
Three Network Profiles:
  Domain  → connected to organization's domain network
            (corporate office, managed by IT)
  Private → trusted networks (home, lab environment)
            allows more connections
  Public  → untrusted networks (café, airport Wi-Fi)
            most restrictive — blocks most inbound connections

Rules control:
  Inbound rules  → what can connect TO this computer
  Outbound rules → what this computer can connect TO
  Per-app rules  → allow specific apps through the firewall

Advanced settings (wf.msc):
  Full rule creation — by port, protocol, program, IP range
  Monitor active connections
  Export/import rule sets
```

### 💻 Windows Security from PowerShell

```powershell
# ── DEFENDER ──────────────────────────────────────────────────────
# Check Defender status
Get-MpComputerStatus

# Run quick scan
Start-MpScan -ScanType QuickScan

# Run full scan
Start-MpScan -ScanType FullScan

# Scan specific folder
Start-MpScan -ScanType CustomScan -ScanPath "C:\Users\Downloads"

# Check threat history
Get-MpThreatDetection

# Update definitions
Update-MpSignature

# ── FIREWALL ──────────────────────────────────────────────────────
# Check firewall status all profiles
Get-NetFirewallProfile | Select Name, Enabled

# Show all inbound rules
Get-NetFirewallRule -Direction Inbound |
  Where-Object {$_.Enabled -eq "True"} |
  Select DisplayName, Action, Direction

# Block specific port (create rule)
New-NetFirewallRule -DisplayName "Block Port 4444" `
  -Direction Inbound -Action Block -Protocol TCP -LocalPort 4444

# Allow specific app
New-NetFirewallRule -DisplayName "Allow Nmap" `
  -Direction Inbound -Action Allow `
  -Program "C:\Program Files\Nmap\nmap.exe"

# Disable firewall (⚠️ dangerous — for lab only)
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
```

---

## 🔷 9. Key Windows Terminology — Quick Reference

| Term                          | Definition                                                  |
| ----------------------------- | ----------------------------------------------------------- |
| **Desktop**                   | Main workspace where files, folders, shortcuts live         |
| **Taskbar**                   | Control strip for apps, tools, settings, notifications      |
| **Start Menu**                | Primary way to access apps, settings, power options         |
| **Search**                    | Quick-access method for finding apps, files, settings       |
| **File Explorer**             | Built-in tool to browse, manage, organize files/folders     |
| **Windows Update**            | Built-in tool to keep OS and security features current      |
| **Microsoft Store**           | Native app for installing trusted applications              |
| **Windows Settings**          | Centralized config for system, device, security settings    |
| **Control Panel**             | Legacy management interface for advanced system config      |
| **Task Manager**              | Real-time system monitor for processes and performance      |
| **Windows Security**          | Central dashboard for built-in security tools               |
| **Windows Defender Firewall** | Built-in firewall for blocking unauthorized network traffic |

---

## 🔗 Security Attack Map — Windows Specific

| Target                    | Attack                   | Tool/Technique                                       |
| ------------------------- | ------------------------ | ---------------------------------------------------- |
| **Administrator account** | Privilege escalation     | UAC bypass, token impersonation                      |
| **AppData\Roaming**       | Malware persistence      | Startup scripts, RATs hiding here                    |
| **Registry Run keys**     | Persistence              | `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` |
| **SAM database**          | Password hash extraction | Mimikatz, secretsdump                                |
| **LSASS process**         | Credential theft         | Mimikatz `sekurlsa::logonpasswords`                  |
| **Windows Defender**      | AV evasion               | Obfuscated payloads, AMSI bypass                     |
| **Firewall rules**        | Inbound connection       | Create allow rule or disable completely              |
| **Windows Update**        | Exploit unpatched CVE    | EternalBlue (MS17-010), PrintNightmare               |
| **Services**              | Persistence/privilege    | Malicious service installation                       |
| **Scheduled Tasks**       | Persistence              | `schtasks /create` for malware persistence           |

---

## ⚡ Enriched Insights (Beyond the Source Material)

### The Windows Registry — The Brain of Windows

```
The registry is a massive hierarchical database storing:
  ALL system configuration
  ALL user preferences
  ALL installed software settings
  ALL startup programs
  ALL device driver information

Key hives:
  HKLM (HKEY_LOCAL_MACHINE)  → system-wide settings (all users)
  HKCU (HKEY_CURRENT_USER)   → current user's settings
  HKCR (HKEY_CLASSES_ROOT)   → file associations
  HKU  (HKEY_USERS)          → all user profiles
  HKCC (HKEY_CURRENT_CONFIG) → hardware profile

Critical security keys:
  Persistence locations (malware loves these!):
  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
  HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce

Check these during incident response:
  reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
  reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
```

### Windows Event Logs — The SOC Analyst's Bible

```
Location: C:\Windows\System32\winevt\Logs\

Key logs:
  Security.evtx   → authentication, logon, privilege use
  System.evtx     → service starts/stops, driver errors
  Application.evtx → application errors and warnings

Must-know Event IDs (from earlier notes):
  4624  Successful logon
  4625  Failed logon (brute force!)
  4672  Admin privileges assigned
  4688  New process created (malware execution!)
  4720  User account created (backdoor!)
  4732  User added to admin group (escalation!)
  7045  New service installed (persistence!)

Access via PowerShell:
  Get-EventLog -LogName Security -Newest 50
  Get-EventLog -LogName Security -InstanceId 4625  # failed logins
  Get-WinEvent -FilterHashtable @{LogName='Security';Id=4624}
```

---

_Notes compiled from TryHackMe — Windows Fundamentals Module_
_Enriched with PowerShell commands, registry details, and security context_
