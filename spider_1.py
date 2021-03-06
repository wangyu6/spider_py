#常规的下载函数 无requests
import urllib.request
import re
from urllib.error import URLError,HTTPError,ContentTooShortError

def download(url, user_agent='wsap', num_retries = 2, charset = 'utf-8',proxy = None):

	print('Downloading:',url)
	request = urllib.request.Request(url)
	request.add_header('user_agent',user_agent)
	try:
		if proxy:
			proxy_support = urllib.request.Proxy.Handler({'http':proxy})
			opener = urllib.request.buildopener(opener)
		resp = urllib.request.urlopen(request)
		cs = resp.headers.get_content_charset()
		if not cs:
			cs = charset
		html =resp.read().decode(cs)
	except (URLError, HTTPError, ContentTooShortError) as e:
		print('Download error:',e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
			#之后会重新尝试50x类错误
				return download(url, num_retries - 1)
	return html
def crawl_sitemap(url):
		#下载网站地图
	sitemap = download(url)
		#抽取网页中的链接
	links = re.findall('<loc>(.*?)</loc>', sitemap)
	for link in links:
		html = download(link)
		#scrape html here
		#...

# print(download('http://example.python-scraping.com/sitemap.xml'))
# print(crawl_sitemap('http://example.python-scraping.com/sitemap.xml'))
