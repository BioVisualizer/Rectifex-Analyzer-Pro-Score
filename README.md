# Rectifex Analyzer Pro-Score
Dynamic Hybrid Scoring & Market Analysis Tool
Rectifex Analyzer Pro-Score is more than a simple stock screener; it is your personalized, dynamic investment cockpit. The app is based on an advanced 12-Point Hybrid Scoring System that combines proven metrics from Value Analysis (inspired by Piotroski, Magic Formula) with current Market Dynamics (Momentum and Sentiment). The goal is to quickly and transparently identify companies in a crowded market that are both financially sound and currently purchasable under your specific risk tolerance.

🚀 Core Features
Personalized Strategy via Sliders: The core of the application. The three main sliders transform complex financial metrics into intuitive thresholds that reflect your personal investment strategy:

"Quality Standard" (Safety vs. Speculation): Controls the requirements for financial security (e.g., Equity Ratio, stability of Cash Flow) and profitability (Return on Equity, Profit Margin). A higher standard aggressively filters for financially healthy companies.

"Valuation Approach" (Value vs. Growth): Defines the tolerance for high multiples such as the P/E Ratio (KGV) and the Price-to-Book Ratio (KBV). A focus on "Value" (low setting) strictly filters for cheaply valued stocks. "Growth" (high setting) accepts higher valuations for companies with strong expected earnings growth.

"Momentum & Timing" (Long-term vs. Dynamic): Focuses on the relative price strength over the last 6 and 12 months, as well as the distance from the 52-week high. This helps determine the optimal buying time and recognize trend reversals early.

Market Scan & Dynamic Top List: With one click, you simultaneously evaluate hundreds of stored stocks. The system performs an in-depth quantitative analysis and dynamically sorts the results by the achieved overall score. The generated top list immediately provides clear, rule-based recommendations (Buy, Hold, Sell). The control section is collapsible by default for optimal UX and can be refreshed at any time using the Refresh button.

Transparency & Detailed Score: Upon selecting a ticker, you get a detailed view of the score (e.g., 7 out of 12 possible points). The app transparently shows which of the 12 underlying criteria were met (+1), which are neutral (0), and which disqualify the stock (-1). This builds confidence in the recommendation and serves as an excellent learning tool.

⚠️ Important Limitations
Data Source (Simulation): The current version of the app is a Proof of Concept running on simulated financial data. The displayed prices and metrics are not current or accurate in reality. For live usage, the implementation of a Backend Proxy (e.g., in Node.js or Python) is mandatory to fetch real-time financial data from API providers (like Yahoo Finance). Without this proxy, the data will not be current.

Logic & Industry Specifics: The thresholds used by the sliders are currently generic and apply across the broad market. For maximum precision, industry-specific logic (e.g., for banks, which naturally have lower equity ratios, or technology companies with typically higher P/E ratios) must be implemented and refined to ensure fair comparisons between sectors.

Scaling and Speed: The speed of the market scan directly depends on the number of stocks queried and the latency of the data backend being used.

⚖️ Liability Disclaimer
This is NOT investment advice.

The Rectifex Analyzer Pro-Score is a pure analysis and demonstration tool. The generated purchase recommendations are based on a quantitative, rule-based algorithm. The tool does not consider personal financial circumstances, risk tolerance, or specific market conditions.

The use of the generated recommendations for actual investment decisions is solely at your own risk. The software operator assumes no liability for any direct or indirect losses resulting from the use or misinterpretation of the results. Always consult a certified financial advisor before making any investment decisions.
