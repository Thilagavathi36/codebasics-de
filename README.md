# Loafly Order Processing Pipeline

A refactored Python order-processing pipeline for Loafly. The project demonstrates clean code structure, object-oriented design, configuration management, logging, exception handling, retries, and environment-based secrets.

## Project Structure

```text
codebasics-de/
│
├── loafly/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── logger.py
│   └── gateway.py
│
├── raw_orders.csv
├── run_pipeline.py
├── requirements.txt
├── .env
├── env.example
├── .gitignore
└── README.md
```

## Features

- Reads raw order data from a CSV file
- Groups item rows into orders
- Uses an `Order` class to encapsulate order data and behavior
- Cleans and validates item prices
- Applies a configurable discount
- Handles missing or invalid prices without stopping the pipeline
- Uses Python logging instead of `print()`
- Writes timestamped logs to a log file
- Retries failed API requests before giving up
- Reads API credentials from environment variables
- Keeps configuration in a central configuration module
- Separates extraction, transformation, and loading into different modules

## Requirements

- Python 3.x
- `pip`
- `python-dotenv`

## Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd codebasics-de
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it using Git Bash:

```bash
source .venv/Scripts/activate
```

For Command Prompt:

```bash
.venv\Scripts\activate
```

For PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```text
LOAFLY_API_KEY=your-api-key-here
```

The `.env` file is used for local development and should **not** be committed to GitHub.

An `env.example` file is included as a template:

```text
LOAFLY_API_KEY=your-api-key-here
```

### 5. Run the pipeline

Make sure `raw_orders.csv` is present in the project root, then run:

```bash
python run_pipeline.py
```

## Configuration

Pipeline settings are maintained in `loafly/config.py`.

Example:

```python
API_KEY = os.getenv("LOAFLY_API_KEY")
DISCOUNT_PERCENT = 10
RAW_ORDERS_FILE = "raw_orders.csv"
RETRY_COUNT = 3
```

Changing the discount percentage, input file, or retry count can therefore be done through configuration rather than changing the pipeline logic.

## Logging

The pipeline uses Python's `logging` module.

Logs include:

- `INFO` — normal pipeline progress and successful operations
- `WARNING` — recoverable problems such as missing prices or retry attempts
- `ERROR` — failures that could not be recovered

The log output is written to:

```text
loafly.log
```

## Error Handling

If an order contains an item with a missing or invalid price:

1. The price-cleaning function raises an exception.
2. The exception is caught while processing the order.
3. A warning is written to the log.
4. The invalid item is skipped.
5. Processing continues with the remaining items and orders.

This prevents a single bad input row from stopping the entire pipeline.

## Retry Handling

When the orders API raises a `ConnectionError`, the pipeline retries the request according to `RETRY_COUNT`.

After all retry attempts are exhausted, the failure is logged as an error and processing can continue to the next order.


## Running the Project

From the project root:

```bash
source .venv/Scripts/activate
pip install -r requirements.txt
python run_pipeline.py
```

The pipeline will:

```text
Extract → Transform → Load
```

and log the execution details to `loafly.log`.