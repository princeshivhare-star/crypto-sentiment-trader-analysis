# Bitcoin Market Sentiment vs Trader Performance Analysis

## 1. Objective

The objective of this project is to analyze the relationship between Bitcoin market sentiment and trader performance using Fear/Greed Index data and historical trader data from Hyperliquid.

## 2. Datasets Used

### Bitcoin Market Sentiment Dataset
Columns used:
- date
- value
- classification

### Historical Trader Dataset
Important columns used:
- account
- coin
- execution price
- size
- side
- time
- start position
- event
- closedPnL
- fee

## 3. Data Cleaning

The historical trader dataset contained repeated column names, so columns were manually renamed.  
Date and time columns were converted into proper datetime format.  
Numerical fields such as execution price, size, USD value, closed PnL, and fee were converted into numeric format.

## 4. Feature Engineering

New features created:
- trade date
- market sentiment
- profitable trade flag
- PnL per USD
- fee ratio
- win rate

## 5. Analysis Performed

The analysis focused on:
- Average PnL by sentiment
- Win rate by sentiment
- Trading volume by sentiment
- Buy vs Sell performance
- Top profitable traders
- Loss-making traders

## 6. Key Insights

1. Trader profitability varies across different sentiment phases.
2. Fear-based markets can create profitable opportunities for some traders.
3. Greed-based markets may attract higher trading volume but also higher risk.
4. Buy and Sell trades behave differently under different sentiment conditions.
5. Top-performing traders can be identified by combining total PnL, average PnL, and win rate.
6. Sentiment can be used as an additional feature for building smarter trading strategies.

## 7. Business Recommendation

Traders should not rely only on price movement.  
Market sentiment can be used as a supporting signal to adjust risk, position size, and trade direction.

During Fear or Extreme Fear phases, traders may look for reversal or accumulation opportunities.  
During Greed or Extreme Greed phases, traders should manage risk carefully because crowded trades can increase volatility.

## 8. Conclusion

This analysis shows that Bitcoin market sentiment has a meaningful relationship with trader behavior and performance.  
Combining sentiment data with trader-level metrics can help identify profitable strategies, risky trading periods, and high-performing trader profiles.