import matplotlib.pyplot as plt
import seaborn as sns


def save_pnl_by_sentiment(df, path):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="market_sentiment", y="closed_pnl")
    plt.title("Average Closed PnL by Market Sentiment")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def save_winrate_by_sentiment(df, path):
    winrate = df.groupby("market_sentiment")["is_profitable"].mean().reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=winrate, x="market_sentiment", y="is_profitable")
    plt.title("Win Rate by Market Sentiment")
    plt.ylabel("Win Rate")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def save_volume_by_sentiment(df, path):
    volume = df.groupby("market_sentiment")["usd_value"].sum().reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=volume, x="market_sentiment", y="usd_value")
    plt.title("Trading Volume by Market Sentiment")
    plt.ylabel("Total USD Volume")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()