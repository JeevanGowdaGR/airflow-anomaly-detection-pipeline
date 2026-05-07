# Airflow Anomaly Detection Pipeline

## Overview
This project demonstrates an end-to-end anomaly detection pipeline using time-series data.

The pipeline includes:
- Data generation
- Anomaly detection using Isolation Forest
- Visualization of anomalies
- Airflow-style DAG for pipeline orchestration

---

## Project Structure

```bash
airflow-anomaly-detection-pipeline/
│
├── data/                  # Dataset and results
├── notebooks/             # Data generation notebook
├── src/                   # Core logic (detection + visualization)
├── dags/                  # Airflow DAG file
├── README.md
└── requirements.txt
```

---

## Pipeline Steps

1. Generate synthetic time-series data  
2. Inject anomalies into dataset  
3. Detect anomalies using Isolation Forest  
4. Store results  
5. Visualize anomalies  
6. Orchestrate pipeline using DAG  

---

## Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib  
- Apache Airflow (DAG design)  

---

## How to Run

### Install dependencies
```bash
pip install pandas numpy scikit-learn matplotlib
```

### Run pipeline
```bash
cd src
python detect_anomalies.py
python visualize_anomalies.py
```

---

## Output

- `data/time_series.csv` → Generated dataset  
- `data/anomaly_results.csv` → Detected anomalies  
- `data/anomaly_plot.png` → Visualization of anomalies  

---

## Note

The Airflow DAG file is included to demonstrate pipeline orchestration design.  
The pipeline scripts can be executed locally without running Airflow.
