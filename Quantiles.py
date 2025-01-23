from statistics import quantiles

import numpy as np
import pandas as pd

print('\n   Calculate quantiles of sample from columns: return of equity of corporate banks ROE, cost of funding COF '
      'and credit rating (rating)')
print('\n   DataFrame')
df = pd.DataFrame({'ROE': [7.4, 7.8, 5.9, 7.1, 6.8, 7.6, 7.9, 8.3, 7.2, 6.9, 7.9],
                   'COF': [6.3, 4.2, 6.2, 8.1, 8.4, 7.5, 6.5, 7.8, 6.9, 7.1, 7.2],
                   'rating': ['AAA', 'BB+', 'BB+', 'AAA', 'BBB-', 'AA', 'AAA', 'AAA', 'BBB-', 'AAA', 'BB+']})
print(df)
Q = [0.25, 0.5, 0.75]
print('\n   Quantiles for list [0.25, 0.5, 0.75]')
print(df['ROE'].quantile(Q))

print('\n   Calculate the 0.25 quantile of the sample of cost of funding (COF) values for banks with AAA '
      'credit rating (rating). Display the resulting float value on the screen, rounding to 1 decimal place. '
      'Use the groupby() functin')

def solution(A): # A - dataframe
    x = (A.groupby('rating')['COF']
          .quantile(0.25)['AAA']
          .round(1))
    return x

print(solution(df))

print('\n   Calculate the 0.25-quantile and 0.5-quantile values of the sample of cost of funding (COF) values for banks '
      'with a credit rating of BB+ (rating). Display the maximum of the resulting float values on the screen, rounded '
      'to 1 decimal place.')

def solution(A): # A - dataframe
    x = (A.groupby('rating')['COF']
          .quantile([0.25, 0.5])['BB+']
          .max()
          .round(1))
    return x

print(solution(df))

print('\n   Calculate the 53rd percentile of the sample of cost of funding (COF) values for all banks. '
      'Display the resulting float value on the screen, rounded to 3 decimal places.')

def solution(A): # A - dataframe
    x = (A.COF
         .quantile(0.53)
         .round(3))
    return x

print(solution(df))