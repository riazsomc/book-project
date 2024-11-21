import requests
from bs4 import BeautifulSoup
import time

def scrape_ebanglalibrary_article(url):
    """
    Scrapes the main content from an eBanglaLibrary article.
    
    Parameters:
        url (str): The URL of the article to scrape.
    
    Returns:
        tuple: A tuple containing the article title and its text content.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the article title
        title_tag = soup.find('h1', class_='entry-title')
        title = title_tag.get_text(strip=True) if title_tag else 'No Title Found'

        # Extract the article content
        content = ''
        content_div = soup.find('div', class_='entry-content')
        if content_div:
            # Iterate over all child elements within the content div
            for element in content_div.children:
                if element.name == 'p':
                    content += element.get_text(strip=True) + '\n\n'
                elif element.name == 'h2':
                    content += element.get_text(strip=True) + '\n\n'
                elif element.name == 'ul':
                    for li in element.find_all('li'):
                        content += '- ' + li.get_text(strip=True) + '\n'
                    content += '\n'
        else:
            content = 'No content found.'

        return title, content.strip()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the article: {e}")
        return None, None

def save_to_consolidated_file(content, title, filename="consolidated_ebanglalibrary.txt"):
    """
    Appends the article's text content to a consolidated file with its title as a header.
    
    Parameters:
        content (str): The article's text content.
        title (str): The article's title.
        filename (str): The name of the consolidated file. Default is "consolidated_ebanglalibrary.txt".
    """
    try:
        with open(filename, "a", encoding="utf-8") as file:  # Open in append mode
            file.write(f"=== {title} ===\n")
            file.write(content + "\n\n")
        print(f"Content appended to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

# Main program execution
if __name__ == "__main__":
    # List of eBanglaLibrary article URLs to scrape
    urls = [
                'https://www.ebanglalibrary.com/lessons/%e0%a6%9b%e0%a6%be%e0%a6%af%e0%a6%bc%e0%a6%be%e0%a6%98%e0%a6%be%e0%a6%a4%e0%a6%95-%e0%a7%ab/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%9b%e0%a6%be%e0%a6%af%e0%a6%bc%e0%a6%be%e0%a6%98%e0%a6%be%e0%a6%a4%e0%a6%95-%e0%a7%a7%e0%a7%a6/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%9b%e0%a6%be%e0%a6%af%e0%a6%bc%e0%a6%be%e0%a6%98%e0%a6%be%e0%a6%a4%e0%a6%95-%e0%a7%a7%e0%a7%ab/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%9b%e0%a6%be%e0%a6%af%e0%a6%bc%e0%a6%be%e0%a6%98%e0%a6%be%e0%a6%a4%e0%a6%95-%e0%a7%a8%e0%a7%a6/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%9b%e0%a6%be%e0%a6%af%e0%a6%bc%e0%a6%be%e0%a6%98%e0%a6%be%e0%a6%a4%e0%a6%95-%e0%a7%a9%e0%a7%a6/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%9b%e0%a6%be%e0%a6%af%e0%a6%bc%e0%a6%be%e0%a6%98%e0%a6%be%e0%a6%a4%e0%a6%95-%e0%a7%a9%e0%a7%ab/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%9b%e0%a6%be%e0%a6%af%e0%a6%bc%e0%a6%be%e0%a6%98%e0%a6%be%e0%a6%a4%e0%a6%95-%e0%a7%aa%e0%a7%a6/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%9b%e0%a6%be%e0%a6%af%e0%a6%bc%e0%a6%be%e0%a6%98%e0%a6%be%e0%a6%a4%e0%a6%95-%e0%a7%aa%e0%a7%ab/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%9b%e0%a6%be%e0%a6%af%e0%a6%bc%e0%a6%be%e0%a6%98%e0%a6%be%e0%a6%a4%e0%a6%95-%e0%a7%ab%e0%a7%a6/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a7/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a8/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a9/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%aa/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%ab/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%ac/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%ad/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%ae/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%af/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a7%e0%a7%a6/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a7%e0%a7%a7/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a7%e0%a7%a8/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a7%e0%a7%a9/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a7%e0%a7%aa/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a7%e0%a7%ab/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a7%e0%a7%ac/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a7%e0%a7%ad/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a7%e0%a7%ae/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a7%e0%a7%af/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a8%e0%a7%a6/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a8%e0%a7%a7/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a8%e0%a7%a8/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a8%e0%a7%a9/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a8%e0%a7%aa/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a8%e0%a7%ab/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a8%e0%a7%ac/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a8%e0%a7%ad/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a8%e0%a7%ae/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a8%e0%a7%af/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a9%e0%a7%a6/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a9%e0%a7%a7/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a9%e0%a7%a8/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a9%e0%a7%a9/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a9%e0%a7%aa/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a9%e0%a7%ab/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a9%e0%a7%ac/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a9%e0%a7%ad/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a9%e0%a7%ae/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%a9%e0%a7%af/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%aa%e0%a7%a6/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%aa%e0%a7%a7/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%aa%e0%a7%a8/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%aa%e0%a7%a9/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%aa%e0%a7%aa/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%aa%e0%a7%ab/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%aa%e0%a7%ac/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%aa%e0%a7%ad/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%aa%e0%a7%ae/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%aa%e0%a7%af/',
        'https://www.ebanglalibrary.com/lessons/%e0%a6%a7%e0%a7%8d%e0%a6%ac%e0%a6%82%e0%a6%b8%e0%a6%af%e0%a6%9c%e0%a7%8d%e0%a6%9e-%e0%a7%ab%e0%a7%a6/',
    ]
    
    # Consolidated file to store all articles
    consolidated_file = "consolidated_ebanglalibrary.txt"
    
    for url in urls:
        # Scrape each article
        article_title, article_content = scrape_ebanglalibrary_article(url)

        # Save the content if successfully scraped
        if article_title and article_content:
            save_to_consolidated_file(article_content, article_title, filename=consolidated_file)
        else:
            print(f"Failed to retrieve content from {url}")
        
        # Add a one-second delay between requests
        time.sleep(3)
