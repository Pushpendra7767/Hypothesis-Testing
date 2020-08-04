# import packages
import pandas as pd
import numpy as np
import scipy 
from scipy import stats
import statsmodels.api as sm
import plotly as py
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF
from statsmodels.formula.api import ols

import seaborn as sns
# print datasets
cutlet=pd.read_csv("C:\\Users\\ACER\\Desktop\\scrap\\1 SC\\Hypothesis Testing\\Cutlets.csv")
cutlet.columns = "unitA","unitB"
# Normality test 
#Shapiro Test
# unit A
cutlet1=stats.shapiro(cutlet["unitA"])
sns.distplot(cutlet["unitA"])
cutlet1_pValue = cutlet1[1]
print("p-value is: "+str(cutlet1_pValue))
# unit B
cutlet2=stats.shapiro(cutlet["unitB"])
cutlet2_pValue=cutlet2[1]
sns.distplot(cutlet["unitB"])
print("p-value is: "+str(cutlet2_pValue))
#Varience Test
cut1 = scipy.stats.levene(cutlet["unitA"], cutlet["unitB"])
cut1

cut2 = scipy.stats.ttest_ind(cutlet["unitA"], cutlet["unitB"])
cut2

c1 ={"cutlet1":[cutlet1[0],cutlet1[1]],"cutlet2":[cutlet2[0],cutlet2[1]],"cut1":[cut1[0],cut1[1]],"cut2":[cut2[0],cut2[1]]}
c1
cutlet_ab = pd.DataFrame.from_dict(c1)
cutlet_ab

#hypothesis testing
#ANOVA test
cutresult = stats.f_oneway(cutlet["unitA"], cutlet["unitB"])
print(cutresult[1])
# function for print Ho / Ha
if cutresult[1] < 0.05:
  k='Ha'
else:
 k='Ho'
print(k)






















































