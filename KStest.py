print("\n   Test the normality of a sample of 1254 daily changes in the S&P 500 index using the Kolmogorov-Smirnov test."
      "Display the resulting Kolmogorov-Smirnov statistic, rounded to 5 decimal places.")

import pandas as pd
from scipy.stats import kstest

def solution(A):
    x = kstest(A, 'norm')
    return x

print(solution(df))