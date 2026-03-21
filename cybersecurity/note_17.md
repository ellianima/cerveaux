# ☁️ Cloud Computing Fundamentals

> **Source:** TryHackMe — Pre-Security / Cloud Computing Fundamentals Module
> **Purpose:** Cloud knowledge for cybersecurity, DevOps & remote work
> **Covers:** Evolution to cloud, benefits, deployment types, service
> models (IaaS/PaaS/SaaS), major vendors, AWS EC2, billing, regions

---

## 🧒 Feynman Explanation — What Is the Cloud?

Before the cloud, if you wanted a server, you had to:

- Buy physical hardware (expensive)
- Set it up in your building (slow)
- Maintain it forever (costly)
- If you needed more power — buy MORE hardware

The cloud says: **"Stop buying hardware. Just rent ours."**

It's like electricity. You don't build your own power plant to
light your home. You plug in and pay for what you use.
The cloud is the power plant for computing.

```
Old way: Buy a generator, maintain it, hope it doesn't break
Cloud:   Plug in, pay per kWh, someone else handles everything
```

---

## 🔷 1. How Servers Evolved Into the Cloud

### The Timeline

```
1960s–Early 2000s     1999–2006           2003–2006
PHYSICAL SERVERS  →   VIRTUALIZATION  →   AUTOMATION &
    ERA                                   REMOTE MGMT
─────────────────     ──────────────      ─────────────
Physical servers      Multiple VMs        Servers managed
in company buildings  on one machine      over the internet
One server = one job  Better hardware     Early automation
Expensive, slow       utilization         Infrastructure
to scale              Faster              became flexible
                      provisioning


2006                  2012 – Today
CLOUD COMPUTING   →   MODERN CLOUD ERA
(AWS LAUNCH)
─────────────────     ──────────────────────────────
Rent virtual          AWS, Azure, Google Cloud
computers & storage   Containers everywhere
on demand             Focus on apps, not servers
No hardware ownership Global-scale platforms
Elastic scaling       Serverless, AI services
in minutes
```

> 💡 **Key insight:** AWS launched in 2006 and changed
> everything. Before AWS, if you wanted a server, you waited
> weeks and spent thousands. With AWS, you get a server in
> 90 seconds and pay $0.01/hour. This is why every startup
> now runs on the cloud — it removed the upfront cost
> barrier entirely.

---

## 🔷 2. Cloud Benefits & Characteristics

### The Six Core Benefits

| Benefit                       | What It Means                                      | Real Example                                                |
| ----------------------------- | -------------------------------------------------- | ----------------------------------------------------------- |
| **Scalability**               | Scale up or down instantly as needs change         | Netflix adding 1,000 servers for a new show release         |
| **On-demand self-service**    | Create servers and storage instantly, no waiting   | Spin up EC2 instance in 90 seconds                          |
| **Pay only for what you use** | Charged on usage, not upfront costs                | Stop a VM = stop paying immediately                         |
| **Security**                  | Cloud providers protect physical infrastructure    | AWS has more security than most companies' own datacenters  |
| **High availability**         | Apps keep running even if part of the system fails | Multiple regions ensure uptime even if one datacenter burns |
| **Global access**             | App accessible by users anywhere in the world      | Users in Manila and London both get fast response           |

---

## 🔷 3. Types of Cloud — Deployment Models

### 🧒 Feynman Explanation

Think of cloud deployment types like places you can work:

- **Public Cloud** = working in a coworking space (shared, affordable)
- **Private Cloud** = working in your company's private office (secure, yours only)
- **Hybrid Cloud** = working from home sometimes, office sometimes

### Deployment Types Compared

| Type              | Who Uses It                   | Why                                                       | Examples                  |
| ----------------- | ----------------------------- | --------------------------------------------------------- | ------------------------- |
| **Public Cloud**  | Startups, websites, apps      | Affordable, easy to scale, no infrastructure mgmt         | AWS, Azure, GCP           |
| **Private Cloud** | Banks, healthcare, government | Control, customization, compliance for sensitive data     | On-prem VMware, OpenStack |
| **Hybrid Cloud**  | E-commerce, enterprise        | Keep sensitive data private, scale publicly during spikes | AWS + on-prem data center |

