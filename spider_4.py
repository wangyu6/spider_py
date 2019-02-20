def get_robots_parser(robots_url):
	"return the robots parser object using the robots_url"
	rp = robotsparser.RobotsFileParser()
	rp.set_url(robots_url)
	rp.read()
	return rp