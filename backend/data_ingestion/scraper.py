import requests
import json
import time
from bs4 import BeautifulSoup

# Base URLs for each CDP
CDP_DOCS = {
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

visited_urls = set()  # Track visited URLs
failed_urls = []  # Log failed URLs
session = requests.Session()  # Maintain session for efficiency

# Function to fetch and parse HTML content
def get_html_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        failed_urls.append(url)
        return None

# Function to extract relevant content
def extract_content(soup):
    content_blocks = soup.find_all(["p", "li", "code", "h1", "h2", "h3", "h4", "pre", "span", "div"])
    return " ".join(block.get_text(strip=True) for block in content_blocks if block.get_text(strip=True))

# Function to extract internal links
def extract_links(base_url, soup):
    links = set()
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"].strip()
        if href.startswith("/") or href.startswith(base_url):
            full_url = href if href.startswith(base_url) else base_url.rstrip("/") + "/" + href.lstrip("/")
            links.add(full_url)
    return links

# Function to scrape a webpage
def scrape_page(url, base_url, depth=0, max_depth=2):
    if url in visited_urls or depth > max_depth:
        return None  # Avoid duplicate scraping or exceeding depth

    print(f"Scraping ({depth}/{max_depth}): {url}")
    visited_urls.add(url)
    time.sleep(1)  # Respectful delay

    html_data = get_html_content(url)
    if not html_data:
        return None

    soup = BeautifulSoup(html_data, "html.parser")

    # Extract content and links
    page_content = extract_content(soup)
    links = extract_links(base_url, soup)

    return {"url": url, "content": page_content, "links": list(links)}

# Main function to scrape all documentation
def scrape_all_docs(max_depth=2):
    all_data = []

    for name, base_url in CDP_DOCS.items():
        print(f"Starting to scrape {name} documentation...")

        main_page_data = scrape_page(base_url, base_url, depth=0, max_depth=max_depth)
        if main_page_data:
            all_data.append(main_page_data)

            for link in main_page_data["links"]:
                page_data = scrape_page(link, base_url, depth=1, max_depth=max_depth)
                if page_data:
                    all_data.append(page_data)

    # Save data to JSON
    with open("scraped_data.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=4, ensure_ascii=False)

    # Save failed URLs
    if failed_urls:
        with open("failed_urls.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(failed_urls))

    print("Scraping complete. Data saved to scraped_data.json")
    if failed_urls:
        print(f"Some URLs failed to scrape. Check failed_urls.txt for details.")

# Run the scraper
if __name__ == "__main__":
    scrape_all_docs(max_depth=2)
