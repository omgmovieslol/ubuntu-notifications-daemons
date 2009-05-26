#!/usr/bin/env python

usr="username" # username 
pwd="password" # password
wait=15 # in seconds

################################################################################
##
## Info: 
##    Twitter notifications daemon
## 
## Dependencies:
##    python-twitter
##       http://code.google.com/p/python-twitter/
##       (apt-get install python-twitter)
##
## Run:
##    python twitter-notify.py 
##			(from Run prompt or Session/start-up programs)
##		python twitter-notify.py & 
##			(from command line. just don't close out the terminal window)
##
##			actual daemon will happen soon enough
##
## Copyright 2009 James Wilson
##
## Author:
##    James Wilson <j@meswilson.com>
##    http://ja.meswilson.com/blog/
##
## This program is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Public License version 3, as published
## by the Free Software Foundation.
##
## This program is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranties of
## MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
## PURPOSE.  See the GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License along
## with this program.  If not, see <http://www.gnu.org/licenses/>.
##
################################################################################

import twitter
import time
import pynotify

if not pynotify.init ("icon-summary-body"):
	sys.exit(1)

api = 0
def login():
	global api, usr, pwd
	try:
		api = twitter.Api(username=usr, password=pwd)
	except:
		time.sleep(15)
		return login()

login()

all = []

def notify(usr,message,icon="notification-message-IM"):
	n = pynotify.Notification (usr,message,icon)
	n.show()
while 1:
	try:	
		stat = api.GetFriendsTimeline()
	except:
		time.sleep(15)
		login()
	else:
		if len(all) == 0:
			for s in stat:
				all.append(s.text)
		for s in stat:
			if not s.text in all:
				notify(s.user.screen_name, s.text)
				all.append(s.text)

		time.sleep(wait)
#	print [s.text for s in stat]
