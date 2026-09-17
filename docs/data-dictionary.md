# Data Dictionary — Revenue Backlog Automation

| Table | Field | Type | Description |
|---|---|---|---|
| project | project_id | string | Synthetic project key |
| project | project_name | string | Fictional project name |
| project | entity | string | Legal / reporting entity |
| project | region | string | Reporting region |
| project | customer_id | string | Synthetic customer key |
| backlog | project_id | string | Project foreign key |
| backlog | snapshot_date | date | Reporting snapshot |
| backlog | currency_code | string | Source currency |
| backlog | backlog_local | decimal | Backlog in local currency |
| backlog | fx_rate | decimal | Reporting conversion rate |
| backlog | backlog_reporting | decimal | Backlog in reporting currency |
| backlog | backlog_type | string | T&M / fixed / other governed category |
| backlog | revenue_category | string | Reporting classification |
| backlog | expected_period | date | Expected delivery / recognition period |
| mapping | source_entity | string | Source entity label |
| mapping | reporting_entity | string | Standardized entity |
| mapping | reporting_region | string | Standardized region |

All public project, customer, entity, and financial values are synthetic.