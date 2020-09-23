# Aim: to list total downloads in iisg dataverse by month
# Author: richard.zijdeman@iisg.nl
# Date: 2020-09-23

# import libraries
import requests
import json
import datetime

# define current datetime
now = datetime.datetime.now()

# up until current year loop over all month/year combo's
for yyyy in range(2017,now.year):

	for mm in range(1,13):

		base = "https://datasets.iisg.amsterdam/api/info/metrics/downloads/toMonth/"
		date = str(yyyy) + "-" + str(mm).zfill(2)
		response = requests.get(base+date)
		data = json.loads(json.dumps(response.json()))

		print(date+","+str(data['data']['count']))

# add data for current year
for mm in range(1,now.month):

		base = "https://datasets.iisg.amsterdam/api/info/metrics/downloads/toMonth/"
		date = str(now.year) + "-" + str(mm).zfill(2)
		response = requests.get(base+date)
		data = json.loads(json.dumps(response.json()))

		print(date+","+str(data['data']['count']))