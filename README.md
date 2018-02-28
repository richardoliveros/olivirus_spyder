# olivirus_spyder
spyder programmed in python, generates a list with all the resources and links detected


a spyder programmed in python is exposed which generates a list with all the resources and links detected in a page, to make a spyder inside an application with authentication you can use the function:

import urllib
import urllib2

url =' http://www.someserver.com/cgi-bin/register.cgi' 
user_agent =' Mozilla/5.0 (Windows NT 6.1; Win64; x64)'.
values = {' name':' Michael Foord',
          location: Northampton,
          language':' Python' }
headers = {' User-Agent': user_agent}

data = urllib. urlencode (values)
req = urllib2. Request (url, data, headers)
response = urllib2. urlopen (req)
the_page = response. read ()

example taken from: https://docs.python.org/2/howto/urllib2.html
