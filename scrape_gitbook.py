import bs4
import requests
import urllib

from bs4 import BeautifulSoup
import urllib.request,sys,time
import pandas as pd


#url of the page that we want to Scarpe
#+str() is used to convert int datatype of the page no. and concatenate that to a URL for pagination purposes.
url = 'https://opyn.gitbook.io/squeeth/squeeth/contracts-documentation'
#Use the browser to get the URL. This is a suspicious command that might blow up.

try:
    # this might throw an exception if something goes wrong.
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # this describes what to do if an exception is thrown
except Exception as e:

    # get the exception information
    error_type, error_obj, error_info = sys.exc_info()

    # print the link that cause the problem
    print('ERROR FOR LINK:', url)

    # print error info and line that threw the exception
    print(error_type, 'Line:', error_info.tb_lineno)