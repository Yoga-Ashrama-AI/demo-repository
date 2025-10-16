# 🧠 Universal Semantic Layer (USL) — AI-Infused & Lake-less Architecture

## Overview
The **Universal Semantic Layer (USL)** unifies metrics, dimensions, and business logic across systems — without requiring a centralized data lake. It provides semantic consistency, AI-assisted querying, and explainable data governance.

## Architecture Summary
- **Virtual Federation:** Data remains in source systems (Postgres, APIs, etc.) and is queried via Trino/Denodo.
- **Semantic Layer:** Defines entities, measures, and metrics in YAML using Cube or dbt + MetricFlow.
- **AI Gateway:** Converts natural language → validated DSL → SQL.
- **Governance:** Metrics catalog, lineage, policies, and testing (DataHub, OpenMetadata, Great Expectations).

## Folder Layout
```
/docs/architecture/
    Universal_Semantic_Layer.md
/semantic/
    metrics/
    entities/
/ai/
    gateway/
    embeddings/
```
