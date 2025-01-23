import pandas as pd
from scipy.stats import pearsonr
import numpy as np

print('\n   Calculating the Pearson correlation value by different libraries')
print('\n   Creating Series of data')
NIM = pd.Series([7.6, 7.9, 8.3, 7.2, 6.9, 7.9, 7.4, 7.8, 5.9, 7.1, 6.8])
rate = pd.Series([10, 12, 12, 8, 8, 7.5, 7.5, 7.5, 6.5, 7, 7])
print(NIM, rate)
print('\n   Calculating the Pearson correlation value between two data series by scipy.stats pearsonr():')
corr = pearsonr(NIM, rate)
print(corr)
print('Scipy coefficient of Pearson pearsonr().statistic =', corr.statistic)

print('\n   Calculating the Pearson correlation value between each data columns of dataframe by Pandas corr():')
print('\n   Creating DataFrame')
df = pd.DataFrame({'NIM': [7.6, 7.9, 8.3, 7.2, 6.9, 7.9, 7.4, 7.8, 5.9, 7.1, 6.8],
                   'rate': [10, 12, 12, 8, 8, 7.5, 7.5, 7.5, 6.5, 7, 7],
                   'GDP_growth': [2.5, 1.8, 3.1, 1.9, 2.4, 2.8, 1.0, 3.2, 2.1, 2.2, 0.5]})
print(df)
corr_matrix = df.corr().round(2)
print('\n   Pandas coefficient of Pearson corr()')
print(corr_matrix)

print('\n   Calculate the Pearson correlation value between two sets A and B using .pearsonr[0]. '
      'Display the resulting float value on the screen, rounding to 5 decimal places.')
A = np.array([43, 32, 42, 48, 58, 57.5, 47.5, 37.5, 56.5, 67, 47.3])
B = np.array([12.5, 11.8, 13.1, 11.9, 12.4, 17.8, 13.3, 13.2, 12.1, 12.2, 8.5])
print(A, B)
def solution(a,b): # a,b - Numpy array
    x = (pearsonr(A, B)[0]
         .round(5))
    return x

print(solution(A,B))





