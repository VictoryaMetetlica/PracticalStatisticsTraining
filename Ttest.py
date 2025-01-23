import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import ttest_ind

print("\n   Conduct a one-sample t-test to determine whether the mean of the population of Jersey men's weights is equal"
      " to 86.44. We have data on a sample of 40 Jersey men. The sample mean is 83.55, and the standard deviation is "
      "7.74. Display the resulting p-value (pvalue) on the screen, rounded to 5 decimal places.")

weight = np.array([100, 82, 92, 88, 78, 85, 89, 79, 61, 87, 89, 87, 89, 86, 79, 78, 78, 85, 89, 79,
                   61, 87, 92, 88, 78, 85, 79, 78, 78, 85, 101, 87, 89, 86, 79, 78, 78, 85, 89, 79])
    # Hypothetical population mean
population_mean = 86.44
    # Perform a one-sample t-test
t_stat, p_value = stats.ttest_1samp(weight, population_mean)
    # Print p-value rounded to 5 decimal places
print(round(p_value, 5))

print("\n   There are two samples of average annual returns of the banking sector in the US and China from 1971 to 2019."
      "Calculate the homogeneity of variances. Display the ratio of the larger sample variance to the smaller sample "
      "variance on the screen, rounding the resulting value to 5 decimal places.")

data = {
    "Year": [
        1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980,
        1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990,
        1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000,
        2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
        2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019
    ],
    "China": [
        1.995611, 4.138085, 4.642153, -1.445129, -1.184589, 4.391463,
        3.577153, 4.422982, 2.033892, -1.209300, 1.536320, -2.734557,
        3.631993, 6.312155, 3.250656, 2.510892, 2.538941, 3.235401,
        2.698175, 0.741482, -1.434195, 2.096615, 1.406758, 2.760928,
        1.468787, 2.572196, 3.197253, 3.270524, 3.557193, 2.975209,
        0.003649, 0.802104, 1.980926, 2.842681, 2.563502, 1.867956,
        0.911866, -1.076700, -3.387436, 1.718201, 0.822278, 1.508614,
        1.145053, 1.709322, 2.131960, 0.841916, 1.574044, 2.391097,
        1.849711
    ],
    "US": [
        3.073314, 3.968556, 6.318245, -2.545877, -1.466335, 2.935589,
        2.491438, 4.198675, 3.655966, -2.148387, -0.822285, 2.031456,
        4.186321, 2.107380, 3.911319, 2.911710, 5.168872, 5.497881,
        2.310929, 0.433081, -1.408486, 0.129933, 2.244411, 3.581968,
        2.260784, 2.230895, 3.587693, 3.343266, 3.083962, 3.068548,
        2.578699, 1.892090, 2.806552, 1.793156, 2.473712, 2.035550,
        1.636058, -1.062893, -4.969350, 1.153475, 0.749697, 0.775735,
        1.457702, 1.854585, 1.547697, 1.148663, 1.202194, 0.728524,
        0.841075
    ]
}

df = pd.DataFrame(data)
def solution(A):
    x = [np.var(A['China']), np.var(A['US'])]
    return round(max(x) / min(x), 5)

print(solution(df))

print("\n   There are two samples of average annual returns of the banking sector in the US and China from 1971 to 2019. "
      "Conduct the required t-test to check the equality of means. Display the p-value on the screen, rounding the obtained"
      "value to 5 decimal places.")

print(ttest_ind(df.China, df.US).pvalue.round(5))

print("\n   A university conducted a study to find out whether loud music in students' headphones during exams negatively"
      " affects their results. To do this, 250 students were randomly selected during final exams and randomly divided "
      "into two equal samples: test and control. Students from the test sample were given headphones during the exam and"
      " Led Zeppelin was played at full volume. Students from the control sample were provided with a quiet classroom "
      "and cool water. The final results of students from the two samples are recorded in a data frame (0-poor, "
      "50-excellent). Conduct the necessary statistical tests, do not forget to check the distributions for normality "
      "and their variances for homogeneity. Based on the test results, determine whether it is possible to reject the "
      "null hypothesis that loud music does not interfere with students' exams. Display the p-value on the screen, "
      "rounding the resulting value to 5 decimal places.")

