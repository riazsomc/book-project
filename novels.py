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
        'https://www.ebanglalibrary.com/books/মুক্তিযুদ্ধ-কেন-অনিবার্য/',
        'https://www.ebanglalibrary.com/lessons/১-মনুষ্যসমাজ-কত-বিচিত্র/',
        'https://www.ebanglalibrary.com/lessons/২-মেহেরজান/',
        'https://www.ebanglalibrary.com/lessons/৩-রীনা/',
        'https://www.ebanglalibrary.com/lessons/৪-শেফা/',
        'https://www.ebanglalibrary.com/lessons/৫-ময়না/',
        'https://www.ebanglalibrary.com/lessons/৬-ফতি-পাগলী/',
        'https://www.ebanglalibrary.com/lessons/৭-মিনা/',
        'https://www.ebanglalibrary.com/lessons/০১-বারো-ভাই-বোনের-সবচেয়ে-ছ/',
        'https://www.ebanglalibrary.com/lessons/০২-বুড়িকে-সঙ্গে-আনলে/',
        'https://www.ebanglalibrary.com/lessons/০৩-নীতা-ধূলো-ওড়া-পথ-দিয়ে-চল/',
        'https://www.ebanglalibrary.com/lessons/০৪-গাঁয়ে-ফিরে-বুড়ি/',
        'https://www.ebanglalibrary.com/lessons/০৫-বেশ-অনেক-দিন-অসুখে-ভুগল/',
        'https://www.ebanglalibrary.com/lessons/০৬-গাঁয়ের-শেষ-মাথার-বড়-শিম/',
        'https://www.ebanglalibrary.com/lessons/০৭-বুড়ি-মনোযোগ-দিয়ে-গান-শো/',
        'https://www.ebanglalibrary.com/lessons/০৮-কলীম-উঠোনে-নেমে-গেলে/',
        'https://www.ebanglalibrary.com/lessons/০৯-রমিজার-বাবা-রমিজাকে-নি/',
        'https://www.ebanglalibrary.com/lessons/১০-পরদিন-রমজান-আলী-ফিরে-এল/',
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
