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
        'https://www.prothomalo.com/bangladesh/jnh2ptg3hc',
        'https://www.prothomalo.com/sports/cricket/zud7a0j0n1',
        'https://www.prothomalo.com/bangladesh/district/45ohmz1pqv',
        'https://www.prothomalo.com/sports/cricket/8879m8x1kb',
        'https://www.prothomalo.com/politics/x08rqt8lwp',
        'https://www.prothomalo.com/politics/fjjew47o4c',
        'https://www.prothomalo.com/bangladesh/district/dbn955ow8x',
        'https://www.prothomalo.com/business/economics/gf5ud2ksv4',
        'https://www.prothomalo.com/video/bangladesh/6e6dxolfp5',
        'https://www.prothomalo.com/sports/cricket/iausrk5c0h',
        'https://www.prothomalo.com/bangladesh/1yructx9nw',
        'https://www.prothomalo.com/lifestyle/beauty/igjgpy8jxv',
        'https://www.prothomalo.com/entertainment/dhallywood/ie9wz7wz8y',
        'https://www.prothomalo.com/sports/cricket/m2c3rfic1w',
        'https://www.prothomalo.com/world/europe/921o7wapa2',
        'https://www.prothomalo.com/opinion/column/ldjxzv97fm',
        'https://www.prothomalo.com/chakri/chakri-news/4gd84yk4l4',
        'https://www.prothomalo.com/sports/football/m2a6cev5ai',
        'https://www.prothomalo.com/bangladesh/district/me5dynadck',
        'https://www.prothomalo.com/bangladesh/district/u2ysz5jxdw',
        'https://www.prothomalo.com/bangladesh/district/xg7vf2hnp4',
        'https://www.prothomalo.com/world/usa/2g4pd3luz6',
        'https://www.prothomalo.com/world/asia/22n994zw6z',
        'https://www.prothomalo.com/world/south-america/0efwodrky6',
        'https://www.prothomalo.com/world/usa/n1aex8ak9n',
        'https://www.prothomalo.com/entertainment/dhallywood/hy79glojz1',
        'https://www.prothomalo.com/entertainment/bollywood/ydtvpop2dj',
        'https://www.prothomalo.com/entertainment/tv/q2ikllnsul',
        'https://www.prothomalo.com/entertainment/dhallywood/glvpp3hps4',
        'https://www.prothomalo.com/entertainment/song/i3b2q9liyh',
        'https://www.prothomalo.com/entertainment/bollywood/qjun3xyq7e',
        'https://www.prothomalo.com/entertainment/drama/rskc5mp15j',
        'https://www.prothomalo.com/lifestyle/health/ifddqzqv06',
        'https://www.prothomalo.com/lifestyle/shopping/3tumkdcvor',
        'https://www.prothomalo.com/lifestyle/recipe/3ichwcsei9',
        'https://www.prothomalo.com/opinion/column/ldjxzv97fm',
        'https://www.prothomalo.com/opinion/column/6772x4l3cz',
        'https://www.prothomalo.com/opinion/editorial/oykb2g99dp',
        'https://www.prothomalo.com/opinion/column/c67eif2qcf',
        'https://www.prothomalo.com/business/market/siv9ernkaj',
        'https://www.prothomalo.com/business/market/rrc8k54blw',
        'https://www.prothomalo.com/business/5j31yuiebt',
        'https://www.prothomalo.com/technology/iz3vzjlpe3',
        'https://www.prothomalo.com/technology/science/7xd9njfpcb',
        'https://www.prothomalo.com/technology/artificial-intelligence/ob8iz5os13',
        'https://www.prothomalo.com/technology/gadget/ri9ejpjib4',
        'https://nagorik.prothomalo.com/durporobash/6vgdzbfieq',
        'https://www.prothomalo.com/religion/islam/uy67e5x4ql',
        'https://www.prothomalo.com/business/qv0rh6c3jq',
        'https://www.prothomalo.com/bangladesh/fwrprykw4p',
        'https://www.prothomalo.com/world/asia/16nrtvegvp',
        'https://www.prothomalo.com/bangladesh/2agecz1tg8',
        'https://www.prothomalo.com/bangladesh/60wulzbe0c',
        'https://www.prothomalo.com/business/bank/kzuqeg4c9d',
        'https://www.prothomalo.com/opinion/interview/ij8ps85jq8',
        'https://www.prothomalo.com/entertainment/dhallywood/fqg59z2wyh',
        'https://www.prothomalo.com/world/middle-east/uehv08u0ab',
        'https://www.prothomalo.com/bangladesh/capital/467m64nsvc',
        'https://www.prothomalo.com/sports/football/6yenjjpo5o',
        'https://www.prothomalo.com/sports/cricket/h96qukg6vi',
        'https://www.prothomalo.com/bangladesh/district/fzj0yxacyz',
        'https://www.prothomalo.com/world/asia/96f33ln95o',
        'https://www.prothomalo.com/entertainment/d4an58wx10',
        'https://www.prothomalo.com/lifestyle/health/34oa2r9a74',
        'https://www.prothomalo.com/lifestyle/ev00kbvfht',
        'https://www.prothomalo.com/lifestyle/po6mn5iopf',
        'https://www.prothomalo.com/world/usa/l3o84xsaxf',
        'https://www.prothomalo.com/opinion/column/mn1bmrma5f',
        'https://www.prothomalo.com/world/usa/ytb8fhb77a',
        'https://www.prothomalo.com/sports/cricket/tr2bxdbf39',
        'https://www.prothomalo.com/bangladesh/district/e8so8xv9tm',
        'https://www.prothomalo.com/bangladesh/district/zjkmgzit2z',
        'https://www.prothomalo.com/entertainment/entertainment-interview/a1pbzz5uaz',
        'https://www.prothomalo.com/lifestyle/ti1gby6ki1',
        'https://www.prothomalo.com/bangladesh/district/4ve6xu6unc',
        'https://www.prothomalo.com/bangladesh/crime/97t22prsfr',
        'https://www.prothomalo.com/bangladesh/capital/07kq0pkmsa',
        'https://www.prothomalo.com/bangladesh/crime/tev2cibz6j',
        'https://www.prothomalo.com/bangladesh/crime/yrapoi803w',
        'https://www.prothomalo.com/bangladesh/district/sta6rl7kx2',
        'https://www.prothomalo.com/bangladesh/crime/ldli06aouj',
        'https://www.prothomalo.com/bangladesh/crime/axrx55g1dr',
        'https://www.prothomalo.com/bangladesh/crime/wae8rpteti',
        'https://www.prothomalo.com/bangladesh/crime/genzmkwq8n',
        'https://www.prothomalo.com/bangladesh/crime/lsiv9kb729',
        'https://www.prothomalo.com/bangladesh/crime/d04yi5swz9',
        'https://www.prothomalo.com/entertainment/song/ljx47cnzl9',
        'https://www.prothomalo.com/entertainment/song/004rzwwc3t',
        'https://www.prothomalo.com/entertainment/ott/w32c8bn75o',
        'https://www.prothomalo.com/entertainment/dhallywood/3463qcnlmy',
        'https://www.prothomalo.com/bangladesh/capital/r3myfo0c1e',
        'https://www.prothomalo.com/bangladesh/8mbs4br5ez',
        'https://www.prothomalo.com/bangladesh/capital/7utwmy0snm',
        'https://www.prothomalo.com/bangladesh/zy9upp6crw',
        'https://www.prothomalo.com/bangladesh/15zqioeo1f',
        'https://www.prothomalo.com/bangladesh/h15280uwc5',
        'https://www.prothomalo.com/bangladesh/rwc6luhlfv',
        'https://www.prothomalo.com/bangladesh/district/274e8mc1x1',
        'https://www.prothomalo.com/bangladesh/pcqaexdevw',
        'https://www.prothomalo.com/bangladesh/district/sivkqpvnf4',
        'https://www.prothomalo.com/bangladesh/district/2nqrgok1rr',
        'https://www.prothomalo.com/politics/2vgnp160ql',
        'https://www.prothomalo.com/bangladesh/ko251rwzyd',
        'https://www.prothomalo.com/politics/673jaf635b',
        'https://www.prothomalo.com/world/europe/drc01fdhiq',
        'https://www.prothomalo.com/lifestyle/travel/rtrjhhgi3m',
        'https://www.prothomalo.com/bangladesh/capital/jw5t1b4x0i',
        'https://www.prothomalo.com/world/usa/xduozn82im',
        'https://www.prothomalo.com/bangladesh/capital/ri3f98ufm9',
        'https://www.prothomalo.com/business/economics/es7zw2t2wk',
        'https://www.prothomalo.com/bangladesh/district/if67ihvn6u',
        'https://www.prothomalo.com/bangladesh/district/bv7fsjj7os',
        'https://www.prothomalo.com/bangladesh/0id1jqp5ge',
        'https://www.prothomalo.com/bangladesh/district/9d834ucutk',
        'https://www.prothomalo.com/world/india/xtrn80jhhy',
        'https://www.prothomalo.com/entertainment/dhallywood/0de90rwkkv',
        'https://www.prothomalo.com/opinion/column/0yiuv9t3fq',
        'https://www.prothomalo.com/business/economics/wo0zrzz4o8',
        'https://www.prothomalo.com/business/5p6zdx9p1h',
        'https://www.prothomalo.com/education/higher-education/x3v7lfrs0p',
        'https://www.prothomalo.com/education/admission/bndsw7ugd4',
        'https://www.prothomalo.com/education/scholarship/hdefq50x1h',
        'https://www.prothomalo.com/technology/cyberworld/pxzpbo2htt',
        'https://www.prothomalo.com/technology/a05f3wl195',
        'https://www.prothomalo.com/technology/cyberworld/btsx961f3g',
        'https://www.prothomalo.com/technology/gadget/bbsrk5lxqz',
        'https://www.prothomalo.com/technology/gadget/fp8mh089wr',
        'https://www.prothomalo.com/technology/gadget/ri9ejpjib4',
        'https://www.prothomalo.com/onnoalo/arts/n80n8589oo',
        'https://www.prothomalo.com/onnoalo/interview/qdzmjf6v84',
        'https://nagorik.prothomalo.com/durporobash/h44ov90yz7',
        'https://nagorik.prothomalo.com/durporobash/qh4vpsazo8',
        'https://nagorik.prothomalo.com/durporobash/f25cyjx6jo',
        'https://nagorik.prothomalo.com/n5nyfmfw9y',
        'https://nagorik.prothomalo.com/travel/50tuymwkzt',
        'https://www.prothomalo.com/religion/islam/dv5gno9y39',
        'https://www.prothomalo.com/religion/islam/tktj4dw46r',
        'https://www.prothomalo.com/bangladesh/district/ihzvvd358j',
        'https://www.prothomalo.com/bangladesh/district/zcnio9lxcs',
        'https://www.prothomalo.com/bangladesh/district/rhizqga2fb',
        'https://www.prothomalo.com/bangladesh/capital/m3qfudcn9t',
        'https://www.prothomalo.com/bangladesh/district/rvftmvo6q3',
        'https://www.prothomalo.com/bangladesh/4r6uhxilj8',
        'https://www.prothomalo.com/roundtable/ag8e2nt3r6',
        'https://www.prothomalo.com/bangladesh/3z23p9i5qg',
        'https://www.prothomalo.com/bangladesh/yvkrvnzwgi',
        'https://www.prothomalo.com/bangladesh/r5b8ws6n59',
        'https://www.prothomalo.com/opinion/letter/5bbbawhcoj',
        'https://www.prothomalo.com/bangladesh/district/gdj085dnu1',
        'https://www.prothomalo.com/bangladesh/0h2cb1zs6a',
        'https://www.prothomalo.com/bangladesh/ekuxbj5rex',
        'https://www.prothomalo.com/bangladesh/district/1n112yb344',
        'https://www.prothomalo.com/opinion/column/qml433jue2',
        'https://www.prothomalo.com/roundtable/76djdrk7yk',
        'https://www.prothomalo.com/bangladesh/4kp7ti3qk3',
        'https://www.prothomalo.com/bangladesh/capital/xufdwl93lk',
        'https://www.prothomalo.com/photo/bangladesh/t63zpfz56f',
        'https://www.prothomalo.com/bangladesh/district/u8mo9nuapv',
        'https://www.prothomalo.com/bangladesh/4e6uimvk1l',
        'https://www.prothomalo.com/bangladesh/pss85fwp3k',
        'https://www.prothomalo.com/lifestyle/health/wh24bks74v',
        'https://www.prothomalo.com/world/middle-east/2aclqqcuh6',
        'https://www.prothomalo.com/politics/5q96f9uhgk',
        'https://www.prothomalo.com/bangladesh/uopk70za4k',
        'https://www.prothomalo.com/chakri/a37iidseas',
        'https://www.prothomalo.com/lifestyle/ehkvshagjq',
        'https://www.prothomalo.com/bangladesh/ogpsoj6coh',
        'https://www.prothomalo.com/bangladesh/capital/y8lcgj857e',
        'https://www.prothomalo.com/bangladesh/district/%E0%A6%AC%E0%A6%BE%E0%A6%A8%E0%A6%BE%E0%A6%B0%E0%A7%80%E0%A6%AA%E0%A6%BE%E0%A7%9C%E0%A6%BE%E0%A7%9F-%E0%A6%B8%E0%A7%8D%E0%A6%AC%E0%A6%BE%E0%A6%B8%E0%A7%8D%E0%A6%A5%E0%A7%8D%E0%A6%AF-%E0%A6%95%E0%A6%AE%E0%A6%AA%E0%A7%8D%E0%A6%B2%E0%A7%87%E0%A6%95%E0%A7%8D%E0%A6%B8%E0%A7%87%E0%A6%B0-%E0%A6%B8%E0%A6%BF%E0%A6%81%E0%A7%9C%E0%A6%BF%E0%A6%B0-%E0%A6%A8%E0%A6%BF%E0%A6%9A%E0%A7%87-%E0%A6%AA%E0%A6%BE%E0%A6%93%E0%A7%9F%E0%A6%BE-%E0%A6%97%E0%A7%87%E0%A6%B2-%E0%A6%85%E0%A6%9C%E0%A7%8D%E0%A6%9E%E0%A6%BE%E0%A6%A4-%E0%A6%A8%E0%A6%AC%E0%A6%9C%E0%A6%BE%E0%A6%A4%E0%A6%95',
        'https://www.prothomalo.com/roundtable/rnmno0dd03',
        'https://www.prothomalo.com/opinion/column/whf99yjcl6',
        'https://www.prothomalo.com/lifestyle/health/fbyv0bb6uj',
        'https://www.prothomalo.com/opinion/editorial/cuzq6szd8j',
        "https://www.prothomalo.com/business/r9tfzrmrwi",
        "https://www.prothomalo.com/bangladesh/k7nniz071m",  # Replace with actual URLs
        "https://www.prothomalo.com/lifestyle/health/4rn0dnppwv",  # Replace with actual URLs
        "https://www.prothomalo.com/world/usa/eilf32hh89",
        "https://www.prothomalo.com/opinion/column/528mpbz3z7",
        "https://www.prothomalo.com/politics/7lg9gbatfm",
        "https://www.prothomalo.com/politics/18uepqerqo",
        "https://www.prothomalo.com/politics/348lt3gkn5",
        "https://www.prothomalo.com/world/usa/wodytagsa1",
        "https://www.prothomalo.com/world/india/abo41ahppl",
        "https://www.prothomalo.com/world/asia/31yfzxtcb1",
        "https://www.prothomalo.com/world/india/8tgl56ay2a",
        "https://www.prothomalo.com/opinion/editorial/9ab7xh1aor",
        "https://www.prothomalo.com/opinion/editorial/pvl713dvd1",
        "https://www.prothomalo.com/opinion/0aofpbkq0n",
        "https://www.prothomalo.com/opinion/column/0yiuv9t3fq",
        "https://www.prothomalo.com/opinion/column/yywcdyzfr1",
        "https://www.prothomalo.com/opinion/column/5xfsda6vf3",
        "https://www.prothomalo.com/opinion/column/tdk89kt3w5",
        "https://www.prothomalo.com/opinion/column/rnvhbv6da1",
        "https://www.prothomalo.com/opinion/column/zaao50jgxp",
        "https://www.prothomalo.com/opinion/4r2jg0ezmt",
        "https://www.prothomalo.com/opinion/column/9oeku3ic9y",
        "https://www.prothomalo.com/business/r9tfzrmrwi",
        "https://www.prothomalo.com/bangladesh/k7nniz071m",
        "https://www.prothomalo.com/lifestyle/health/4rn0dnppwv",
        "https://www.prothomalo.com/world/usa/eilf32hh89",
        "https://www.prothomalo.com/opinion/column/528mpbz3z7",
        "https://www.prothomalo.com/politics/7lg9gbatfm",
        "https://www.prothomalo.com/politics/18uepqerqo",
        "https://www.prothomalo.com/politics/348lt3gkn5",
        "https://www.prothomalo.com/world/usa/wodytagsa1",
        "https://www.prothomalo.com/world/india/abo41ahppl",
        "https://www.prothomalo.com/world/asia/31yfzxtcb1",
        "https://www.prothomalo.com/world/india/8tgl56ay2a",
        "https://www.prothomalo.com/opinion/editorial/9ab7xh1aor",
        "https://www.prothomalo.com/opinion/editorial/pvl713dvd1",
        "https://www.prothomalo.com/opinion/0aofpbkq0n",
        "https://www.prothomalo.com/opinion/column/0yiuv9t3fq",
        "https://www.prothomalo.com/opinion/column/yywcdyzfr1",
        "https://www.prothomalo.com/opinion/column/5xfsda6vf3",
        "https://www.prothomalo.com/opinion/column/tdk89kt3w5",
        "https://www.prothomalo.com/opinion/column/rnvhbv6da1",
        "https://www.prothomalo.com/opinion/column/zaao50jgxp",
        "https://www.prothomalo.com/opinion/4r2jg0ezmt",
        "https://www.prothomalo.com/opinion/column/9oeku3ic9y",
        "https://www.prothomalo.com/business/r9tfzrmrwi",
        "https://www.prothomalo.com/bangladesh/k7nniz071m",
        "https://www.prothomalo.com/lifestyle/health/4rn0dnppwv",
        "https://www.prothomalo.com/world/usa/eilf32hh89",
        "https://www.prothomalo.com/opinion/column/528mpbz3z7",
        "https://www.prothomalo.com/politics/7lg9gbatfm",
        "https://www.prothomalo.com/politics/18uepqerqo",
        "https://www.prothomalo.com/politics/348lt3gkn5",
        "https://www.prothomalo.com/world/usa/wodytagsa1",
        "https://www.prothomalo.com/world/india/abo41ahppl",
        "https://www.prothomalo.com/world/asia/31yfzxtcb1",
        "https://www.prothomalo.com/world/india/8tgl56ay2a",
        "https://www.prothomalo.com/opinion/editorial/9ab7xh1aor",
        "https://www.prothomalo.com/opinion/editorial/pvl713dvd1",
        "https://www.prothomalo.com/opinion/0aofpbkq0n",
        "https://www.prothomalo.com/opinion/column/0yiuv9t3fq",
        "https://www.prothomalo.com/opinion/column/yywcdyzfr1",
        "https://www.prothomalo.com/opinion/column/5xfsda6vf3",
        "https://www.prothomalo.com/opinion/column/tdk89kt3w5",
        "https://www.prothomalo.com/opinion/column/rnvhbv6da1",
        "https://www.prothomalo.com/opinion/column/zaao50jgxp",
        "https://www.prothomalo.com/opinion/4r2jg0ezmt",
        "https://www.prothomalo.com/opinion/4r2jg0ezmt",
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
