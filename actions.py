
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


class open_email(Action):
	def name(self):
		return 'open_email'
		
	def run(self, dispatcher, tracker, domain):
		import webbrowser
		webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox?compose=new")	

class tell_bustimetable(Action):
	def name(self):
		return 'tell_bustimetable'

	def func(trow,tcol,xl,stoplist,place,transport_type="Buses"):
		print(transport_type+"\n")
		trow=trow+2
		t = xl[xl.columns[tcol]][trow].strip() #time
		#print(t)
		temp_check=0 
		temp_check2=0 #to check if we need to u/p none
		while((t not in stoplist) and ((t.lower() in place) or t[0].isdigit())):
			#print(t)
			t=t.lower()
			if(t in place):
				utter_message(t.upper())
				temp_check = 0;         
				#print("xxxxyyyy")
			else:
				if(t[-2:] == 'pm' and int(t[:-6])!=12):
					t = str(int(t[:-6]) + 12) + t[-6:]
				#print(t)
				time_para[3] = int(t[:-6])
				time_para[4] = int(t[-5:-3])
				dt_obj = date.datetime(*time_para[0:6])
				#print(t)
				if( dt_obj >= time_input):
					temp_check=1
					s = xl[xl.columns[tcol]][trow] + " : " + xl[xl.columns[tcol+1]][trow]
					utter_message(s)
			trow = trow + 1
			#print(trow)
			t = xl[xl.columns[tcol]][trow].strip()
			#print(t in place)
			if((t.lower() in place) and temp_check == 0):
				utter_message("none")
		if(temp_check == 0):
				utter_message("none")
	def func2(trow,tcol,xl,stoplist,place,transport_type="Buses"):
		utter_message(transport_type+"\n")
		trow=trow+1
		t = xl[xl.columns[tcol]][trow].strip() #time
		#print(t)
		temp_check=0 
		temp_check2=0 #to check if we need to u/p none
		while((t not in stoplist) and ((t.lower() == "time") or t[0].isdigit())):
			#print(t)
			t=t.lower()
			if(t == "time"):
				utter_message(xl[xl.columns[tcol+1]][trow].strip().upper())
				temp_check = 0;         
				#print("xxxxyyyy")
			else:
				if(t[-2:] == 'pm' and int(t[:-6])!=12):
					t = str(int(t[:-6]) + 12) + t[-6:]
				#print(t)
				time_para[3] = int(t[:-6])
				time_para[4] = int(t[-5:-3])
				dt_obj = date.datetime(*time_para[0:6])
				#print(t)
				if( dt_obj >= time_input):
					temp_check=1
					s = xl[xl.columns[tcol]][trow] + " : " + xl[xl.columns[tcol+1]][trow]
					utter_message(s)
			trow = trow + 1
			#print(trow)
			t = xl[xl.columns[tcol]][trow].strip()
			#print(t in place)
			if((t.lower() == "time") and temp_check == 0):
				utter_message("none")
		if(temp_check == 0):
				utter_message("none")

	def run(self, dispatcher, tracker, domain):
		import pandas as pd
		import datetime as date
		import calendar

		#inputs
		dt_obj = datetime(*time_tuple[0:6])
		time_input=date.datetime.now()

		xl = pd.read_excel(r'transport.xlsx')
		stoplist = ['Bus Supervisor (Mangu): 9439432305', 'BUS SCHEDULE ON WORKING DAYS', 'BUS SCHEDULE  ON SATURDAY/SUNDAY/HOLIDAYS', 'BUS SCHEDULE ON WORKING DAYS', 'TRAVELER SCHEDULE ON SATURDAY', 'TRAVELER SCHEDULE ON SUNDAY/HOLIDAY', 'Abbreviations:']
		working_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
		place = ['bhubaneswar-argul', 'argul-niser/bhubaneswar', 'argul-bhubaneswar']
		holiday = [(12,8), (15,8), (2,9), (10,9), (2,10), (7,10), (8,10), (27,10), (10,11), (12,11), (25,12)] #list of holidays in 2019. Each pair: (date,month)

		if(day_input == 'today'):
			day = (date.datetime.today().strftime("%A")).lower()
			time_para = list(date.datetime.now().timetuple())
		elif(day_input == 'tomorrow'):
			day = calendar.day_name[(date.datetime.today() + date.timedelta(days=1)).weekday()]
			time_para = list((date.datetime.today() + date.timedelta(days=1)).timetuple())
		if((time_para[2], time_para[1]) in holiday):
			day = "sunday"

		if(day in working_days):
			trow,tcol=[(xl[col][xl[col].eq('BUS SCHEDULE ON WORKING DAYS')].index[i], xl.columns.get_loc(col)) for col in xl.columns for i in range(0,len(xl[col][xl[col].eq('BUS SCHEDULE ON WORKING DAYS')].index))][0]
			func(trow,tcol,xl,stoplist,place,"Buses")
					utter_message("\n")
			trow,tcol=[(xl[col][xl[col].eq('TRAVELER SCHEDULE ON WORKING DAYS')].index[i], xl.columns.get_loc(col)) for col in xl.columns for i in range(0,len(xl[col][xl[col].eq('TRAVELER SCHEDULE ON WORKING DAYS')].index))][0]
			func(trow,tcol,xl,stoplist,place,"Traveler")
		elif(day == "saturday" or day == "sunday"):
			trow,tcol=[(xl[col][xl[col].eq('BUS SCHEDULE  ON SATURDAY/SUNDAY/HOLIDAYS')].index[i], xl.columns.get_loc(col)) for col in xl.columns for i in range(0,len(xl[col][xl[col].eq('BUS SCHEDULE  ON SATURDAY/SUNDAY/HOLIDAYS')].index))][0]
			func(trow,tcol,xl,stoplist,place,"Buses")
			utter_message("\n")
		if(day == "saturday"):
			trow,tcol=[(xl[col][xl[col].eq('TRAVELER SCHEDULE ON SATURDAY')].index[i], xl.columns.get_loc(col)) for col in xl.columns for i in range(0,len(xl[col][xl[col].eq('TRAVELER SCHEDULE ON SATURDAY')].index))][0]
			func2(trow,tcol,xl,stoplist,place,"Traveler")
			utter_message("\n")
		elif(day == "sunday"):
					trow,tcol=[(xl[col][xl[col].eq('TRAVELER SCHEDULE ON SUNDAY/HOLIDAY')].index[i], xl.columns.get_loc(col)) for col in xl.columns for i in range(0,len(xl[col][xl[col].eq('TRAVELER SCHEDULE ON SUNDAY/HOLIDAY')].index))][0]
			func2(trow,tcol,xl,stoplist,place,"Traveler")
			utter_message("\n")


