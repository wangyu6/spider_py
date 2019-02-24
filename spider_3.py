import re
from urllib.parse import urljoin
from spider_1 import *

def link_crawer(start_url, link_regex):
	

	"""
	crawl from the given start url following links matched by 
	link_regex
	"""
	# abs_link = start_url
	crawl_queue = [start_url]
	seen = set(crawl_queue)
	
	while crawl_queue:
		url = crawl_queue.pop()
		html = download(url)
		if not html:
			continue

		# fliter for links matching our regular expression
		
		for link in get_links(html):
			# print(link)
			if re.match(link_regex, link):
				abs_link = urljoin(start_url,link)
				print (abs_link)
			# crawl_queue.append(abs_link)
				if abs_link not in seen:
					seen.add(abs_link)
					crawl_queue.append(abs_link)





def get_links(html):
	# return a lisk of link from html
	# a regular expression to extract all links form web page
	webpage_regex = re.compile("""<a[^>]+href=["'](.*?)["']>""", re.IGNORECASE)
	# list of all links from the web page
	return webpage_regex.findall(html)


def get_robots_parser(robots_url):
	"return the robots parser object using the robots_url"
	rp = robotsparser.RobotsFileParser()
	rp.set_url(robots_url)
	rp.read()
	return rp


link_crawer('http://example.python-scraping.com', '/(places|view)/')
# print(link_crawer('http://example.python-scraping.com', '/(index|view)/'))
