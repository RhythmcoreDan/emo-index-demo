"""
emo_engine_demo.py
-------------------
Lightweight demonstration of an emotional-behavior market indicator.

This simplified version analyzes:
- Volatility expansion
- Wick dominance
- Trend strength
- Composite EMO_SCORE
- Zone classification

This is a safe, public version of a larger emotional engine.
"""

import pandas as pd


def wick_ratio(row):
    body = abs(row['close'] - row['open'])
    upper = row['high'] - max(row['open'], row['close'])
    lower = min(row['open'], row['close']) - row['low']
    total_wick = upper + lower
    return total_wick / (body + 1e-8)


def trend_strength(df):
    # Simple directional momentum: close vs previous close
    df['trend'] = df['close'].diff()
    return df['trend'].rolling(5).mean()


def volatility(df):
    return df['close'].pct_change().rolling(5).std()


def classify_zone(score):
    if score > 0.6:
        return "GREEN"
    if score > 0.25:
        return "LIGHT_GREEN"
    if score > -0.25:
        return "GRAY"
    if score > -0.6:
        return "ORANGE"
    return "RED"


def compute_emo(df: pd.DataFrame):
    df['wick_ratio'] = df.apply(wick_ratio, axis=1)
    df['trend_strength'] = trend_strength(df)
    df['volatility'] = volatility(df)

    # Normalize each component
    df['wick_norm'] = (df['wick_ratio'] - df['wick_ratio'].mean()) / (df['wick_ratio'].std() + 1e-8)
    df['trend_norm'] = (df['trend_strength'] - df['trend_strength'].mean()) / (df['trend_strength'].std() + 1e-8)
    df['vol_norm'] = (df['volatility'] - df['volatility'].mean()) / (df['volatility'].std() + 1e-8)

    # Final emotional score (scaled)
    df['emo_score'] = (
        0.4 * df['wick_norm'] +
        0.3 * df['trend_norm'] +
        0.3 * df['vol_norm']
    )

    df['emo_zone'] = df['emo_score'].apply(classify_zone)

    return df
