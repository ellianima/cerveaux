# 🌐 LAN Topologies, Network Devices & Core Protocols

> **Source:** TryHackMe — Networking Module  
> **Purpose:** Foundational networking knowledge for cybersecurity

---

## 🔷 1. Network Topology

A **topology** is the design or layout of a network — how devices are physically or logically connected.

---

## ⭐ Star Topology

All devices connect individually to a **central switch or hub**.

| ✅ Advantages                  | ❌ Disadvantages                                    |
| ------------------------------ | --------------------------------------------------- |
| Most reliable & scalable today | More expensive (more cabling + dedicated equipment) |
| Easy to add new devices        | More maintenance as network grows                   |
| Fault isolation is easier      | If central device fails → entire network fails      |

> 💡 **Key insight:** The central device (switch/hub) is the single point of failure — but modern switches are very robust.

---

## 🚌 Bus Topology

All devices connect to a **single backbone cable** — like leaves on a branch.

| ✅ Advantages            | ❌ Disadvantages                             |
| ------------------------ | -------------------------------------------- |
| Cheap and easy to set up | Prone to bottlenecks (all data on one cable) |
| Less cabling required    | Difficult to troubleshoot                    |
|                          | Single point of failure (the backbone cable) |
|                          | Little redundancy                            |

> 💡 **Key insight:** All data travels the same route → traffic jams happen easily.

---

## 💍 Ring Topology (Token Topology)

Devices connect **directly to each other in a loop**. Data travels in **one direction** around the ring.

| ✅ Advantages                             | ❌ Disadvantages                                                      |
| ----------------------------------------- | --------------------------------------------------------------------- |
| Little cabling needed                     | Inefficient — data may visit many devices before reaching destination |
| Less reliance on dedicated hardware       | One broken cable/device = **entire network breaks**                   |
| Easy to troubleshoot (one direction only) |                                                                       |
| Less prone to bottlenecks                 |                                                                       |

> 💡 **Key insight:** A device only forwards data if it has nothing to send itself — it prioritizes its own data first.

---

## 📊 Topology Comparison Table

| Topology | Cost   | Scalability | Fault Tolerance | Speed  |
| -------- | ------ | ----------- | --------------- | ------ |
| Star     | High   | High        | Medium          | High   |
| Bus      | Low    | Low         | Low             | Low    |
| Ring     | Medium | Low         | Low             | Medium |

---

## 🔌 2. Network Devices

### 🔀 Switch

- Aggregates multiple devices (computers, printers) via **Ethernet**
- Tracks which device is on which **port**
- Sends packets **only to the intended target** (unlike a hub which broadcasts to all)
- Port counts: 4, 8, 16, 24, 32, 64
- Used in: businesses, schools, large networks

> 💡 **Switch vs Hub:** A hub is "dumb" — it broadcasts to every port. A switch is "smart" — it sends only to the right port.

### 🌐 Router

- Connects **different networks** together
- Uses **routing** — creating paths so data can travel between networks
- Multiple switches/routers can be connected for **redundancy** (if one path fails, another is used)

> 💡 **Routing = GPS for data.** It finds the best path for packets to travel across networks.

### 🏗️ Internet → Router → Switch → Devices (Typical Setup)

```
The Internet (Cloud)
       ↓
    Router          ← connects to the internet
       ↓
    Switch          ← connects local devices
   /   |   \
Accounting  HR  Finance
```

---

## 🍰 3. Subnetting

**Subnetting** = splitting a large network into smaller **sub-networks** (subnets).

> Analogy: Like slicing a cake — there's a limited amount, and subnetting decides who gets what slice.

### Why Subnet?

- **Efficiency** — traffic only goes where it needs to
- **Security** — departments are isolated from each other
- **Full control** — admins can manage each subnet independently

### Real-World Example

A café has two subnets:

1. Employees, cash registers, internal devices
2. Public Wi-Fi hotspot

These are separated but both still connect to the internet.

---

## 🔢 IP Addresses & Subnet Masks

An IP address has **4 octets** (e.g., `192.168.1.1`), each ranging from **0–255**.

### Three Ways Subnets Use IP Addresses

| Type                | Purpose                                    | Example                          |
| ------------------- | ------------------------------------------ | -------------------------------- |
| **Network Address** | Identifies the network itself              | `192.168.1.0`                    |
| **Host Address**    | Identifies a specific device on the subnet | `192.168.1.100`                  |
| **Default Gateway** | Device that sends data to _other_ networks | `192.168.1.1` or `192.168.1.254` |

> 💡 **Key insight:** Home networks rarely need subnetting (max ~254 devices). Businesses with hundreds of devices do.

---

## 📡 4. ARP — Address Resolution Protocol

### What is ARP?

ARP links a device's **IP address** (logical) to its **MAC address** (physical).

- Every device keeps an **ARP cache** — a table of known IP-to-MAC mappings
- Without ARP, devices can't find _where_ to physically send data

### How ARP Works

1. **ARP Request** — broadcast to all devices: _"Who has IP 192.168.1.10?"_
2. **ARP Reply** — the device with that IP responds: _"I have it! My MAC is 18:AC:33:12:88:29"_
3. The requesting device **stores this in its ARP cache** for future use

### ARP Message Diagram

```
Step 1 — ARP Request (Broadcast):
  SRC MAC: 01:00:AB:78:99:33
  DST MAC: FF:FF:FF:FF:FF:FF  ← broadcast to ALL
  MSG: Who has IP 192.168.1.10?

Step 2 — ARP Reply (Unicast back):
  SRC MAC: 18:AC:33:12:88:29
  DST MAC: 01:00:AB:78:99:33  ← directly back to requester
  MSG: I have IP 192.168.1.10
```

> ⚠️ **Security note:** ARP has no authentication — this makes it vulnerable to **ARP Spoofing / Poisoning** (a common attack technique).

---

## 🏠 5. DHCP — Dynamic Host Configuration Protocol

### What is DHCP?

DHCP **automatically assigns IP addresses** to devices when they join a network (instead of manual configuration).

### The DORA Process (4-Step Handshake)

| Step         | Who Sends            | Message                           | Meaning                              |
| ------------ | -------------------- | --------------------------------- | ------------------------------------ |
| **Discover** | Client → Network     | "Hey, is there a DHCP server?"    | Device is new, needs an IP           |
| **Offer**    | DHCP Server → Client | "Yes! Here, use 192.168.1.10"     | Server offers an available IP        |
| **Request**  | Client → DHCP Server | "Yes please, I'll take that IP!"  | Client confirms the offer            |
| **ACK**      | DHCP Server → Client | "Confirmed! Use it for 24 hours." | Server acknowledges — IP is assigned |

> 💡 **Key insight:** DHCP leases IPs for a time period. When the lease expires, the device must request a new one.

---

## 🧠 Quick Recall — Key Protocols

| Protocol | Full Name                           | Purpose                   |
| -------- | ----------------------------------- | ------------------------- |
| **ARP**  | Address Resolution Protocol         | Maps IP → MAC address     |
| **DHCP** | Dynamic Host Configuration Protocol | Auto-assigns IP addresses |

---

## 🔗 Connections to Cybersecurity

| Concept       | Attack Vector                            |
| ------------- | ---------------------------------------- |
| ARP           | ARP Spoofing / Poisoning (MITM attacks)  |
| DHCP          | Rogue DHCP server attacks                |
| Star topology | Central switch = high-value target       |
| Subnetting    | Improper subnets = lateral movement risk |

---

_Notes compiled from TryHackMe Networking Module_
