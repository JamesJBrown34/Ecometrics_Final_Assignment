import streamlit as st
import streamlit.components.v1 as components

# Set the page config for the Streamlit app
st.set_page_config(
    page_title="StudentETF - Smart Investing for Students",
    layout="wide"
)

# Define your full HTML code as a multiline string.
# (Note: The HTML provided in your message appears to be truncated.
#  Make sure to complete it as needed.)
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>StudentETF - Smart Investing for Students</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Open+Sans:wght@400;600&family=Roboto+Mono&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary-blue: #1A2980;
            --primary-teal: #26D0CE;
            --light-gray: #F5F7FA;
            --white: #FFFFFF;
            --coral: #FF6B6B;
            --mint-green: #7CFFCB;
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
        
        body {
            font-family: 'Open Sans', sans-serif;
            color: var(--text-dark);
            background-color: var(--light-gray);
            line-height: 1.6;
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        /* Header Styles */
        header {
            background: linear-gradient(to right, var(--primary-blue), var(--primary-teal));
            color: var(--white);
            padding: 15px 0;
            box-shadow: var(--shadow);
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            display: flex;
            align-items: center;
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
            font-size: 1.5rem;
        }
        
        .logo i {
            margin-right: 8px;
        }
        
        nav ul {
            display: flex;
            list-style: none;
        }
        
        nav ul li {
            margin: 0 15px;
        }
        
        nav ul li a {
            color: var(--white);
            text-decoration: none;
            font-weight: 600;
            padding: 5px 10px;
            border-radius: 4px;
            transition: var(--transition);
        }
        
        nav ul li a:hover, nav ul li a.active {
            background-color: rgba(255, 255, 255, 0.2);
        }
        
        .user-area {
            display: flex;
            align-items: center;
        }
        
        .user-area .notifications {
            margin-right: 15px;
            position: relative;
        }
        
        .user-area .notifications .badge {
            position: absolute;
            top: -5px;
            right: -5px;
            background-color: var(--coral);
            color: var(--white);
            border-radius: 50%;
            width: 16px;
            height: 16px;
            font-size: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .user-avatar {
            width: 35px;
            height: 35px;
            border-radius: 50%;
            background-color: var(--white);
            display: flex;
            justify-content: center;
            align-items: center;
            color: var(--primary-blue);
            font-weight: bold;
        }
        
        /* Hero Section */
        .hero {
            background-color: var(--white);
            padding: 40px 0;
            margin-bottom: 30px;
            box-shadow: var(--shadow);
        }
        
        .hero-content {
            text-align: center;
            max-width: 700px;
            margin: 0 auto;
        }
        
        .hero h1 {
            font-size: 2rem;
            margin-bottom: 10px;
            color: var(--primary-blue);
        }
        
        .hero p {
            color: var(--text-gray);
            margin-bottom: 20px;
        }
        
        .quick-input {
            background-color: var(--light-gray);
            padding: 20px;
            border-radius: var(--radius);
            margin-top: 20px;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            gap: 15px;
        }
        
        .input-group {
            flex: 1;
            min-width: 200px;
        }
        
        .input-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: 600;
            color: var(--text-dark);
        }
        
        .input-group input, .input-group select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: 'Open Sans', sans-serif;
        }
        
        .slider-container {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .slider {
            flex: 1;
            -webkit-appearance: none;
            height: 8px;
            border-radius: 4px;
            background: linear-gradient(to right, var(--low-risk), var(--medium-risk), var(--high-risk));
            outline: none;
        }
        
        .slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: var(--primary-blue);
            cursor: pointer;
        }
        
        .slider-value {
            font-family: 'Roboto Mono', monospace;
            min-width: 30px;
            text-align: center;
        }
        
        .btn {
            padding: 10px 20px;
            border: none;
            border-radius: 30px;
            font-family: 'Montserrat', sans-serif;
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
        
        /* Main Content */
        .main-content {
            display: flex;
            gap: 30px;
            margin-bottom: 40px;
        }
        
        .content-left {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        .content-right {
            width: 300px;
        }
        
        .card {
            background-color: var(--white);
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            padding: 20px;
            transition: var(--transition);
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        }
        
        .section-title {
            font-size: 1.3rem;
            margin-bottom: 15px;
            color: var(--primary-blue);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .section-title i {
            color: var(--primary-teal);
        }
        
        /* Profile Section */
        .profile-card {
            display: flex;
            gap: 20px;
            align-items: center;
        }
        
        .profile-visual {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: linear-gradient(135deg, #7F7FD5, #86A8E7, #91EAE4);
            display: flex;
            justify-content: center;
            align-items: center;
            color: var(--white);
            font-size: 2rem;
        }
        
        .profile-details h3 {
            font-size: 1.5rem;
            margin-bottom: 5px;
        }
        
        .badge {
            display: inline-block;
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--white);
            background-color: var(--primary-teal);
            margin-bottom: 10px;
        }
        
        .profile-stats {
            display: flex;
            gap: 15px;
            margin-top: 10px;
        }
        
        .stat {
            text-align: center;
        }
        
        .stat-value {
            font-family: 'Roboto Mono', monospace;
            font-size: 1.2rem;
            font-weight: 600;
            color: var(--primary-blue);
        }
        
        .stat-label {
            font-size: 0.8rem;
            color: var(--text-gray);
        }
        
        /* ETF Recommendations */
        .recommendations-list {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        
        .etf-card {
            display: flex;
            border-radius: var(--radius);
            overflow: hidden;
            background-color: var(--white);
            box-shadow: var(--shadow);
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
            font-family: 'Montserrat', sans-serif;
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
            color: var(--text-dark);
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
        
        .category-esg {
            background-color: #E8F5E9;
            color: #388E3C;
        }
        
        .etf-metrics {
            display: flex;
            gap: 15px;
            margin-bottom: 15px;
        }
        
        .metric {
            display: flex;
            flex-direction: column;
        }
        
        .metric-value {
            font-family: 'Roboto Mono', monospace;
            font-weight: 600;
        }
        
        .metric-label {
            font-size: 0.8rem;
            color: var(--text-gray);
        }
        
        .etf-risk {
            margin-bottom: 15px;
        }
        
        .risk-label {
            display: flex;
            justify-content: space-between;
            font-size: 0.8rem;
            margin-bottom: 5px;
        }
        
        .risk-bar {
            height: 6px;
            width: 100%;
            background-color: #e0e0e0;
            border-radius: 3px;
            overflow: hidden;
        }
        
        .risk-level {
            height: 100%;
            border-radius: 3px;
        }
        
        .risk-low {
            width: 30%;
            background-color: var(--low-risk);
        }
        
        .risk-medium {
            width: 60%;
            background-color: var(--medium-risk);
        }
        
        .risk-high {
            width: 80%;
            background-color: var(--high-risk);
        }
        
        .etf-actions {
            display: flex;
            gap: 10px;
        }
        
        .btn-secondary {
            background-color: var(--light-gray);
            color: var(--text-dark);
        }
        
        .btn-secondary:hover {
            background-color: #e0e0e0;
        }
        
        .btn-sm {
            padding: 5px 12px;
            font-size: 0.85rem;
        }
        
        /* Additional CSS for performance chart, sidebar, educational banner, footer and mobile responsiveness omitted for brevity */
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container header-container">
            <div class="logo">
                <i class="fas fa-chart-line"></i>
                <span>StudentETF</span>
            </div>
            
            <nav>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#" class="active">Recommendations</a></li>
                    <li><a href="#">Learn</a></li>
                    <li><a href="#">Profile</a></li>
                </ul>
            </nav>
            
            <div class="user-area">
                <div class="notifications">
                    <i class="far fa-bell"></i>
                    <span class="badge">2</span>
                </div>
                <div class="user-avatar">
                    <i class="fas fa-user"></i>
                </div>
            </div>
        </div>
    </header>
    
    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <div class="hero-content">
                <h1>Find ETFs that match your investment style</h1>
                <p>Answer a few questions to get personalized ETF recommendations based on your risk tolerance and investment goals.</p>
                
                <div class="quick-input">
                    <div class="input-group">
                        <label for="risk">Risk Tolerance</label>
                        <div class="slider-container">
                            <input type="range" min="1" max="10" value="6" class="slider" id="risk">
                            <span class="slider-value">6</span>
                        </div>
                    </div>
                    
                    <div class="input-group">
                        <label for="amount">Investment Amount (€)</label>
                        <input type="number" id="amount" placeholder="Enter amount" value="2500">
                    </div>
                    
                    <div class="input-group">
                        <button class="btn btn-primary">Get Recommendations</button>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <!-- Main Content -->
    <div class="container">
        <div class="main-content">
            <div class="content-left">
                <!-- Profile Card -->
                <div class="card">
                    <h2 class="section-title"><i class="fas fa-user-circle"></i> Your Investor Profile</h2>
                    <div class="profile-card">
                        <div class="profile-visual">
                            <i class="fas fa-chart-pie"></i>
                        </div>
                        <div class="profile-details">
                            <h3>Novice Aggressive</h3>
                            <span class="badge">57% of student investors</span>
                            <p>You have limited experience but are willing to take calculated risks for better returns.</p>
                            <div class="profile-stats">
                                <div class="stat">
                                    <div class="stat-value">6/10</div>
                                    <div class="stat-label">Risk Tolerance</div>
                                </div>
                                <div class="stat">
                                    <div class="stat-value">1.5 yrs</div>
                                    <div class="stat-label">Experience</div>
                                </div>
                                <div class="stat">
                                    <div class="stat-value">€2500</div>
                                    <div class="stat-label">Investment</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- ETF Recommendations -->
                <div class="card">
                    <h2 class="section-title"><i class="fas fa-star"></i> Top ETF Recommendations</h2>
                    <div class="recommendations-list">
                        <!-- ETF Card 1 -->
                        <div class="etf-card">
                            <div class="etf-match-score">
                                <div class="match-value">92%</div>
                                <div class="match-label">Match</div>
                            </div>
                            <div class="etf-details">
                                <div class="etf-header">
                                    <div class="etf-name">Iota ETF</div>
                                    <span class="etf-category category-equity">Equity</span>
                                </div>
                                <div class="etf-metrics">
                                    <div class="metric">
                                        <div class="metric-value">12.77%</div>
                                        <div class="metric-label">Annual Return</div>
                                    </div>
                                    <div class="metric">
                                        <div class="metric-value">0.36%</div>
                                        <div class="metric-label">Expense Ratio</div>
                                    </div>
                                    <div class="metric">
                                        <div class="metric-value">12.1%</div>
                                        <div class="metric-label">Volatility</div>
                                    </div>
                                </div>
                                <div class="etf-risk">
                                    <div class="risk-label">
                                        <span>Risk Level</span>
                                        <span>8/10</span>
                                    </div>
                                    <div class="risk-bar">
                                        <div class="risk-level risk-high"></div>
                                    </div>
                                </div>
                                <div class="etf-actions">
                                    <button class="btn btn-sm btn-primary">View Details</button>
                                    <button class="btn btn-sm btn-secondary">Add to Watchlist</button>
                                </div>
                            </div>
                        </div>
                        
                        <!-- ETF Card 2 -->
                        <div class="etf-card">
                            <div class="etf-match-score">
                                <div class="match-value">85%</div>
                                <div class="match-label">Match</div>
                            </div>
                            <div class="etf-details">
                                <div class="etf-header">
                                    <div class="etf-name">Epsilon ETF</div>
                                    <span class="etf-category category-equity">Equity</span>
                                </div>
                                <div class="etf-metrics">
                                    <div class="metric">
                                        <div class="metric-value">2.59%</div>
                                        <div class="metric-label">Annual Return</div>
                                    </div>
                                    <div class="metric">
                                        <div class="metric-value">0.49%</div>
                                        <div class="metric-label">Expense Ratio</div>
                                    </div>
                                    <div class="metric">
                                        <div class="metric-value">6.7%</div>
                                        <div class="metric-label">Volatility</div>
                                    </div>
                                </div>
                                <!-- Additional content for ETF Card 2 can be added here -->
                            </div>
                        </div>
                        
                        <!-- More ETF Cards can be added here -->
                    </div>
                </div>
            </div>
            
            <!-- Optional right sidebar content can be added in .content-right -->
        </div>
    </div>
    
    <!-- Additional sections like Performance Chart, Educational Banner, Footer, etc. can be appended below -->
</body>
</html>
"""

# Use Streamlit's components.html to embed the HTML code.
# Adjust the height and scrolling as needed.
components.html(html_code, height=1500, scrolling=True)





