# **Group ICT Security Policy**

## **1\. Document Control**

* **Version:** 2.0  
* **Effective Date:** January 1, 2024  
* **Policy Owner:** Chief Information Security Officer (CISO)  
* **Audience:** All employees, contractors, and third-party vendors

## **2\. Purpose and Scope**

This document sets the mandatory security requirements for the European Banking Group to ensure compliance with the Digital Operational Resilience Act (DORA) and European Banking Authority (EBA) ICT Guidelines.  
The policy applies to all systems, networks, applications, and data managed by the Group or its third-party service providers. Non-compliance will result in immediate access revocation and disciplinary action.

## **3\. Policy Requirements**

### **3.1. Identity & Access Management (IAM)**

> 1. **Authentication:** Multi-Factor Authentication (MFA) is strictly mandatory for all systems. No exceptions.  
> 2. **Password Length:** Minimum password length is 14 characters.  
> 3. **Password Rotation:** Passwords must be rotated every 60 days.  
> 4. **Access Reviews:** System owners must execute access rights audits every 90 days.

### **3.2. Backup & Recovery**

> 1. **Frequency:** Backups must be performed daily.  
> 2. **Immutability:** All backups must be immutable to prevent ransomware tampering.  
> 3. **Storage:** All backups must be stored in a geographically separated, off-site location.  
> 4. **Testing:** Full data recovery tests must be executed bi-annually.

### **3.3. Incident Management**

> 1. **Internal Reporting:** Critical ICT incidents must be reported to the Group Risk Committee within 4 hours of detection.  
> 2. **Regulatory Reporting:** Major ICT-related incidents must be reported to the competent authority within 24 hours of classification.  
> 3. **Containment Authority:** Security teams possess unilateral authority to isolate compromised network segments immediately.

### **3.4. Vendor Management**

> 1. **Auditing:** All third-party ICT service providers must undergo a full security audit annually.  
> 2. **Contractual SLA:** Vendor agreements must include right-to-audit clauses and binding incident response timelines.  
> 3. **Termination:** Contracts with vendors failing the annual audit must be paused or terminated until remediation is verified.

### **3.5. System Hardening & Patching**

> 1. **Vulnerability Patching:** High-severity vulnerabilities must be patched within 48 hours of detection.  
> 2. **Scanning:** External-facing assets require automated weekly scans. Internal assets require monthly scans.  
> 3. **Encryption:** Data at rest must use AES-256 encryption. Data in transit must use TLS 1.3.