import requests
import datetime
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    stream=sys.stdout
)

# List of URLs to ping (add as many as you want)
URLS = [
    "https://manuj-ecommerce.vercel.app/",
    "https://nova-cart-olive.vercel.app/",
    "https://gen-ai-qk66.onrender.com/health"
]

def ping_site(url):
    """Ping a single URL and log the result"""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            logging.info(f"✅ {url} - Status: {response.status_code}")
            return True
        else:
            logging.warning(f"⚠️  {url} - Status: {response.status_code}")
            return True  # Still counts as successful ping
    except requests.exceptions.Timeout:
        logging.error(f"❌ {url} - Error: Request timeout")
        return False
    except requests.exceptions.ConnectionError:
        logging.error(f"❌ {url} - Error: Connection failed")
        return False
    except Exception as e:
        logging.error(f"❌ {url} - Error: {e}")
        return False

def main():
    """Ping all URLs once (for GitHub Actions)"""
    logging.info(f"{'='*60}")
    logging.info(f"🚀 Starting site keep-alive pings")
    logging.info(f"📍 Pinging {len(URLS)} URLs")
    logging.info(f"{'='*60}\n")
    
    success_count = 0
    failed_urls = []
    
    for url in URLS:
        if ping_site(url):
            success_count += 1
        else:
            failed_urls.append(url)
    
    logging.info(f"\n{'='*60}")
    logging.info(f"📊 Results: {success_count}/{len(URLS)} successful")
    
    if failed_urls:
        logging.warning(f"⚠️  Failed URLs:")
        for url in failed_urls:
            logging.warning(f"   - {url}")
    else:
        logging.info(f"✅ All sites are active!")
    
    logging.info(f"{'='*60}")
    
    # Exit with error code if any pings failed (optional)
    # sys.exit(1 if failed_urls else 0)

if __name__ == "__main__":
    main()
