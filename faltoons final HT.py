
#import pacakages.
import pandas as pd
import numpy as np
import scipy 
from scipy import stats
from statsmodels.formula.api import ols
from scipy.stats import chi2_contingency
from scipy.stats import chi2

#print dataset.
falt=pd.read_csv("C:\\Users\\ACER\\Desktop\\scrap\\Hypothesis Testing\\Faltoons.csv")
# convert string into unique int values and count.
falt.loc[falt['Weekdays']=='Male','Weekdays']=1
falt.loc[falt['Weekdays']=='Female','Weekdays']=0
f = falt['Weekdays'].value_counts()

falt.loc[falt['Weekend']=='Male','Weekend']=1
falt.loc[falt['Weekend']=='Female','Weekend']=0
f1 = falt['Weekend'].value_counts()

# store count data in dataframe.
d={'Weekend':[f[0],f[1]],'Weekdays':[f1[0],f1[1]]}
faltoon=pd.DataFrame.from_dict(d)

# Normality test 
# Anderson-Darling test
fa=stats.anderson(faltoon["Weekend"],dist='gumbel')
Weekend_pValue = fa[1]
print("p-value is: "+str(Weekend_pValue))

fa1=stats.anderson(faltoon["Weekdays"],dist='gumbel')
Weekdays_pValue = fa1[1]
print("p-value is: "+str(Weekdays_pValue))
#
# chi-square test
# contingency table
faltoon1 = faltoon
print(faltoon1)
stat, p, dof, expected = chi2_contingency(faltoon1)
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
# probability=0.950, critical=3.841, stat=15.434
# Dependent (reject H0)
# 
# apha = 0.05        
# interpret p-value
alpha = 1.0 - prob
print('significance=%.3f, p=%.3f' % (alpha, p))
if p <= alpha:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')
# significance=0.050, p=0.000
# Dependent (reject H0)





















