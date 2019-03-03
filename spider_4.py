#:spider  requests 版本

def download(url,user_agent="wswp",num_retries=2,pronxies = None):
	print('downloading:',url)
	headers = {'user_agent':user_agent}
	try:
		resp = requests.get(url,headers=headers,pronxies= pronxies)
		html = resp.text
		if resp.status_code >= 400:
			print('download error:',resp.text)
			html = None
			if num_retries and 500 <= resp.status_code < 600:
				#重新再尝试50x类错误
				return download(url, num_retries - 1)
	except requests.exceptions.RequestException as e:
		print ("download error:",e.reason)
		html = None

	