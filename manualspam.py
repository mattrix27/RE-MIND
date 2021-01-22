import datetime
import sys
from messenger import FBMessage
#from slackchat import SlackMessage
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
#scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
#creds = ServiceAccountCredentials.from_json_keyfile_name('remind-216610-e14d61996a08.json', scope)
#client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
#sheet = client.open("Brother List").sheet1

#print(type(sheet))
class GenericMessenger():
	def __init__(self, sheet):
		self.sheet = sheet.get_all_values()
		self.brothers = []
		self.FB = FBMessage()
		for i in range(1, len(self.sheet)):
			brother = self.sheet[i]
			print(brother)
			self.brothers.append(Brother(brother[0], brother[1], brother[2], brother[3], brother[4]))
			print('Brother added: ', brother[0]) 
	def AllMessage(self, message, inactive = False):
		for bro in self.brothers:
			if bro.active == 'Yes' or inactive:
				self.FB.SingleMessage(bro.fbuser, message)
				print('sent to ', bro.name)
			

class Brother():
	def __init__(self, name, mode, active, grade, fbuser = ''):
		self.name = name
		self.mode = mode
		self.active = active
		self.grade = grade
		self.fbuser = fbuser

#messenger = GenericMessenger(sheet)
#message = "Hello, this is a bot message to test my HackMIT project, but it is also a REMINDER there is a pretty important brotherhood meeting tonight and the first Pledge Meeting right after. Attendance is crucial for this, we want to make sure we have a strong presence as a brotherhood with these freshmen, so I expect EVERYONE to be able to make it. If you have a legit excuse, please respond to this message, if not I will be taking attendance this meeting and I will hunt you down. Other than that, I'll see you tonight."
#message = "heey, actually tho, are u free any time today to help with rally :( ?"
#messenger.AllMessage(message)

brothers = []
brother = None
while True:
	print("Give Person to Message, Press 'E' to finish")
	brother = input()
	if brother == "E":
		break
	brothers.append(brother)

fb = FBMessage()
message = sys.argv[1]
for x in brothers:
	fb.SingleMessage(x, message)

