# AWS VPC Peering & Transit Gateway – Key Lecture Points

---

## 1. VPC Peering

<img width="747" height="517" alt="image" src="https://github.com/user-attachments/assets/c25a9863-44b9-4630-abd7-4c09a782261d" />



### What is VPC Peering?
VPC Peering is a **one-to-one networking connection** between two VPCs that enables traffic to flow **privately using AWS backbone infrastructure**.

---

### Supported Scenarios
- Same AWS account
- Cross-account
- Cross-region

---

### Mandatory Technical Requirements
- **CIDR blocks must NOT overlap**
- Explicit **route table entries are required on both sides**
- Security Groups and NACLs are **still enforced**
- Peering connection must be **accepted** by the peer VPC

---

### Critical Limitations (Very Important)
- ❌ **No transitive routing**
  - VPC-A ↔ VPC-B
  - VPC-B ↔ VPC-C
  - VPC-A ❌ cannot reach VPC-C
- ❌ No centralized routing control
- ❌ No route propagation
- ❌ No hub-and-spoke architecture

---

### Traffic Characteristics
- Traffic stays on **AWS private network**
- No Internet Gateway, NAT Gateway, or VPN required
- No bandwidth bottleneck imposed by AWS

---

### Cost Model
- No hourly cost
- Data transfer charges apply
- Cross-region peering has **higher data transfer cost**

---

### When to Use VPC Peering
- Small environments
- Simple VPC-to-VPC communication
- Limited number of connections
- No need for centralized networking or security

---

## 2. AWS Transit Gateway (TGW)

<img width="833" height="458" alt="image" src="https://github.com/user-attachments/assets/4f5ece93-a5dd-4555-9057-da1c36cd1a33" />

<img width="1030" height="752" alt="image" src="https://github.com/user-attachments/assets/2c40d927-0830-47f4-a626-c22f105e8f83" />

<img width="815" height="437" alt="image" src="https://github.com/user-attachments/assets/ff46b61a-b7bb-4f6b-bf71-f088adba8142" />



### What is Transit Gateway?
AWS Transit Gateway is a **regional, highly scalable network hub** that enables **transitive routing** between connected networks.

---

### Core Architecture
- Hub-and-spoke model
- One TGW connects:
  - Multiple VPCs
  - On-premises networks
  - VPN connections
  - Direct Connect gateways

---

### Key Capabilities
- ✅ **Transitive routing supported**
- ✅ Centralized route management
- ✅ Scales to thousands of VPC attachments
- ✅ Supports hybrid cloud architectures

---

### Routing Mechanics
- TGW uses **route table association and propagation**
- Multiple TGW route tables supported:
  - Production
  - Non-production
  - Shared services
  - Inspection / firewall

---

### Security & Control
- Enables centralized **inspection VPC**
- Better blast-radius isolation
- Easier compliance enforcement
- Works with third-party firewalls

---

### Cost Model (Be Clear in Lecture)
- Hourly cost per attachment
- Per-GB data processing charge
- More expensive than VPC Peering
- Cost justified for scale and control

---

### When to Use Transit Gateway
- Medium to large AWS environments
- Multi-account AWS organizations
- Hybrid cloud (AWS + on-prem)
- Centralized security and routing required

---

## 3. VPC Peering vs Transit Gateway (Exam & Interview Ready)

| Feature | VPC Peering | Transit Gateway |
|------|-----------|----------------|
| Connection Type | Point-to-Point | Hub-and-Spoke |
| Transitive Routing | ❌ No | ✅ Yes |
| Scalability | Poor | Excellent |
| Route Management | Manual | Centralized |
| Security Centralization | ❌ No | ✅ Yes |
| Cost | Low | Higher |
| Enterprise Ready | ❌ No | ✅ Yes |

---

## 4. One-Line Teaching Summary

> **VPC Peering is for simple, direct communication.  
Transit Gateway is for scalable, enterprise networking.**

---

## 5. Common Mistakes to Highlight to Students
- Assuming VPC Peering supports transitive routing
- Forgetting route table updates
- Overusing VPC Peering in large environments
- Ignoring TGW costs without understanding value

---

## 6. Exam Tip
If the question mentions:
- **Scale**
- **Transitive routing**
- **Centralized networking**
→ Answer is **Transit Gateway**

If the question mentions:
- **Simple connectivity**
- **Few VPCs**
→ Answer is **VPC Peering**

# AWS Transit Gateway – Regional vs Cross-Region Connectivity

## Direct Answer

**AWS Transit Gateway (TGW) is a regional service.**

- A Transit Gateway is created **inside a single AWS Region**
- It can attach **only to resources within the same region**
- A single Transit Gateway **cannot directly connect VPCs across regions**

---

## Why Transit Gateway Is Regional

AWS Regions are designed to be **failure-isolated units**.

Keeping Transit Gateway regional provides:
- Low and predictable latency
- Strong fault isolation
- Independent scaling per region
- Clear operational and cost boundaries

A global Transit Gateway would break AWS’s regional isolation model.

---

## What Does NOT Work (Common Misconception)

❌ You **cannot** do this:


VPC (Mumbai) ───► Transit Gateway (Singapore)


Direct cross-region attachment is **not supported**.

---

## How Cross-Region Connectivity Actually Works

AWS supports **Inter-Region Transit Gateway Peering**.

This requires:
- One Transit Gateway **per region**
- A peering connection **between the two Transit Gateways**

---

## Inter-Region Transit Gateway Peering (Correct Design)

VPC (Region A)

│

▼

Transit Gateway A

│

▼ (AWS Global Backbone)

Transit Gateway B

│

▼

VPC (Region B)



### Key Points
- Each region has its **own Transit Gateway**
- Transit Gateways are **peered together**
- Traffic flows over AWS’s private backbone
- Communication is encrypted and managed by AWS

---

## What You Can and Cannot Do

### ✅ Supported
- Connect VPCs across regions using **TGW Peering**
- Build multi-region hub-and-spoke architectures
- Use AWS backbone instead of public internet
- Integrate on-premises networks across regions

### ❌ Not Supported
- Single global Transit Gateway
- Direct cross-region VPC attachment
- Avoiding multiple TGWs in multi-region setups

---

## Cost and Latency Considerations

- Inter-region data transfer **is chargeable**
- Latency depends on **physical distance between regions**
- TGW peering is still cleaner than:
  - Large VPC peering meshes
  - VPN chaining
  - Custom routing appliances

---

## When to Use What

| Scenario | Recommended Solution |
|--------|----------------------|
Single region, many VPCs | One Transit Gateway |
Multi-region architecture | TGW per region + TGW Peering |
Few VPCs, simple routing | VPC Peering |
Hybrid (On-prem + AWS) | TGW + Direct Connect |
Hybrid + Multi-Region | TGW per region + DX + TGW Peering |

---

## One-Line Summary

> **AWS Transit Gateway is regional.  
> Cross-region connectivity is achieved using Transit Gateway peering, not direct attachment.**

---

## Exam / Interview Ready Statement

> “AWS Transit Gateway is a regional service.  
> To connect VPCs across regions, AWS requires Transit Gateway peering between regional Transit Gateways.”

---

## End


---