```
Example — E-commerce on Black Friday:
  Normal days:  run on private cloud (sensitive payment data secure)
  Black Friday: public cloud auto-scales for 10x traffic spike
  → Hybrid cloud = best of both worlds
```

---

## 🔷 4. Cloud Service Models — IaaS, PaaS, SaaS

### 🧒 Feynman Explanation — The Apartment Analogy

| Service Model | Analogy                  | What YOU manage         | What THEY manage        |
| ------------- | ------------------------ | ----------------------- | ----------------------- |
| **IaaS**      | Empty apartment          | OS, apps, data, runtime | Physical hardware only  |
| **PaaS**      | Semi-furnished apartment | Apps and data only      | Hardware + OS + runtime |
| **SaaS**      | Hotel room               | Nothing — just use it   | Everything              |

```
IaaS — Empty Apartment:
  "Here's a server. Install your own OS, configure it,
   deploy your app. We just provide the hardware."
  → You choose the furniture, install appliances, handle maintenance
  → Examples: AWS EC2, Azure VMs, Google Compute Engine

PaaS — Semi-Furnished Apartment:
  "OS is already installed. Just upload your code and it runs."
  → The basics are set up — just focus on building
  → Examples: Heroku, Google App Engine, AWS Elastic Beanstalk

SaaS — Hotel Room:
  "Just open the browser and use the app. Everything is handled."
  → Everything ready to use — cleaning, maintenance, services included
  → Examples: Gmail, Zoom, Slack, Microsoft 365, Salesforce
```

### Responsibility Breakdown

```
                    IaaS    PaaS    SaaS
Applications         YOU     YOU    THEM
Data                 YOU     YOU    THEM
Runtime              YOU    THEM    THEM
Middleware           YOU    THEM    THEM
OS                   YOU    THEM    THEM
Virtualization      THEM    THEM    THEM
Servers             THEM    THEM    THEM
Storage             THEM    THEM    THEM
Networking          THEM    THEM    THEM
```

> ⚠️ **Security note:** In IaaS, YOU are responsible for
> securing the OS, patching it, configuring firewalls,
> and locking down the application. Cloud providers use
> the "Shared Responsibility Model" — they secure the
> infrastructure, you secure what's on top of it.
> Misconfigured IaaS (open S3 buckets, unpatched EC2s)
> is one of the most common causes of cloud data breaches.

---

## 🔷 5. Major Cloud Vendors

| Vendor                 | Strengths                             | Market Position            |
| ---------------------- | ------------------------------------- | -------------------------- |
| **AWS (Amazon)**       | Largest service catalog, global reach | #1 market leader           |
| **Microsoft Azure**    | Enterprise integration, hybrid cloud  | #2, dominant in enterprise |
| **Google Cloud (GCP)** | Data analytics, AI/ML tools           | #3, strong in data         |
| **Alibaba Cloud**      | Asia-Pacific dominance                | #4 globally                |
| **IBM Cloud**          | Hybrid cloud, AI (Watson)             | Enterprise/government      |
| **Oracle Cloud**       | Enterprise databases, ERP             | Database-heavy enterprise  |

### How Major Companies Use the Cloud

```
Netflix    → AWS entire platform, global CDN for streaming
Spotify    → Google Cloud, scales when new music drops
Instagram  → AWS for storing billions of photos/videos
Amazon     → AWS (their own!) for Black Friday traffic spikes

The pattern: focus on the PRODUCT, not the HARDWARE.
Cloud lets companies hire engineers to build features —
not to manage servers in a basement.
```

---

## 🔷 6. AWS Core Concepts — EC2 & Regions

### Key AWS Terminology

| Term                  | Simple Definition                                        |
| --------------------- | -------------------------------------------------------- |
| **EC2**               | Elastic Compute Cloud — a virtual computer/server in AWS |
| **Instance**          | A single EC2 virtual machine that is running             |
| **Instance Type**     | The size/power of the VM (CPU, RAM, storage)             |
| **Region**            | A geographical location where AWS has data centers       |
| **Availability Zone** | A specific data center within a region                   |
| **AMI**               | Amazon Machine Image — template to launch instances      |

### Instance Types — Choose Your Power Level

