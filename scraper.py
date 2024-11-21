import os
import re
import requests
from bs4 import BeautifulSoup
import time

def scrape_wikipedia_page(url):
    """
    Scrapes the main text content from a Wikipedia page and removes references.
    
    Parameters:
        url (str): The URL of the Wikipedia page to scrape.
    
    Returns:
        tuple: A tuple containing the page title and the cleaned text content.
    """
    try:
        # Step 1: Send a GET request to the URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        
        # Step 2: Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Step 3: Extract the page title
        title = soup.find('h1', {'id': 'firstHeading'}).text
        print(f"Scraping Page: {title}")
        
        # Step 4: Extract all paragraph text
        paragraphs = soup.find_all('p')
        content = ""
        for para in paragraphs:
            content += para.get_text() + "\n"
        
        # Step 5: Remove references like [৬২], [12], etc.
        content = re.sub(r'\[\d+]', '', content)  # Removes [62], [12], etc.
        content = re.sub(r'\[[০-৯]+\]', '', content)  # Removes [৬২], [৩], etc. (Bangla numerals)
        
        return title, content.strip()
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None, None

def save_to_individual_file(content, title, folder="scraped_pages"):
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"{title.replace(' ', '_')}.txt")
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Content saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

def append_to_single_file(content, title, filename="consolidated_corpus.txt"):
    try:
        with open(filename, "a", encoding="utf-8") as file:  # Open in append mode
            file.write(f"=== {title} ===\n")
            file.write(content + "\n\n")
        print(f"Content appended to {filename}")
    except Exception as e:
        print(f"Error appending to file: {e}")

