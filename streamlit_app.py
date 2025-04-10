import streamlit as st
import pandas as pd

# --------------------------------------------------------------------
# Set page configuration
st.set_page_config(page_title="Fintro - Learn About ETFs", layout="wide")

# --------------------------------------------------------------------
# Inject detailed CSS styles from your original React component.
css = """
<style>
:root {
  --primary-blue: #1A2980;
  --primary-teal: #26D0CE;
  --light-gray: #F5F7FA;
  --white: #FFFFFF;
  --coral: #FF6B6B;
  --low-risk: #4CAF50;
  --medium-risk: #FFC107;
  --high-risk: #F44336;
  --text-dark: #333333;
  --text-gray: #666666;
  --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  --radius: 8px;
  --transition: all 0.3s ease;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.app-container {
  font-family: 'Roboto', sans-serif;
  color: var(--text-dark);
  background-color: var(--light-gray);
  line-height: 1.6;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

/* Navigation & Header */
header {
  background: linear-gradient(to right, var(--primary-blue), var(--primary-teal));
  color: var(--white);
  padding: 15px 20px;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  margin-bottom: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.logo {
  display: flex;
  align-items: center;
  font-size: 1.5rem;
  font-weight: 700;
}
.logo-icon {
  margin-right: 8px;
}
.nav-links {
  display: flex;
  gap: 15px;
}
.nav-link {
  color: var(--white);
  padding: 5px 10px;
  border-radius: 4px;
  transition: var(--transition);
  cursor: pointer;
  font-weight: 600;
}
.nav-link.active, .nav-link:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

/* Hero Section */
.hero {
  background-color: var(--white);
  padding: 30px;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  margin-bottom: 20px;
  text-align: center;
}
.hero h1 {
  font-size: 1.8rem;
  margin-bottom: 10px;
  color: var(--primary-blue);
}
.hero p {
  color: var(--text-gray);
  margin-bottom: 20px;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

/* Input Panel */
.input-panel {
  background-color: var(--light-gray);
  padding: 20px;
  border-radius: var(--radius);
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  justify-content: center;
  align-items: flex-end;
}
.input-group {
  min-width: 200px;
  flex: 1;
}
.input-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
}
.slider-container {
  display: flex;
  align-items: center;
  gap: 10px;
}
.slider {
  flex: 1;
  height: 8px;
  border-radius: 4px;
  background: linear-gradient(to right, var(--low-risk), var(--medium-risk), var(--high-risk));
  outline: none;
}
.slider-value {
  min-width: 30px;
  text-align: center;
  font-weight: bold;
}
.input-group input[type="number"] {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 30px;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
}
.btn-primary {
  background-color: var(--coral);
  color: var(--white);
}
.btn-primary:hover {
  background-color: #ff5252;
  transform: translateY(-2px);
}

/* Card Styles */
.card {
  background-color: var(--white);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 20px;
  margin-bottom: 20px;
  transition: var(--transition);
}
.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}
.section-title {
  font-size: 1.2rem;
  margin-bottom: 15px;
  color: var(--primary-blue);
  display: flex;
  align-items: center;
  gap: 8px;
}
.section-icon {
  color: var(--primary-teal);
}

/* ETF Card */
.etf-card {
  display: flex;
  border-radius: var(--radius);
  overflow: hidden;
  background-color: var(--white);
  box-shadow: var(--shadow);
  margin-bottom: 15px;
  transition: var(--transition);
}
.etf-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}
.etf-match-score {
  width: 70px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(to bottom, var(--primary-blue), var(--primary-teal));
  color: var(--white);
  padding: 15px 10px;
}
.match-value {
  font-size: 1.5rem;
  font-weight: 700;
}
.match-label {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.etf-details {
  flex: 1;
  padding: 15px;
}
.etf-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 10px;
}
.etf-name {
  font-size: 1.1rem;
  font-weight: 600;
}
.etf-category {
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
}
.category-equity {
  background-color: #E3F2FD;
  color: #1976D2;
}
.category-bond {
  background-color: #F3E5F5;
  color: #7B1FA2;
}
.category-mixed {
  background-color: #FFFDE7;
  color: #FFA000;
}

/* ETF Metrics & Risk */
.etf-metrics {
  display: flex;
  gap: 15px;
}
.metric {
  text-align: center;
  flex: 1;
}
.metric-value {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--primary-blue);
}
.metric-label {
  font-size: 0.8rem;
  color: var(--text-gray);
}
.etf-risk {
  margin-top: 15px;
}
.risk-label {
  display: flex;
  justify-content: space-between;
  font-size: 0.8rem;
  font-weight: 600;
  margin-bottom: 5px;
}
.risk-bar {
  height: 6px;
  background-color: #e0e0e0;
  border-radius: 3px;
  overflow: hidden;
}
.risk-level {
  height: 100%;
  border-radius: 3px;
}

/* Chart Section */
.chart-container {
  background-color: #fff;
  padding: 20px;
  border-radius: var(--radius);
}
.time-filters {
  display: flex;
  gap: 10px;
  margin-bottom: 15px;
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
}
.time-filter {
  padding: 5px 15px;
  border-radius: 20px;
  background-color: #f0f0f0;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
}
.time-filter.active {
  background-color: var(--primary-blue);
  color: white;
}
.time-filter:hover:not(.active) {
  background-color: #e0e0e0;
}

/* Learn Tab (Chat) */
.chat-container {
  flex: 1;
  min-width: 300px;
  background-color: white;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  display: flex;
  flex-direction: column;
  height: 600px;
  margin-bottom: 20px;
}
.chat-header {
  padding: 15px;
  background: linear-gradient(to right, var(--primary-blue), var(--primary-teal));
  color: white;
  border-radius: var(--radius) var(--radius) 0 0;
  display: flex;
  align-items: center;
}
.chat-header-icon {
  margin-right: 10px;
  font-size: 1.5rem;
}
.chat-header h2 {
  font-size: 1.2rem;
}
.chat-messages {
  flex: 1;
  padding: 15px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.message {
  max-width: 80%;
  padding: 10px 15px;
  border-radius: 18px;
  line-height: 1.4;
  font-size: 0.95rem;
}
.message-bot {
  align-self: flex-start;
  background-color: #f0f0f0;
  border-bottom-left-radius: 5px;
}
.message-user {
  align-self: flex-end;
  background-color: var(--primary-teal);
  color: white;
  border-bottom-right-radius: 5px;
}
.chat-form {
  padding: 15px;
  border-top: 1px solid #eee;
  display: flex;
  gap: 10px;
}
.chat-input {
  flex: 1;
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 20px;
  outline: none;
  font-size: 0.9rem;
}
.chat-input:focus {
  border-color: var(--primary-teal);
}
.chat-submit {
  width: 40px;
  height: 40px;
  border: none;
  border-radius: 50%;
  background-color: var(--primary-teal);
  color: white;
  font-size: 1rem;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: var(--transition);
}
.chat-submit:hover {
  background-color: var(--primary-blue);
}

/* Profile Tab */
.profile-page {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.profile-header {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}
.user-info-card {
  flex: 1;
  min-width: 300px;
  background-color: white;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 20px;
  text-align: center;
}
.user-avatar-large {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--primary-blue), var(--primary-teal));
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 3rem;
  margin: 0 auto 15px;
}
.user-name {
  font-size: 1.5rem;
  margin-bottom: 5px;
  color: var(--primary-blue);
}
.user-email {
  color: var(--text-gray);
  margin-bottom: 20px;
}
.user-info-list {
  text-align: left;
  border-top: 1px solid #eee;
  padding-top: 15px;
}
.info-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}
.info-label {
  font-weight: 600;
}
.info-value {
  color: var(--text-dark);
}
.green {
  color: var(--low-risk);
}
.profile-stats-cards {
  flex: 2;
  min-width: 300px;
  display: flex;
  gap: 15px;
}
.stat-card {
  flex: 1;
  background-color: white;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transition: var(--transition);
}
.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
}
.stat-icon {
  font-size: 2rem;
  margin-bottom: 10px;
}
.stat-value {
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--primary-blue);
  margin-bottom: 5px;
}
.stat-label {
  font-size: 0.9rem;
  color: var(--text-gray);
}
.portfolio-section {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.portfolio-card {
  background-color: white;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 20px;
}
.section-header {
  font-size: 1.2rem;
  margin-bottom: 15px;
  color: var(--primary-blue);
}
.portfolio-table, .watchlist-table, .activity-table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #eee;
}
th {
  font-weight: 600;
  color: var(--text-gray);
}
.ticker {
  font-family: monospace;
  font-weight: 600;
}
.change-positive {
  color: var(--low-risk);
  font-weight: 600;
}
.change-negative {
  color: var(--high-risk);
  font-weight: 600;
}
.allocation-bar-container {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 10px;
}
.allocation-bar {
  height: 8px;
  background: linear-gradient(to right, var(--primary-blue), var(--primary-teal));
  border-radius: 4px;
}
.portfolio-columns {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}
.watchlist-section, .activity-section {
  flex: 1;
  min-width: 300px;
  background-color: white;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 20px;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# --------------------------------------------------------------------
# Initialize session state variables (to preserve unsimplified logic)
if "risk_tolerance" not in st.session_state:
    st.session_state.risk_tolerance = 6
if "investment_amount" not in st.session_state:
    st.session_state.investment_amount = 2500
if "profile" not in st.session_state:
    st.session_state.profile = "Novice Aggressive"
if "recommendations" not in st.session_state:
    st.session_state.recommendations = []
if "selected_time_period" not in st.session_state:
    st.session_state.selected_time_period = "6M"
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"sender": "bot", "text": "Hi there! I'm your ETF learning assistant. Ask me anything about ETFs, investing, or financial concepts!"}
    ]

# --------------------------------------------------------------------
# Sample ETF data (as in your React code)
etfs = [
    {
      "id": 1,
      "name": "Iota ETF",
      "ticker": "IETF",
      "category": "Equity",
      "annualReturn": 12.77,
      "expenseRatio": 0.36,
      "volatility": 12.1,
      "riskLevel": 8,
      "matchScore": 92,
      "returns": { "1M": 1.2, "3M": 3.6, "6M": 6.8, "1Y": 12.77, "5Y": 64.3 }
    },
    {
      "id": 2,
      "name": "Epsilon ETF",
      "ticker": "EPSN",
      "category": "Equity",
      "annualReturn": 2.59,
      "expenseRatio": 0.49,
      "volatility": 6.7,
      "riskLevel": 7,
      "matchScore": 85,
      "returns": { "1M": 0.1, "3M": 0.8, "6M": 1.4, "1Y": 2.59, "5Y": 13.5 }
    },
    {
      "id": 3,
      "name": "Alpha ETF",
      "ticker": "ALFA",
      "category": "Bond",
      "annualReturn": 9.77,
      "expenseRatio": 0.26,
      "volatility": 8.5,
      "riskLevel": 5,
      "matchScore": 75,
      "returns": { "1M": 0.7, "3M": 2.3, "6M": 4.7, "1Y": 9.77, "5Y": 48.2 }
    },
    {
      "id": 4,
      "name": "Delta ETF",
      "ticker": "DTEF",
      "category": "Mixed",
      "annualReturn": 8.25,
      "expenseRatio": 0.31,
      "volatility": 7.9,
      "riskLevel": 6,
      "matchScore": 70,
      "returns": { "1M": 0.9, "3M": 2.5, "6M": 4.1, "1Y": 8.25, "5Y": 42.8 }
    }
]

# Sample user profile data
user_profile = {
    "name": "Alex Johnson",
    "email": "alex.j@university.edu",
    "portfolioValue": "€3,742.50",
    "totalInvested": "€3,500.00",
    "totalReturn": "€242.50 (6.93%)",
    "watchlist": [
      {"name": "Delta ETF", "ticker": "DTEF", "change": "+2.4%"},
      {"name": "Sigma ETF", "ticker": "SGETF", "change": "-0.7%"},
      {"name": "Omega ETF", "ticker": "OMGA", "change": "+1.2%"}
    ],
    "recentActivity": [
      {"date": "Oct 5, 2024", "action": "Purchased Alpha ETF", "amount": "€500.00"},
      {"date": "Sept 28, 2024", "action": "Dividend Payment", "amount": "€12.75"},
      {"date": "Sept 15, 2024", "action": "Purchased Iota ETF", "amount": "€750.00"}
    ],
    "holdings": [
      {"name": "Alpha ETF", "ticker": "ALFA", "shares": "12.5", "value": "€1,221.75", "allocation": "32.6%"},
      {"name": "Iota ETF", "ticker": "IETF", "shares": "18.2", "value": "€2,243.40", "allocation": "59.9%"},
      {"name": "Cash", "ticker": "-", "shares": "-", "value": "€277.35", "allocation": "7.5%"}
    ]
}

# Detailed chatbot responses (as per the original React code)
chatbot_responses = {
    "what is an etf": "An ETF (Exchange-Traded Fund) is an investment fund that trades on stock exchanges, holding assets such as stocks, bonds, or commodities with typically lower fees than mutual funds.",
    "what exactly is an etf": "An ETF (Exchange-Traded Fund) is a fund that trades like a stock and holds a basket of assets. It typically offers liquidity and diversification.",
    "how do etfs work": "ETFs pool money from investors to buy a diversified portfolio of assets. They trade like stocks and often track a specific index.",
    "what are the benefits of etfs": "ETFs offer diversification, low costs, tax efficiency, and liquidity—making them attractive investment vehicles.",
    "what's the difference between etfs and mutual funds": "ETFs trade throughout the day and generally have lower fees. Mutual funds trade once per day and may have higher fees and minimum investments.",
    "what are index etfs": "Index ETFs track a specific market index, offering broad exposure to a sector or market with typically lower costs.",
    "what are the risks of etfs": "Risks include market risk, tracking error, liquidity risk, and concentration risk. Always consider your risk tolerance.",
    "how do i buy an etf": "ETFs can be purchased through brokerage accounts. Simply search for the ETF by its ticker, then place a buy order similar to stock transactions.",
    "what is an expense ratio": "The expense ratio is the annual fee charged by an ETF, expressed as a percentage of the fund's assets. Lower ratios typically mean lower costs to investors.",
    "how are etfs taxed": "ETFs are generally tax-efficient. Dividends and capital gains may be taxable, but their unique structure often minimizes capital gains distributions.",
    "what is the difference between active and passive etfs": "Passive ETFs aim to replicate an index, while active ETFs are managed by portfolio managers attempting to outperform the market.",
    "what are the different types of etfs": "Types include equity ETFs, bond ETFs, commodity ETFs, currency ETFs, specialty ETFs (like ESG), inverse ETFs, leveraged ETFs, and international ETFs.",
    "are etfs good for beginners": "Yes, ETFs provide diversification and low costs, making them an excellent starting point for beginner investors."
}

# --------------------------------------------------------------------
# Helper functions
def get_risk_level_class(risk_level):
    if risk_level <= 3:
        return "Low"
    elif risk_level <= 6:
        return "Medium"
    else:
        return "High"

def get_expected_return(etf, period):
    return etf["returns"].get(period, 0)

def get_chart_data(recommendations, period):
    data = {
        "ETF": [etf["name"] for etf in recommendations],
        "Return (%)": [etf["returns"].get(period, 0) for etf in recommendations]
    }
    return pd.DataFrame(data)

def update_recommendations():
    risk = st.session_state.risk_tolerance
    amount = st.session_state.investment_amount
    filtered = etfs.copy()
    # Apply filtering based on risk tolerance:
    if risk < 4:
        filtered = [etf for etf in filtered if etf["category"] == "Bond" or etf["riskLevel"] < 6]
    elif risk > 7:
        filtered = [etf for etf in filtered if etf["annualReturn"] > 5]
    # Sort by match score descending
    filtered.sort(key=lambda x: x["matchScore"], reverse=True)
    st.session_state.recommendations = filtered
    # Update profile text based on risk and amount:
    if risk <= 4:
        st.session_state.profile = "Experienced Conservative" if amount > 3000 else "Novice Conservative"
    elif risk <= 7:
        st.session_state.profile = "Experienced Moderate" if amount > 3000 else "Novice Moderate"
    else:
        st.session_state.profile = "Experienced Aggressive" if amount > 3000 else "Novice Aggressive"

def handle_chat(user_message):
    st.session_state.chat_messages.append({"sender": "user", "text": user_message})
    query = user_message.lower().strip()
    response = chatbot_responses.get(query, "I'm not sure about that. Try asking about ETFs, investment basics, or risk profiles.")
    st.session_state.chat_messages.append({"sender": "bot", "text": response})

# --------------------------------------------------------------------
# Navigation using sidebar
tab = st.sidebar.radio("Navigation", ["Recommendations", "Learn", "Profile"])

# Wrap the entire app content in a main container div for styling
st.markdown('<div class="app-container">', unsafe_allow_html=True)

# --------------------------------------------------------------------
# Recommendations Tab
if tab == "Recommendations":
    st.header("Find ETFs that match your investment style with Fintro")
    
    # Render a hero section (using st.markdown to preserve detailed styling)
    st.markdown("""
    <div class="hero">
      <h1>Find ETFs that match your investment style with Fintro</h1>
      <p>Answer a few questions to get personalized ETF recommendations based on your risk tolerance and investment goals.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input panel: risk slider, amount input, and button
    st.markdown('<div class="input-panel">', unsafe_allow_html=True)
    st.session_state.risk_tolerance = st.slider("Risk Tolerance (1-10)", 1, 10, st.session_state.risk_tolerance)
    st.session_state.investment_amount = st.number_input("Investment Amount (€)", min_value=100, step=100, value=st.session_state.investment_amount)
    if st.button("Get Recommendations"):
        update_recommendations()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Display investor profile card
    st.markdown("### Your Investor Profile")
    st.write(f"**Profile:** {st.session_state.profile}")
    st.write(f"**Risk Tolerance:** {st.session_state.risk_tolerance}/10")
    exp_text = "3+ yrs" if "Experienced" in st.session_state.profile else "0-2 yrs"
    st.write(f"**Experience:** {exp_text}")
    st.write(f"**Investment Amount:** €{st.session_state.investment_amount}")
    
    # Display ETF recommendations
    st.markdown("### Top ETF Recommendations")
    if st.session_state.recommendations:
        for etf in st.session_state.recommendations:
            st.markdown(f"""
            <div class="etf-card">
              <div class="etf-match-score">
                <div class="match-value">{etf['matchScore']}%</div>
                <div class="match-label">Match</div>
              </div>
              <div class="etf-details">
                <div class="etf-header">
                  <div class="etf-name">{etf['name']} ({etf['ticker']})</div>
                  <span class="etf-category category-{etf['category'].lower()}">{etf['category']}</span>
                </div>
                <div class="etf-metrics">
                  <div class="metric">
                    <div class="metric-value">{etf['annualReturn']}%</div>
                    <div class="metric-label">Annual Return</div>
                  </div>
                  <div class="metric">
                    <div class="metric-value">{etf['expenseRatio']}%</div>
                    <div class="metric-label">Expense Ratio</div>
                  </div>
                  <div class="metric">
                    <div class="metric-value">{etf['volatility']}%</div>
                    <div class="metric-label">Volatility</div>
                  </div>
                </div>
                <div class="etf-risk">
                  <div class="risk-label">
                    <span>Risk Level</span>
                    <span>{etf['riskLevel']}/10</span>
                  </div>
                  <div class="risk-bar">
                    <div class="risk-level" style="width: {etf['riskLevel']*10}%"></div>
                  </div>
                </div>
              </div>
            </div>
            <hr>
            """, unsafe_allow_html=True)
        # Chart Section: Select a time period and display a bar chart
        st.markdown("### Performance Comparison")
        st.session_state.selected_time_period = st.radio("Select Time Period", ["1M", "3M", "6M", "1Y", "5Y"], index=2)
        chart_df = get_chart_data(st.session_state.recommendations, st.session_state.selected_time_period)
        st.bar_chart(chart_df.set_index("ETF"))
    else:
        st.write("Click **Get Recommendations** to display matching ETFs.")

