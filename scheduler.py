import datetime
import schedule
from houseworks import Houseworks

class Scheduler():
	def __init__(self, demo = False):
		self.houseworks = Houseworks('FB')
		self.demo = demo
	def check_houseworks(self, group_row, group_col, sched_row, sched_col):
		groups = self.houseworks.GROUPON(group_row,group_col)
		self.houseworks.Check_Sched(groups, sched_row, sched_col, self.demo)


scheduler = Scheduler(demo=True)
scheduler.check_houseworks(2,2,1,6)

