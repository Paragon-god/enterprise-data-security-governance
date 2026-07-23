# Privacy and Data Protection Assessment

## Purpose

This assessment identifies privacy concerns in the simulated Northstar Retail Group analytics environment.

## Processing activities

### Retail transaction analytics

Purpose: profitability and operational analysis.

Main concern: customer and commercial information could be used beyond its approved purpose or exposed to unauthorised analysts.

Required controls:

* remove or mask direct identifiers in analytical copies;
* restrict access by role;
* record the approved purpose;
* apply retention and secure deletion; and
* prevent uncontrolled exports.

### Website event analysis

Purpose: understand digital behaviour and conversion patterns.

Main concern: behavioural data can become personal when linked to identifiers or other datasets.

Required controls:

* collect only necessary event fields;
* document transparency and authorised use;
* limit retention;
* control data linkage; and
* assess reidentification risk before new uses.

### Model development

Purpose: explore factors associated with profit.

Main concern: predictions could be overtrusted or used outside the approved purpose.

Required controls:

* document model purpose and limitations;
* prohibit sole automated decisions;
* require human review;
* monitor performance; and
* retain approved model evidence.

### Dashboard and query access

Purpose: authorised decision support.

Main concern: public links or broad queries could reveal sensitive information.

Required controls:

* authenticate users;
* apply role aware views;
* minimise displayed fields;
* secure exports; and
* log access and administrative changes.

## Privacy principles

The implementation applies:

1. Purpose limitation.
2. Data minimisation.
3. Access control.
4. Retention limitation.
5. Secure disposal.
6. Transparency.
7. Accountability.
8. Controlled third party processing.

## Residual privacy risk

Residual privacy risk is Medium.

The public portfolio uses simulated and sanitised evidence. A production deployment would still require formal legal basis review, privacy notices, rights handling, approved retention, vendor assessment, and operational deletion controls.
