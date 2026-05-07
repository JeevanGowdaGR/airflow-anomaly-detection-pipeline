import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(input_path="../data/time_series.csv", output_path="../data/anomaly_results.csv"):
    df = pd.read_csv(input_path)

    model = IsolationForest(
        contamination=0.04,
        random_state=42
    )

    df["anomaly"] = model.fit_predict(df[["value"]])
    df["is_anomaly"] = df["anomaly"].map({1: 0, -1: 1})

    df.to_csv(output_path, index=False)

    return df


if __name__ == "__main__":
    results = detect_anomalies()
    print(results.head())
    print("Anomaly detection complete.")