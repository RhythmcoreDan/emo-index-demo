EMO Index Demo

A lightweight demonstration of an emotional-behavior market indicator.
This simplified engine analyzes wick behavior, volatility expansion, and trend strength to generate a composite EMO_SCORE and color-coded EMO_ZONE.

This is a safe, public version of a larger proprietary emotional engine used in my advanced trading system (RhythmCore).

🚀 What This Demo Shows

Wick ratio measurement (upper + lower wick vs. body)

Volatility calculation (rolling standard deviation)

Trend strength (rolling momentum)

Normalization of components

Composite emotional score

Zone classification:

GREEN — strong positive behavior

LIGHT_GREEN — mild bullish behavior

GRAY — neutral

ORANGE — mild fear

RED — emotional stress / exhaustion

📂 Project Structure
emo-index-demo/
│
├── emo_engine_demo.py      # Core emotional engine
├── run_demo.py             # Runs the engine and prints last readings
├── sample_data.csv         # Example candle data
└── README.md               # Documentation

🧪 Running the Demo

Make sure you have pandas installed:

pip install pandas


Then run:

python run_demo.py

📈 Example Output
=== EMO ENGINE DEMO ===
2024-01-06 | close=1.11150 | EMO_SCORE=0.187 | ZONE=GRAY
2024-01-07 | close=1.11200 | EMO_SCORE=0.312 | ZONE=LIGHT_GREEN
2024-01-08 | close=1.11550 | EMO_SCORE=0.455 | ZONE=LIGHT_GREEN
2024-01-09 | close=1.11800 | EMO_SCORE=0.520 | ZONE=LIGHT_GREEN
2024-01-10 | close=1.12050 | EMO_SCORE=0.640 | ZONE=GREEN

🧠 How the EMO_SCORE Works

The score is a weighted blend of:

40% wick behavior

30% trend strength

30% volatility

These components are normalized, combined, and mapped into zones.

This creates a simple, intuitive emotional reading of market conditions.

💬 About This Repo

This project is a small public demo showing how I approach emotional-behavior modeling in trading systems.
My full system includes:

Real-time data ingestion

Emotional state engines

Regime mapping

Execution APIs

Backtesting and forward-testing pipelines

Automated multi-feed monitoring

If you’d like to collaborate, build custom indicators, or integrate this type of logic into a trading bot, feel free to reach out.
