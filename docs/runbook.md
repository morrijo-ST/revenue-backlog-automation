# Operations Runbook — Revenue Backlog Automation

## Monthly / Periodic Run
1. Confirm all regional source files are received.
2. Validate required columns and data types.
3. Check unmapped entities, projects, and revenue categories.
4. Confirm the approved FX-rate table for the reporting period.
5. Run normalization and mapping.
6. Apply backlog classifications and FX conversion.
7. Reconcile aggregate totals to source controls.
8. Produce project, entity, region, and management outputs.

## Common Failures
### Missing file
Flag the affected region/entity and do not represent totals as complete.

### Mapping failure
Add the item to the mapping exception report and resolve before final publication.

### FX mismatch
Confirm currency, period, and rate-source alignment before rerunning.

### Output total differs from source
Trace differences through validation exclusions, mappings, FX, and classification logic.

## Recovery
Rerun from the original source population using the same mapping and FX versions to reproduce prior results.

## Publication Control
Management outputs should not be distributed until source counts, converted totals, and regional rollups reconcile.