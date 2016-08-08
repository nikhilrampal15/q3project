"""
    Get Zilliow Property Info for a given ZPID
    To run the program, change following input parameters
    @city at line 45

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
    address = address.split(',')
    state_zip = address[len(address) - 1]
    address = address[0: len(address) - 1]
    for item in address:
        features.append(item)
    state_zip = state_zip.split(' ')
    state_zip = state_zip[1: len(state_zip)-1]
    features.append(state_zip[0])
    features.append(state_zip[1])

    for span in header_div.findAll('span', class_="addr_bbs"):
        feature = span.text
        features.append(feature)

    zest_div = soup.find("div", class_="zest-value")
    features.append(zest_div.text)

    outfile.write("\t".join(features)  + '\n')

    return

def readZillowPropertyIds(fname):
    zpids = [line.rstrip('\n') for line in open(fname)]
    return zpids

if __name__ == '__main__':
    city = "san-francisco-ca"
    zpids = readZillowPropertyIds('../data/zpid/{}.txt'.format(city))
    filename = "../data/propertyInfo/{}.csv".format(city)
    outfile = open(filename, "a")
    # outfile.write("zpid, street, city, state, zipcode, bedroom, bathroom, sqft, zestimate\n")
    for zpid in zpids:
        print "Scraping zpid: {}".format(zpid)
        scrape_property(zpid, city, outfile)
    outfile.close()
