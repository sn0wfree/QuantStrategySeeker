#coding=utf8
import pandas as pd
import numpy as np


RiskLevel={'stock':5,
债券类	2
实物资产	3
货币类	1.5
stock fund	4
trust	4
bfp	3
bfp(bond)	2
gov bond	1
'}

class MetaAssets(object):

	def __new__(mcs,*args,**kwargs):
		name,bases,attr = args[:3]
		
	def __init__(self,price_dataframe):
		self.price_dataframe = price_dataframe
		pass
		
		
	def risk_score(self):
		
		
	
class Asset(MetaAssets):
	def __init__(self,price_dataframe):
		self.price_dataframe = price_dataframe
		
		pass
	