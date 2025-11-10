from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import validators 
from soupMK import SoupMaker



def main():
    url = "https://www.amazon.com/s?k="
    soupM = SoupMaker(url, headers=None)

    usrinput = input("Enter the product you want to search for on Amazon: ")
    url += usrinput.replace(" ", "+") #Replace spaces with '+' for URL encoding

    
    soup = soupM.makeSoup(url)

    

    
    print(f"Page Title: {soup.title}")
    print(soup.prettify()[:1000])


if __name__ == "__main__":
    main()