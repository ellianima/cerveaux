# 🖥️ Virtualization — VMs, Hypervisors, Containers & Docker

> **Source:** TryHackMe — Pre-Security / Virtualization Fundamentals Module
> **Purpose:** Core virtualization knowledge for cybersecurity & DevOps
> **Covers:** Why virtualization exists, Hypervisors (Type 1 & 2),
> Virtual Machines, Containers, Docker, VM Management, Host Monitoring

---

## 🧒 Feynman Explanation — The Building Analogy

**Before virtualization:** One person lives in an entire 10-floor
building alone. They use only the ground floor. The other 9 floors
sit empty — but they still pay electricity, water, and maintenance
for the whole building. Massively wasteful.

**After virtualization:** The building is divided into separate
apartments. Each apartment has its own door, kitchen, and privacy.
Different people live independently without bothering each other.
They all share the building's infrastructure — cheaper for everyone.

```
Building          = Physical Server
Apartments        = Virtual Machines
Tenants           = Applications / Operating Systems
Building Manager  = Hypervisor (divides building safely)
```

---

## 🔷 1. The Problem Virtualization Solved

### Before Virtualization: "One Server = One Application"

```
Company needs 4 services → buys 4 physical servers

[Web Server]  [Database]  [Email]  [Internal App]
     │              │         │           │
  Using 10%    Using 15%  Using 8%    Using 12%
  of capacity  of capacity           of capacity

Problems:
  ❌ High cost     — hardware + electricity + cooling + space
  ❌ Low use       — servers running at 5–20% capacity
  ❌ Slow deploy   — new server takes days or weeks to set up
  ❌ Hard to scale — need more resources? buy another server
```

### After Virtualization: Many Apps, One Server

```
One physical server runs ALL 4 services as VMs:

┌──────────────────────────────────────────┐
│           Physical Server                │
│  ┌────────┐ ┌──────────┐ ┌────────────┐ │
│  │Web-VM  │ │Database-VM│ │  Email-VM  │ │
│  │(10% CPU│ │(15% CPU)  │ │(8% CPU)    │ │
│  └────────┘ └──────────┘ └────────────┘ │
│            Hypervisor                    │
└──────────────────────────────────────────┘

Benefits:
  ✅ Cost savings     — one physical server, multiple VMs
  ✅ Better utilization — use the hardware fully
  ✅ Fast deployment  — spin up VM in minutes, not weeks
  ✅ Easy scaling     — allocate more CPU/RAM in seconds
  ✅ Isolation        — if one VM crashes, others unaffected
  ✅ Snapshots        — freeze state, restore if something breaks
```

---

## 🔷 2. The Hypervisor — The Building Manager

### What Is a Hypervisor?

```
A hypervisor is software that:
  1. Divides physical hardware into multiple virtual machines
  2. Gives each VM its own share of CPU, RAM, storage
  3. Keeps VMs completely isolated from each other
  4. Manages VM lifecycle: start, stop, pause, clone, delete
  5. Acts as the referee — VMs cannot fight over resources
```

### Type 1 vs Type 2 Hypervisor

| Feature          | Type 1 (Bare Metal)                 | Type 2 (Hosted)                |
| ---------------- | ----------------------------------- | ------------------------------ |
| Runs on          | Directly on hardware                | Inside a host OS               |
| Performance      | High (no OS overhead)               | Lower (double OS layer)        |
| Use case         | Production servers, data centers    | Learning, testing, home labs   |
| Examples         | VMware ESXi, Microsoft Hyper-V, KVM | VirtualBox, VMware Workstation |
| Setup difficulty | Complex                             | Easy                           |

```
TYPE 1 — Bare Metal:              TYPE 2 — Hosted:
┌─────────────────┐               ┌─────────────────┐
│  Physical HW    │               │  Physical HW    │
├─────────────────┤               ├─────────────────┤
│   Hypervisor    │               │   Host OS       │
│  (VMware ESXi)  │               │  (Windows/Linux)│
├───────┬─────────┤               ├─────────────────┤
│  VM A │  VM B   │               │   Hypervisor    │
│       │         │               │  (VirtualBox)   │
└───────┴─────────┘               ├───────┬─────────┤
                                  │  VM A │  VM B   │
                                  └───────┴─────────┘
```

### Which Hypervisor Type for Which Use Case?

| Use Case                     | Type 1 | Type 2 |
| ---------------------------- | ------ | ------ |
| Production server            | ✅     |        |
| Database server              | ✅     |        |
| Data center                  | ✅     |        |
| Test malicious files         |        | ✅     |
| Software testing             |        | ✅     |
| **Kali Linux (your setup!)** |        | ✅     |
| Learning/home lab            |        | ✅     |

