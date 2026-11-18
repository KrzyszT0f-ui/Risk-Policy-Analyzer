# **Local Branch Standard Operating Procedure (SOP) \- Daily IT Operations**

**Version:** 1.4  
**Effective Date:** March 15, 2024  
**Document Owner:** Local IT Operations Manager  
**Scope:** Regional Branch IT Operations Team

## **1\. Objective**

This Standard Operating Procedure (SOP) outlines the daily on-the-ground IT workflows for the regional branch. It serves as the primary operational guide for local IT staff to manage access, ensure data availability, handle daily incidents, and maintain hardware assets without disrupting branch business operations.

## **2\. Identity and Access Management (IAM)**

Proper access controls are critical to protecting customer data. Local IT must adhere to the following user management procedures:

> 1. **User Provisioning:** Access requests for new hires must be submitted via the ticketing system by the branch manager at least 48 hours prior to the start date.  
> 2. **Multi-Factor Authentication (MFA):** MFA is fully implemented across the branch infrastructure. It is mandatory for all local employees to register and use the Microsoft Authenticator application on their corporate devices for accessing any internal system.  
> 3. **Password Lifecycle:** Active Directory policies are configured to enforce mandatory password rotation for all branch staff every 90 days.  
> 4. **Account Resets:** Service desk agents must verify the user's identity visually or via their employee ID number before unlocking accounts or issuing temporary passwords.

## **3\. Data Backup and Recovery**

To guarantee that branch-level data is protected and can be restored quickly during hardware failures, the following backup routines are enforced:

> 1. **Schedule:** Automated full-system and file-share backups are scheduled to run daily at 02:00 AM local time to avoid bandwidth congestion during business hours.  
> 2. **Storage Location:** To ensure fast recovery times and minimize operational downtime during an outage, all daily backups are stored directly on the secondary NAS server located in the local branch server room (Rack 3, Server Unit B).  
> 3. **Verification:** The morning shift IT technician must review the automated backup logs daily by 08:30 AM.  
> 4. **Failures:** Any backup job marked as "Failed" or "Incomplete" must be manually restarted and monitored until completion before 10:00 AM.

## **4\. Incident Management and Support**

Local IT is responsible for the rapid triage and resolution of all technical issues affecting branch staff.

> 1. **Ticketing:** All support requests must be logged in the Jira Service Desk portal. Walk-up requests must be manually entered into Jira by the IT technician before work begins.  
> 2. **Prioritization:** Tickets are triaged as Low, Medium, High, or Critical based on the number of users affected and the impact on customer-facing operations.  
> 3. **Critical Incident Handling:** In the event of a critical incident (e.g., complete network outage, core banking app failure, or localized malware detection), the on-duty IT staff must immediately attempt isolation and system triage.  
> 4. **Reporting:** All critical incidents must be thoroughly documented in Jira, and a full incident summary must be reported to the Regional Head within 24 hours of the issue being detected.

## **5\. Vendor and Asset Management**

Management of physical hardware and external support staff must follow strict inventory and audit guidelines.

> 1. **Inventory Tracking:** All branch hardware, including laptops, desktops, and printers, must be tagged with a physical barcode and logged in the local CMDB upon arrival.  
> 2. **Physical Audits:** IT staff will conduct a physical inventory check of all branch workstations and server room equipment on the last Friday of every quarter.  
> 3. **Vendor Auditing:** For externally contracted IT services (e.g., specialized printer maintenance, local ISP support), all third-party vendors supporting the branch must undergo a full security audit annually. This is coordinated directly with the local procurement and compliance officers.  
> 4. **Escort Policy:** Third-party technicians are not permitted in the server room without a local IT staff member present at all times.