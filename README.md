#  CryptoBuddy – Your AI-Powered Financial Sidekick! 

**CryptoBuddy** is a beginner-friendly, rule-based Python chatbot that helps analyze cryptocurrencies based on **profitability** (price trends, market cap) and **sustainability** (energy use, environmental impact). Developed as part of the **PLP Academy – AI for Software Engineering Week 1 Assignment**.

## What Can It Do?

**Sample queries**:
- "Which crypto is trending up?"
- "What's the most sustainable coin?"
- "Is Bitcoin a good investment?"

 **CryptoBuddy replies with**:
- Clear, friendly investment tips based on logical rules.
- Sustainability or profitability-based coin recommendations.
- Disclaimers to encourage personal research.

##  Chatbot Personality

-  **Name**: CryptoBuddy
- **Tone**: Friendly, casual, informative
- **Greeting Example**:
  >  Hey there! I'm CryptoBuddy, your AI-powered financial sidekick! 💸


##  Decision Logic (Rules-Based AI)

###  Profitability Rules
- Recommend cryptos with:
  - `"price_trend" == "rising"`
  - `"market_cap" == "high"`

###  Sustainability Rules
- Recommend cryptos with:
  - `"energy_use" == "low"`
  - `"sustainability_score" > 7`

---

##  Built-in Dataset

```python
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}


#Sample Conversation
text
Copy
Edit
Hey there! I'm CryptoBuddy, your AI-powered financial sidekick! 💸
You: Which crypto is trending up?
CryptoBuddy: Cardano is on the rise and also ranks high in sustainability! A smart move! 📈🌱

You: What's the most sustainable coin?
CryptoBuddy: Cardano! It uses low energy and has a high sustainability score.

You: Is Bitcoin a good investment?
CryptoBuddy: Bitcoin is trending up and has a high market cap, but it consumes a lot of energy. 

#50-Word Summary
CryptoBuddy mimics basic AI reasoning by applying rule-based logic to static crypto data. It analyzes user queries using simple NLP and responds with recommendations based on trend, market cap, and energy use. The project showcases how logic and conditions power early AI systems and lays a foundation for future enhancements.


#Future Improvements
Use real-time crypto data with CoinGecko API

Upgrade NLP using spaCy

Deploy as a chatbot on WhatsApp or Telegram

Add persistent storage (SQLite / Firebase)

Host as a web app using Flask + HTML

#Disclaimer
Crypto is risky — always do your own research before investing! CryptoBuddy is for educational purposes only.

# Author
Jefther Simeon Afuyo
PLP Academy – AI for Software Engineering
afuyojefther@gmail.com

# License
This project is for educational use under the PLP Academy assignment guidelines. Feel free to reuse or modify it for learning purposes only.

