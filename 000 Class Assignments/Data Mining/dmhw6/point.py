import math

class Point:
	def __init__(self, x: int, y: int, color='black'):
		self.x = x
		self.y = y
		self.color = color

	def __str__(self):
		return f'({self.x},{self.y})'

	def __repr__(self):
		return f'({self.x},{self.y})'

	def dist(self, other):
		if type(other) != Point:
			raise Exception('Invalid point for "Other".')

		res = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
		return res
	def __cmp__(self, other):
		return self.x == other.x and self.y == other.y

	def set_color(self, color: str):
		self.color = color
