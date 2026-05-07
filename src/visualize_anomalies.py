import pandas as pd
import matplotlib.pyplot as plt


def plot_anomalies(input_path="../data/anomaly_results.csv", output_path="../data/anomaly_plot.png"):
    df = pd.read_csv(input_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    normal = df[df["is_anomaly"] == 0]
    anomalies = df[df["is_anomaly"] == 1]

    plt.figure(figsize=(12, 6))
    plt.plot(normal["timestamp"], normal["value"], label="Normal")
    plt.scatter(anomalies["timestamp"], anomalies["value"], label="Anomaly")
    plt.title("Time-Series Anomaly Detection")
    plt.xlabel("Timestamp")
    plt.ylabel("Metric Value")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)

    print("Anomaly plot saved.")


if __name__ == "__main__":
    plot_anomalies()