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
        'https://www.prothomalo.com/bangladesh/capital/uzyc4w7xtk',
        'https://www.prothomalo.com/bangladesh/capital/ep8xcxh0vr',
        'https://www.prothomalo.com/bangladesh/capital/b4pe9wztea',
        'https://www.prothomalo.com/sports/cricket/9jxakxdeq5',
        'https://www.prothomalo.com/bangladesh/district/ng8hkwbdzg',
        'https://www.prothomalo.com/opinion/column/cdx81u86np',
        'https://www.prothomalo.com/opinion/column/crdhig6qo7',
        'https://www.prothomalo.com/technology/84cvo4q4f2',
        'https://www.prothomalo.com/video/bangladesh/x5grm3ngyf',
        'https://www.prothomalo.com/entertainment/song/5abhtmb3dc',
        'https://www.prothomalo.com/bangladesh/yt9st0n9k7',
        'https://www.prothomalo.com/world/usa/cgmbx7zwaf',
        'https://www.prothomalo.com/bangladesh/z4h6bf3c8w',
        'https://www.prothomalo.com/sports/cricket/miu1302gd4',
        'https://www.prothomalo.com/world/europe/vqtl1vr4m5',
        'https://www.prothomalo.com/bangladesh/district/i1x3iavd9i',
        'https://www.prothomalo.com/education/l69u81ncmx',
        'https://www.prothomalo.com/lifestyle/relation/cm4ga838mt',
        'https://www.prothomalo.com/chakri/employment/m3q22bhe0m',
        'https://www.prothomalo.com/bangladesh/pn1g6q5wrw',
        'https://www.prothomalo.com/bangladesh/o9hgtwiqgd',
        'https://www.prothomalo.com/politics/qu1nrbk2jc',
        'https://www.prothomalo.com/politics/82wnkhldn6',
        'https://www.prothomalo.com/bangladesh/de5o6hsx3w',
        'https://www.prothomalo.com/entertainment/tv/840e900hwy',
        'https://www.prothomalo.com/bangladesh/0t3cnjgaee',
        'https://www.prothomalo.com/bangladesh/capital/jie6svlm9p',
        'https://www.prothomalo.com/bangladesh/district/rixj58mmom',
        'https://www.prothomalo.com/sports/cricket/miu1302gd4',
        'https://www.prothomalo.com/sports/football/p5xuc6yocc',
        'https://www.prothomalo.com/sports/cricket/lbme0f6apk',
        'https://www.prothomalo.com/sports/football/npc2cdny84',
        'https://www.prothomalo.com/bangladesh/bhv9d99p0c',
        'https://www.prothomalo.com/world/europe/y5gyhv2w8c',
        'https://www.prothomalo.com/world/usa/0cy6cerdg6',
        'https://www.prothomalo.com/world/europe/vqtl1vr4m5',
        'https://www.prothomalo.com/world/usa/qsy2kza3wq',
        'https://www.prothomalo.com/entertainment/bollywood/eakwxn9vvm',
        'https://www.prothomalo.com/entertainment/bollywood/ke0fy39ep0',
        'https://www.prothomalo.com/entertainment/song/hd9n2k0c3y',
        'https://www.prothomalo.com/lifestyle/relation/fe75gvetlo',
        'https://www.prothomalo.com/lifestyle/health/onkwt3pyh7',
        'https://www.prothomalo.com/lifestyle/health/3ad7svkym3',
        'https://www.prothomalo.com/lifestyle/relation/d9n4tnm2et',
        'https://www.prothomalo.com/opinion/column/7lyzjc1r4s',
        'https://www.prothomalo.com/opinion/editorial/twiz653wvh',
        'https://www.prothomalo.com/business/market/84q08mzhcq',
        'https://www.prothomalo.com/business/market/5rybo3eh2i',
        'https://www.prothomalo.com/business/market/2franmdim6',
        'https://www.prothomalo.com/business/bank/v07i5xhrpu',
        'https://www.prothomalo.com/business/economics/8o9bazkwr4',
        'https://www.prothomalo.com/chakri/chakri-news/h5tasfhlt1',
        'https://www.prothomalo.com/technology/cyberworld/j48xu63s1o',
        'https://nagorik.prothomalo.com/durporobash/ojx0c4otby',
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
