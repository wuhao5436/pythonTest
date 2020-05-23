# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import os
import time
import re

if __name__ == '__main__':
	list_url = []
	p1 = '\/'
	pattern1 = re.compile(p1)	
	for num in range(1,41):
		if num == 1:
			url = 'https://www.umei.cc/meinvtupian/meinvxiezhen/213517.htm'
		else:
			url = 'https://www.umei.cc/meinvtupian/meinvxiezhen/213517_%d.htm' % num
		headers = {
				"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
		}

		req = requests.get(url = url,headers = headers)
		req.encoding = 'utf-8'
		html = req.text
		bf = BeautifulSoup(html, 'html.parser')
		targets_url = bf.find_all("div", class_='ImageBody')
		for each in targets_url:
			print(each.find('img').get('src'))
			list_url.append(each.find('img').get('src'))
		print(list_url)

	for index, each_img in enumerate(list_url):
		target_url = each_img
		img_info = each_img.split('2020/')
		filename = re.sub(p1, "_", img_info[1]) 
		print('下载：' + each_img)
		headers = {
			"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
		}
		img_req = requests.get(url = target_url,headers = headers)
		img_req.encoding = 'utf-8'
		if 'images' not in os.listdir():
			os.makedirs('images')
		for file in os.listdir():
			print(file)             
		tryeFilename = 'images/%d_%s' % (index, filename) 
		print(tryeFilename)
		urlretrieve(url = each_img, filename = tryeFilename )
		time.sleep(1)

	print('下载完成！')