# Main program execution
if __name__ == "__main__":
    urls = [
        'https://bn.wikipedia.org/wiki/%E0%A6%9F%E0%A6%AE%E0%A6%BE%E0%A6%B8_%E0%A6%8F%E0%A6%A1%E0%A6%BF%E0%A6%B8%E0%A6%A8',
        'https://bn.wikipedia.org/wiki/%E0%A6%AC%E0%A6%BF%E0%A6%9C%E0%A7%8D%E0%A6%9E%E0%A6%BE%E0%A6%A8%E0%A7%80',
        'https://bn.wikipedia.org/wiki/%E0%A6%B8%E0%A6%BE%E0%A6%B2%E0%A6%AB%E0%A6%BF%E0%A6%89%E0%A6%B0%E0%A6%BF%E0%A6%95_%E0%A6%85%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%B8%E0%A6%BF%E0%A6%A1',
        'https://bn.wikipedia.org/wiki/%E0%A6%AC%E0%A6%BF%E0%A6%A6%E0%A7%8D%E0%A6%AF%E0%A7%81%E0%A7%8E_%E0%A6%B6%E0%A6%95%E0%A7%8D%E0%A6%A4%E0%A6%BF_%E0%A6%89%E0%A7%8E%E0%A6%AA%E0%A6%BE%E0%A6%A6%E0%A6%A8',
        'https://bn.wikipedia.org/wiki/%E0%A6%9F%E0%A7%87%E0%A6%B2%E0%A6%BF%E0%A6%97%E0%A7%8D%E0%A6%B0%E0%A6%BE%E0%A6%AB',
        'https://bn.wikipedia.org/wiki/%E0%A6%AB%E0%A7%8D%E0%A6%B0%E0%A6%BE%E0%A6%99%E0%A7%8D%E0%A6%95%E0%A6%B2%E0%A6%BF%E0%A6%A8_%E0%A6%AA%E0%A6%A6%E0%A6%95',
        'https://bn.wikipedia.org/wiki/%E0%A6%97%E0%A7%8D%E0%A6%B0%E0%A6%BE%E0%A6%AE%E0%A7%8B%E0%A6%AB%E0%A7%8B%E0%A6%A8',
        'https://bn.wikipedia.org/wiki/%E0%A6%B0%E0%A7%82%E0%A6%AA%E0%A6%BE%E0%A6%A8%E0%A7%8D%E0%A6%A4%E0%A6%B0%E0%A6%95',
        'https://bn.wikipedia.org/wiki/%E0%A6%A8%E0%A6%BF%E0%A6%89%E0%A6%95%E0%A7%8D%E0%A6%B2%E0%A7%80%E0%A6%AF%E0%A6%BC_%E0%A6%AB%E0%A6%BF%E0%A6%B6%E0%A6%A8',
        'https://bn.wikipedia.org/wiki/%E0%A6%97%E0%A6%A4%E0%A6%BF%E0%A6%B6%E0%A6%95%E0%A7%8D%E0%A6%A4%E0%A6%BF',
        'https://bn.wikipedia.org/wiki/%E0%A6%A4%E0%A6%BE%E0%A6%AA_%E0%A6%87%E0%A6%9E%E0%A7%8D%E0%A6%9C%E0%A6%BF%E0%A6%A8',
        'https://bn.wikipedia.org/wiki/%E0%A6%9A%E0%A7%81%E0%A6%AE%E0%A7%8D%E0%A6%AC%E0%A6%95',
        'https://bn.wikipedia.org/wiki/%E0%A6%AE%E0%A6%BE%E0%A6%87%E0%A6%95%E0%A7%87%E0%A6%B2_%E0%A6%AB%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%B0%E0%A6%BE%E0%A6%A1%E0%A7%87',
        'https://bn.wikipedia.org/wiki/%E0%A6%B8%E0%A7%8C%E0%A6%B0_%E0%A6%B6%E0%A6%95%E0%A7%8D%E0%A6%A4%E0%A6%BF',
        'https://bn.wikipedia.org/wiki/%E0%A6%A4%E0%A6%A1%E0%A6%BC%E0%A6%BF%E0%A7%8E_%E0%A6%AC%E0%A6%BF%E0%A6%B6%E0%A7%8D%E0%A6%B2%E0%A7%87%E0%A6%B7%E0%A6%A3',
        'https://bn.wikipedia.org/wiki/%E0%A6%95%E0%A6%BE%E0%A6%AE%E0%A6%BE%E0%A6%B0',
        'https://bn.wikipedia.org/wiki/%E0%A6%A1%E0%A6%BE%E0%A6%AF%E0%A6%BC%E0%A6%A8%E0%A6%BE%E0%A6%AE%E0%A7%8B',
        'https://bn.wikipedia.org/wiki/%E0%A6%9C%E0%A7%87%E0%A6%AE%E0%A6%B8_%E0%A6%95%E0%A7%8D%E0%A6%B2%E0%A6%BE%E0%A6%B0%E0%A7%8D%E0%A6%95_%E0%A6%AE%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%95%E0%A7%8D%E0%A6%B8%E0%A6%93%E0%A6%AF%E0%A6%BC%E0%A7%87%E0%A6%B2',
        'https://bn.wikipedia.org/wiki/%E0%A6%85%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%B2%E0%A6%AC%E0%A6%BE%E0%A6%B0%E0%A7%8D%E0%A6%9F_%E0%A6%86%E0%A6%87%E0%A6%A8%E0%A6%B8%E0%A7%8D%E0%A6%9F%E0%A6%BE%E0%A6%87%E0%A6%A8',
        'https://bn.wikipedia.org/wiki/%E0%A6%86%E0%A6%87%E0%A6%9C%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%95_%E0%A6%A8%E0%A6%BF%E0%A6%89%E0%A6%9F%E0%A6%A8',
        'https://bn.wikipedia.org/wiki/%E0%A6%86%E0%A6%B0%E0%A7%8D%E0%A6%A8%E0%A7%87%E0%A6%B8%E0%A7%8D%E0%A6%9F_%E0%A6%B0%E0%A6%BE%E0%A6%A6%E0%A6%BE%E0%A6%B0%E0%A6%AB%E0%A7%8B%E0%A6%B0%E0%A7%8D%E0%A6%A1',
        'https://bn.wikipedia.org/wiki/%E0%A6%9C%E0%A7%87%E0%A6%AE%E0%A6%BE%E0%A6%A8_%E0%A6%95%E0%A7%8D%E0%A6%B0%E0%A6%BF%E0%A6%AF%E0%A6%BC%E0%A6%BE',
        'https://bn.wikipedia.org/wiki/%E0%A6%B0%E0%A6%B8%E0%A6%BE%E0%A6%AF%E0%A6%BC%E0%A6%A8',
        'https://bn.wikipedia.org/wiki/%E0%A6%B0%E0%A6%82%E0%A6%AA%E0%A7%81%E0%A6%B0_%E0%A6%AE%E0%A6%A1%E0%A7%87%E0%A6%B2_%E0%A6%95%E0%A6%B2%E0%A7%87%E0%A6%9C',
        'https://bn.wikipedia.org/wiki/%E0%A6%B0%E0%A6%95%E0%A7%8D%E0%A6%A4%E0%A6%B8%E0%A7%8D%E0%A6%AC%E0%A6%B2%E0%A7%8D%E0%A6%AA%E0%A6%A4%E0%A6%BE',
        'https://bn.wikipedia.org/wiki/%E0%A6%B0%E0%A6%95%E0%A7%8D%E0%A6%A4%E0%A6%AC%E0%A6%BF%E0%A6%9C%E0%A7%8D%E0%A6%9E%E0%A6%BE%E0%A6%A8',
        'https://bn.wikipedia.org/wiki/%E0%A6%B0%E0%A6%95%E0%A7%8D%E0%A6%A4',
        'https://bn.wikipedia.org/wiki/%E0%A6%B0%E0%A6%95%E0%A7%87%E0%A6%9F',
        'https://bn.wikipedia.org/wiki/%E0%A6%B0%E0%A6%95%E0%A6%BF_%E0%A6%AA%E0%A6%B0%E0%A7%8D%E0%A6%AC%E0%A6%A4%E0%A6%AE%E0%A6%BE%E0%A6%B2%E0%A6%BE',
        'https://bn.wikipedia.org/wiki/%E0%A6%B0%E0%A6%95%E0%A6%AE%E0%A6%BE%E0%A6%B0%E0%A6%BF_%E0%A6%A1%E0%A6%9F_%E0%A6%95%E0%A6%AE',
        'https://bn.wikipedia.org/wiki/%E0%A6%B0%E0%A6%82%E0%A6%AA%E0%A7%81%E0%A6%B0_%E0%A6%B2%E0%A6%BE%E0%A6%B2%E0%A6%A6%E0%A6%BF%E0%A6%98%E0%A6%BF_%E0%A6%AE%E0%A6%B8%E0%A6%9C%E0%A6%BF%E0%A6%A6',
        'https://bn.wikipedia.org/wiki/%E0%A6%B0%E0%A6%82%E0%A6%AA%E0%A7%81%E0%A6%B0_%E0%A6%9A%E0%A6%BF%E0%A6%A8%E0%A6%BF_%E0%A6%95%E0%A6%B2_%E0%A6%B2%E0%A6%BF%E0%A6%AE%E0%A6%BF%E0%A6%9F%E0%A7%87%E0%A6%A1',
        'https://bn.wikipedia.org/wiki/%E0%A6%95%E0%A6%93%E0%A6%AE%E0%A7%80_%E0%A6%AE%E0%A6%BE%E0%A6%A6%E0%A6%B0%E0%A6%BE%E0%A6%B8%E0%A6%BE',
        'https://bn.wikipedia.org/wiki/%E0%A6%95%E0%A6%95%E0%A6%AA%E0%A6%BF%E0%A6%9F',
        'https://bn.wikipedia.org/wiki/%E0%A6%95%E0%A6%95%E0%A7%87%E0%A6%B6%E0%A6%BE%E0%A6%B8',
        'https://bn.wikipedia.org/wiki/%E0%A6%95%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%AA%E0%A6%A5_(%E0%A6%97%E0%A7%8D%E0%A6%B0%E0%A6%B9)',
        'https://bn.wikipedia.org/wiki/%E0%A6%95%E0%A6%95%E0%A7%8D%E0%A6%B8%E0%A6%AC%E0%A6%BE%E0%A6%9C%E0%A6%BE%E0%A6%B0-%E0%A6%9F%E0%A7%87%E0%A6%95%E0%A6%A8%E0%A6%BE%E0%A6%AB_%E0%A6%AE%E0%A7%87%E0%A6%B0%E0%A6%BF%E0%A6%A8_%E0%A6%A1%E0%A7%8D%E0%A6%B0%E0%A6%BE%E0%A6%87%E0%A6%AD',
        'https://bn.wikipedia.org/wiki/%E0%A6%95%E0%A6%99%E0%A7%8D%E0%A6%97%E0%A7%8B_%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%9C%E0%A6%BE%E0%A6%A4%E0%A6%A8%E0%A7%8D%E0%A6%A4%E0%A7%8D%E0%A6%B0',
        'https://bn.wikipedia.org/wiki/%E0%A6%95%E0%A6%99%E0%A7%8D%E0%A6%95%E0%A6%BE%E0%A6%B2',
        'https://bn.wikipedia.org/wiki/%E0%A6%95%E0%A6%9F%E0%A6%95%E0%A7%87%E0%A6%B0_%E0%A6%AF%E0%A7%81%E0%A6%A6%E0%A7%8D%E0%A6%A7_(%E0%A7%A7%E0%A7%AD%E0%A7%AA%E0%A7%A7)',
        'https://bn.wikipedia.org/wiki/%E0%A6%95%E0%A6%9F%E0%A7%8D%E0%A6%9F%E0%A6%B0%E0%A6%AA%E0%A6%A8%E0%A7%8D%E0%A6%A5%E0%A7%80_%E0%A6%A8%E0%A6%BE%E0%A6%B0%E0%A7%80%E0%A6%AC%E0%A6%BE%E0%A6%A6',
        'https://bn.wikipedia.org/wiki/%E0%A6%AA%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%BE%E0%A6%98%E0%A6%BE%E0%A6%A4%E0%A6%97%E0%A7%8D%E0%A6%B0%E0%A6%B8%E0%A7%8D%E0%A6%A5%E0%A6%A6%E0%A7%87%E0%A6%B0_%E0%A6%AA%E0%A7%81%E0%A6%A8%E0%A6%B0%E0%A7%8D%E0%A6%AC%E0%A6%BE%E0%A6%B8%E0%A6%A8_%E0%A6%95%E0%A7%87%E0%A6%A8%E0%A7%8D%E0%A6%A6%E0%A7%8D%E0%A6%B0',
        'https://bn.wikipedia.org/wiki/%E0%A6%AA%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%AA%E0%A6%BE%E0%A6%A4',
        'https://bn.wikipedia.org/wiki/%E0%A6%AA%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A7%80%E0%A6%AC%E0%A6%BF%E0%A6%9C%E0%A7%8D%E0%A6%9E%E0%A6%BE%E0%A6%A8',
        'https://bn.wikipedia.org/wiki/%E0%A6%AA%E0%A6%9A%E0%A6%A8_%E0%A6%A8%E0%A6%BF%E0%A6%AC%E0%A6%BE%E0%A6%B0%E0%A6%95',
        'https://bn.wikipedia.org/wiki/%E0%A6%AA%E0%A6%9E%E0%A7%8D%E0%A6%9C%E0%A6%BF%E0%A6%95%E0%A6%BE',
        'https://bn.wikipedia.org/wiki/%E0%A6%AA%E0%A6%9F%E0%A6%B2',
        'https://bn.wikipedia.org/wiki/%E0%A6%AA%E0%A6%9F%E0%A6%BE%E0%A6%B6%E0%A6%BF%E0%A6%AF%E0%A6%BC%E0%A6%BE%E0%A6%AE_%E0%A6%95%E0%A6%BE%E0%A6%B0%E0%A7%8D%E0%A6%AC%E0%A6%A8%E0%A7%87%E0%A6%9F',
        'https://bn.wikipedia.org/wiki/%E0%A6%AA%E0%A6%9F%E0%A6%BE%E0%A6%B6%E0%A6%BF%E0%A6%AF%E0%A6%BC%E0%A6%BE%E0%A6%AE_%E0%A6%AA%E0%A6%BE%E0%A6%B0%E0%A6%95%E0%A7%8D%E0%A6%B2%E0%A7%8B%E0%A6%B0%E0%A7%87%E0%A6%9F',
        'https://bn.wikipedia.org/wiki/%E0%A6%AA%E0%A6%9F%E0%A6%BE%E0%A6%B6%E0%A6%BF%E0%A6%AF%E0%A6%BC%E0%A6%BE%E0%A6%AE_%E0%A6%AA%E0%A6%BE%E0%A6%B0%E0%A6%AE%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%99%E0%A7%8D%E0%A6%97%E0%A6%BE%E0%A6%A8%E0%A7%87%E0%A6%9F',
        'https://bn.wikipedia.org/wiki/%E0%A6%AA%E0%A6%9F%E0%A6%BE%E0%A6%B8%E0%A6%BF%E0%A6%AF%E0%A6%BC%E0%A6%BE%E0%A6%AE_%E0%A6%86%E0%A6%AF%E0%A6%BC%E0%A7%8B%E0%A6%A1%E0%A6%BE%E0%A6%87%E0%A6%A1',
        'https://bn.wikipedia.org/wiki/%E0%A6%AA%E0%A6%9F%E0%A6%BE%E0%A6%B8%E0%A6%BF%E0%A6%AF%E0%A6%BC%E0%A6%BE%E0%A6%AE_%E0%A6%AB%E0%A7%87%E0%A6%B0%E0%A6%BF%E0%A6%B8%E0%A6%BE%E0%A6%AF%E0%A6%BC%E0%A6%BE%E0%A6%A8%E0%A6%BE%E0%A6%87%E0%A6%A1',
        'https://bn.wikipedia.org/wiki/%E0%A6%AA%E0%A6%9F%E0%A6%BE%E0%A6%B8%E0%A6%BF%E0%A6%AF%E0%A6%BC%E0%A6%BE%E0%A6%AE_%E0%A6%B8%E0%A6%BE%E0%A6%AF%E0%A6%BC%E0%A6%BE%E0%A6%A8%E0%A6%BE%E0%A6%87%E0%A6%A1',
        'https://bn.wikipedia.org/wiki/%E0%A6%AA%E0%A6%B0%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%AF%E0%A6%BC_%E0%A6%B8%E0%A6%BE%E0%A6%B0%E0%A6%A3%E0%A6%BF',
        'https://bn.wikipedia.org/wiki/%E0%A6%AA%E0%A6%BE%E0%A6%B0%E0%A6%AE%E0%A6%BE%E0%A6%A3%E0%A6%AC%E0%A6%BF%E0%A6%95_%E0%A6%B8%E0%A6%82%E0%A6%96%E0%A7%8D%E0%A6%AF%E0%A6%BE',
        'https://bn.wikipedia.org/wiki/%E0%A6%97%E0%A6%93%E0%A6%B9%E0%A6%B0_%E0%A6%B0%E0%A6%BF%E0%A6%9C%E0%A6%AD%E0%A7%80',
        'https://bn.wikipedia.org/wiki/%E0%A6%97%E0%A6%9E%E0%A7%8D%E0%A6%9C%E0%A6%BF%E0%A6%AB%E0%A6%BE',
        'https://bn.wikipedia.org/wiki/%E0%A6%97%E0%A6%9C%E0%A6%A8%E0%A6%BF',
        'https://bn.wikipedia.org/wiki/%E0%A6%97%E0%A6%A3-%E0%A6%86%E0%A6%A6%E0%A6%BE%E0%A6%B2%E0%A6%A4',
        'https://bn.wikipedia.org/wiki/%E0%A6%97%E0%A6%A3%E0%A6%AD%E0%A6%AC%E0%A6%A8',
    ]
    
    output_folder = "scraped_pages"
    consolidated_file = "consolidated_corpus.txt"
    
    # Remove the line that clears the file to preserve previous content
    # open(consolidated_file, "w", encoding="utf-8").close()
    
    for url in urls:
        title, content = scrape_wikipedia_page(url)
        if title and content:
            save_to_individual_file(content, title, folder=output_folder)
            append_to_single_file(content, title, filename=consolidated_file)
        time.sleep(3)