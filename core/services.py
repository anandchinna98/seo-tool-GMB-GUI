import time
import random
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import quote_plus
from bs4 import BeautifulSoup


def get_page_soup(query=None,url=None):     
    browser_string= "Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11"
    header={"User-Agent": browser_string}
    if query is not None and url is None:
        print("...")
        parsed_query=quote_plus(query)    
        url = "http://www.google.com/search?gl=us&q=%s&num=20&hl=en&start=0" % (parsed_query)      
    request = Request(url,None, header,)
    try:
        urlfile = urlopen(request)
        page = urlfile.read()
        soup = BeautifulSoup(page, "html.parser")
        return soup
    except Exception as e:
        print("Exception:", e)
        return None

def get_links(soup):
    # To extract organic result
    links = []
    for li in soup.findAll("div", attrs={"class": "g"}):
        sLink = li.find("a")
        try:
            if sLink["href"] and sLink["href"].startswith("http"):
                links.append(sLink["href"])
        except KeyError:
            print("error")
    return links

def process_page(soup):
    # To extract map links
    result_list = list()
    sleep_time = random.randint(16, 33)    
    links = soup.find_all("div", class_="dbg0pd")    
    for link in links:        
        result_list.append(link.text)
    time.sleep(sleep_time)    
    return result_list

def check_is_map(soup):
    return soup.find("div", class_="xERobd")

def get_next_page(base_url, soup):    
    sleep_time = random.randint(58, 78)
    link = soup.find("a", class_="Q2MMlc")    
    if link is None:
        return None
    next_page = link["href"]    
    url = base_url + next_page    
    soup = get_page_soup(url=url)    
    time.sleep(sleep_time)    
    return soup


def get_map_result(name, key, city):   
    found, count = 0, 0
    query = key + " " + city    
    base_url = "https://www.google.com"
    sleep_time = random.randint(36, 58)
    soup = get_page_soup(query)
    check_map = check_is_map(soup)      
    try:
        if check_map is not None:
            time.sleep(sleep_time)
            map_soup = get_next_page(base_url, soup)            
            if map_soup is None:
                return found            
            site_names = process_page(map_soup)
            for site_name in site_names: 
                print(site_name)                              
                count += 1
                for names in name.split(","):                   
                    if site_name.lower().find(names.lower()) != -1 and found == 0:
                        found = count
            return found
        else:
            return found
    except Exception:
        return found


# if __name__=='__main__':
    # soup=get_page_soup("hospital")
    # links=get_links(soup)
    # print(links)

    # name='Desss'
    # city='houston'
    # key='web hosting consulting'
    # get_map_result(name,key,city)