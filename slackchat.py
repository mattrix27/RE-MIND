import sys
from slackclient import SlackClient
from slacker import Slacker

#user = sc.users.list()
#bro = {}
#for i in user.body['members']:
        
#	if 'real_name' in i.keys():
#		bro[i['real_name']] = i['id']
#print(bro)

class SlackMessage():
	def __init__(self):
		self.client = Slacker("xoxb-32350626434-435771195360-ikvzuD1JDhS8n9e7rYHknru9")
		self.users = self.client.users.list()
		self.bro = {}
		for i in self.users.body['members']:
			if 'real_name' in i.keys():
				self.bro[i['real_name']] = i['id']
	def ChannelMessage(self, channel, message):
		slack.chat.post_message(channel, message)
	def SingleMessage(self, name, message):
		channel = self.bro[name]
		slack.chat.post_message(channel, message)
	def GroupMessage(self, names, message):
		friends = []
		for name in names:
			friends.append(self.bro[name])
		group = slack.groups.create(friends)
		slack.chat.post_message(group.info(), message)

