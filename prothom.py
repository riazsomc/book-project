import requests
from bs4 import BeautifulSoup
import time

def scrape_prothom_alo_article(url):
    """
    Scrapes the main content from a Prothom Alo article, avoiding duplicate paragraphs.
    
    Parameters:
        url (str): The URL of the article to scrape.
    
    Returns:
        tuple: A tuple containing the article title and its full text content.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the article title
        title_tag = soup.find('h1')
        title = title_tag.get_text(strip=True) if title_tag else 'No Title Found'

        # Extract the article content
        content = ''
        unique_paragraphs = set()  # Track unique paragraphs
        article_sections = soup.find_all('div', {'class': 'story-element'})  # Locate all content sections
        if article_sections:
            for section in article_sections:
                # Extract paragraphs from each section
                paragraphs = section.find_all('p')
                for para in paragraphs:
                    para_text = para.get_text(strip=True)
                    if para_text and para_text not in unique_paragraphs:  # Avoid duplicates
                        unique_paragraphs.add(para_text)
                        content += para_text + '\n'
        else:
            content = 'No content found.'

        return title, content.strip()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the article: {e}")
        return None, None

def save_to_consolidated_file(content, title, filename="consolidated_prothom_alo.txt"):
    """
    Appends the article's text content to a consolidated file with its title as a header.
    
    Parameters:
        content (str): The article's text content.
        title (str): The article's title.
        filename (str): The name of the consolidated file. Default is "consolidated_prothom_alo.txt".
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
    # List of Prothom Alo article URLs to scrape
    urls = [
        'https://www.prothomalo.com/bangladesh/r781i485j8',
        'https://www.prothomalo.com/politics/n1g0t28x09',
        'https://www.prothomalo.com/bangladesh/s25peq29d3',
        'https://www.prothomalo.com/sports/cricket/au86f13sgo',
        'https://www.prothomalo.com/world/asia/3q6p40xuip',
        'https://www.prothomalo.com/bangladesh/8kenmerfsb',
        'https://www.prothomalo.com/bangladesh/district/99m3h6vxr6',
        'https://www.prothomalo.com/business/bank/63xwqj46pq',
        'https://www.prothomalo.com/entertainment/dhallywood/mjzop07f87',
        'https://www.prothomalo.com/lifestyle/health/qmyceabeqn',
        'https://www.prothomalo.com/sports/cricket/i0p7gd4vmq',
        'https://www.prothomalo.com/lifestyle/vn432xjecb',
        'https://www.prothomalo.com/world/india/v5jhvpvio2',
        'https://www.prothomalo.com/bangladesh/crime/54paz9teob',
        'https://www.prothomalo.com/bangladesh/zlpv2h44ur',
        'https://www.prothomalo.com/opinion/column/va9scq94es',
        'https://www.prothomalo.com/opinion/column/vszpanb4f6',
        'https://www.prothomalo.com/bangladesh/m662q6u9e9',
        'https://www.prothomalo.com/bangladesh/sf4pamv4em',
        'https://www.prothomalo.com/sports/cricket/vynhxg0w8q',
        'https://www.prothomalo.com/world/asia/9okl374zd0',
        'https://www.prothomalo.com/bangladesh/hegmp3xf7u',
        'https://www.prothomalo.com/bangladesh/zt246ez2ay',
        'https://www.prothomalo.com/world/asia/vluj4itl2n',
        'https://www.prothomalo.com/bangladesh/qfq8xn1wes',
        'https://www.prothomalo.com/sports/cricket/au86f13sgo',
        'https://www.prothomalo.com/sports/football/6hm70tt6zf',
        'https://www.prothomalo.com/bangladesh/district/kis74sj41l',
        'https://www.prothomalo.com/bangladesh/district/g7ebqo8bms',
        'https://www.prothomalo.com/bangladesh/district/kis74sj41l',
        'https://www.prothomalo.com/bangladesh/uoyozdvkoa',
        'https://www.prothomalo.com/bangladesh/district/b4a9mz95en',
        'https://www.prothomalo.com/bangladesh/district/tc93mksetk',
        'https://www.prothomalo.com/world/middle-east/bc1jm3i7us',
        'https://www.prothomalo.com/world/asia/jo0pmjdsed',
        'https://www.prothomalo.com/lifestyle/nspjt1kkxn',
        'https://www.prothomalo.com/lifestyle/health/sylt87guiy',
        'https://www.prothomalo.com/business/ee5x93vr2h',
        'https://www.prothomalo.com/business/economics/96es8higv2',
        'https://www.prothomalo.com/business/world-business/hhbpu559wd',
        'https://www.prothomalo.com/business/world-business/nln5t4zwof',
        'https://www.prothomalo.com/chakri/employment/gefcyw9zdt',
        'https://www.prothomalo.com/chakri/employment/5ulxnhv777',
        'https://www.prothomalo.com/chakri/employment/9qod9uu9yb',
        'https://www.prothomalo.com/education/higher-education/3rjel59c3l',
        'https://www.prothomalo.com/education/higher-education/ne0elf226j',
        'https://www.prothomalo.com/education/scholarship/0q963nhx9t',
        'https://www.prothomalo.com/technology/kabpbyuyxe',
        'https://www.prothomalo.com/technology/n4ljnkknlf',
        'https://www.prothomalo.com/technology/science/righllivtf',
        'https://www.prothomalo.com/technology/gadget/rfgiyz07hb',
        'https://www.prothomalo.com/technology/gadget/ldm8nwmv6p',
        'https://www.prothomalo.com/technology/gadget/w3m52py6xb',
        'https://nagorik.prothomalo.com/durporobash/h0cl3o5n9w',
        'https://nagorik.prothomalo.com/durporobash/hqfud33ukh',
        'https://nagorik.prothomalo.com/ayojon/c8qaxk7dea',
        'https://nagorik.prothomalo.com/reader/fofqga3kpy',
        'https://www.prothomalo.com/religion/islam/viz01gc6rs',
        'https://www.prothomalo.com/religion/islam/i3s6j74c5u',
        'https://www.prothomalo.com/religion/islam/lt6vr9x14z',
    ]
    
    # Consolidated file to store all articles
    consolidated_file = "consolidated_prothom_alo.txt"
    
    # Do NOT clear the file; previous content will be preserved
    for url in urls:
        # Scrape each article
        article_title, article_content = scrape_prothom_alo_article(url)

        # Save the content if successfully scraped
        if article_title and article_content:
            save_to_consolidated_file(article_content, article_title, filename=consolidated_file)
            time.sleep(3)
        else:
            print(f"Failed to retrieve content from {url}")
