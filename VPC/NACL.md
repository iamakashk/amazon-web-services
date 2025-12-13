# What is a NACL (Network Access Control List)?

## Short definition

A **NACL (Network Access Control List)** is a **subnet-level firewall** in AWS that controls **inbound and outbound traffic** for all resources inside a subnet.

---

## Why do we need a NACL?

In AWS networking, security is applied in **layers**:

- **Security Group** → Instance-level security  
- **NACL** → Subnet-level security  

NACL is used when you want to:
- Control traffic at the **subnet boundary**
- Block or allow traffic **before it reaches EC2**
- Apply **coarse-grained** network rules

---

## What a NACL actually does

A Network Access Control List:
- Is **attached to a subnet**
- Applies to **all resources** in that subnet
- Controls **both inbound and outbound** traffic
- Uses **numbered rules** (processed in ascending order)
- First matching rule is applied

If no rule matches → **traffic is denied**

---

## Important property (very common mistake)

### NACLs are STATELESS

This means:
- If you allow **inbound** traffic,
- You must also allow **outbound** response traffic explicitly

If you forget this, applications will not work.

---

## Simple real-life analogy

Think of a **society gate**:

- Society = Subnet  
- Watchman at the gate = NACL  
- Individual flat locks = Security Groups  

The watchman checks everyone entering or leaving the society,  
before they reach individual flats.

---

## NACL vs Security Group

| Feature | NACL | Security Group |
|------|------|----------------|
| Level | **Subnet** | Instance |
| Stateful | ❌ No | ✅ Yes |
| Rules | Allow and Deny | Allow only |
| Rule order | Evaluated by rule number | All rules evaluated |
| Default action | Deny if no match | Deny if no allow |

---

## Default vs Custom NACL

### Default NACL
- Allows **all inbound traffic**
- Allows **all outbound traffic**

### Custom NACL
- Denies **all traffic by default**
- You must explicitly add allow rules

---

## When should you use NACL?

Use NACL when:
- You want an **extra layer of security**
- You need to **block specific IP ranges**
- You want subnet-wide traffic control

Do NOT use NACL for:
- Application-level security
- Instance-specific access rules (use Security Groups)

---

## One-line explanation (interview-ready)

> A NACL is a stateless, subnet-level firewall that controls inbound and outbound traffic using ordered allow and deny rules.

---
