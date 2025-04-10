import React, { useState, useEffect } from 'react';

const StudentETFApp = () => {
  // State variables
  const [activeTab, setActiveTab] = useState('recommendations');
  const [riskTolerance, setRiskTolerance] = useState(6);
  const [investmentAmount, setInvestmentAmount] = useState(2500);
  const [profile, setProfile] = useState('Novice Aggressive');
  const [recommendations, setRecommendations] = useState([]);
  const [selectedTimePeriod, setSelectedTimePeriod] = useState('6M');
  const [currentChatMessage, setCurrentChatMessage] = useState('');
  const [chatMessages, setChatMessages] = useState([
    { sender: 'bot', text: "Hi there! I'm your ETF learning assistant. Ask me anything about ETFs, investing, or financial concepts!" }
  ]);

  // Use useEffect to initialize recommendations
  useEffect(() => {
    // Load initial recommendations
    getRecommendations();
  }, []);

  // Sample ETF data
  const etfs = [
    {
      id: 1,
      name: 'Iota ETF',
      ticker: 'IETF',
      category: 'Equity',
      annualReturn: 12.77,
      expenseRatio: 0.36,
      volatility: 12.1,
      riskLevel: 8,
      matchScore: 92,
      returns: { '1M': 1.2, '3M': 3.6, '6M': 6.8, '1Y': 12.77, '5Y': 64.3 }
    },
    {
      id: 2,
      name: 'Epsilon ETF',
      ticker: 'EPSN',
      category: 'Equity',
      annualReturn: 2.59,
      expenseRatio: 0.49,
      volatility: 6.7,
      riskLevel: 7,
      matchScore: 85,
      returns: { '1M': 0.1, '3M': 0.8, '6M': 1.4, '1Y': 2.59, '5Y': 13.5 }
    },
    {
      id: 3,
      name: 'Alpha ETF',
      ticker: 'ALFA',
      category: 'Bond',
      annualReturn: 9.77,
      expenseRatio: 0.26,
      volatility: 8.5,
      riskLevel: 5,
      matchScore: 75,
      returns: { '1M': 0.7, '3M': 2.3, '6M': 4.7, '1Y': 9.77, '5Y': 48.2 }
    },
    {
      id: 4,
      name: 'Delta ETF',
      ticker: 'DTEF',
      category: 'Mixed',
      annualReturn: 8.25,
      expenseRatio: 0.31,
      volatility: 7.9,
      riskLevel: 6,
      matchScore: 70,
      returns: { '1M': 0.9, '3M': 2.5, '6M': 4.1, '1Y': 8.25, '5Y': 42.8 }
    }
  ];

  // User profile data
  const userProfile = {
    name: "Alex Johnson",
    email: "alex.j@university.edu",
    portfolioValue: "€3,742.50",
    totalInvested: "€3,500.00",
    totalReturn: "€242.50 (6.93%)",
    watchlist: [
      { name: "Delta ETF", ticker: "DTEF", change: "+2.4%" },
      { name: "Sigma ETF", ticker: "SGETF", change: "-0.7%" },
      { name: "Omega ETF", ticker: "OMGA", change: "+1.2%" }
    ],
    recentActivity: [
      { date: "Oct 5, 2024", action: "Purchased Alpha ETF", amount: "€500.00" },
      { date: "Sept 28, 2024", action: "Dividend Payment", amount: "€12.75" },
      { date: "Sept 15, 2024", action: "Purchased Iota ETF", amount: "€750.00" }
    ],
    holdings: [
      { name: "Alpha ETF", ticker: "ALFA", shares: "12.5", value: "€1,221.75", allocation: "32.6%" },
      { name: "Iota ETF", ticker: "IETF", shares: "18.2", value: "€2,243.40", allocation: "59.9%" },
      { name: "Cash", ticker: "-", shares: "-", value: "€277.35", allocation: "7.5%" }
    ]
  };

  // Expanded chatbot responses
  const chatbotResponses = {
    "what is an etf": "An ETF (Exchange-Traded Fund) is an investment fund that trades on stock exchanges, much like stocks. ETFs hold assets such as stocks, bonds, or commodities, and trade at market-determined prices. They typically have higher daily liquidity and lower fees than mutual funds, making them attractive for individual investors.",
    "what exactly is an etf": "An ETF (Exchange-Traded Fund) is an investment fund that trades on stock exchanges, much like stocks. ETFs hold assets such as stocks, bonds, or commodities, and trade at market-determined prices. They typically have higher daily liquidity and lower fees than mutual funds, making them attractive for individual investors.",
    "how do etfs work": "ETFs work by pooling money from many investors to buy a diversified portfolio of assets. When you buy shares of an ETF, you're buying a small portion of the entire portfolio. ETFs trade throughout the day like stocks, with prices that fluctuate based on supply and demand. Most ETFs are designed to track an index, sector, commodity, or other asset but can be bought and sold like a common stock.",
    "what are the benefits of etfs": "ETFs offer several advantages: 1) Diversification - instant exposure to many stocks or bonds, 2) Low costs - typically lower expense ratios than mutual funds, 3) Tax efficiency - generally trigger fewer capital gains, 4) Liquidity - can be bought and sold throughout the trading day, 5) Transparency - holdings are disclosed daily, and 6) Flexibility - can be used for various investment strategies including long-term investing.",
    "what's the difference between etfs and mutual funds": "The main differences between ETFs and mutual funds are: 1) Trading - ETFs trade like stocks throughout the day while mutual funds trade once per day after market close, 2) Fees - ETFs typically have lower expense ratios, 3) Tax efficiency - ETFs are usually more tax-efficient, 4) Minimum investment - ETFs have no minimums beyond the share price, while mutual funds often require minimum investments, and 5) Management style - most ETFs are passively managed while mutual funds are often actively managed.",
    "what are index etfs": "Index ETFs are exchange-traded funds designed to track a specific market index, such as the S&P 500 or NASDAQ. They aim to replicate the performance of their target index by holding all (or a representative sample) of the securities in the index. Index ETFs offer low-cost diversification and typically have lower expense ratios than actively managed funds because they simply follow an index rather than paying managers to select investments.",
    "what are the risks of etfs": "The main risks of ETFs include: 1) Market risk - ETF prices fluctuate with their underlying assets, 2) Tracking error risk - some ETFs may not perfectly match their benchmark index, 3) Liquidity risk - some specialized ETFs may have lower trading volumes, 4) Concentration risk - sector or country-specific ETFs lack broad diversification, 5) Currency risk - international ETFs may be affected by exchange rate fluctuations, and 6) Trading costs - frequent buying and selling can add costs through bid-ask spreads and commissions.",
    "how do i buy an etf": "You can buy ETFs through most brokerage accounts, including traditional brokers and online platforms. The process is similar to buying stocks: 1) Open a brokerage account if you don't have one, 2) Fund your account, 3) Research ETFs that match your investment goals, 4) Place an order using the ETF's ticker symbol, and 5) Specify the number of shares or amount you wish to invest. ETFs trade at market prices throughout the trading day, so you can buy them whenever the market is open.",
    "what is an expense ratio": "An expense ratio is the annual fee that ETFs and mutual funds charge shareholders for managing the fund. It's expressed as a percentage of the fund's average net assets. For example, an expense ratio of 0.5% means that for every $1,000 invested, you pay $5 annually in fees. ETFs typically have lower expense ratios than mutual funds, especially passive index ETFs. The expense ratio is important because higher fees directly reduce your investment returns over time.",
    "how are etfs taxed": "ETFs are generally more tax-efficient than mutual funds. When you hold ETFs: 1) Dividends and capital gain distributions are taxable in the year they're received, 2) When you sell ETF shares at a profit, you'll owe capital gains tax based on how long you held them (short-term or long-term rates), 3) ETFs typically generate fewer capital gain distributions than mutual funds due to their unique creation/redemption process, making them more tax-efficient for long-term investors. Tax laws vary by country, so consult a tax professional for specific advice.",
    "what is the difference between active and passive etfs": "Passive ETFs aim to track a specific index or benchmark, while active ETFs have portfolio managers who make investment decisions to try to outperform the market. Key differences: 1) Management style - passive ETFs follow a rules-based approach while active ETFs rely on manager expertise, 2) Expense ratios - passive ETFs typically have lower fees than active ETFs, 3) Trading activity - active ETFs generally have higher turnover, 4) Performance goals - passive ETFs seek to match their benchmark's performance, while active ETFs aim to exceed it, and 5) Transparency - passive ETFs disclose holdings daily, while some active ETFs may disclose less frequently.",
    "what are the different types of etfs": "The main types of ETFs include: 1) Stock (equity) ETFs - track stock indices, sectors, or investment strategies, 2) Bond (fixed income) ETFs - invest in government, corporate, or municipal bonds, 3) Commodity ETFs - track physical commodities like gold or oil, 4) Currency ETFs - track currency values or baskets of currencies, 5) Specialty ETFs - focus on specific themes like ESG (Environmental, Social, Governance), 6) Inverse ETFs - aim to profit from market declines, 7) Leveraged ETFs - use financial derivatives to amplify returns, and 8) International ETFs - focus on global or country-specific markets outside your home country.",
    "are etfs good for beginners": "Yes, ETFs can be excellent investment vehicles for beginners for several reasons: 1) Instant diversification - a single ETF can give you exposure to hundreds of securities, reducing risk, 2) Low minimum investment - you can start with just the price of one share, 3) Simplicity - index ETFs are straightforward to understand compared to selecting individual stocks, 4) Low costs - many ETFs have very low expense ratios, 5) Liquidity - easy to buy and sell when needed, and 6) Variety - you can start with broad market ETFs and gradually add more specific ones as you learn. For beginners, broad-based index ETFs are often recommended as a core investment."
  };

  // Functions
  const handleRiskChange = (e) => {
    setRiskTolerance(parseInt(e.target.value));
  };

  const handleAmountChange = (e) => {
    setInvestmentAmount(parseInt(e.target.value));
  };

  const getRecommendations = () => {
    // In a real app, this would filter and sort ETFs based on risk tolerance and investment amount
    // For now, show all ETFs but with different filtering based on risk tolerance
    let filteredEtfs = [...etfs];
    
    if (riskTolerance < 4) {
      // Conservative investors prefer bonds and lower volatility
      filteredEtfs = filteredEtfs.filter(etf => etf.category === 'Bond' || etf.riskLevel < 6);
    } else if (riskTolerance > 7) {
      // Aggressive investors prefer higher return potential
      filteredEtfs = filteredEtfs.filter(etf => etf.annualReturn > 5);
    }
    
    // Sort by match score
    filteredEtfs.sort((a, b) => b.matchScore - a.matchScore);
    
    setRecommendations(filteredEtfs);
    
    // Update profile based on risk tolerance
    if (riskTolerance <= 4) {
      setProfile(investmentAmount > 3000 ? 'Experienced Conservative' : 'Novice Conservative');
    } else if (riskTolerance <= 7) {
      setProfile(investmentAmount > 3000 ? 'Experienced Moderate' : 'Novice Moderate');
    } else {
      setProfile(investmentAmount > 3000 ? 'Experienced Aggressive' : 'Novice Aggressive');
    }
  };

  const handleChatSubmit = (e) => {
    e.preventDefault();
    
    if (!currentChatMessage.trim()) return;
    
    // Add user message
    const userMessage = currentChatMessage;
    setChatMessages([...chatMessages, { sender: 'user', text: userMessage }]);
    setCurrentChatMessage(''); // Clear input immediately for better UX
    
    // Find bot response
    setTimeout(() => {
      const query = userMessage.toLowerCase();
      let botResponse = "I'm not sure about that. Could you try asking about ETFs, investment basics, or risk profiles?";
      
      // Check for exact matches first
      if (chatbotResponses[query]) {
        botResponse = chatbotResponses[query];
      } else {
        // Check for key phrases
        const keyPhraseMatches = {
          "what": {
            "etf": "what is an etf",
            "exactly": "what exactly is an etf",
            "index": "what are index etfs",
            "risk": "what are the risks of etfs",
            "expense ratio": "what is an expense ratio",
            "type": "what are the different types of etfs",
            "different type": "what are the different types of etfs",
            "active and passive": "what is the difference between active and passive etfs"
          },
          "how": {
            "work": "how do etfs work",
            "buy": "how do i buy an etf",
            "purchase": "how do i buy an etf",
            "tax": "how are etfs taxed"
          },
          "benefit": {
            "": "what are the benefits of etfs"
          },
          "advantage": {
            "etf": "what are the benefits of etfs"
          },
          "difference": {
            "mutual fund": "what's the difference between etfs and mutual funds",
            "active": "what is the difference between active and passive etfs",
            "passive": "what is the difference between active and passive etfs"
          },
          "vs": {
            "mutual": "what's the difference between etfs and mutual funds"
          },
          "beginner": {
            "": "are etfs good for beginners"
          },
          "new": {
            "investor": "are etfs good for beginners"
          }
        };
        
        // Check if query contains multiple key phrases
        let matched = false;
        Object.entries(keyPhraseMatches).forEach(([primaryKey, secondaryMatches]) => {
          if (query.includes(primaryKey) && !matched) {
            Object.entries(secondaryMatches).forEach(([secondaryKey, responseKey]) => {
              if ((secondaryKey === "" || query.includes(secondaryKey)) && !matched) {
                botResponse = chatbotResponses[responseKey];
                matched = true;
              }
            });
          }
        });
      }
      
      setChatMessages(prev => [...prev, { sender: 'bot', text: botResponse }]);
    }, 600);
  };

  // Helper functions
  const getRiskLevelClass = (riskLevel) => {
    if (riskLevel <= 3) return "risk-low";
    if (riskLevel <= 6) return "risk-medium";
    return "risk-high";
  };
  
  const getExpectedReturns = (etf, period) => {
    return etf.returns[period];
  };
  
  // Chart data based on selected time period
  const getChartData = () => {
    return recommendations.map(etf => ({
      name: etf.name,
      return: getExpectedReturns(etf, selectedTimePeriod),
      color: etf.id === 1 ? '#1976D2' : 
             etf.id === 2 ? '#7B1FA2' : 
             etf.id === 3 ? '#FFA000' : '#388E3C'
    }));
  };

  // Render navigation
  const renderNavigation = () => (
    <header>
      <div className="logo">
        <span className="logo-icon">📈</span> Fintro
      </div>
      <div className="nav-links">
        <div 
          className={`nav-link ${activeTab === 'recommendations' ? 'active' : ''}`}
          onClick={() => setActiveTab('recommendations')}
        >
          Recommendations
        </div>
        <div 
          className={`nav-link ${activeTab === 'learn' ? 'active' : ''}`}
          onClick={() => setActiveTab('learn')}
        >
          Learn
        </div>
        <div 
          className={`nav-link ${activeTab === 'profile' ? 'active' : ''}`}
          onClick={() => setActiveTab('profile')}
        >
          My Profile
        </div>
      </div>
    </header>
  );

  // Render tabs
  const renderRecommendationsTab = () => (
    <>
      <div className="hero">
        <h1>Find ETFs that match your investment style with Fintro</h1>
        <p>Answer a few questions to get personalized ETF recommendations based on your risk tolerance and investment goals.</p>
        
        <div className="input-panel">
          <div className="input-group">
            <label htmlFor="risk">Risk Tolerance (1-10)</label>
            <div className="slider-container">
              <input 
                type="range" 
                min="1" 
                max="10" 
                value={riskTolerance} 
                onChange={handleRiskChange}
                className="slider" 
                id="risk"
              />
              <span className="slider-value">{riskTolerance}</span>
            </div>
          </div>
          
          <div className="input-group">
            <label htmlFor="amount">Investment Amount (€)</label>
            <input 
              type="number" 
              id="amount" 
              value={investmentAmount}
              onChange={handleAmountChange}
              min="100"
              step="100"
            />
          </div>
          
          <div className="input-group" style={{ flex: 'none' }}>
            <button className="btn btn-primary" onClick={getRecommendations}>
              Get Recommendations
            </button>
          </div>
        </div>
      </div>
      
      <div className="main-content">
        <div className="content-left">
          {/* Profile Card */}
          <div className="card">
            <h2 className="section-title">
              <span className="section-icon">👤</span> Your Investor Profile
            </h2>
            <div className="profile-card">
              <div className="profile-visual">📊</div>
              <div className="profile-details">
                <h3>{profile}</h3>
                <span className="profile-badge">
                  {profile === 'Novice Conservative' ? '11.8%' : 
                   profile === 'Novice Moderate' ? '35.2%' :
                   profile === 'Novice Aggressive' ? '27.0%' :
                   profile === 'Experienced Conservative' ? '5.5%' : 
                   profile === 'Experienced Moderate' ? '10.3%' : '10.2%'} of students
                </span>
                <p>{profile === 'Novice Conservative' ? 'You prefer stability and are cautious with your investments.' :
                    profile === 'Novice Moderate' ? 'You seek a balance between risk and return with limited investment experience.' :
                    profile === 'Novice Aggressive' ? 'You have limited experience but are willing to take calculated risks for better returns.' :
                    profile === 'Experienced Conservative' ? 'Despite your experience, you prefer consistent returns over high-risk opportunities.' :
                    profile === 'Experienced Moderate' ? 'You have investment experience and prefer a balanced approach to risk and return.' :
                    'You have investment experience and are comfortable with higher risk for potentially greater returns.'}</p>
                <div className="profile-stats">
                  <div className="stat">
                    <div className="stat-value">{riskTolerance}/10</div>
                    <div className="stat-label">Risk</div>
                  </div>
                  <div className="stat">
                    <div className="stat-value">{profile.includes('Experienced') ? '3+ yrs' : '0-2 yrs'}</div>
                    <div className="stat-label">Experience</div>
                  </div>
                  <div className="stat">
                    <div className="stat-value">€{investmentAmount}</div>
                    <div className="stat-label">Investment</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          {/* ETF Recommendations */}
          <div className="card">
            <h2 className="section-title">
              <span className="section-icon">⭐</span> Top ETF Recommendations
            </h2>
            <div className="recommendations-list">
              {recommendations.length > 0 ? (
                recommendations.map(etf => (
                  <div className="etf-card" key={etf.id}>
                    <div className="etf-match-score">
                      <div className="match-value">{etf.matchScore}%</div>
                      <div className="match-label">Match</div>
                    </div>
                    <div className="etf-details">
                      <div className="etf-header">
                        <div className="etf-name">{etf.name} ({etf.ticker})</div>
                        <span className={`etf-category category-${etf.category.toLowerCase()}`}>{etf.category}</span>
                      </div>
                      <div className="etf-metrics">
                        <div className="metric">
                          <div className="metric-value">{etf.annualReturn}%</div>
                          <div className="metric-label">Annual Return</div>
                        </div>
                        <div className="metric">
                          <div className="metric-value">{etf.expenseRatio}%</div>
                          <div className="metric-label">Expense Ratio</div>
                        </div>
                        <div className="metric">
                          <div className="metric-value">{etf.volatility}%</div>
                          <div className="metric-label">Volatility</div>
                        </div>
                      </div>
                      <div className="etf-risk">
                        <div className="risk-label">
                          <span>Risk Level</span>
                          <span>{etf.riskLevel}/10</span>
                        </div>
                        <div className="risk-bar">
                          <div 
                            className={`risk-level ${getRiskLevelClass(etf.riskLevel)}`}
                            style={{ width: `${etf.riskLevel*10}%` }}
                          ></div>
                        </div>
                      </div>
                    </div>
                  </div>
                ))
              ) : (
                <p>Click "Get Recommendations" to see ETFs that match your profile.</p>
              )}
            </div>
          </div>
          
          {/* Chart Section */}
          {recommendations.length > 0 && (
            <div className="card">
              <h2 className="section-title">
                <span className="section-icon">📊</span> Performance Comparison
              </h2>
              <div className="chart-container">
                <div className="time-filters">
                  <div 
                    className={`time-filter ${selectedTimePeriod === '1M' ? 'active' : ''}`}
                    onClick={() => setSelectedTimePeriod('1M')}
                  >1M</div>
                  <div 
                    className={`time-filter ${selectedTimePeriod === '3M' ? 'active' : ''}`}
                    onClick={() => setSelectedTimePeriod('3M')}
                  >3M</div>
                  <div 
                    className={`time-filter ${selectedTimePeriod === '6M' ? 'active' : ''}`}
                    onClick={() => setSelectedTimePeriod('6M')}
                  >6M</div>
                  <div 
                    className={`time-filter ${selectedTimePeriod === '1Y' ? 'active' : ''}`}
                    onClick={() => setSelectedTimePeriod('1Y')}
                  >1Y</div>
                  <div 
                    className={`time-filter ${selectedTimePeriod === '5Y' ? 'active' : ''}`}
                    onClick={() => setSelectedTimePeriod('5Y')}
                  >5Y</div>
                </div>
                
                <div className="chart">
                  <div className="returns-data">
                    <h3>Expected Returns ({selectedTimePeriod})</h3>
                    {recommendations.map(etf => (
                      <div className="return-item" key={etf.id}>
                        <span className="return-etf">{etf.name}:</span>
                        <span className={getExpectedReturns(etf, selectedTimePeriod) >= 0 ? 'positive' : 'negative'}>
                          {getExpectedReturns(etf, selectedTimePeriod) >= 0 ? '+' : ''}
                          {getExpectedReturns(etf, selectedTimePeriod)}%
                        </span>
                      </div>
                    ))}
                  </div>
                  
                  <div className="chart-visual">
                    <svg width="100%" height="250">
                      <rect x="0" y="0" width="100%" height="100%" fill="#f9f9f9" />
                      <line x1="50" y1="220" x2="550" y2="220" stroke="#333" strokeWidth="1" />
                      <line x1="50" y1="30" x2="50" y2="220" stroke="#333" strokeWidth="1" />
                      
                      {getChartData().map((etfData, index) => {
                        const maxHeight = 190;
                        const returnValue = etfData.return;
                        const maxReturn = Math.max(...getChartData().map(d => d.return));
                        const height = Math.max(Math.abs(returnValue) / maxReturn * maxHeight, 10);
                        
                        return (
                          <g key={index}>
                            <rect 
                              x={100 + index * 120} 
                              y={220 - height}
                              width="80" 
                              height={height}
                              fill={etfData.color}
                              opacity="0.8"
                            />
                            <text
                              x={140 + index * 120}
                              y={235}
                              textAnchor="middle"
                              fontSize="12"
                              fill="#333"
                            >
                              {etfData.name.split(' ')[0]}
                            </text>
                            <text
                              x={140 + index * 120}
                              y={220 - height - 10}
                              textAnchor="middle"
                              fontSize="12"
                              fill="#333"
                              fontWeight="bold"
                            >
                              {returnValue}%
                            </text>
                          </g>
                        );
                      })}
                    </svg>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </>
  );

  const renderLearnTab = () => (
    <div className="learn-container">
      <div className="chat-container">
        <div className="chat-header">
          <span className="chat-header-icon">🤖</span>
          <h2>ETF Learning Assistant</h2>
        </div>
        
        <div className="chat-messages">
          {chatMessages.map((msg, index) => (
            <div 
              key={index} 
              className={`message message-${msg.sender}`}
            >
              {msg.text}
            </div>
          ))}
        </div>
        
        <form className="chat-form" onSubmit={handleChatSubmit}>
          <input 
            type="text" 
            className="chat-input" 
            placeholder="Ask me anything about ETFs..."
            value={currentChatMessage}
            onChange={(e) => setCurrentChatMessage(e.target.value)}
          />
          <button type="submit" className="chat-submit">➤</button>
        </form>
      </div>
      
      <div className="faq-container">
                    <h3 className="faq-title">Frequently Asked Questions</h3>
        <div className="faq-card">
          <div className="faq-question">What is an ETF?</div>
          <p>An ETF (Exchange-Traded Fund) is an investment fund that trades on stock exchanges, much like stocks. They typically have lower fees than mutual funds.</p>
        </div>
        
        <div className="faq-card">
          <div className="faq-question">How do I choose an ETF?</div>
          <p>Consider your goals, risk tolerance, the sector the ETF tracks, expense ratio, liquidity, and the fund provider's reputation.</p>
        </div>
        
        <div className="faq-card">
          <div className="faq-question">What's the difference between ETFs and mutual funds?</div>
          <p>ETFs trade throughout the day like stocks, while mutual funds trade once at market close. ETFs typically have lower fees and more tax efficiency.</p>
        </div>
        
        <div className="faq-card">
          <div className="faq-question">How do ETFs work?</div>
          <p>ETFs work by pooling money from investors to buy a portfolio of assets. Most ETFs track an index, but some are actively managed.</p>
        </div>
        
        <div className="suggested-questions">
          <h4>Try asking:</h4>
          <div className="question-chips">
            <div className="question-chip" onClick={() => {
              setCurrentChatMessage("What exactly is an ETF?");
              handleChatSubmit({ preventDefault: () => {} });
            }}>What exactly is an ETF?</div>
            <div className="question-chip" onClick={() => {
              setCurrentChatMessage("How do ETFs work?");
              handleChatSubmit({ preventDefault: () => {} });
            }}>How do ETFs work?</div>
            <div className="question-chip" onClick={() => {
              setCurrentChatMessage("What are the benefits of ETFs?");
              handleChatSubmit({ preventDefault: () => {} });
            }}>What are the benefits of ETFs?</div>
            <div className="question-chip" onClick={() => {
              setCurrentChatMessage("What are the risks of ETFs?");
              handleChatSubmit({ preventDefault: () => {} });
            }}>What are the risks of ETFs?</div>
            <div className="question-chip" onClick={() => {
              setCurrentChatMessage("Are ETFs good for beginners?");
              handleChatSubmit({ preventDefault: () => {} });
            }}>Are ETFs good for beginners?</div>
            <div className="question-chip" onClick={() => {
              setCurrentChatMessage("What is an expense ratio?");
              handleChatSubmit({ preventDefault: () => {} });
            }}>What is an expense ratio?</div>
          </div>
        </div>
      </div>
    </div>
  );

  const renderProfileTab = () => (
    <div className="profile-page">
      <div className="profile-header">
        <div className="user-info-card">
          <div className="user-avatar-large">👤</div>
          <h2 className="user-name">{userProfile.name}</h2>
          <p className="user-email">{userProfile.email}</p>
          
          <div className="user-info-list">
            <div className="info-item">
              <span className="info-label">Portfolio Value:</span>
              <span className="info-value">{userProfile.portfolioValue}</span>
            </div>
            <div className="info-item">
              <span className="info-label">Total Invested:</span>
              <span className="info-value">{userProfile.totalInvested}</span>
            </div>
            <div className="info-item">
              <span className="info-label">Total Return:</span>
              <span className="info-value green">{userProfile.totalReturn}</span>
            </div>
          </div>
        </div>
        
        <div className="profile-stats-cards">
          <div className="stat-card">
            <div className="stat-icon">💰</div>
            <div className="stat-value">3</div>
            <div className="stat-label">ETFs Owned</div>
          </div>
          <div className="stat-card">
            <div className="stat-icon">📈</div>
            <div className="stat-value">6.93%</div>
            <div className="stat-label">Total Return</div>
          </div>
          <div className="stat-card">
            <div className="stat-icon">⭐</div>
            <div className="stat-value">7/10</div>
            <div className="stat-label">Risk Profile</div>
          </div>
        </div>
      </div>
      
      <div className="portfolio-section">
        <div className="portfolio-card">
          <h3 className="section-header">Portfolio Holdings</h3>
          <table className="portfolio-table">
            <thead>
              <tr>
                <th>ETF Name</th>
                <th>Ticker</th>
                <th>Shares</th>
                <th>Value</th>
                <th>Allocation</th>
              </tr>
            </thead>
            <tbody>
              {userProfile.holdings.map((item, index) => (
                <tr key={index}>
                  <td>{item.name}</td>
                  <td className="ticker">{item.ticker}</td>
                  <td>{item.shares}</td>
                  <td>{item.value}</td>
                  <td>
                    <div className="allocation-bar-container">
                      <div 
                        className="allocation-bar" 
                        style={{width: item.allocation}}
                      ></div>
                      <span>{item.allocation}</span>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        
        <div className="portfolio-columns">
          <div className="watchlist-section">
            <h3 className="section-header">Your Watchlist</h3>
            <table className="watchlist-table">
              <thead>
                <tr>
                  <th>ETF Name</th>
                  <th>Ticker</th>
                  <th>Change</th>
                </tr>
              </thead>
              <tbody>
                {userProfile.watchlist.map((item, index) => (
                  <tr key={index}>
                    <td>{item.name}</td>
                    <td className="ticker">{item.ticker}</td>
                    <td className={item.change.startsWith('+') ? 'change-positive' : 'change-negative'}>
                      {item.change}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          
          <div className="activity-section">
            <h3 className="section-header">Recent Activity</h3>
            <table className="activity-table">
              <thead>
                <tr>
                  <th>Date</th>
                  <th>Action</th>
                  <th>Amount</th>
                </tr>
              </thead>
              <tbody>
                {userProfile.recentActivity.map((item, index) => (
                  <tr key={index}>
                    <td>{item.date}</td>
                    <td>{item.action}</td>
                    <td>{item.amount}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );

  return (
    <div className="app-container">
      {/* Navigation */}
      {/* App Title in Browser Tab */}
      <title>Fintro - Learn About ETFs</title>
      
      {renderNavigation()}
      
      {/* Main Content */}
      {activeTab === 'recommendations' && renderRecommendationsTab()}
      {activeTab === 'learn' && renderLearnTab()}
      {activeTab === 'profile' && renderProfileTab()}
      
      {/* CSS Styles */}
      <style>
        {`
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
          
          /* Main Content */
          .main-content {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
            flex-wrap: wrap;
          }
          
          .content-left {
            flex: 1;
            min-width: 300px;
          }
          
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
          
          /* Profile Card */
          .profile-card {
            display: flex;
            gap: 20px;
            align-items: center;
          }
          
          .profile-visual {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background: linear-gradient(135deg, #7F7FD5, #86A8E7, #91EAE4);
            display: flex;
            justify-content: center;
            align-items: center;
            color: var(--white);
            font-size: 2rem;
          }
          
          .profile-details h3 {
            font-size: 1.3rem;
            margin-bottom: 5px;
          }
          
          .profile-badge {
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
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--primary-blue);
          }
          
          .stat-label {
            font-size: 0.8rem;
            color: var(--text-gray);
          }
          
          /* ETF Cards */
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
          
          .category-esg-focused {
            background-color: #E8F5E9;
            color: #388E3C;
          }
          
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
          
          .risk-low {
            background-color: var(--low-risk);
          }
          
          .risk-medium {
            background-color: var(--medium-risk);
          }
          
          .risk-high {
            background-color: var(--high-risk);
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
          
          .chart {
            display: flex;
            gap: 20px;
          }
          
          .returns-data {
            width: 200px;
          }
          
          .returns-data h3 {
            font-size: 1rem;
            margin-bottom: 10px;
            color: var(--text-dark);
          }
          
          .return-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
            font-size: 0.9rem;
          }
          
          .return-etf {
            font-weight: 600;
          }
          
          .positive {
            color: var(--low-risk);
            font-weight: 600;
          }
          
          .negative {
            color: var(--high-risk);
            font-weight: 600;
          }
          
          .chart-visual {
            flex: 1;
          }
          
          /* Learn Tab */
          .learn-container {
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
          }
          
          .chat-container {
            flex: 1;
            min-width: 300px;
            background-color: white;
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            display: flex;
            flex-direction: column;
            height: 600px;
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
            position: relative;
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
          
          .faq-container {
            flex: 1;
            min-width: 300px;
            display: flex;
            flex-direction: column;
            gap: 15px;
          }

          .faq-title {
            font-size: 1.3rem;
            color: var(--primary-blue);
            margin-bottom: 10px;
          }
          
          .faq-card {
            background-color: white;
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            padding: 15px;
            transition: var(--transition);
          }
          
          .faq-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
          }
          
          .faq-question {
            font-weight: 600;
            margin-bottom: 8px;
            color: var(--primary-blue);
          }

          .suggested-questions {
            background-color: white;
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            padding: 15px;
          }

          .suggested-questions h4 {
            font-size: 1rem;
            margin-bottom: 10px;
            color: var(--text-dark);
          }

          .question-chips {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
          }

          .question-chip {
            background-color: #f0f0f0;
            padding: 8px 12px;
            border-radius: 16px;
            font-size: 0.85rem;
            cursor: pointer;
            transition: var(--transition);
          }

          .question-chip:hover {
            background-color: var(--primary-teal);
            color: white;
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
        `}
      </style>
    </div>
  );
};

export default StudentETFApp;



