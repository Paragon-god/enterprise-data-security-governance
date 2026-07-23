# Data Security Incident Response Playbook

## Purpose

This playbook provides a concise response structure for suspected data exposure, integrity failure, credential compromise, or unauthorised analytics access.

## Roles

* Incident lead: Security Officer
* Technical lead: Platform Administrator
* Data owner: relevant business Data Owner
* Privacy lead: Privacy Officer
* Evidence lead: GRC Analyst
* Communications lead: authorised management representative

## Response stages

### 1. Detect and validate

* confirm the alert or report;
* identify affected systems and data;
* preserve logs and evidence;
* avoid altering evidence unnecessarily; and
* assign severity and ownership.

### 2. Contain

* revoke exposed credentials;
* restrict network access;
* disable affected accounts or applications;
* isolate compromised environments; and
* stop unauthorised data flows.

### 3. Assess impact

* identify data assets, classifications, and individuals affected;
* determine whether confidentiality, integrity, or availability was compromised;
* review backups, replicas, exports, and public links;
* assess model or reporting impact; and
* determine notification duties with qualified legal and privacy advisers.

### 4. Eradicate and recover

* remove malicious or incorrect changes;
* rotate secrets and keys;
* correct configurations;
* restore trusted data and services;
* validate record counts and integrity; and
* increase monitoring during recovery.

### 5. Communicate

* provide accurate updates to authorised stakeholders;
* avoid speculative claims;
* protect investigation details;
* complete required notifications; and
* document decisions and approvals.

### 6. Learn and improve

* conduct a lessons review;
* record root cause and control gaps;
* update risks and treatments;
* assign corrective actions; and
* test the improved controls.

## Evidence checklist

Retain:

* event timeline;
* affected assets;
* access and configuration logs;
* credential rotation record;
* containment actions;
* recovery validation;
* notification decisions; and
* lessons and corrective actions.
