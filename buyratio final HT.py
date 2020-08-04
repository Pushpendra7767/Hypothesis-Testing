# import pacakages.
import pandas as pd
import numpy as np
import scipy 
from scipy import stats
import statsmodels.api as sm
import plotly as py
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF
import seaborn as sns
from statsmodels.formula.api import ols
from scipy.stats import chi2_contingency
from scipy.stats import chi2

#print dataset.
buyer=pd.read_csv("C:\\Users\\ACER\\Desktop\\scrap\\Hypothesis Testing\\BuyerRatio.csv")

# Normality test 
# Anderson-Darling test
east=stats.anderson(buyer["East"],dist='gumbel')
East_pValue = east[1]
print("p-value is: "+str(East_pValue))

east=stats.anderson(buyer["West"],dist='gumbel')
East_pValue = east[1]
print("p-value is: "+str(East_pValue))

east=stats.anderson(buyer["North"],dist='gumbel')
East_pValue = east[1]
print("p-value is: "+str(East_pValue))

east=stats.anderson(buyer["South"],dist='gumbel')
East_pValue = east[1]
print("p-value is: "+str(East_pValue))

#hypothesis testing

#ANOVA test
eastresult = stats.f_oneway(buyer["East"],buyer["West"],buyer["North"],buyer["South"])
print(eastresult[1])
#pvalue < 0.05 --- reject null hypothesis.

# chi-square test
# contingency table
buyratio = buyer.iloc[:,1:]
print(buyratio)
stat, p, dof, expected = chi2_contingency(buyratio)
print('dof=%d' % dof)
print(expected)
# interpret test-statistic
prob = 0.95
critical = chi2.ppf(prob, dof)
print('probability=%.3f, critical=%.3f, stat=%.3f' % (prob, critical, stat))
if abs(stat) >= critical:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')
# probability=0.950, critical=7.815, stat=1.596
# Independent (fail to reject H0)
# 
# apha = 0.05        
# interpret p-value
alpha = 1.0 - prob
print('significance=%.3f, p=%.3f' % (alpha, p))
if p <= alpha:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')
# significance=0.05, p=0.660,  p-Value > alpha
# Independent (fail to reject H0),  All proportions are equal