> 💡 **Your Kali Linux VM runs on VirtualBox or VMware
> Workstation — both Type 2 hypervisors. Perfect for learning,
> malware analysis, and pentesting labs.**

---

## 🔷 3. Virtual Machines (The Apartments)

### What Is a VM?

```
A Virtual Machine is a complete virtual computer:
  ✅ Has its own virtual CPU
  ✅ Has its own virtual RAM
  ✅ Has its own virtual storage (disk image file)
  ✅ Has its own virtual network interface
  ✅ Can run ANY operating system (Windows, Linux, macOS)
  ✅ Completely isolated from other VMs on the same host

It behaves EXACTLY like a real physical computer.
The applications running inside have no idea they're virtual.
```

### Why Pentesters NEED VMs

```
Use case 1: Run Kali Linux on a Windows laptop
  → Install VirtualBox/VMware on Windows
  → Create Kali Linux VM
  → Full Kali environment without buying a second laptop

Use case 2: Test malware safely
  → Create isolated VM (no network connection to host)
  → Run suspicious file inside VM
  → Malware infects VM only — host machine stays clean
  → Take snapshot BEFORE → restore AFTER testing

Use case 3: Build vulnerable lab targets
  → Spin up intentionally vulnerable VMs (Metasploitable, DVWA)
  → Practice attacks legally on YOUR OWN machines
  → Delete or restore snapshot when done
```

### 💻 VM Management (VirtualBox CLI)

```bash
# List all VMs
VBoxManage list vms

# List running VMs
VBoxManage list runningvms

# Start a VM (headless = no window, like a server)
VBoxManage startvm "Kali-Linux" --type headless

# Take a snapshot (freeze current state)
VBoxManage snapshot "Kali-Linux" take "clean-state"

# Restore snapshot
VBoxManage snapshot "Kali-Linux" restore "clean-state"

# Delete VM
VBoxManage unregistervm "Kali-Linux" --delete

# Show VM info
VBoxManage showvminfo "Kali-Linux"
```

### VM States You'll See in a Virtualization Manager

| Status         | Meaning                           | Action              |
| -------------- | --------------------------------- | ------------------- |
| 🟢 **Running** | VM is active and serving          | Normal              |
| ⚪ **Stopped** | VM is off, not using CPU/RAM      | Start if needed     |
| 🔴 **Error**   | VM crashed or misconfigured       | Restart/investigate |
| 🟡 **Paused**  | VM frozen, state preserved in RAM | Resume              |
| 🔵 **Cloning** | VM being duplicated               | Wait                |

---

## 🔷 4. Containers (The Rooms Inside the Apartment)

### 🧒 Feynman Explanation

A VM is a full apartment — it has its own kitchen, bathroom,
bedroom, everything. But what if you just need one room for a
specific purpose? A container is like renting just a room in
an existing apartment. It has privacy and isolation but shares
the building's plumbing and electricity (the OS kernel).

### VM vs Container — The Critical Difference

```
VIRTUAL MACHINE:                    CONTAINER:
┌──────────────────┐                ┌──────────────────┐
│ Guest OS (Linux) │                │   App + Libs     │
│ (full OS kernel) │                │ (no separate OS) │
├──────────────────┤                ├──────────────────┤
│   App + Libs     │                │  Container Engine│
├──────────────────┤                │    (Docker)      │
│   Hypervisor     │                ├──────────────────┤
├──────────────────┤                │  Host OS Kernel  │
│  Physical HW     │                ├──────────────────┤
└──────────────────┘                │  Physical HW     │
                                    └──────────────────┘
Size:  Gigabytes                    Size:  Megabytes
Boot:  Minutes                      Boot:  Seconds
OS:    Full separate OS             OS:    Shares host kernel
```

### Containers vs VMs — Full Comparison

| Feature   | Virtual Machine            | Container                     |
| --------- | -------------------------- | ----------------------------- |
| Size      | GBs (full OS included)     | MBs (app + libs only)         |
| Boot time | Minutes                    | Seconds                       |
| Isolation | Complete (separate kernel) | Process-level (shared kernel) |
| OS        | Any OS                     | Must match host kernel type   |
| Overhead  | High                       | Very low                      |
| Use case  | Full environments, testing | App deployment, microservices |
| Security  | Stronger isolation         | Weaker (shared kernel)        |
| Tool      | VirtualBox, VMware         | Docker, Podman                |

### The Full Stack — Physical → VM → Container

