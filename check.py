#!/usr/bin/python3

url = "https://www.raspberrypi.org/software/operating-systems/"
user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0"
download_path = ""
watch_path = ""

from mechanize import Browser, HTTPRedirectHandler
import os, shutil

b = Browser()
b.set_handle_robots(False)
b.set_handle_refresh(False)
b.set_handle_redirect(HTTPRedirectHandler)
b.addheaders = [('User-agent', user_agent)]

b.open(url)
for link in b.links():

	torrent_url = str(link.absolute_url)
	if not(torrent_url.endswith('.torrent')):
		continue

	filename = torrent_url.split('/')[-1]
	download_file = os.path.join(download_path, filename)
	watch_file = os.path.join(watch_path, filename)
	if os.path.exists(download_file):
		continue
	if os.path.exists(watch_file):
		continue
	try:
		b.retrieve(torrent_url, download_file)
	except:
		pass
	if not(os.path.exists(download_file)):
		continue
	if os.stat(download_file).st_size == 0:
		os.remove(download_file)
		continue

	print(watch_file)
	shutil.copy2(download_file, watch_file)
