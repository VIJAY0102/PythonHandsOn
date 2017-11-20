#!/usr/bin/env python3

class Hello:
	
	def __init__(self):
		self.ring = 'Hello World'
	
	def fun(self):
		return self.ring

if __name__=='__main__':
	print(Hello().fun())