# --------------------------------------------------------------------
# Learn Tab (Chatbot)
elif tab == "Learn":
    st.header("ETF Learning Assistant")
    st.markdown("<p>Ask me anything about ETFs, investing, or financial concepts.</p>", unsafe_allow_html=True)
    
    # Display chat messages with styling
    for msg in st.session_state.chat_messages:
        if msg["sender"] == "bot":
            st.markdown(f'<div class="message message-bot"><strong>Bot:</strong> {msg["text"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="message message-user"><strong>You:</strong> {msg["text"]}</div>', unsafe_allow_html=True)
    
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("Your Question:")
        if st.form_submit_button("Send") and user_input.strip():
            handle_chat(user_input)

# --------------------------------------------------------------------
# Profile Tab
elif tab == "Profile":
    st.header("My Profile")
    st.markdown("### User Information")
    st.write(f"**Name:** {user_profile['name']}")
    st.write(f"**Email:** {user_profile['email']}")
    st.write(f"**Portfolio Value:** {user_profile['portfolioValue']}")
    st.write(f"**Total Invested:** {user_profile['totalInvested']}")
    st.write(f"**Total Return:** {user_profile['totalReturn']}")
    
    st.markdown("### Portfolio Holdings")
    holdings_df = pd.DataFrame(user_profile["holdings"])
    st.table(holdings_df)
    
    st.markdown("### Your Watchlist")
    watchlist_df = pd.DataFrame(user_profile["watchlist"])
    st.table(watchlist_df)
    
    st.markdown("### Recent Activity")
    activity_df = pd.DataFrame(user_profile["recentActivity"])
    st.table(activity_df)

# Close the main container div
st.markdown("</div>", unsafe_allow_html=True)


