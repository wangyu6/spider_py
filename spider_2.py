import itertools
from spider_1 import *
def crawl_site(url,maxerrors=5):
	for page in itertools.count(1):
		pg_url = '{}{}'.format(url,page)
		html=download(pg_url)
		if html is None:
			num_errors += 1
			if num_errors == maxerrors:
				#max error reached ,exit loop
				break
			else :
				num_errors = 0
				#success can scrape the result



# crawl_site('http://example.python-scraping.com/view/-')