import requests
import json

def get_random_quote():
    url = "https://api.quotable.io/random"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            quote_data = response.json()
            quote = quote_data['content']
            author = quote_data['author']
            return f'"{quote}" - {author}'
        except json.JSONDecodeError:
            return "Failed to decode JSON response"
    else:
        return "Failed to fetch a quote"

if __name__ == "__main__":
    quote = get_random_quote()
    print(quote)
