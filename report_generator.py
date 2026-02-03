import pandas as pd

def analyze_csv(file_path):
    # Read CSV
    df = pd.read_csv(file_path)

    report = {
        "file_name": file_path,
        "total_records": len(df),
        "total_columns": len(df.columns),
        "columns": list(df.columns),
        "numeric_analysis": {}
    }

    # Detect numeric columns
    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        report["numeric_analysis"][col] = {
            "min": float(df[col].min()),
            "max": float(df[col].max()),
            "average": round(float(df[col].mean()), 2),
            "sum": round(float(df[col].sum()), 2)
        }

    return report


# -----------------------------
# TEST / DEMO
# -----------------------------
if __name__ == "__main__":
    csv_file = "data.csv"   # any CSV
    analysis_report = analyze_csv(csv_file)

    print("\n📊 CSV ANALYSIS REPORT\n")
    print(f"Total Records : {analysis_report['total_records']}")
    print(f"Total Columns : {analysis_report['total_columns']}")
    print("\nNumeric Columns Summary:\n")

    for col, stats in analysis_report["numeric_analysis"].items():
        print(f"➡ {col}")
        print(f"   Min     : {stats['min']}")
        print(f"   Max     : {stats['max']}")
        print(f"   Average : {stats['average']}")
        print(f"   Sum     : {stats['sum']}")
        print()
