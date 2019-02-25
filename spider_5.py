from urllib.parse import urlparse
import time
class  Throttle:
	"""add some delay between each downloads to the same domain"""
	def __init__(self, delay):
		#amount of each delay between each domain
		self.delay = delay
		#timestamp of when a domain wa last accessed
		self.domains = ()
	def wait (self,url):
		domain = urlparse(url).netloc
		last_accessed = self.domains.get(domain)

		if self.delay > 0 and last_accessed is not None:
			sleep_secs = self.delay - (time.time() - last_accessed)
			if sleep_secs > 0:
				#domain has been accessed recently
				#so need to sleep
				time.sleep(sleep_secs)
			#update the last accessed time 
		self.domains[domain] = time.time()