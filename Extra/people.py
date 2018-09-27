#!/usr/bin/python
from operator import attrgetter

class Address(object):
	def __init__(self, zip, city, country):
		self.data = dict()
		self.data["zip"] = zip
		self.data["city"] = city
		self.data["country"] = country

	def __str__(self):
		return str(self.data["city"]) + " " + str(self.data["zip"]) + " " + str(self.data["country"])

class Person(object):
	def __init__(self, name, age, gender, address):
		self.data = dict()
		self.data["name"] = name
		self.data["age"]  = age
		self.data["gender"] = gender
		self.data["address"] = address
	
	def __getattr__(self, key):
		return self.data[key]

	def __str__(self):
		return "Name: " + str(self.data["name"]) + "\nAge: " + str(self.data["age"]) + "\nSex: " + str(self.data["gender"]) + "\nAddress: " + str(self.data["address"]) + "\n"
	
class Solution(object):
	def __init__(self):
		self.people = list()

	def __str__(self):
		ret = ""
		for index in range(len(self.people)):
			ret += "\n---Index[" + str(index) + "]---\n"
			ret += str(self.people[index])
		return ret
	def addPerson(self, p):
		self.people.append(p)

	def sort(self, key):
		if "." in key:
			keyArr = key.split(".")
			self.people.sort(key=lambda x: x.data[keyArr[0]].data[keyArr[1]])
		else:
			self.people.sort(key=lambda x: x.data[key])


a1 = Address(95134, "San Jose", "USA")
a2 = Address(12345, "Seattle", "USA")
p1 = Person("Ishan", 28, "Male", a1)
p2 = Person("Alexa", 2, "Female", a2) 
s = Solution()
s.addPerson(p1)
s.addPerson(p2)

s1 = Solution()
s1.addPerson(p1)
s1.addPerson(p2)

s2 = Solution()
s2.addPerson(p1)
s2.addPerson(p2)

print "\nOriginal:\n------------\n"+ str(s1) 
s1.sort("name")
print "\nSorted By Name:\n-------------\n" + str(s1)

print "\nOriginal:\n------------\n"+ str(s2) 
s2.sort("address.zip")
print "\nSorted By Zipcode:\n-------------\n" + str(s2)

print "\nOriginal:\n------------\n"+ str(s) 
s.sort("address.city")
print "\nSorted By City:\n-------------\n" + str(s)
