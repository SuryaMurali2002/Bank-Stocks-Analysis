\# Bank Stocks Time Series Analysis 💹



This project explores historical stock prices of major U.S. banks over a decade (2006–2016) to uncover trends, risks, and inter-bank relationships. The analysis is conducted using Python and various data visualization techniques.



---



\## 🎯 Objective



To analyze the performance, volatility, and relationships between major U.S. bank stocks over time. Specifically, we aim to:



\- Visualize historical closing prices and moving averages.

\- Compare daily returns to understand volatility.

\- Detect correlation between different bank stocks.

\- Quantify financial risk using Value at Risk (VaR).



---



\## 📈 Dataset



\- \*\*Source\*\*: Yahoo Finance via `pandas\_datareader`

\- \*\*Stocks analyzed\*\*:

&nbsp; - Bank of America (BAC)

&nbsp; - Citigroup (C)

&nbsp; - Goldman Sachs (GS)

&nbsp; - JPMorgan Chase (JPM)

&nbsp; - Morgan Stanley (MS)

\- \*\*Time Range\*\*: January 1, 2006 to January 1, 2016



---



\## 📊 Techniques Used



\- Time Series Visualization of stock prices and moving averages

\- Return distribution using histograms and KDE plots

\- Correlation analysis with heatmaps and pairplots

\- Value at Risk (VaR) estimation using quantiles

\- Risk vs Return scatter plots



---



\## 🧰 Tools \& Libraries



\- `pandas`

\- `pandas\_datareader`

\- `matplotlib`

\- `seaborn`

\- `datetime`

\- `numpy`



---



\## 🔍 Key Insights



\- All bank stocks crashed around 2008 due to the financial crisis.

\- Goldman Sachs (GS) exhibited the most volatility.

\- JPMorgan (JPM) showed relatively stable returns over time.

\- Strong positive correlations were found between most bank stocks.