```
┌─────────────────────────────────────┐
│         Physical Server             │
├─────────────────────────────────────┤
│            Hypervisor               │
├──────────────────┬──────────────────┤
│  Virtual         │  Virtual         │
│  Machine A       │  Machine B       │
│  (standalone)    │                  │
│                  │  ┌────────────┐  │
│                  │  │Container A │  │
│                  │  ├────────────┤  │
│                  │  │Container B │  │
│                  │  └────────────┘  │
└──────────────────┴──────────────────┘

VMs provide maximum separation and flexibility.
Containers inside VMs give lightweight, fast-deploying apps.
This is how AWS, Google Cloud, and Azure actually work.
```

---

## 🔷 5. Docker — The Container Platform

### What Is Docker?

```
Docker is the most popular platform for building,
deploying, and running containers.

Key concepts:
  Image    → Blueprint/recipe for a container
             (like a class in programming)
  Container → A running instance of an image
             (like an object created from a class)
  Registry → Library of images (Docker Hub)
  Dockerfile → Instructions to build a custom image
```

### 💻 Docker Commands — Essential for Security Work

```bash
# ── BASIC COMMANDS ────────────────────────────────────────────────

# Download an image from Docker Hub
docker pull ubuntu:22.04
docker pull kalilinux/kali-rolling

# Run a container interactively
docker run -it ubuntu:22.04 bash
docker run -it kalilinux/kali-rolling bash

# List running containers
docker ps

# List ALL containers (including stopped)
docker ps -a

# Stop a container
docker stop <container_id>

# Delete a container
docker rm <container_id>

# List downloaded images
docker images

# Delete an image
docker rmi ubuntu:22.04

# ── USEFUL PATTERNS FOR SECURITY WORK ────────────────────────────

# Run isolated container with NO network (safe malware analysis)
docker run --network none -it ubuntu bash

# Run container and auto-delete when done (clean testing)
docker run --rm -it ubuntu bash

# Run container with shared folder (pass files in/out)
docker run -v /home/user/tools:/tools -it kali bash
#                 ↑ host path    ↑ container path

# Run a web server (nginx) on port 8080
docker run -d -p 8080:80 nginx
# Now visit http://localhost:8080

# ── DOCKERFILE — BUILD YOUR OWN IMAGE ────────────────────────────

# Create a Dockerfile
cat > Dockerfile << 'EOF'
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y nmap python3 curl
WORKDIR /tools
COPY scripts/ /tools/scripts/
CMD ["/bin/bash"]
EOF

# Build the image
docker build -t my-pentest-tools .

# Run your custom image
docker run -it my-pentest-tools
```

### Container Images — Templates for Containers

```
Container Image = a pre-packed template that contains:
  ├── The application
  ├── All its dependencies (libraries, tools)
  ├── Configuration files
  └── Instructions to start

Like a snapshot of a perfect working environment.
Share it once → anyone can run the exact same app anywhere.

Popular security images on Docker Hub:
  kalilinux/kali-rolling    → full Kali Linux
  remnux/remnux             → malware analysis tools
  owasp/webgoat-8.0         → intentionally vulnerable web app
  vulnerables/web-dvwa      → DVWA (practice SQLi, XSS, etc.)
```

---

## 🔷 6. Virtualization Manager — Real-World Operations

### Reading a VM Dashboard

```
VM Dashboard columns explained:

Name          → VM identifier (Mail-SERVER, WebServer-PROD)
Status        → Running / Stopped / Error
CPU Cores     → virtual CPUs allocated to this VM
Memory (GB)   → RAM allocated
Disk (GB)     → Storage allocated
IP Address    → DHCP = auto-assigned | static IP shown
Uptime        → how long it's been running
Host          → which physical server it lives on (HV-PROD-01)
```

### VM Actions

```
▶  Play button   → START the VM
⬛  Stop button   → STOP the VM (graceful shutdown)
🔄  Restart       → RESTART the VM (fix errors!)
🗑️  Delete        → REMOVE the VM permanently
```

### Reading Host Monitoring Dashboard

```
Physical host health metrics:

CPU Usage   → % of physical CPU being used by all VMs
Memory Usage → % of physical RAM allocated to VMs
Storage Usage → % of physical disk used
VMs count    → how many VMs this host is running
Status       → Connected / Disconnected

HEALTHY:     CPU < 80%, Memory < 80%, Storage < 85%
WARNING:     CPU 80–90%, Memory 80–90%
CRITICAL:    CPU > 90%, Memory > 90% → VMs will slow down!
DISASTER:    Disconnected → all VMs on this host are unreachable
```

### Example from the Screenshots — Real Analysis

