import fbchat
from getpass import getpass
#client = fbchat.Client("matthew.tung.355", "megaman27")
#friends = client.searchForUsers('Tom Benavidas')
#print(friends)
#print(friends[0].url)
#print(friends[0].uid)
#print(client)
#print(client.uid)
#message = fbchat.Message("hi, this an api test :)")
#client.send(message, friends[0].uid, fbchat.ThreadType.USER)

class FBMessage():
	def __init__(self):
		self.client = fbchat.Client("matthew.tung.355", "Megaman27?")
	def SingleMessage(self, name, message, user = False):
		if (user):
			userid = name
		else:
			friend = self.client.searchForUsers(name)
			userid = friend[0].uid
			print('Brother Added: ', friend[0].name)

		message = fbchat.Message(message)
		self.client.send(message, userid, fbchat.ThreadType.USER)
		print('Message Sent')
	def GroupMessage(self, names, message):
		print(names)
		friends = []		
		for name in names:
			friend = self.client.searchForUsers(name)
			print(friend)
			friends.append(friend[0].uid)
		message = fbchat.Message(message)
		print(friends)
		if len(friends) > 1:
			group = self.client.createGroup(message, friends)
		else:
			print('hey, you need more friends XD')


#fb = FBMessage()
#fb.SingleMessage('matthew.tung.355', 'hi')

