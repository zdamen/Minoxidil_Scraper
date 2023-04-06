from Data_File import *
from bs4 import BeautifulSoup
from helium import *
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import math
from decimal import Decimal, ROUND_HALF_UP
import time

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists


# and if it doesn't exist, download it automatically,
# then add chromedriver to path

def GetParsedHtmlText(url):

    # intializing options to make website think im a real person or else it will not grab the data in headless Mode

    chrome_options = Options()
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    chrome_options.add_argument(f'user-agent={user_agent}')

    ###

    browser = start_chrome(url,headless=True,options=chrome_options)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    kill_browser()
    return soup


def GetHimsPrices():
        GetHimsFoamMinoxidilPrice()
        GetHimsSolutionMinoxidilPrice()
        GetHimsFinPrice()



# GetKeepsPrices():

def GetHappyHeadPrices():

        GetHappyHeadMinoxidilSolution()
        GetHappyHeadFinPrice()

def GetRogainPrices():
        GetRogainMinoxidilSolutionPrice()
        GetRogainMinoxidilFoamPrice()


def GetKirklandPrices():


        GetKirklandMinoxidilCostcoPrices()
def GetRomanPrices():
        GetRomanSitePrice()

def GetAllPrices():
    GetHimsPrices()
    GetKeepsPrices()
    GetHappyHeadPrices()
    GetRogainPrices()
    GetKirklandPrices()
    GetRomanPrices()
    GetAmazonFinPrice()


def PrintData():
       return(len(data['MinoxidilFoam']),len(data['MinoxidilSolution']),len(data['Finasteride']))  # should be 5,7,5


def GetHimsFinPrice():
    try:
        url = 'https://www.forhims.com/shop/hair-finasteride'
        soup = GetParsedHtmlText(url)
        # div element for price
        priceElement = soup.find('p', {
            'class': "bodystyle__BodyTwo-sc-aexhyq-3 bodystyle__BodyTwoSemi-sc-aexhyq-5 cAwtxq jnVclm"}).text
        # parsed price
        price = priceElement[1:3]
        months = 1
        data['Finasteride']['Hims'] = [float(price) / months, url]
    except:
        GetHimsFinPrice()


def GetHimsFoamMinoxidilPrice():
    url = "https://www.forhims.com/hair-loss/minoxidil-foam"
    soup = GetParsedHtmlText(url)
    price = None
    # try multiple options for the priceF
    try:
        price = soup.find('div',
                          {'class': "upsell-subscription-selectstyle__DropdownPrice-sc-1qia928-1 gGNTNa"}).span.text[
                1:6]
    except AttributeError:
        pass

    if price is None:
        try:
            price = soup.find('div', {'class': "dropdownstyle__DropdownPrice-sc-lbyjtg-4 knefKS"}).span.text[1:6]
        except AttributeError:
            pass
    if price is None:
        try:
            price = soup.find('p', {'class': "pstyle__P-sc-uhg2rw-0 captionstyle__Caption-sc-66n69b-0 upsellstyle__UpsellButtonLabel-sc-1xp9ucd-4 brHkNR kbJSPx bolMUt"}).text[1:3]
        except AttributeError:
            pass

    # Error handeling
    if price is None:
        GetHimsFoamMinoxidilPrice()

    months = 1
    data['MinoxidilFoam']['Hims'] = [float(price) / float(months), url]


def GetHimsSolutionMinoxidilPrice():
    try:
        url = 'https://www.forhims.com/hair-loss/minoxidil'
        soup = GetParsedHtmlText(url)
        # div element for price
        priceElement = soup.find('p', {
            'class': "pstyle__P-sc-uhg2rw-0 captionstyle__Caption-sc-66n69b-0 upsellstyle__UpsellButtonLabel-sc-1xp9ucd-4 brHkNR kbJSPx bolMUt"}).text
        # parsed price
        price = priceElement[1:3]
        months = 1
        data['MinoxidilSolution']['Hims'] = [float(price) / months, url]
    except:
        GetHimsSolutionMinoxidilPrice()


def GetKeepsPrices():
    url = 'https://www.keeps.com/our-products'
    soup = GetParsedHtmlText(url)
    # gets the prices for all 3
    try:
        try:
            priceElement = soup.find_all('span', {'class': "sc-2a8bf221-0 hrOyHq"})
        except:
            pass

        try:
            priceElement = soup.find_all('span', {'class': "sc-5d48d8e5-0 lnSKLN"})
        except:
            print("price not found in keeps")


        # parsing / indexing is -2 from price element
        finasteridePrice = priceElement[-7].text[1:5]
        minoxidilFoamPrice = priceElement[-6].text[1:5]
        minoxidilSolutionPrice = priceElement[-5].text[1:5]
        months = 3
        data['Finasteride']['Keeps'] = [float(finasteridePrice) / months, url]
        data['MinoxidilSolution']['Keeps'] = [float(minoxidilSolutionPrice) / months, url]
        data['MinoxidilFoam']['Keeps'] = [float(minoxidilFoamPrice) / months, url]
    except:
        GetKeepsPrices()


