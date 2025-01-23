from numpy.random import seed
from numpy.random import poisson
from numpy.random import normal
from numpy.random import lognormal
from scipy.stats import shapiro

print("The Shapiro-Wilk test is based on the correlation between our data and the corresponding normally distributed "
      "values and provides higher power than the K-S test even after taking into account the Lilliefors correction."
      " When p-value < 0.01, we can reject the null hypothesis of normality of the data.")

print("\n   Conduct the Shapiro-Wilk test for normality of data")

    # initialize the pseudo-random number generator
seed(0)
    # generate 100 values that have a Poisson distribution with lambda equal to 5
data = poisson(5, 100)
    # running the Shapiro-Wilk test to see if the distribution (data) is normal
print(shapiro(data))

print("\n   Test a sample of 100 values distributed in a standard normal manner (seed(0) pseudorandom number generator)"
      " for normality. Use the Shapiro-Wilk test. Print the resulting p-value to the screen.")

    # initialize the pseudo-random number generator
seed(0)
    # generate 100 values that have a normal distribution
data = normal(0, 1, 100)
    # running the Shapiro-Wilk test to see if the distribution (data) is normal
print(shapiro(data).pvalue)

print("\n   Test the normality of a sample of 10,000 values that have a lognormal distribution with a mean of 1 and "
      "a standard deviation of 13.22 (seed(0) pseudorandom number generator). Use the Shapiro-Wilk test. Display "
      "the resulting Shapiro-Wilk statistic (statistic) on the screen, rounded to 5 decimal places.")

    # initialize the pseudo-random number generator
seed(0)
    # generate 10 000 values that have a lognormal distribution
data = lognormal(1, 13.22, 10000)
    # running the Shapiro-Wilk test to see if the distribution (data) is normal
print(shapiro(data).statistic.__round__(5))