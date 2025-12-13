# What is an Internet Gateway (IGW)?

## Short definition

An **Internet Gateway (IGW)** is a VPC component that **enables communication between a VPC and the public internet**.

Without an Internet Gateway, resources inside a VPC **cannot send or receive traffic from the internet**, even if they have a public IP.

---

## Why do we need an Internet Gateway?

Launching an EC2 instance with:
- A public IP
- Open Security Group rules

is **not enough**.

The VPC itself needs a **path to the internet**, and that path is provided by the **Internet Gateway**.

---

## What an Internet Gateway actually does

An Internet Gateway:
- Is **attached to a VPC** (1 IGW per VPC)
- Allows **inbound and outbound** internet traffic
- Works together with **Route Tables**
- Supports **IPv4 and IPv6**

It performs two key functions:
1. **Routes traffic** between the VPC and the internet
2. **Performs NAT** for instances with public IPv4 addresses

---

## How internet access works (must know)

For an EC2 instance to be accessible from the internet, **all conditions must be true**:

1. Internet Gateway is attached to the VPC
2. Subnet Route Table contains:
0.0.0.0/0 → Internet Gateway

yaml
Copy code
3. EC2 instance has a **Public IP or Elastic IP**
4. Security Group allows inbound traffic
5. NACL allows the traffic

Missing any one of these → **no internet access**

---

## Public Subnet definition

A subnet is called **public** only if:
- Its Route Table routes `0.0.0.0/0` to an Internet Gateway

Without this route, the subnet is **private**, regardless of public IPs.

---

## Simple real-life analogy

Think of a **building**:

- Building = VPC  
- Flats = Subnets  
- Residents = EC2 instances  
- Main gate = Internet Gateway  

Without the main gate, no one can enter or leave the building.

---

## Internet Gateway vs NAT Gateway

| Feature | Internet Gateway | NAT Gateway |
|------|------------------|-------------|
| Traffic direction | Inbound + Outbound | Outbound only |
| Used by | Public subnets | Private subnets |
| Public IP on EC2 | Required | Not required |
| Security | Less restrictive | More restrictive |

---

## Key exam & interview points

- One Internet Gateway per VPC
- One VPC per Internet Gateway
- Required for public internet access
- Works only through Route Tables
- Stateless at the VPC edge

---

## One-line explanation (interview-ready)

> An Internet Gateway allows resources in a VPC to communicate with the public internet and is required to make a subnet public.

---