def GetHappyHeadMinoxidilSolution():
    try:
        url = 'https://www.happyhead.com/products/topical-minoxidil/'
        soup = GetParsedHtmlText(url)
        # priceElement contains
        # $29 for the first month – use code ‘GOHAIR’
        # $59/month after first month  so if sale is gone code will break
        priceElement = soup.find('section',
                                 {'class': "av_textblock_section av-1frmmb2-8195fbbcc532a34db27466746d433103"}).div.text
        price = priceElement[45:47]
        months = 1
        data['MinoxidilSolution']['HappyHead'] = [float(price) / months, url]
    except:
        GetHappyHeadMinoxidilSolution()

def GetHappyHeadFinPrice():
    try:
        url = 'https://www.happyhead.com/products/oral-finasteride/'
        soup = GetParsedHtmlText(url)
        priceElement = soup.find('label', {'for': "slide10"}).text.strip()
        price = priceElement[1:3]
        months = 1
        data['Finasteride']['HappyHead'] = [float(price) / months, url]
    except:
        GetHappyHeadFinPrice()

def GetRogainMinoxidilFoamPrice():
    try:
        url = 'https://www.amazon.com/Rogaine-Minoxidil-Regrowth-Treatment-Thinning/dp/B0012BNVE8/'
        soup = GetParsedHtmlText(url)
        priceElement = soup.find('span', {'class': "a-offscreen"}).text
        price = priceElement[1:6]
        months = 3
        data['MinoxidilFoam']['Rogain'] = [float(price) / months, url]
    except:
        GetRogainMinoxidilFoamPrice()


def GetRogainMinoxidilSolutionPrice():
    try:
        url = 'https://www.amazon.com/Rogaine-Strength-Minoxidil-Solution-Treatment/dp/B0000Y8H3S/'
        soup = GetParsedHtmlText(url)
        priceElement = soup.find('span', {'class': "a-offscreen"}).text
        price = priceElement[1:6]
        months = 3
        data['MinoxidilSolution']['Rogain'] = [float(price) / months, url]
    except:
        GetRogainMinoxidilSolutionPrice()


def GetKirklandMinoxidilSolutionAmazonPrice():
    try:
        url = 'https://www.amazon.com/Months-Kirkland-Minoxidil-percentage-Treatment/dp/B008BMOEGA'
        soup = GetParsedHtmlText(url)
        priceElement = soup.find('span', {'class': "a-offscreen"}).text
        price = priceElement[1:6]
        months = 6
        data['MinoxidilSolution']['Kirkland'] = [float(price) / months, url]
    except:
        GetKirklandMinoxidilSolutionAmazonPrice()

def GetKirklandMinoxidilFoamPriceAmazon():
    try:
        url = 'https://www.amazon.com/Kirkland-Signature-Minoxidil-12-66oz-6x2-11oz/dp/B007Z75H0Y'
        soup = GetParsedHtmlText(url)
        priceElement = soup.find('span', {'class': "a-offscreen"}).text
        price = priceElement[1:6]
        months = 6
        data['MinoxidilFoam']['Kirkland'] = [float(price) / months, url]
    except:
        GetKirklandMinoxidilFoamPriceAmazon()


def GetKirklandMinoxidilCostcoPrices():
    try:
        url = 'https://www.costco.com/CatalogSearch?dept=All&keyword=Kirkland+Signature+Hair+Regrowth+Treatment+'
        soup = GetParsedHtmlText(url)
        priceElement = soup.find_all('div', {'class': 'price'})
        foamPrice = priceElement[0].text.strip()[1:6]
        solutionPrice = priceElement[1].text.strip()[1:6]
        months = 6
        data['MinoxidilSolution']['KirklandCostco'] = [float(solutionPrice) / months, url]
        data['MinoxidilFoam']['KirklandCostco'] = [float(foamPrice) / months, url]
    except:
        GetKirklandMinoxidilCostcoPrices()


def GetRomanSitePrice():
    url = 'https://ro.co/hair-loss/'
    soup = GetParsedHtmlText(url)
    prices = None

    try:
        prices = soup.find_all('p', {'class': "style__StyledParagraph-sc-143pjbh-0 fKYcTL"})
    except AttributeError:
        pass

    if prices == []:
        try:
            prices = soup.find_all('p', {'class': "style__StyledParagraph-sc-143pjbh-0 fZqGfL"})
        except AttributeError:
            pass
    # Error handeling
    if prices == []:
        GetRomanSitePrice()

    if prices != []:
        finPrice = prices[1].text[1:3]
        minoxidil = prices[3].text[1:3]
        months = 1
        data['Finasteride']['Roman'] = [float(finPrice) / months, url]
        data['MinoxidilSolution']['Roman'] = [float(minoxidil) / months, url]
    else:
        print("Prices not found")






def GetAmazonFinPrice():
    try:
        url = 'https://pharmacy.amazon.com/dp/B084BR2Z6S?keywords=Finasteride&qid=1674104225&sr=8-1'
        soup = GetParsedHtmlText(url)
        priceWhole = soup.find('span', {'class': "a-price-whole"}).text
        priceDecimal = soup.find('span', {'class': "a-price-fraction"}).text
        price = str(priceWhole) + str(priceDecimal)
        months = 1
        data['Finasteride']['AmazonPharmacy'] = [float(price) / months, url]
    except:
        GetAmazonFinPrice()


