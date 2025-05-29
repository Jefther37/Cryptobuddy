import nltk
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK data only once
nltk.download("punkt_tab")
nltk.download('stopwords')

# Chatbot personality
print("Hey there! I'm CryptoBuddy, your AI-powered financial sidekick!")
print("Ask me anything like 'Which crypto is trending up?' or 'What's the most sustainable coin?'")
print("Type 'exit' anytime to leave.\n")

# Sample crypto dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3 / 10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6 / 10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8 / 10
    }
}

# Optional: Function to get real-time price (CoinGecko API)
def get_price(coin_name):
    try:
        coin_id = coin_name.lower()
        response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd")
        data = response.json()
        price = data[coin_id]['usd']
        return f" The current price of {coin_name.capitalize()} is ${price}"
    except:
        return "Sorry, I couldn't fetch the live price at the moment."

# NLP Preprocessing
stop_words = set(stopwords.words('english'))

def clean_query(query):
    tokens = word_tokenize(query.lower())
    return [word for word in tokens if word.isalnum() and word not in stop_words]

# Chatbot main logic
def crypto_buddy():
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("CryptoBuddy: See you later! Stay smart and invest wisely!")
            break

        cleaned = clean_query(user_input)

        if "sustainable" in cleaned or "eco" in cleaned or "green" in cleaned:
            coin = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            print(f"CryptoBuddy: {coin} is your best bet! It's energy-efficient and has long-term potential.")
        elif "trending" in cleaned or "rising" in cleaned or "profitable" in cleaned:
            trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["market_cap"] in ["high", "medium"]]
            if trending:
                print(f"CryptoBuddy:  These are rising stars right now: {', '.join(trending)}")
            else:
                print("CryptoBuddy: Nothing is strongly trending up right now.")
        elif "price" in cleaned:
            for coin in crypto_db:
                if coin.lower() in cleaned:
                    print("CryptoBuddy:", get_price(coin.lower()))
                    break
            else:
                print("CryptoBuddy: Please specify which crypto's price you want to check.")
        elif "recommend" in cleaned or "buy" in cleaned:
            coin = max(crypto_db, key=lambda x: (crypto_db[x]["price_trend"] == "rising", crypto_db[x]["market_cap"], crypto_db[x]["sustainability_score"]))
            print(f"CryptoBuddy: I'd recommend looking into {coin} — it's on the rise and eco-friendlier than most!")
        else:
            print("CryptoBuddy:  I'm not sure how to help with that yet. Try asking about trends, prices, or sustainability!")

# Run bot
if __name__ == "__main__":
    crypto_buddy()

