I have completed a new data security GRC portfolio implementation.

The project converts a working enterprise analytics prototype into a full governance, risk, privacy, model governance, and control assurance case study for Northstar Retail Group, a simulated retail organisation.

The technical environment processes retail transactions and website events through Spark, Parquet, R, Shiny, MongoDB, and a basic query application.

The implementation produced:

1. An inventory and classification register for 11 data assets
2. A risk register covering 12 material data security risks
3. A treatment plan with accountable owners
4. A catalogue of 20 controls
5. A role based access matrix and governance RACI
6. A retention and secure disposal schedule
7. A privacy assessment
8. A model risk governance record
9. A control to evidence matrix
10. Sanitised technical evidence from the implemented prototype

One of the most important findings came from data integrity testing. A quotation parsing issue shifted a product description into a numerical field. Correcting the parser and validating the critical fields showed why data quality controls are part of security and governance, not only engineering.

The model governance review was equally important. The regression model produced measurable results, but its limitations mean it should support human judgement rather than drive automated pricing or discount decisions.

The final decision is clear:

The prototype is suitable for portfolio demonstration and controlled improvement planning. It is not approved for production deployment.

Production readiness would require restricted database connectivity, enforced access roles, authenticated applications, central monitoring, tested recovery, approved retention automation, vendor assurance, incident response exercises, and independent model validation.

This is a simulated portfolio implementation, not a client engagement or regulatory certification.

AI tools supported planning, documentation, code assistance, artefact generation, and quality review. I retained responsibility for technical execution, evidence validation, risk decisions, oversight, and final approval.

GitHub:
https://github.com/Paragon-god/enterprise-data-security-governance

Notion case study:
https://app.notion.com/p/3a693b2a32e7814b89c8d8b6e3b652fe

#GRC #DataSecurity #Cybersecurity #Privacy #RiskManagement #DataGovernance #ModelGovernance #ApacheSpark #MongoDB #PortfolioProject
