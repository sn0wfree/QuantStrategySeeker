#coding=utf8
import pandas as pd
import numpy as np


RiskLevel={'Stock':5,
'ծȯ��':2,
'ʵ���ʲ�':3,
'������':1.5,
'StockFund':4,
'Trust':4,
'bfp':3,
'bfp(bond)':2,
'govbond':1,
}

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
	