# What is a Route Table?

## Short definition

A **Route Table** defines **where network traffic from a subnet is directed**.  
It contains routing rules that decide the **next hop** for traffic based on the destination IP address.

---

## Why do we need a Route Table?

Every time an EC2 instance sends traffic, AWS must decide:

- Should this traffic stay inside the VPC?
- Should it go to the internet?
- Should it go via a NAT Gateway?
- Should it go to on-prem via VPN or Direct Connect?

The **Route Table answers this question**.

---

## What a Route Table actually does

A Route Table:
- Is a **collection of routing rules**
- Is **associated with subnets**
- Uses **Destination CIDR → Target** mapping
- Controls traffic flow **out of a subnet**

Each rule follows this logic:

If destination IP matches this CIDR
→ forward traffic to this target


---

## Common Route Table entries

| Destination | Target | Purpose |
|------------|--------|---------|
| 10.0.0.0/16 | local | Internal VPC traffic |
| 0.0.0.0/0 | Internet Gateway | Public internet access |
| 0.0.0.0/0 | NAT Gateway | Outbound-only internet |
| 192.168.0.0/16 | Virtual Private Gateway | On-prem network |

> The `local` route is automatically created and **cannot be removed**.

---

# Destination and Target (Route Table)

## What does Destination → Target mean?

In a Route Table, each rule answers one question:

> **If traffic is going to this destination, where should it be sent next?**

---

## Destination

**Destination** defines **where the traffic wants to go**.  
It is always written as a **CIDR block**.

### Common Destination examples
- `10.0.0.0/16` → Traffic within the same VPC
- `0.0.0.0/0` → Traffic going anywhere (internet)
- `192.168.0.0/16` → On-premises network

Think of Destination as the **address range**.

---

## Target

**Target** defines **how or where the traffic should be forwarded**.

### Common Target examples
- `local` → Stay inside the VPC
- `Internet Gateway (igw-xxxx)` → Route to the internet
- `NAT Gateway (nat-xxxx)` → Outbound internet from private subnet
- `Virtual Private Gateway (vgw-xxxx)` → On-premises network
- `VPC Peering Connection` → Another VPC

Think of Target as the **next hop or exit path**.

---

## How AWS processes Destination → Target

1. EC2 sends a network request
2. AWS checks the subnet’s Route Table
3. Matches the **Destination CIDR**
4. Selects the **most specific route** (longest prefix match)
5. Forwards traffic to the **Target**

If no route matches, traffic is dropped.

---

## Common Destination → Target examples

| Destination | Target | Explanation |
|------------|--------|------------|
| `10.0.0.0/16` | local | Internal VPC traffic |
| `0.0.0.0/0` | Internet Gateway | Public internet access |
| `0.0.0.0/0` | NAT Gateway | Private subnet internet access |
| `192.168.1.0/24` | Virtual Private Gateway | On-prem routing |

---

## Simple real-life analogy

- **Destination** = City you want to reach  
- **Target** = Highway or road to reach it  

> “If destination is Pune → take Express Highway”

---

## One-line explanation (interview-ready)

> Destination defines where the traffic is going, and Target defines the next hop used to reach it.

---



## Public vs Private Subnet (decided by Route Table)

A subnet is **not public or private by default**.

It becomes:

### Public Subnet
- Route Table contains:


0.0.0.0/0 → Internet Gateway


### Private Subnet
- Route Table contains:


0.0.0.0/0 → NAT Gateway

or no internet route at all.

**Route Tables define subnet behavior.**

---

## Simple real-life analogy

Think of a **GPS system** for network traffic:

- Destination IP = Address
- Route Table = Navigation rules
- Target = Next turn (IGW, NAT, VPN)

Without a Route Table, traffic has **no direction**.

---

## Route Table vs NACL vs Security Group

| Component | Role |
|---------|------|
| Route Table | **Where traffic goes** |
| NACL | Whether traffic is allowed at subnet level |
| Security Group | Whether traffic is allowed at instance level |

They solve **different problems**.

---

## Key exam & interview points

- Route Tables work at **subnet level**
- One subnet → **one Route Table**
- One Route Table → **multiple subnets**
- Uses **longest prefix match**
- Route Tables do **not allow or deny traffic**; they only route it

---

## One-line explanation (interview-ready)

> A Route Table determines how network traffic is forwarded from a subnet based on destination IP rules.

---
