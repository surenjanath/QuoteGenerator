import requests
import random

def Scrape():
    quotes_api = 'http://api.forismatic.com/api/1.0/'
    Post = {'method':'getQuote',
            'key'   :random.randint(1,999999),
            'format':'json',
            'lang'  :'en'}

    r = requests.post(quotes_api,data=Post)
    if r.status_code == 200 :

        try:
            q =  r.json()['quoteText']
            p =  r.json()['quoteAuthor']
        except :
            q = None
            p = None
    else:
            q = None
            p = None


    return {
            'Quote'         : q,
            'Author'        : p
            }
