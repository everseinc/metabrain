# -*- coding: utf-8 -*- 

import tensorflow as tf
import random

class Analyze:

	def __init__(self):
		print("init")

	def emotion(self, data):
		return {
			'好感度': self.test(data),
			'嫌悪度': self.test(data),
			'興奮度': self.test(data),
			'冷静度': self.test(data),
			'興味度': self.test(data)
		}

	def test(self, data):
		before = random.randint(35, 65)
		res = []
		for x in data:
			if before > 85:
				after = before + random.randint(-10, 0)
			elif before < 15:
				after = before + random.randint(0, 10)
			else:
				after = before + random.randint(-10, 10)
			
			res.append(after)
			before = after
		return res