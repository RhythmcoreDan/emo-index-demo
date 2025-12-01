"""
run_demo.py
-----------
Runs the demo emotional engine on a small candle dataset
and prints EMO_SCORE + EMO_ZONE for the latest candles.
"""

import pandas as pd
from emo_engine_demo import compute_emo


def main():
    df = pd.read_csv("sample_data.csv")

    df = compute_emo(df)

    latest = df.tail(10)  # last 10 rows for display

    print("=== EMO ENGINE DEMO ===")
    for _, row in latest.iterrows():
        print(
            f"{row['time']} | close={row['close']:.5f} | "
            f"EMO_SCORE={row['emo_score']:.3f} | ZONE={row['emo_zone']}"
        )

    last_row = latest.iloc[-1]
    print("\nLatest reading:")
    print(
        f"EMO_SCORE={last_row['emo_score']:.3f} | "
        f"ZONE={last_row['emo_zone']}"
    )


if __name__ == "__main__":
    main()
