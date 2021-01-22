import datetime
from messenger import FBMessage
from slackchat import SlackMessage
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('remind-216610-e14d61996a08.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("HouseWorks").sheet1

Mongers = ['Tom Benavides', 'Wei Chen']

class Houseworks():
	def __init__(self, medium):
		self.sheet = self.get_sheet()
		self.medium = medium

	def get_sheet(self):
		scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
		creds = ServiceAccountCredentials.from_json_keyfile_name('remind-216610-e14d61996a08.json', scope)
		client = gspread.authorize(creds)

		# Find a workbook by name and open the first sheet
		# Make sure you use the right name here.
		sheet = client.open("HouseWorks").sheet1
		return sheet
	def GROUPON(self, start_row, start_col):
		Groups = {}
		get_groups = True
		i = start_col
		while get_groups:
			val = self.sheet.cell(1, i).value
			if 'Group' in val:
				print('new group', val)
				brothers = []
				Groups[val[-1]] = brothers
				get_group = True
				j = start_row
				while get_group:
					bro = self.sheet.cell(j, i).value
					if bro != '':
						Groups[val[-1]].append(bro) 
						j += 1
					else:
						get_group = False
				i += 1
			else:
				get_groups = False
		return Groups

	def Check_Sched(self, groups, start_row, start_col, demo = False):
		if self.sheet.cell(start_row, start_col).value == 'Date':
			i = start_row+1
			check_dates = True
			while check_dates:
				datez = self.sheet.cell(i, start_col).value
				if datez != '':				
					datez = datez.split('/')
					today = str(datetime.date.today())
					today = today.split('-')
					print(today)
					if datez[2] == today[0][2:] and int(today[1]) == int(datez[0]):
						if int(datez[1]) == int(today[2])-1:
							da_time = self.sheet.cell(i, start_col+1).value
							time = datetime.datetime.now()
							if da_time[0] == time.hour or demo:
								message = 'HELLO, THIS IS A FRIENDLY REMINDER THAT YOU ARE SCHEDULED FOR HOUSEWORKS AT ' + da_time + ' TOMORROW, UNLESS YOU HAVE A VALID EXCUSE AND TELL YOUR MONGERS, YOU ARE EXPECTED TO BE THERE. TY <3'
								if self.medium == 'FB':
									msg = FBMessage()
									group = groups[self.sheet.cell(i, start_col+2).value] + Mongers
									msg.GroupMessage(group, message)
								elif self.medium == 'SLACK':
									msg = SlackMessage()
									group = groups[self.sheet.cell(i, start_col+2).value] + Mongers
									msg.GroupMessage(group, message)
						elif int(datez[1]) == int(today[2]):
							da_time = self.sheet.cell(i, start_col+1).value
							time = datetime.datetime.now()
							if da_time[0] == time.hour+4 or da_time[0] == time.hour +1 or demo:
								message = 'HELLO, THIS IS A FRIENDLY REMINDER THAT YOU ARE SCHEDULED FOR HOUSEWORKS AT ' + da_time + ' TODAY, UNLESS YOU HAVE A VALID EXCUSE AND TELL YOUR MONGERS, YOU ARE EXPECTED TO BE THERE. TY <3'
								if self.medium == 'FB':
									msg = FBMessage()
									group = groups[self.sheet.cell(i, start_col+2).value] + Mongers
									msg.GroupMessage(group, message)									
								elif self.medium == 'SLACK':
									msg = SlackMessage()
									group = groups[self.sheet.cell(i, start_col+2).value] + Mongers
									msg.GroupMessage(group, message)
					i += 1
				else:
					check_dates = False