```
t3.micro    → 2 vCPU, 1GB RAM    → ~$0.01/hr   (dev, testing)
t3.small    → 2 vCPU, 2GB RAM    → ~$0.02/hr   (small apps)
t3.medium   → 2 vCPU, 4GB RAM    → ~$0.04/hr   (medium apps)
m5.large    → 2 vCPU, 8GB RAM    → ~$0.10/hr   (production)
m5.xlarge   → 4 vCPU, 16GB RAM   → ~$0.19/hr   (heavy apps)
c5.2xlarge  → 8 vCPU, 16GB RAM   → ~$0.34/hr   (compute-heavy)
r5.4xlarge  → 16 vCPU, 128GB RAM → ~$1.00/hr   (memory-heavy)

Rule: bigger instance = more power = higher cost per hour
      stopped instance = $0.00/hour (no compute charge)
```

### Regions and Why They Matter

```
AWS Regions (examples):
  us-east-1    → Northern Virginia, USA (largest, most services)
  ap-southeast-1 → Singapore (closest to Philippines!)
  eu-west-1    → Ireland, Europe
  ap-east-1    → Hong Kong

WHY REGIONS MATTER:
  1. Latency    → Closer region = faster response for users
  2. Compliance → Some data must stay in specific countries
  3. Cost       → Pricing varies by region
  4. Disaster   → Multi-region = survive if one datacenter fails

FOR PHILIPPINE USERS:
  Use ap-southeast-1 (Singapore) for lowest latency
  ~20ms vs ~200ms+ for us-east-1
```

---

## 🔷 7. Cloud Billing — Pay Only for What You Use

### How Cloud Billing Works

```
Running instance   → pays per hour (or per second on AWS)
Stopped instance   → NO compute charge (only storage charge)
Deleted instance   → NO charge at all

This is the "pay for what you use" model:
  Running: t3.micro at $0.01/hr = $7.20/month
  Stopped: $0.00/hr compute + small storage fee
  On/Off:  Only pay when it's actually running
```

### Billing Example From the Screenshots

```
SCENARIO: Cybersecurity training environment

5 VMs running:
  web-1              t3.micro  running  10.0 credits/mo
  db-1               t3.micro  running  10.0 credits/mo
  application-interface t3.micro running 10.0 credits/mo
  study-machine-1    m5.large  running  70.0 credits/mo
  study-machine-2    m5.large  running  70.0 credits/mo
                              TOTAL: 170.0 credits/month

COST OPTIMIZATION:
  Stop study-machine-1 and study-machine-2 (not needed yet)

  After stopping:
  study-machine-1    m5.large  stopped   0.0 credits/mo
  study-machine-2    m5.large  stopped   0.0 credits/mo
                              TOTAL: 30.0 credits/month

SAVINGS: 140 credits/month (82% cost reduction!)
→ This is the cloud advantage: turn off what you don't use
```

### 💻 AWS CLI — Managing EC2 From Terminal

```bash
# Install AWS CLI
pip install awscli --break-system-packages
aws configure  # enter your Access Key, Secret, region

# List all EC2 instances
aws ec2 describe-instances --output table

# Start an instance
aws ec2 start-instances --instance-ids i-1234567890abcdef0

# Stop an instance
aws ec2 stop-instances --instance-ids i-1234567890abcdef0

# Create a new EC2 instance (t3.micro, Amazon Linux)
aws ec2 run-instances \
  --image-id ami-0c02fb55956c7d316 \
  --instance-type t3.micro \
  --key-name my-key-pair \
  --security-group-ids sg-12345678

# Terminate (delete) an instance
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0

# Check instance status
aws ec2 describe-instance-status --instance-ids i-1234567890abcdef0

# Get public IP of running instance
aws ec2 describe-instances \
  --query 'Reservations[].Instances[].PublicIpAddress' \
  --output text
```

### Python — Automate Cloud with Boto3 (AWS SDK)

```python
import boto3

# Connect to AWS EC2
ec2 = boto3.client('ec2', region_name='ap-southeast-1')

# List all instances
response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"ID: {instance['InstanceId']}")
        print(f"Type: {instance['InstanceType']}")
        print(f"State: {instance['State']['Name']}")
        print(f"IP: {instance.get('PublicIpAddress', 'None')}")
        print("---")

# Start an instance
ec2.start_instances(InstanceIds=['i-1234567890abcdef0'])
print("Instance started!")

# Stop an instance
ec2.stop_instances(InstanceIds=['i-1234567890abcdef0'])
print("Instance stopped! No more charges.")

# Create a new instance
new_instance = ec2.run_instances(
    ImageId='ami-0c02fb55956c7d316',
    InstanceType='t3.micro',
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[{
        'ResourceType': 'instance',
        'Tags': [{'Key': 'Name', 'Value': 'my-security-lab'}]
    }]
)
print("New instance ID:", new_instance['Instances'][0]['InstanceId'])
```

