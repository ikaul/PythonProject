#!/usr/bin/python

def hex2base64(string):
	return string.decode("hex").encode("base64")
