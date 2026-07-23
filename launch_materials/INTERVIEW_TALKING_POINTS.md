# Interview Talking Points

## Thirty second explanation

I built a working retail analytics prototype and then converted it into a data security GRC implementation. I connected the technical evidence to data classification, risk ownership, access governance, privacy, retention, model oversight, and management decisions.

## Strong examples

### Data integrity

A quotation parsing issue placed text inside a numerical field. I corrected the parser, converted the critical fields, checked for nulls, and reconciled record counts. This showed how engineering validation supports governance and reliable decision making.

### Access and secrets

I used a separate database application identity, kept credentials outside code, used TLS, excluded unsafe screenshots, and documented the risk created by temporary broad network access.

### Model governance

I reported the actual MAE, RMSE, and R squared results, documented limitations, prohibited sole automated decisions, required human oversight, and withheld production approval.

### Evidence based GRC

Each implemented control is mapped to technical or governance evidence. Controls that were not implemented are clearly labelled as recommendations.

## Questions to expect

1. Why did you classify credentials as Restricted?
2. How did you calculate inherent and residual risk?
3. Which controls were implemented and which were only recommended?
4. Why was production approval withheld?
5. How would you enforce least privilege in a production database?
6. What would you monitor for model drift?
7. How would retention and deletion work across backups and replicas?
8. What third party risks exist in managed cloud analytics?
9. How did you prevent the portfolio itself from exposing secrets?
10. How did AI assistance affect accountability?

## Honest limitations

The organisation and website events are simulated. The environment is a prototype. The model has no independent validation. Production authentication, central monitoring, recovery testing, and formal vendor assurance were not implemented.
