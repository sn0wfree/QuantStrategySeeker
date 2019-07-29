#coding=utf8
import pandas as pd
import numpy as np


# this project to do portfolio study and inspire by @Scorpi000/QuantStudio

from functools import reduce

import numpy as np
import pandas as pd
import statsmodels.api as sm


def LogisticCDF(x,mu,gamma):
"""# Logistic分布函数"""
    return 1/(1+np.exp(-(x-mu)/gamma))
	
	

def LogisticPDF(x,mu,gamma):
"""# Logistic密度函数"""
	(1/gamma )* np.exp(-(x-mu)/gamma)*(1+np.exp(-(x-mu).gamma)**-2


    #return np.exp(-(x-mu)/gamma)/gamma/(1+np.exp(-(x-mu)/gamma))**2