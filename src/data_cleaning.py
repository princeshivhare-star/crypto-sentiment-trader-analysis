import pandas as pd


def load_trader_data(path):
    df = pd.read_csv(path)

    df.columns = [
        "account",
        "coin",
        "execution_price",
        "size",
        "usd_value",
        "side",
        "time",
        "start_position",
        "event",
        "closed_pnl",
        "hash",
        "order_id",
        "crossed",
        "fee",
        "trade_id",
        "timestamp"
    ]

    df["time"] = pd.to_datetime(df["time"], dayfirst=True, errors="coerce")
    df["date"] = df["time"].dt.date

    numeric_cols = [
        "execution_price",
        "size",
        "usd_value",
        "start_position",
        "closed_pnl",
        "fee",
        "timestamp"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["side"] = df["side"].str.upper()
    df["event"] = df["event"].str.lower()

    df = df.dropna(subset=["time", "account"])

    return df


def load_sentiment_data(path):
    df = pd.read_csv(path)

    df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date
    df["classification"] = df["classification"].str.strip()

    return df