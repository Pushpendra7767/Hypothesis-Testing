
#import pacakages.
import pandas as pd
import numpy as np
import scipy 
from scipy import stats
import statsmodels.api as sm
from scipy.stats import chi2_contingency
from scipy.stats import chi2


#print dataset.
cust=pd.read_csv("C:\\Users\\ACER\\Desktop\\scrap\\Hypothesis Testing\\Costomer+OrderForm.csv")
# convert string into unique int values and count.
cust.loc[cust['Phillippines']=='Error Free','Phillippines']=1
cust.loc[cust['Phillippines']=='Defective','Phillippines']=0
c = cust['Phillippines'].value_counts()

cust.loc[cust['Indonesia']=='Error Free','Indonesia']=1
cust.loc[cust['Indonesia']=='Defective','Indonesia']=0
c1 = cust['Indonesia'].value_counts()

cust.loc[cust['Malta']=='Error Free','Malta']=1
cust.loc[cust['Malta']=='Defective','Malta']=0
c2 = cust['Malta'].value_counts()

cust.loc[cust['India']=='Error Free','India']=1
cust.loc[cust['India']=='Defective','India']=0
c3 = cust['India'].value_counts()

# store count data in dataframe.
di={'Phillippines':[c[0],c[1]],'Indonesia':[c1[0],c1[1]],'Malta':[c2[0],c2[1]],'India':[c3[0],c3[1]]}
custorder=pd.DataFrame.from_dict(di)

# Normality test 
# Anderson-Darling test
cu=stats.anderson(custorder["Phillippines"],dist='gumbel')
Weekend_pValue = cu[1]
print("p-value is: "+str(Weekend_pValue))

cu1=stats.anderson(custorder["Indonesia"],dist='gumbel')
Weekend_pValue = cu1[1]
print("p-value is: "+str(Weekend_pValue))

cu3=stats.anderson(custorder["India"],dist='gumbel')
Weekend_pValue = cu3[1]
print("p-value is: "+str(Weekend_pValue))

#
# chi-square test
# contingency table
custorder1 = custorder
print(custorder1)
stat, p, dof, expected = chi2_contingency(custorder1)
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
# probability=0.950, critical=7.815, stat=3.859
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
# significance=0.050, p=0.277
# Independent (fail to reject H0)













