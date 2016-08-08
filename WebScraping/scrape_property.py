"""
    Get Zilliow Property Info for a given ZPID
    To run the program, change following input parameters
    @city at line 44

    @result: output file in data/propertyInfo/{cityname}.csv
"""
import bs4
import requests

def scrape_property(zpid, city, outfile):
    base_url = 'http://www.zillow.com/homedetails/{}_zpid/'.format(zpid)

    response = requests.get(base_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    soup.prettify()

    header_div = soup.find("div", class_="hdp-header-description")
    # print header_div
    if(header_div == None):
        return

    features = [zpid]
    address = header_div.find("h1", class_="notranslate").text
    features.append(address)

    for span in header_div.findAll('span', class_="addr_bbs"):
        feature = span.text
        features.append(feature)

    zest_div = soup.find("div", class_="zest-value")
    features.append(zest_div.text)

    outfile.write(",".join(features)  + '\n')

    # outfile.close()
    return

def readZillowPropertyIds(fname):
    zpids = [line.rstrip('\n') for line in open(fname)]
    return zpids

if __name__ == '__main__':
    city = "santa-clara-ca"
    zpids = readZillowPropertyIds('../data/zpid/{}.txt'.format(city))
    filename = "../data/propertyInfo/{}.csv".format(city)
    outfile = open(filename, "a")
    outfile.write("ZPID,Street, City, State_Zipcode, Bedroom, Bathroom, Sqft, Zestimate\n")
    for zpid in zpids:
        print "Scraping zpid: {}".format(zpid)
        scrape_property(zpid, city, outfile)
    outfile.close()
