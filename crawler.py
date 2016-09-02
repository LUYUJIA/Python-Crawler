import requests
from pyquery import PyQuery as pq
import os
import os.path

def download_pageImage(url):

	if not os.path.exists("./images"):
		os.mkdir("./images")
	req = requests.get(url)
	req.encoding = "utf-8"
	doc = pq(req.text)

	images = doc('img[class*="BDE_Image"]')

	for image in images.items():
		url_img = image.attr("src")
		num_list = url_img.split("/")
		num = num_list[len(num_list)-1]
		print "downloading {0} image".format(num)
		req_img = requests.get(url_img)
		imagename = os.path.join("./images",str(num))
		with open(imagename,"wb") as fp:
			fp.write(req_img.content)


if __name__=="__main__":
	download_pageImage("http://tieba.baidu.com/p/2166231880")