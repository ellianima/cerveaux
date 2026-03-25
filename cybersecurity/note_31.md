# 🔐 Security Fundamentals — CIA Triad, AAA & Non-Repudiation

> **Source:** Personal learning sessions — Security concepts deep dive
> **Purpose:** Foundation for Security+, eJPT, SOC Analyst roles
> **Covers:** Non-Repudiation, Authentication, Authorization,
> Accounting/Auditing, CIA + AAAA model, enterprise workflows

---

## 🧒 Feynman Explanation — Security as a Company Building

Imagine a high-security corporate office:

- **CIA** = the building's security GOALS
  - Confidentiality = only authorized people enter certain floors
  - Integrity = nobody tampers with the files inside
  - Availability = the building is always accessible to those who need it

- **AAAA** = the building's security MECHANISMS
  - Authentication = proving who you are at the door
  - Authorization = which floors/rooms you can enter
  - Accounting = the camera system recording everything
  - Non-Repudiation = the signed visitor log you can't deny signing

---

## 🔷 The Full Model — CIA + AAAA

```
CIA (What we protect)           AAAA (How we protect it)
─────────────────────           ────────────────────────
Confidentiality                 Authentication
  Only authorized users           Prove who you are
  can see the data

Integrity                       Authorization
  Data isn't tampered             Prove what you can do
  with or modified

Availability                    Accounting / Auditing
  Systems work when               Record what you did
  needed

                                Non-Repudiation
                                  Prove you can't deny it
```

### Enterprise Workflow — All 4 in Action

```
Alice approaches the system:

STEP 1 — Authentication
  Alice logs in with password + YubiKey (MFA)
  "Who are you?" → Identity VERIFIED

STEP 2 — Authorization
  Alice requests access to finance server
  IAM check: does her role allow this?
  Principle of Least Privilege enforced
  "What can you do?" → Permissions GRANTED

STEP 3 — Accounting
  System logs: Alice accessed finance server
  Timestamp, IP, action, resource recorded
  SIEM aggregates and monitors in real time
  "What did you do?" → Action RECORDED

STEP 4 — Non-Repudiation
  Log entry is hashed (SHA-256)
  Hash is signed with Alice's private key
  If Alice claims "I didn't do that" →
  Decrypt signature with public key →
  Hash matches log entry → GUILTY
  "Can you deny it?" → Absolutely NOT
```

---

## 🔷 1. Non-Repudiation — You Can't Deny It

### Definition

Cryptographic proof that an action occurred AND who performed it,
making it impossible for that person to deny it later.

### Technical Mechanisms

```
MECHANISM 1: Cryptographic Hashing
  Action/file → SHA-256 hash → unique fingerprint
  Even 1 character changed → completely different hash
  Proves the data wasn't tampered with (integrity!)

MECHANISM 2: Digital Signatures (Asymmetric Encryption)
  User has: Private Key (secret, only they have it)
             Public Key (shared with everyone)

  Signing process:
    Hash of action/file
         ↓
    Encrypted with PRIVATE KEY = Digital Signature
         ↓
    Anyone can decrypt with PUBLIC KEY
         ↓
    Decrypted hash matches original? → Valid signature
    Hash matches audit log? → Action confirmed!

MECHANISM 3: Audit Trail + PKI
  Actions timestamped + logged
  Logs themselves are hashed and signed
  Certificate Authority (CA) ties keys to real identities
```

### SOC-Level Workflow — Catching the Denier

```
SCENARIO: User claims "I didn't delete that file"

STEP 1: File deletion is a CRITICAL ACTION
  → Automatically logged by auditd/SIEM

STEP 2: Cryptographic hash generated
  → SHA-256 of the action = unique fingerprint

STEP 3: Log entry signed with user's private key
  → Digital signature created

STEP 4: Verification
  SOC analyst takes user's PUBLIC KEY
  Decrypts the digital signature
  Recovers the hash → matches the log entry
  RESULT: User's private key signed this → they did it

STEP 5: Conviction
  Hash matches log ✅
  Public key decrypted private key ✅
  Timestamp confirmed ✅
  → User CANNOT repudiate the action
```

### Tools & Protocols

