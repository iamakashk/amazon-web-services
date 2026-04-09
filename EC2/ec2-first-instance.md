# AWS EC2 – Create Your First Virtual Server

## 🎯 Objective
In this lab, you will learn how to create your first EC2 (Elastic Compute Cloud) instance in AWS.

After completing this exercise you should be able to:

- Launch an EC2 instance
- Select instance type
- Configure security groups
- Connect to EC2 using SSH
- Understand basic EC2 components

---

## 📌 Prerequisites

Before starting, ensure you have:

- AWS Account
- Internet connection
- Basic Linux knowledge (optional)

Create AWS free account:
https://aws.amazon.com/free/

---

## 📖 What is EC2?

EC2 is a virtual server in AWS cloud.

Instead of buying a physical server, AWS allows you to rent servers.

Example:

Your laptop → Physical machine  
EC2 → Cloud machine

---

## 🏗 EC2 Architecture Components

When creating EC2 you will configure:

- AMI (Operating System)
- Instance Type (CPU/RAM)
- Key Pair (Login access)
- Security Group (Firewall)
- Storage (Disk)

---

## 🚀 Steps to Create EC2 Instance

---

## Step 1: Login to AWS Console

Go to:

https://console.aws.amazon.com

Search:

EC2

Click:

EC2 Dashboard

<img width="2764" height="1466" alt="image" src="https://github.com/user-attachments/assets/b0c29376-751a-487a-a06d-ca298a3ba38a" />

---

## Step 2: Click Launch Instance

Click:

Launch Instance button

<img width="2782" height="1462" alt="image" src="https://github.com/user-attachments/assets/2a3c5b7a-c78b-498d-bdb2-ae865f1bf811" />

<img width="1796" height="925" alt="image" src="https://github.com/user-attachments/assets/160d184d-2fcd-4566-89ee-5815e385069c" />



---

## Step 3: Configure Basic Details

Enter:

Name:


---

## Step 4: Select Operating System (AMI)

Select:

Amazon Linux

OR

Ubuntu

Explanation:

AMI = Operating system template.
NOTE : Mostly used Operating systems are Amazon Linux and Ubuntu.


<img width="2810" height="1450" alt="image" src="https://github.com/user-attachments/assets/47de5323-867b-43b4-965a-ba0c401bd23e" />

---

## Step 5: Choose Instance Type

Select:

Reason:

- Free tier eligible
- 1 CPU
- 1 GB RAM

Explanation:

Instance type is type of hardware which we want. For Example Iphone Model 
Iphone 17 -- Lower configuration 
Iphone 17 Pro -- Medium Configuration 
Iphone 17 Pro Max -- Higher Configuration 

Similary AWS provides lots of hardware types from which we can select. ( Depending on our application use case ) 

<img width="1807" height="927" alt="image" src="https://github.com/user-attachments/assets/a7520dd9-2729-4682-a949-8c8d7010d2c5" />

## Step 6: Create Key Pair

Click:

Create new key pair

Enter:

Select:

RSA

Download key.

⚠️ IMPORTANT:

Never lose this file.
You cannot download it again.


Explanation : 
The KEY PAIR in aws is used to connect to your EC2 instance from outside of aws console.
This is like a master key for all your houses. It means you can either create a single key pair and attach it to multiple EC2 instances or you can attach it to single instance as well.

<img width="2754" height="1454" alt="image" src="https://github.com/user-attachments/assets/3b516553-6fd2-4519-ac2f-3303657a5d4b" />

---

## Step 7: Configure Network Settings

Allow:

SSH → Your IP

OR

SSH → Anywhere (for lab only)

SSH Port:
22

Explanation:

Security group acts like firewall.
Think of it as a security gaurd of your society building. But here is the catch , this gaurd will only such people ( port numbers ) for which 
you have given permission ( Rule to allow port numbers ) 

<img width="2774" height="1462" alt="image" src="https://github.com/user-attachments/assets/ad3b5f25-fec5-4545-8620-fdb1f1299aea" />

---

## Step 8: Configure Storage

Default:


8 GB


Keep default or maybe change to anywhere between 8 to 30 GB. ( for free tier ) 
<img width="2868" height="1488" alt="image" src="https://github.com/user-attachments/assets/6fbe8175-6b77-4a8e-bbd4-1d797ad1efdc" />


---

## Step 9: Launch Instance

Click:

Launch Instance

Status should become:

Running


---

<img width="2802" height="1458" alt="image" src="https://github.com/user-attachments/assets/c802706e-01f2-46d5-bc5b-69fef3759fcf" />

<img width="2796" height="1458" alt="image" src="https://github.com/user-attachments/assets/4a054654-8da4-489f-9709-f860dc2137a7" />

---

## Step 10: Connect to EC2

Select instance which you want to connect to 

Click:

Connect

<img width="2810" height="1456" alt="image" src="https://github.com/user-attachments/assets/77c79611-d7ae-44f6-a8aa-2449a8c2f1ff" />


Choose:

EC2 Instance Connect

Click:

Connect
<img width="2954" height="1434" alt="image" src="https://github.com/user-attachments/assets/ea86cb68-5e9b-4735-8fd3-796da4c3e130" />


You will see terminal.

<img width="2834" height="1448" alt="image" src="https://github.com/user-attachments/assets/148a78b5-98ed-4d85-b153-9a09598d54f3" />

