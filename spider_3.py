

import re
from urllib.parse import urljoin
from urllib import robotparser
from spider_1 import *

def link_crawer(start_url, link_regex,robots_url = None,user_agent = "wawp",max_depth=4):
	

	"""
	crawl from the given start url following links matched by 
	link_regex
	"""
	
	crawl_queue = [start_url]
	
	seen = {}
	if not robots_url:
		robots_url='{}/robots.txt'.format(start_url)
	rp = get_robots_parser(robots_url)
	while crawl_queue:
		url = crawl_queue.pop()
		#check url passes robots.txt restrations

		if rp.can_fetch(user_agent,url):
			depth = seen.get(url,0)
			if depth == max_depth:
				print ('SKIPing %s due to its depth' %url)
				continue
				html = download(url)
				if not html:
					continue
		# fliter for links matching our regular expression
		
				for link in get_links(html):
					if re.match(link_regex, link):
						abs_link = urljoin(start_url,link)
						if abs_link not in seen:
							seen[abs_link] = depth + 1
							crawl_queue.append(abs_link)
		else:
			print ('blocked by robots.txt',url)





def get_links(html):
	# return a lisk of link from html
	# a regular expression to extract all links form web page
	webpage_regex = re.compile("""<a[^>]+href=["'](.*?)["']>""", re.IGNORECASE)
	# list of all links from the web page
	return webpage_regex.findall(html)


def get_robots_parser(robots_url):
	"return the robots parser object using the robots_url"
	rp = robotparser.RobotFileParser()
	rp.set_url(robots_url)
	rp.read()
	return rp


link_crawer('http://example.python-scraping.com', '/(places|view)/')
print(link_crawer('http://example.python-scraping.com', '/(index|view)/'))