| Tool/Protocol          | Purpose                               |
| ---------------------- | ------------------------------------- |
| **RSA / ECDSA**        | Digital signature algorithms          |
| **SHA-256 / SHA-512**  | Cryptographic hashing                 |
| **X.509 certificates** | PKI — ties public keys to identities  |
| **PGP/GPG**            | Email signing (can't deny sending!)   |
| **TLS/SSL**            | Server identity verification          |
| **Blockchain**         | Immutable transaction non-repudiation |
| **Splunk / ELK**       | Log aggregation with tamper detection |

---

## 🔷 2. Authentication — Prove Who You Are

### Definition

The process of verifying identity before granting access to a system.

### The 5 Authentication Factors

| Factor                 | What It Is       | Example                         | Weakness                                                |
| ---------------------- | ---------------- | ------------------------------- | ------------------------------------------------------- |
| **Something you KNOW** | Knowledge-based  | Password, PIN, secret question  | Social engineering, brute force                         |
| **Something you HAVE** | Possession-based | YubiKey, smart card, RSA token  | Can be lost or stolen                                   |
| **Something you ARE**  | Biometric        | Fingerprint, retina scan        | Requires physical access, hard to change if compromised |
| **Something you DO**   | Behavioral       | Typing patterns, mouse movement | Inconsistent, used as supplement                        |
| **Somewhere you ARE**  | Geolocation      | Login from Philippines only     | Bypassable with VPN (warrants investigation)            |

### Why MFA Is Mandatory in Enterprise

```
Single factor: Password stolen → attacker is IN
Two factors:   Password + YubiKey stolen → attacker still needs the physical device
Three factors: + Biometric → attacker needs the password, device, AND your fingerprint

Each additional factor:
  Covers a DIFFERENT attack vector
  Makes compromise exponentially harder
  Compensates for weaknesses of other factors

Example MFA for a nuclear facility:
  1. Password (something you know)
  2. Smart card (something you have)
  3. Retina scan (something you are)
  4. Location restriction (somewhere you are)
  → Compromising all 4 simultaneously = practically impossible
```

### Behavioral Authentication — Alert, Don't Lock Out

```
The smart approach:
  DON'T automatically lock out on unusual behavior
  DO silently alert the SOC team

Why? Behavioral patterns are INCONSISTENT
  (typing speed varies, mouse movement changes)

Alert-first workflow:
  Alice logs in normally from Manila → no alert
  Unknown user logs in from Moscow with Alice's password
    → Behavioral anomaly detected
    → SOC ALERT triggered
    → SOC investigates BEFORE locking
    → Prevents legitimate user disruption
    → Catches real attackers early

Real-world examples: AWS GuardDuty, Azure Sentinel,
Darktrace — all use behavioral analysis to ALERT, not block
```

### Authentication Protocols

| Protocol                    | Used For                          | Notes                                               |
| --------------------------- | --------------------------------- | --------------------------------------------------- |
| **Kerberos**                | Windows/Linux enterprise networks | Ticket-based, avoids sending passwords over network |
| **RADIUS**                  | Network device authentication     | Central auth for routers, switches, VPN             |
| **TACACS+**                 | Network device auth (Cisco focus) | More granular than RADIUS                           |
| **LDAP / Active Directory** | Enterprise identity management    | Centralized user database                           |
| **OAuth2 / OpenID Connect** | Web apps and APIs                 | "Login with Google" style                           |
| **SAML**                    | SSO (Single Sign-On)              | Enterprise web app federation                       |

---

## 🔷 3. Authorization — Prove What You Can Do

### Definition

Determines what actions an authenticated user is ALLOWED to perform.
Authentication = who you are. Authorization = what you can do.

### Access Control Models

```
RBAC — Role-Based Access Control
  Access based on ROLE in the organization
  Simple, scalable, most common in enterprise

  HR Staff      → can access HR files only
  Finance Manager → can approve payments
  IT Admin      → can modify system configs
  SOC Analyst   → can read logs, not modify them

─────────────────────────────────────────────────────

ABAC — Attribute-Based Access Control
  Access based on ATTRIBUTES:
    Who you are (user attributes)
    What you're accessing (resource attributes)
    Current environment (time, location, device)
    What action you're taking

  Example:
    Finance staff (who)
    + Accessing payroll file (what)
    + From corporate network (where)
    + During business hours (when)
    = ACCESS GRANTED

  Same user, from home, outside hours
    = ACCESS DENIED
  Much more fine-grained than RBAC

─────────────────────────────────────────────────────

DAC — Discretionary Access Control
  OWNER decides who can access their resource
  Owner is most powerful

  Example: Google Drive, GitHub repo, Canva
  You created it → you control sharing
  Weakness: Owner can accidentally over-share

─────────────────────────────────────────────────────

MAC — Mandatory Access Control
  SYSTEM enforces access — even owners can't override
  Based on classification levels

  Example: Government/military:
    Confidential → Secret → Top Secret
    Even if YOU created a Top Secret file,
    you can't share it with anyone below Top Secret clearance

  Why stricter than DAC:
    Prevents insider privilege abuse
    Owner can't "accidentally" give access
    System logic trumps individual decisions
```

### Principle of Least Privilege

```
Core Rule: Give ONLY the permissions needed for the task.
           Nothing more. Never.

Why it matters:
  If credentials are stolen → attacker only gets LIMITED access
  Limits lateral movement in a breach
  Reduces blast radius of insider threats
  #1 SOC alert source: misconfigured permissions

Examples:
  S3 bucket: user can READ but not DELETE
  Database: analyst can SELECT but not DROP TABLE
  Server: app runs as limited user, not root
  API: token can read data, not write or delete
```

### Authorization Tools

| Tool                              | Where Used                     |
| --------------------------------- | ------------------------------ |
| **Linux file permissions / ACLs** | File system access control     |
| **Windows NTFS permissions**      | Windows file system            |
| **AWS IAM policies**              | Cloud resource permissions     |
| **Azure RBAC**                    | Microsoft cloud access control |
| **Network ACLs**                  | Firewall/router traffic rules  |
| **SQL GRANT/REVOKE**              | Database access control        |

---

## 🔷 4. Accounting / Auditing — Record Everything

### Definition

Recording what users and systems did, when, where, and sometimes why.
The evidence room of security — enables traceability and forensics.

### Three Pillars

```
PILLAR 1: LOGGING (Passive Recording)
  Capture critical events automatically:
    Login / logout
    Password changes
    Privilege escalations
    File access and modifications
    Network connections
    Configuration changes
    Failed authentication attempts

  Tools:
    Linux: auditd, syslog, /var/log/auth.log
    Windows: Event Viewer, Windows Event IDs
    Network: Firewall logs, IDS/IPS logs

─────────────────────────────────────────────────────

PILLAR 2: MONITORING (Active Real-Time Analysis)
  Logs are aggregated → analyzed → anomalies flagged

  SIEM (Security Information and Event Management):
    Collects logs from ALL sources
    Correlates events across systems
    Detects suspicious patterns automatically
    Provides dashboard and real-time alerts
    Enables SOC investigation workflow

  Tools: Splunk, ELK Stack, IBM QRadar, Graylog

─────────────────────────────────────────────────────

PILLAR 3: REPORTING / COMPLIANCE (Accountability)
  Generates audits for legal/regulatory purposes

  Standards:
    HIPAA    → healthcare data protection
    PCI-DSS  → payment card data security
    ISO 27001 → information security management
    GDPR     → European data privacy

  Purpose: Prove to regulators what happened,
           when, who did it, and how it was handled
```

### Logging vs Monitoring — Key Distinction

```
LOGGING:
  Passive — records events as they happen
  Raw data — timestamps, IPs, actions, users
  Stored for later review
  "Writing in the diary"

MONITORING:
  Active — analyzes logs in real time
  Turns raw data into actionable intelligence
  Triggers alerts for SOC response
  "Reading the diary AND flagging suspicious entries"

Together: Logging provides the data.
          Monitoring provides the intelligence.
```

### How Accounting Connects to Non-Repudiation

```
Log entries contain:
  Timestamp ← when it happened
  User ID   ← who did it
  Action    ← what they did
  Resource  ← what was affected

Log entries are enhanced with:
  SHA-256 hash of the entry ← proves it wasn't tampered
  Digital signature          ← proves who performed the action

Result:
  User cannot deny the action (non-repudiation)
  Log cannot be silently modified (integrity)
  Chain of evidence preserved (forensics)
```

---

## 🔷 SOC Exam Scenarios — Quick Reference

```
SCENARIO 1:
"An employee accessed sensitive financial data.
Logs show timestamps, hashes, and digital signatures.
What principle is being enforced?"
→ ACCOUNTING + NON-REPUDIATION

SCENARIO 2:
"Alice logs in successfully, but cannot access the HR folder.
What security principle is being enforced?"
→ AUTHORIZATION / PRINCIPLE OF LEAST PRIVILEGE

SCENARIO 3:
"A login attempt from Russia is detected on a Philippines
government account. What should happen?"
→ BEHAVIORAL ALERT triggered → SOC investigates
→ GEOLOCATION-BASED authentication anomaly

SCENARIO 4:
"A user claims they didn't delete a critical file.
How do you prove otherwise?"
→ Check LOGS (accounting)
→ Verify HASH matches (integrity)
→ Decrypt DIGITAL SIGNATURE with public key (non-repudiation)
→ Public key unlocks private key → GUILTY

SCENARIO 5:
"A web app developer can read the database but not delete records.
What model is being used?"
→ AUTHORIZATION — Principle of Least Privilege
→ RBAC (role defines permissions)
```

---

## 🔷 Key Terminology — Quick Reference

| Term                  | Definition                                             |
| --------------------- | ------------------------------------------------------ |
| **Non-Repudiation**   | Cryptographic proof you can't deny an action           |
| **Digital Signature** | Hash encrypted with private key — proves identity      |
| **PKI**               | Infrastructure linking public keys to real identities  |
| **Authentication**    | Proving WHO you are                                    |
| **MFA**               | Multi-Factor Authentication — multiple identity proofs |
| **Authorization**     | Proving WHAT you can do                                |
| **RBAC**              | Role-Based Access Control                              |
| **ABAC**              | Attribute-Based Access Control                         |
| **MAC**               | Mandatory Access Control — system enforces, not owner  |
| **DAC**               | Discretionary Access Control — owner decides           |
| **Least Privilege**   | Only the minimum permissions needed — nothing more     |
| **Accounting**        | Recording what users/systems did                       |
| **SIEM**              | Security Information and Event Management              |
| **Logging**           | Passive recording of critical events                   |
| **Monitoring**        | Active real-time analysis of logs                      |
| **Audit Trail**       | Signed, timestamped record for forensics/compliance    |

---
