#coding=utf8
import pandas as pd
import numpy as np


# this project to do portfolio study and inspire by @Scorpi000/QuantStudio

from functools import reduce



def multi_np_dot(*matrix):
	return reduce(lambda x,y: np.dot(x,y),matrix)
	
class MetaAssets(object):
	def __init__(self):
		
	
class Asset(object):
	def __init__(self,price_dataframe):
		self.price_dataframe = price_dataframe
		
		pass
	