
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class Action_date(Action):
	def name(self):
		return 'Action_date'
		
	def run(self, dispatcher, tracker, domain):
		import datetime
		message = tracker.latest_message
		print(tracker.latest_message['entities'][0])
		print(eval(str(tracker.latest_message['entities'][0]))['value'])
		time  = eval(str(tracker.latest_message['entities'][0]))['value']
		if isinstance(time, str):
			time= time[:10]
		else:
			time = time['from'][:10]
		day = {6:'Sunday',0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thrusday',4:'Friday',5:'Saturday'}
		s = "The Day is :"+str(day[datetime.date(int(time[0:4]),int(time[5:7]),int(time[8:])).weekday()]) + "\nThe Date is:"+ str(time[8:])+"/"+str(time[5:7])+ "/"+str(time[0:4])+"\nDid that help?"
		dispatcher.utter_message(s)


class Action_weather(Action):
	def name(self):
		return 'Action_weather'

	def run(self, dispatcher, tracker, domain):
		import requests
		import lxml.html as lh
		import pandas as pd
		from datetime import date
		import datetime
		url="https://weather.com/en-IN/weather/tenday/l/743702a5b6452a6f22050784d2ef71a8651068590f1b88d4b65ec8690e130990"
		page = requests.get(url)
		doc = lh.fromstring(page.content)
		tr_elements = doc.xpath('//tr')
		today  = date.today()
		print(today)
		message = tracker.latest_message
		time  = eval(str(tracker.latest_message['entities'][0]))['value']
		if isinstance(time, str):
			time= time[:10]
		else:
			time = time['from'][:10]
		data = datetime.date(int(time[0:4]),int(time[5:7]),int(time[8:]))
		difference = data - today
		difference = difference.days
		print(difference)
		row_no = 0
		x = 0
		col =[]
		if difference>0:
			s = "Weather Report for :" + str(data)
			for ti in tr_elements:
				x += 1
				if difference+1 == row_no:
					for t in range(0,len(ti)):
						name=ti[t].text_content() 
						if(t == 1 and  x > 2):
							if(name[3] != '\n'):
								name = name[0:3]+"\n"+name[3:]
						col.append(name)
						#dispatcher.utter_message(name)
				row_no += 1

			s = s +"\n-> Weather: "+str(col[2])+"\n-> Temperature: " + str(col[3][:2]+"/"+col[3][2:])+"Celsius\n-> Precipitation: "+str(col[4]) + "\n-> Wind Speed: "+ str(col[5]) + "\n-> Humidity: " + str(col[6])
			dispatcher.utter_message(s)
		else:
			s = "Weather for Today:"
			for ti in tr_elements:
				x += 1
				if row_no == 1 or row_no == 2:
					for t in range(0,len(ti)):
						name=ti[t].text_content() 
						if(t == 1 and  x > 2):
							if(name[3] != '\n'):
								name = name[0:3]+"\n"+name[3:]
						col.append(name)
						#dispatcher.utter_message(name)
				row_no += 1
			print(col)
			s = s +"\n-> Weather: "+str(col[2])+"\n-> Temperature: " + str(col[3][:2]+"/"+col[3][2:])+"Celsius\n-> Precipitation: "+str(col[4]) + "\n-> Wind Speed: "+ str(col[5]) + "\n-> Humidity: " + str(col[6])
			dispatcher.utter_message(s)
			s = ""
			s = "\nWeather for Tonight:"
			s = s +"\n-> Weather: "+str(col[9])+"\n-> Temperature(High/Low): " + str(col[10][:2]+"/"+col[10][2:])+"Celsius\n-> Precipitation: "+str(col[11]) + "\n-> Wind Speed: "+ str(col[12]) + "\n-> Humidity: " + str(col[13])
			dispatcher.utter_message(s)




