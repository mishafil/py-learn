import requests
from bs4 import BeautifulSoup

def getNYTimes() :
	timesUrl = 'https://www.nytimes.com'
	req = requests.get(timesUrl)
	html_code = req.text
	parseObj = BeautifulSoup(html_code, "html.parser")
	titles = parseObj.find_all('h2', 'story-heading')
	return '\n'.join([x.string for x in titles if x.string != None])

if __name__ == '__main__' :
	print(getNYTimes())
