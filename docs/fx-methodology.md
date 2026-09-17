# FX Methodology — Revenue Backlog Automation

## Objective
Translate project backlog from local currency into a consistent reporting currency using a controlled and reproducible rate process.

## Reference Method
1. Identify the source currency for each backlog record.
2. Select the approved reporting-period FX rate.
3. Apply the configured conversion direction consistently.
4. Store both local and reporting-currency values.
5. Retain the rate used for traceability.

## Required Fields
- `currency_code`
- `fx_rate`
- `backlog_local`
- `backlog_reporting`
- `rate_period`

## Controls
- Missing currency codes are exceptions.
- Missing or zero FX rates are exceptions.
- Rates must come from the approved rate table for the reporting period.
- Manual rate overrides require documented rationale.
- Aggregated reporting should use converted values only after row-level validation.

## Public Demo
Synthetic currencies and rates are used in the portfolio implementation. The methodology demonstrates the control pattern without disclosing proprietary treasury or finance processes.