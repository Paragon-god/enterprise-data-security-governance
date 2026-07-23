# Model Risk Governance: Retail Profit Prediction Prototype

## Purpose
The model demonstrates controlled profit prediction and transparent performance evaluation within the simulated Northstar Retail Group environment.

## Approved use
- Exploratory analytics
- Model-governance demonstration
- Identification of factors associated with profit
- Decision support with accountable human review

## Prohibited use
The model must not be the sole basis for:
- pricing or discount changes;
- customer eligibility or treatment;
- employee actions;
- automated financial or operational decisions; or
- any decision with material legal, financial, or individual impact.

## Performance record
- Training rows: 7,995
- Testing rows: 1,999
- Training R-squared: 0.1665
- Adjusted R-squared: 0.1654
- Test MAE: 57.49
- Test RMSE: 223.13
- Test R-squared: 0.4270

## Main limitations
- Extreme profit and loss outliers
- Omitted explanatory variables
- Linear-regression assumptions
- Single random split
- No independent validation
- No production drift monitoring
- Potential misuse of point predictions without context

## Required governance before production
1. Independent data and model validation
2. Documented model owner and business owner
3. Approved model-use statement
4. Version-controlled training data and code
5. Cross-validation and alternative model comparison
6. Bias and error analysis by relevant segments
7. Data and performance drift monitoring
8. Human review of material decisions
9. Change-control and retirement triggers
10. Incident and override logging

## Residual-risk conclusion
Residual risk is **Medium** for portfolio demonstration and **High** for ungoverned production automation. Production use is not approved.
