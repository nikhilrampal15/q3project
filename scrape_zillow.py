"""
    Get Zilliow Property IDs for a given city
    To run the program, change following input parameters
    @city at line 49
"""
import bs4
import requests

def scrape_zillow(city):
    base_url = 'http://www.zillow.com/{}/'.format(city)

    filename = "./data/zpid/{}.txt".format(city)
    outfile = open(filename, "w")

    # get pages
    response = requests.get(base_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    soup.prettify()
    page_div = soup.find(id="search-pagination-wrapper")
    pages = []
    for a in page_div.findAll('a'):
        page = a.text
        pages.append(page)

    # build url_list of 2nd page to the last page except Next
    if(len(pages) <= 1):
        url_list = ["{}{}_p".format(base_url, 1)]
    else:
        url_list = ["{}{}_p".format(base_url, page) for page in range(1, int(pages[len(pages)-2])+1)]

    for url in url_list:
        print url
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        soup.prettify()
        div = soup.find(id="search-results")
        for article in div.findAll('article'):
            stack = []
            zpid = article.get('id').replace("zpid_", "")
            stack.append(zpid)
            outfile.write(", ".join(stack) + '\n')

    outfile.close()
    return

if __name__ == '__main__':
    city = "soma-san-francisco-ca"
    scrape_zillow(city)
