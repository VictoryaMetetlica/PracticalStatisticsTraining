import pandas as pd

import numpy as np


print('\n   Calculate the median of the overall score values that the players of the football club scored during '
      'the season. Display the resulting float value on the screen, rounding it to 1 decimal place.')
print('\n   DataFrame')
df = pd.DataFrame({'player_number': [10, 8, 12, 22, 36, 7, 1, 20, 9, 4, 14],
 'height': [168, 176, 178, 191, 185, 183, 185, 179, 169, 183, 167],
 'weight': [76, 77, 79, 81, 82, 79, 74, 84, 73, 71, 68],
 'score': [95, 86, 94, 96, 95, 95, 89, 83, 99, 78, 82]})
print(df)

def solution(A): # A - pandas DataFrame
    x = (A['score']
         .median()
         .round(1))
    return float(x)

print(solution(df))

print('\n   Calculate the average value of players weight (weight). Display the resulting float value on the screen, '
      'rounded to 5 decimal places.')

def solution(A): # A - pandas DataFrame
    x = (A['weight']
         .mean()
         .round(5))
    return float(x)

print(solution(df))

print('\n   Calculate the average weight of players who scored more than 90 points during the season (score). Display '
      'the resulting float value on the screen, rounding it to 5 decimal places.')

print('\n   first way')
def solution(A): # A - pandas DataFrame
    print('\n   True/False Series for scores > 90')
    mask = A['score'] > 90
    print(mask)
    print('\n   Series with players weights for scores > 90')
    print(A['weight'][mask])
    print('\n   a mean weight value for players with scores > 90')
    x = (A['weight'][mask]
         .mean()
         .round(5))
    return float(x)

print(solution(df))

print('\n   second way')

def solution(A):  # A - pandas DataFrame
    print('\n   Series with players weights for scores > 90')
    print(A.weight[A.score > 90])
    print('\n   a mean weight value for players with scores > 90')
    x = (A.weight[A.score > 90]
         .mean()
         .round(5))
    return float(x)

print(solution(df))

print('\n   third way')

def solution(A):  # A - pandas DataFrame
    print('\n   DataFrame for players with score > 90')
    print(A.query('score > 90'))
    print('\n   Series with players weights for scores > 90')
    print(A.query('score > 90').weight)
    print('\n   a mean weight value for players with scores > 90')
    x = (A.query('score > 90')
         .weight
         .mean()
         .round(5))
    return float(x)

print(solution(df))

print('\n   Calculate the average height of players who weigh more than 80 kg and scored at least 95 points (score) '
      'during the season. Display the resulting float value on the screen, rounding to 1 decimal place.')

def solution(A): # A - pandas DataFrame
    x = A.height[(A.weight > 80) & (A.score >= 95)].mean().round(1)
    return float(x)

print(solution(df))

print("\n   Calculate the value of the players' overall score mode (score). Display the resulting value on the screen "
      "rounded to the nearest whole number.")

def solution(A): # A - pandas DataFrame
    x = A.score.mode()
    return int(x[0])

print(solution(df))
