import pandas as pd

print('\n   DataFrame')
df = pd.DataFrame({'Company': ['Occidental Petroleum', 'Exxon Mobil Corporation', 'Chevron Corporation',
                               'Ovintiv Inc.', 'Murphy Oil', 'Apache Corp', 'Continental Resources',
                               'PDC Energy', 'Phillips 99', 'Devon Energy Corp', 'Canadian Natural Resources',
                               'Cenovus Energy', 'Enbridge', 'Husky Energy', 'Imperial Oil', 'Irving Oil',
                               'Pembina Pipeline', 'Suncor Energy'],
                   'ROE': [7.35, 4.33, 3.37, 8.3, 3.97, 9.88, 9.52, 7.48, 4.76, 8.95, 9.10, 4.21,
                           6.12, 7.91, 8.49, 8.72, 6.52, 4.75]})
print(df)
var = df.ROE.var()
print('\n   Variance of return on equity (ROE) =', var)
sd = df.ROE.std()
print('\n   Standard deviation of return on equity (ROE) =', sd)
print('\n    Calculate a biased estimate of the sample variance of return on equity (ROE) of oil and gas companies,'
      'the values of which are in the range from 4 to 8 percent in annum inclusive. Display the resulting float value '
      'on the screen, rounding to 5 decimal places')

def solution(A): # A - DataFrame
    x_way1 = (A[A.ROE.between(4,8)]
              .ROE.var(ddof=0)
              .round(5))     # Delta Degrees Of Freedom used in the divisor of the result as N - ddof.
                                                                # Defaults ddof=1 to give an unbiased estimate
    print('\n   A[A.ROE.between(4,8)] returns DataFrame')
    print(A[A.ROE.between(4,8)])
    x_way2 = (A.ROE[(A.ROE >= 4) & (A.ROE <= 8)]
              .var(ddof=0)
              .round(5))
    print('\n   A.ROE[(A.ROE >= 4) & (A.ROE <= 8)] make slice Series')
    print(A.ROE[(A.ROE >= 4) & (A.ROE <= 8)])
    x_way3 = (A.query('4 <= ROE <= 8')
              .ROE
              .var(ddof=0)
              .round(5))
    print("\n   A.query('4 <= ROE <= 8') returns DataFrame")
    print(A.query('4 <= ROE <= 8'))
    return x_way1, x_way2, x_way3

print(solution(df))

print('\n    Calculate a biased estimate of the sample standard deviation of return on equity (ROE) of companies,'
      'except the Apache Corp. Display the resulting float value on the screen, rounding to 5 decimal places')

def solution(A): # A - DataFrame
    x = (A
         .loc[(A['Company'] != 'Apache Corp')]
         .ROE
         .std()
         .round(5))
    return x

print(solution(df))