---

## 🔷 8. Key Terminology — Quick Reference

| Term              | Definition                                               |
| ----------------- | -------------------------------------------------------- |
| **Public Cloud**  | Cloud services many people/companies share over internet |
| **Private Cloud** | Cloud built for one company — more control and security  |
| **Hybrid Cloud**  | Mix of public and private clouds working together        |
| **IaaS**          | Rent basic compute (servers, storage) — you manage OS up |
| **PaaS**          | Ready-to-use environment — just deploy your code         |
| **SaaS**          | Use complete software over internet — manage nothing     |
| **EC2**           | AWS virtual computers you create, use, resize, delete    |
| **Region**        | Geographical AWS location (Singapore, N. Virginia, etc.) |
| **Instance Type** | Size/power specification of a VM (t3.micro, m5.large)    |
| **Billing**       | Pay only for running instances — stopped = no charge     |

---

## 🔗 Cloud Security Attack Map

| Target               | Attack               | Technique                                |
| -------------------- | -------------------- | ---------------------------------------- |
| **S3 Buckets**       | Public data exposure | Misconfigured ACLs, bucket enumeration   |
| **EC2 Metadata**     | Credential theft     | SSRF → `169.254.169.254` → IAM keys      |
| **IAM Roles**        | Privilege escalation | Overly permissive policies               |
| **Security Groups**  | Unauthorized access  | 0.0.0.0/0 on SSH/RDP ports               |
| **Snapshots**        | Data theft           | Public EBS snapshots with sensitive data |
| **Lambda Functions** | Code injection       | Unvalidated input, dependency confusion  |
| **CloudTrail**       | Cover tracks         | Disable logging before attack            |

---

## ⚡ Enriched Insights (Beyond the Source Material)

### The Shared Responsibility Model — Critical for Security

```
AWS is responsible for:           YOU are responsible for:
  Physical data centers             Your data
  Physical hardware                 Your OS patches
  Network infrastructure            Your application security
  Hypervisor layer                  IAM user access control
  Core managed services             Security group configuration
                                    Encryption of data at rest

The most common cloud breaches happen because customers
misconfigure THEIR side of the responsibility:
  → Open S3 buckets (data visible to the whole internet)
  → Weak IAM policies (any user can do anything)
  → Security groups allowing 0.0.0.0/0 on all ports
  → Unpatched OS on EC2 instances
  → EC2 metadata SSRF (stealing IAM credentials via web vuln)
```

### Cloud Security Tools to Know

```bash
# Scout Suite — multi-cloud security audit
pip install scoutsuite
scout aws --profile default

# Prowler — AWS security best practices checker
pip install prowler
prowler aws

# CloudMapper — visualize AWS environment
# pacu — AWS exploitation framework (for pentesting)
# Enumerate cloud resources from a compromised key:
aws sts get-caller-identity  # who am I?
aws iam list-users           # who else exists?
aws s3 ls                    # what buckets exist?
aws ec2 describe-instances   # what VMs are running?
```

### Why Cloud Matters for Your Career

```
SOC Analyst:
  → Most companies now run on cloud
  → Cloud logs (CloudTrail, VPC Flow Logs) = your SIEM data
  → Alert: "EC2 instance querying metadata service repeatedly"
    = possible SSRF attack stealing IAM credentials

Pentester:
  → Cloud pentesting = growing specialization (high pay)
  → AWS Certified Security Specialty = career differentiator
  → Bug bounties increasingly involve cloud misconfigurations

Certifications worth pursuing:
  AWS Cloud Practitioner  → foundation (free prep, ~$100 exam)
  AWS Solutions Architect → architecture understanding
  AWS Security Specialty  → cloud security specialization
```

---

_Notes compiled from TryHackMe — Cloud Computing Fundamentals Module_
_Enriched with AWS CLI, Python Boto3, security context, and career relevance_
