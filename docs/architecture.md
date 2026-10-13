
# Financial Data Platform — Architecture

This diagram represents the implemented banking-inspired data engineering workflow.

```mermaid
flowchart TD
    A["Synthetic Banking Transactions (CSV)"]
    B["Python ETL Pipeline (Pandas)"]
    C{"Data Validation"}
    D["Clean Transactions"]
    E["Rejected Transactions"]
    F["Customer Summary"]
    G["SQLite Database"]
    H["Five SQL Analytics Reports"]
    I["Pytest Data Quality Tests"]
    J["GitHub Actions Artifacts"]

    A --> B
    B --> C
    C -->|Valid| D
    C -->|Invalid| E
    D --> F
    D --> G
    G --> H
    D --> I
    D --> J
    E --> J
    F --> J
    H --> J
    I -.->|Tests must pass| J
```

## Execution

GitHub Actions runs the ETL pipeline, SQL analytics, and automated tests before uploading the generated CSV files as downloadable artifacts.

All data is synthetic and intended for portfolio demonstration.
