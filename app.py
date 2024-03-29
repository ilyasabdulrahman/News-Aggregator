#Web Content Aggregator
#step1: initialize web server
#step2: create function home()
#step3: request HTML content from websites
#step4: iterate through website HTML code
#step5: store data in database
#step5: format web application

from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__, template_folder='.')

@app.route("/")
def home():
    '''
    This function executes the code to be displayed on the home page of the
    web application.
    Returns: display of the web application
    '''
   
    nyt_list = get_nytimes()
    fox_list = get_foxnews()
    tech_list = get_techradar()
    cnbc_list = get_cnbc()
    ndtv_list = get_ndtv()
    sky_list = get_skysports()
    lsj_list = get_lsj()
    det_list = get_detroit_news()
    
    return render_template("home.html", nyt_list=nyt_list, fox_list=fox_list, tech_list=tech_list, cnbc_list=cnbc_list, ndtv_list=ndtv_list, sky_list=sky_list, lsj_list=lsj_list, det_list=det_list)

def get_nytimes():
    '''
    This function retrieves the headlines from the NY Times website and returns
    a list of the headlines.
    Returns: list of NY Times headlines
    '''
    # makes HTTP requests to receive raw HTML content from websites
    try:
        source = requests.get('https://www.nytimes.com').text
    except requests.RequestException:
        return "Error: Could not retrieve raw data from NY Times news."
    
    try:
        soup = BeautifulSoup(source, 'lxml')
    except:
        return "Error: Could not parse NY Times raw data."
    
    nyt_list = []
    for section in soup.find_all('section', class_='story-wrapper'):
        if len(nyt_list) == 6:
            break
        try:
            # iterates through the website's HTML code
            headline = section.a.h3.text
            nyt_list.append(headline)
        except:
            print("Error: Structure of NY Times news website has changed.")
            continue
    return nyt_list

def get_foxnews():
    '''
    This function retrieves the headlines from the FOX News website and returns
    a list of the headlines.
    Returns: list of FOX News headlines
    '''
    try:
        source = requests.get('https://www.foxnews.com').text
    except requests.RequestException:
        return "Error: Could not retrieve raw data from FOX NEWS."
    
    try:
        soup = BeautifulSoup(source, 'lxml')
    except:
        return "Error: Could not parse FOX NEWS raw data."
    
    fox_list = []
    for header in soup.find_all('header')[0:6]:
        if len(fox_list) == 5:
            break
        try:
            headline = header.h3.a.text
            fox_list.append(headline)
        except:
            print("Error: Structure of FOX NEWS website has changed.")
            continue
    return fox_list

def get_techradar():
    '''
    This function retrieves the headlines from the TechRadar website and returns
    a list of the headlines.
    Returns: list of TechRadar headlines
    '''
    try:
        source = requests.get('https://www.techradar.com').text
    except requests.RequestException:
        return "Error: Could not retrieve raw data from TechRadar."
    
    try:
        soup = BeautifulSoup(source, 'lxml')
    except:
        return "Error: Could not parse raw data from TechRadar."
    
    tech_list = []
    for div in soup.find_all('div', class_="wcl-item-right p-u-1-2 p-u-sm-1 p-u-md-1-2 p-u-lg-1-2"):
        if len(tech_list) == 6:
            break
        try:
            headline = div.a.h3.text
            print(headline)
            if headline == '':
                print("none")
            tech_list.append(headline)
        except:
            print("Error: Structure of TechRadar website has changed.")
            continue
    return tech_list

def get_cnbc():
    '''
    This function retrieves the headlines from the CNBC News website and returns
    a list of the headlines.
    Returns: list of CNBC News headlines
    '''
    try:
        source = requests.get('https://www.cnbc.com').text
    except requests.RequestException:
        return "Error: Could not retrieve raw data from CNBC News."
    
    try:
        soup = BeautifulSoup(source, 'lxml')
    except:
        return "Error: Could not parse raw data from CNBC News."
    
    cnbc_list = []
    for div in soup.find_all('div', class_='LatestNews-headlineWrapper'):
        if len(cnbc_list) == 5:
            break
        try:
            headline = div.a.text
            if headline != "":
                cnbc_list.append(headline)
            
        except:
            print("Error: Structure of CNBC News website has changed.")
            continue
    return cnbc_list

def get_skysports():
    '''
    This function retrieves the headlines from the Sky Sports Football News 
    website and returns a list of the headlines.
    Returns: list of Sky Sports Football News headlines
    '''
    try:
        source = requests.get('https://www.skysports.com/football').text
    except requests.RequestException:
        return "Error: Could not retrieve raw data from NY Times news."

    try:
        soup = BeautifulSoup(source, 'lxml')
    except:
        return "Error: Could not parse NY Times raw data."

    sky_list = []
    for div in soup.find_all('div', class_='news-list__item'):
        if len(sky_list) == 8:
            break
        try:
            #iterate through the website's HTML code
            headline = div.h4.a.text
            sky_list.append(headline)
        except:
            print("Error: Structure of Sky Sports Football news website has changed.")
            continue
    return sky_list

def get_ndtv():
    '''
    This function retrieves the headlines from the NDTV News website and returns
    a list of the headlines.
    Returns: list of NDTV News headlines
    '''
    try:
        source = requests.get('https://www.ndtv.com/trends/most-popular-news').text
    except requests.RequestException:
        return "Error: Could not retrieve raw data from NDTV Most Popular News."
    
    try:
        soup = BeautifulSoup(source, 'lxml')
    except:
        return "Error: Could not parse raw data from NDTV Most Popular News."
    
    ndtv_list = []
    for div in soup.find_all('div', class_='trend-list'):
        if len(ndtv_list) == 5:
            break
        try:
            headline = div.h3.a.text
            ndtv_list.append(headline)
        except:
            print("Error: Structure of NDTV Most Popular News website has changed.")
            continue
    return ndtv_list

def get_lsj():
    '''
    This function retrieves the headlines from the Lansing State Journal News
    website and returns a list of the headlines.
    Returns: list of Lansing State Journal News headlines
    '''
    try:
        source = requests.get('https://www.lansingstatejournal.com/news/').text
    except requests.RequestException:
        return "Error: Could not retrieve raw data from Lansing State Journal News."
    
    try:
        soup = BeautifulSoup(source, 'lxml')
    except:
        return "Error: Could not parse raw data from Lansing State Journal News."
    
    lsj_list = []
    for a in soup.find_all('a', class_='gnt_m_th_a'):
        try:
            headline = a.text
            lsj_list.append(headline)
        except:
            print("Error: Structure of Lansing State Journal News website has changed.")
            continue
    return lsj_list

def get_detroit_news():
    '''
    This function retrieves the headlines from the Detroit News website and returns
    a list of the headlines.
    Returns: list of Detroit News headlines
    '''
    try:
        source = requests.get('https://www.detroitnews.com').text
    except requests.RequestException:
        return "Error: Could not retrieve raw data from The Detroit News."
    
    try:
        soup = BeautifulSoup(source, 'lxml')
    except:
        return "Error: Could not parse raw data from The Detroit News."
    
    det_list = []
    for a in soup.find_all('a', class_='gnt_m_th_a'):
        if len(det_list) == 5:
            break
        try:
            headline = a.text
            det_list.append(headline)
        except:
            print("Error: Structure of Detroit News website has changed.")
            continue
    return det_list
    


nyt_list = get_nytimes()
fox_list = get_foxnews()
tech_list = get_techradar()
cnbc_list = get_cnbc()
sky_list = get_skysports()
ndtv_list = get_ndtv()
lsj_list = get_lsj()
det_list = get_detroit_news()



 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8083)
