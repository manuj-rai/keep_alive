import requests
import logging
import sys
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    stream=sys.stdout
)

# List of URLs to ping (add as many as you want)
URLS = [
    "https://trendverse.netlify.app/",
    "https://hair-crezz-salon.vercel.app/",
    "https://gen-ai-qk66.onrender.com/health",
    "https://manuj-rai.vercel.app/",
    "https://manuj-rai.vercel.app/projects",
    "https://kat-katha-web.vercel.app/",
    "https://www.manuj.online/"
]

HEADERS = {"User-Agent": "keep-alive-bot/1.0 (+github-actions)"}
TIMEOUT = 15
MAX_ATTEMPTS = 2
RETRY_DELAY = 3

def ping_site(url):
    """Ping a single URL, retrying once on transient network failure."""
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            if 200 <= response.status_code < 400:
                logging.info(f"✅ {url} - Status: {response.status_code}")
            else:
                logging.warning(f"⚠️  {url} - Status: {response.status_code}")
            return True
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            if attempt < MAX_ATTEMPTS:
                logging.info(f"… {url} - {type(e).__name__}, retrying in {RETRY_DELAY}s")
                time.sleep(RETRY_DELAY)
                continue
            logging.error(f"❌ {url} - Error: {type(e).__name__}")
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

    sys.exit(1 if failed_urls else 0)

if __name__ == "__main__":
    main()