```
HV-PROD-01:  CPU 45%, Memory 68%, Storage 72%  → HEALTHY ✅
             Has capacity for more VMs

HV-PROD-02:  CPU 98%, Memory 90%, Storage 95%  → CRITICAL ❌
             Running 8 VMs, nearly maxed out
             Action needed: migrate VMs to another host

HV-BACKUP-01: CPU 0%, Memory 0%, Disconnected  → DOWN ❌
              No VMs running — needs investigation
```

---

## 🔷 7. Key Terminology — Quick Reference

| Term                     | Simple Definition                                                |
| ------------------------ | ---------------------------------------------------------------- |
| **Virtualization**       | One physical computer acting like multiple separate computers    |
| **Hypervisor**           | The manager software that creates and runs VMs                   |
| **Virtual Machine (VM)** | A whole virtual computer inside a real one, with its own OS      |
| **Container**            | A small, isolated box for one app that shares the host OS kernel |
| **Container Image**      | A pre-packed recipe/template used to create containers           |
| **Docker**               | The most popular platform for building and running containers    |
| **Snapshot**             | A frozen save-state of a VM (restore if something breaks)        |
| **Network Ports**        | Special numbered entry points that apps use to talk over network |
| **Host**                 | The physical machine running the hypervisor                      |
| **Guest**                | The VM running inside the host                                   |

### Benefits of Virtualization (Summary)

```
✅ Cost savings         — fewer physical servers needed
✅ Better resource use  — actually use your hardware fully
✅ Safe security testing— isolate malware from host
✅ Faster deployment    — spin up VM in minutes vs. days
✅ Flexibility          — run any OS on any hardware
✅ Portability          — move VMs between hosts easily
✅ Scalability          — add resources without new hardware
✅ Centralized mgmt     — manage all VMs from one dashboard
```

---

## 🔗 Security Attack Map — Virtualization

| Target                | Attack                          | Technique                              |
| --------------------- | ------------------------------- | -------------------------------------- |
| **VM itself**         | VM escape (rare, high severity) | CVE-based hypervisor exploit           |
| **Snapshots**         | Revert to vulnerable state      | Physical/admin access                  |
| **Docker containers** | Container escape                | Privileged containers, kernel exploits |
| **Docker socket**     | Host takeover                   | `/var/run/docker.sock` exposure        |
| **Images**            | Malicious image from registry   | Supply chain attack on Docker Hub      |
| **Hypervisor**        | Hypervisor rootkit              | Deep persistence, survives reinstall   |
| **VM network**        | VM-to-VM lateral movement       | Misconfigured virtual network          |

---

## ⚡ Enriched Insights (Beyond the Source Material)

### Why YOUR Kali VM Setup Is Perfect for Security

```
Your current setup:
  Windows/Linux host  →  VirtualBox (Type 2 hypervisor)
                      →  Kali Linux VM (your attack machine)

Best practice additions:
  Snapshot "clean" state before each lab
  → If you break something, restore in 30 seconds

Create a second VM as your target:
  Metasploitable 2 (free, intentionally vulnerable Linux)
  → Download from SourceForge
  → Practice exploits legally on YOUR OWN lab

Network modes in VirtualBox:
  NAT         → VM gets internet, host not reachable from VM
  Host-only   → VM and host can talk, no internet
  Internal    → VMs talk to each other, no host/internet
  Bridged     → VM acts like real device on your network
```

### Docker for Security Research

```bash
# Run DVWA (vulnerable web app) for practice
docker run -d -p 80:80 vulnerables/web-dvwa

# Access at http://localhost
# Practice: SQL injection, XSS, CSRF, File Upload, etc.

# Run Juice Shop (OWASP's vulnerable Node.js app)
docker run -d -p 3000:3000 bkimminich/juice-shop

# Access at http://localhost:3000
# 100+ security challenges, modern web vulns

# Run isolated Kali for specific tools
docker run --rm -it kalilinux/kali-rolling bash
apt install nmap sqlmap nikto -y  # install what you need
# Container auto-deletes when you exit (--rm flag)
```

### Cloud = Virtualization at Massive Scale

```
AWS EC2  → virtual machines (VMs) on Amazon's physical hardware
AWS ECS  → containers managed by Amazon
AWS Lambda → serverless (containers that run for milliseconds)

Google GCE → VMs on Google's hardware
Azure VMs  → VMs on Microsoft's hardware

Every cloud "instance" you rent is a VM on a shared
physical server in a data center somewhere.
Virtualization is the technology that makes cloud computing possible.
```

---

_Notes compiled from TryHackMe — Virtualization Fundamentals Module_
_Enriched with Docker commands, security context, and practical lab setup_
