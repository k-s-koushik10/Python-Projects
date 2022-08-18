import requests
import bs4

#http://books.toscrape.com/catalogue/page-1.html -- URL for 1st page

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

#base_url.format(20) --> Goes to page 20

res = requests.get(base_url.format(1))

soup = bs4.BeautifulSoup(res.text,'lxml') #lxml is the engine

prod = soup.select(".product_pod") #Taking the class product_pod which holds all details of a book

example = prod[0]

example.select('.star-rating.two') #To get the books with two-star rating

example.select('a')[1]['title'] #As per source, <a> holds the title of the book

two_star_titles = []

for n in range(1,51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select('.product_pod')

    for b in books:
        if len(b.select('.star-rating.Two')) != 0: #If !0 then Two star rating
            book_title = b.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)
