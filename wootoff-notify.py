#!/usr/bin/env python

wait=15

import pynotify
import time
import urllib


if not pynotify.init ("icon-summary-body"):
	sys.exit(1)


cur = '' # current item
so = False # sold out

def notify(usr,message,icon="notification-message-IM"):
	n = pynotify.Notification (usr,message,icon)
	n.show()

while 1:
	try:
		r = urllib.urlopen('http://www.woot.com/DefaultMicrosummary.ashx').read()
	except:
		pass
	else:
		data = r.split(' : ')
		name = data[2]
		price = data[1]
		percent = data[0]
		out = "SOLD OUT" in r
		if name != cur or (not so and out):
			if out:
				notify(name, "SOLD OUT")
			else:
				notify(name, "%s - %s" % (price, percent))
			cur = name
			so = out
	time.sleep(wait)

