# AI Product Ops Research Agent – Composio Take-Home Assignment

## Overview

This project automates the research of **100 SaaS applications** across **10 categories** by collecting official developer documentation, extracting API-related metadata, verifying a representative sample, and presenting the findings in a self-contained HTML case study.

The goal was to simulate Composio's Product Operations workflow by replacing repetitive manual research with an AI-assisted pipeline while maintaining transparency through verification.

## Project Structure

```
composio-product-ops-assignment/
│── apps.csv
│── research_agent.py
│── extract_results.py
│── generate_final_table.py
│── analyze_results.py
│── results.csv
│── structured_results.csv
│── final_results.csv
│── verification.csv
│── requirements.txt
│── README.md
│── .gitignore
└── case-study/
    ├── index.html
    ├── style.css
    └── script.js
```

## Workflow

The research pipeline follows four stages:

1. **Research Agent**
   - Reads `apps.csv`
   - Uses Tavily Search to find official developer documentation
   - Saves raw search results to `results.csv`

2. **Structured Extraction**
   - Extracts documentation snippets and evidence URLs
   - Saves cleaned data to `structured_results.csv`

3. **Metadata Generation**
   - Detects authentication methods
   - Identifies API surface (REST / GraphQL)
   - Detects MCP mentions
   - Generates `final_results.csv`

4. **Verification**
   - Manually verifies a representative sample of 20 apps
   - Records corrections in `verification.csv`

## Tech Stack

- Python
- Pandas
- Tavily Search API
- VS Code
- HTML
- CSS
- JavaScript
- Chart.js

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/25-Kaaviya/composio-product-ops-assignment.git
cd composio-product-ops-assignment
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows**

```powershell
.\venv\Scripts\Activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```
TAVILY_API_KEY=your_tavily_api_key
```

> The `.env` file is intentionally excluded from Git using `.gitignore`.

## Running the Project

### Step 1 – Collect documentation

```bash
python research_agent.py
```

Output:

- `results.csv`

### Step 2 – Extract structured documentation

```bash
python extract_results.py
```

Output:

- `structured_results.csv`

### Step 3 – Generate research metadata

```bash
python generate_final_table.py
```

Output:

- `final_results.csv`

### Step 4 – Analyze results

```bash
python analyze_results.py
```

Displays:

- Authentication distribution
- API surface distribution
- MCP distribution
- Category counts

## Verification Method

The assignment emphasizes verification rather than blind automation.

A representative sample of **20 applications** was manually compared against official developer documentation.

Verification focused on:

- Authentication method
- Self-serve vs gated onboarding
- API availability
- MCP support
- Buildability

Corrections were documented in `verification.csv`.

## Key Insights

- OAuth2 was the most common authentication pattern.
- REST APIs dominated across SaaS platforms.
- Finance platforms were more likely to require approval or commercial onboarding.
- Native MCP support is growing but remains limited.

## Case Study

The final deliverable is a self-contained HTML dashboard located in:

```
case-study/index.html
```

It includes:

- Executive summary
- KPI cards
- Research workflow
- Key findings
- Verification summary
- Interactive visualizations

## Deliverables

- Python research agent
- Automated documentation pipeline
- Structured API research dataset
- Verification report
- HTML case study
- Public GitHub repository

## Repository

GitHub: https://github.com/25-Kaaviya/composio-product-ops-assignment
