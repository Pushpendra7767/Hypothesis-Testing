
#import pacakages.
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

#print dataset.
labtat=pd.read_csv("C:\\Users\\ACER\\Desktop\\scrap\\Hypothesis Testing\\LabTAT.csv")

#Normality test 
#Shapiro Test
labtat1=stats.shapiro(labtat["Laboratory 1"])
sns.distplot(labtat["Laboratory 1"])
labtat1_pValue = labtat1[1]
print("p-value is: "+str(labtat1_pValue))

labtat2=stats.shapiro(labtat["Laboratory 2"])
sns.distplot(labtat["Laboratory 2"])
labtat2_pValue = labtat2[1]
print("p-value is: "+str(labtat2_pValue))

labtat3=stats.shapiro(labtat["Laboratory 3"])
sns.distplot(labtat["Laboratory 3"])
labtat3_pValue = labtat3[1]
print("p-value is: "+str(labtat3_pValue))

labtat4=stats.shapiro(labtat["Laboratory 4"])
sns.distplot(labtat["Laboratory 4"])
labtat4_pValue = labtat4[1]
print("p-value is: "+str(labtat4_pValue))

#Varience Test
scipy.stats.levene(labtat["Laboratory 1"], labtat["Laboratory 2"], labtat["Laboratory 3"], labtat["Laboratory 4"])

#hypothesis testing
#ANOVA test
labresult = stats.f_oneway(labtat["Laboratory 1"], labtat["Laboratory 2"], labtat["Laboratory 3"], labtat["Laboratory 4"])
print(labresult[1])
 
#pvalue < 0.05 --- reject null hypothesis.



















