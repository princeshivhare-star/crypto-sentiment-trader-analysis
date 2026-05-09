import pandas as pd
import numpy as np


def merge_data(trader_df, sentiment_df):
    merged = trader_df.merge(
        sentiment_df[["date", "value", "classification"]],
        on="date",
        how="left"
    )

    merged = merged.rename(columns={
        "value": "sentiment_value",
        "classification": "market_sentiment"
    })

    return merged


def create_features(df):
    df["is_profitable"] = df["closed_pnl"] > 0
    df["loss_trade"] = df["closed_pnl"] < 0
    df["trade_direction"] = df["side"]

    df["pnl_per_usd"] = df["closed_pnl"] / df["usd_value"]
    df["fee_ratio"] = df["fee"] / df["usd_value"]

    df.replace([np.inf, -np.inf], 0, inplace=True)

    numeric_cols = df.select_dtypes(include=["number"]).columns
    text_cols = df.select_dtypes(include=["object"]).columns

    df[numeric_cols] = df[numeric_cols].fillna(0)
    df[text_cols] = df[text_cols].fillna("Unknown")

    return df