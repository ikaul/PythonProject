#!/usr/bin/python
"""
Given a list of start and end times of meeting.
Return number of meeting rooms needed.
"""

# list the conflicting meetings -> go to different rooms.		 
class Meeting(object):
	def __init__(self, startTime, endTime, id):
		self.startTime = startTime
		self.endTime = endTime
		self.id = id
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.id) + ":" + str(self.startTime) + "-" + str(self.endTime)

class Tree(object):
	def __init__(self, root=None):
		self.root = root
		self.meetingRooms = 0 
						
	def scheduleMeeting(self, meetingList): 
		for meeting in meetingList:
			if self.root == None:
				self.root = meeting
				print "Adding root node: " + str(meeting)
			else:
				current = self.root
				while(1):
					if meeting.startTime < current.startTime:
						if current.left == None:
							current.left = meeting
							print "Adding left node: " + str(meeting)
							break
						else:
							current = current.left
							
					if meeting.startTime >= current.startTime:						  
						if current.right == None:
							current.right = meeting
							print "Adding right node: " + str(meeting)
							break
						else:
							current = current.right

	def overlap(self, current=None):
		if current == None:
			current = self.root
			self.meetingRooms = 1
			
		left = current.left
		right = current.right
		if left != None and left.endTime > current.startTime:
			#we have conflict since the child meeting will end after the parent meeting starts
			print "left"
			self.meetingRooms += 1
		if right != None and right.startTime < current.endTime:
			#we have conflict since child meeting will start before parent meeting end
			print "right"
			self.meetingRooms += 1
			
		if current.left != None:
			self.overlap(current.left)
		if current.right != None:
			self.overlap(current.right)
			
		return self.meetingRooms

meetingList = list()
m = Meeting(9.00, 10.00, 1)
meetingList.append(m)
m = Meeting(9.30, 10.30, 2)
meetingList.append(m)
m = Meeting(10.00, 11.00, 3)
meetingList.append(m)
m = Meeting(8.30, 11.00, 4)
meetingList.append(m)

meetings = Tree()
meetings.scheduleMeeting(meetingList)
print "Meeting Rooms Needed:" + str(meetings.overlap())
