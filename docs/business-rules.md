# Business Rules — Revenue Backlog Automation

**BR-001 — Required project key**  
Every backlog record must contain a valid project or engagement identifier.

**BR-002 — Entity mapping**  
Entity and region values must resolve through an approved mapping table before aggregation.

**BR-003 — FX treatment**  
Foreign-currency backlog is translated using the approved reporting-rate method for the applicable period.

**BR-004 — Backlog classification**  
Backlog categories follow documented finance definitions and cannot be reassigned silently.

**BR-005 — Invalid input handling**  
Rows with invalid numeric values, dates, or required mappings are routed to an exception report.

**BR-006 — Source traceability**  
Each transformed record retains a source-file and source-row reference where practical.

**BR-007 — Aggregation consistency**  
Project, entity, region, and total views must reconcile to the same governed base dataset.

**BR-008 — Manual overrides**  
Any approved override is stored separately from the original source value with rationale.

**BR-009 — Period consistency**  
Management outputs use one approved reporting period and fiscal-calendar definition.

**BR-010 — Reproducibility**  
Given the same source files, mappings, and FX rates, the process should reproduce the same output.