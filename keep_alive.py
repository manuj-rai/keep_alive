import requests
import datetime

# List of URLs to ping (add as many as you want)
URLS = [
    "https://manuj-ecommerce.vercel.app/",
    "https://nova-cart-olive.vercel.app/",
    "https://your-supabase-function-url.supabase.co/function/v1/keepalive"
]

def ping_site(url):
    try:
        response = requests.get(url, timeout=10)
        print(f"[{datetime.datetime.now()}] ✅ {url} - Status: {response.status_code}")
    except Exception as e:
        print(f"[{datetime.datetime.now()}] ❌ {url} - Error: {e}")

def main():
    print(f"=== Pinging {len(URLS)} URLs ===")
    for url in URLS:
        ping_site(url)

if __name__ == "__main__":
    main()
