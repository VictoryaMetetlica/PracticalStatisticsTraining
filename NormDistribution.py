import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

print('\n   Creating normal distribution with a mean of 0 and standard deviation 3')
data = stats.norm(0, 3)
print('\n   Creating an X-axis of 1000 values in the range from -10 to 10')
x = np.linspace(-10, 10, 1000)
print('\n   Creating a cumulative distribution function CDF from values in the interval x')
CDF = data.cdf(x)
plt.figure(figsize=(12, 18))
plt.plot(x, CDF)
plt.title('CDF')
plt.show()
print('\n   Creating a probability density function PDF from values in the interval x')
PDF = data.pdf(x)
plt.plot(x, PDF)
plt.title('PDF')
plt.show()
print('\n   Creating a survival function SF from values in the interval x')
SF = data.sf(x)
plt.plot(x, SF)
plt.title('SF')
plt.show()
print('\n   Creating a percentile point PPF from values in the interval x')
PPF = data.ppf(x)
plt.plot(x, PPF)
plt.title('PPF')
plt.show()
print('\n   Creating an inverse survival function ISF from values in the interval x')
ISF = data.isf(x)
plt.plot(x, ISF)
plt.title('ISF')
plt.show()

print("\n   Calculate the value of the cumulative distribution function at the point x = 46 for a normal distribution with "
      "a mean of 50 and a standard deviation of 2. Display the resulting float value on the screen, rounded to 5 "
      "decimal places.")
print('\n   Creating normal distribution with a mean of 50 and standard deviation 2')
data = stats.norm(50, 2)
print('\n   Creating a cumulative distribution function CDF from values in the interval x')
x = 46
CDF = data.cdf(x)
print(round(CDF, 5))

print("\n   Calculate the value of the survival function at the point x = 34 for a normal distribution with "
      "a mean of 30 and a standard deviation of 4. Display the resulting float value on the screen, rounded to 5 "
      "decimal places.")
data = stats.norm(30, 4)
x = 34
SF = data.sf(x)
print(round(SF, 5))

print("\n   Calculate the value of the probability density function at the point x = 12.11 for a normal distribution with "
      "a mean of 0 and a standard deviation of 4,54. Display the resulting float value on the screen, rounded to 5 "
      "decimal places.")
data = stats.norm(0, 4.54)
x = 12.11
PDF = data.pdf(x)
print(round(PDF, 5))

print("\n   Calculate the probability of a random variable falling within the range from -1 to 2 for a normal distribution with "
      "a mean of 0 and a standard deviation of 1.95. Display the resulting float value on the screen, rounded to 5 "
      "decimal places.")
data = stats.norm(0, 1.95)
x1 = -1
x2 = 2
CDF = data.cdf(x2) - data.cdf(x1)
print(round(CDF, 5))

print("\n   Microcredit organizations have a share of non-performing loans (NPL) in the loan portfolio at an average level "
      "of 7.45% for the sector. The standard deviation is 1.36%. We assume that the distribution is normal. What is the "
      "probability that a randomly selected microcredit organization will have a share of NPL in the portfolio that does "
      "not exceed 8.99%? Display the resulting float value on the screen, rounding to 5 decimal places.")
data = stats.norm(7.45, 1.36)
x = 8.99
CDF = data.cdf(x)
print(round(CDF, 5))

print("\n   There are 876,832 buildings in the city. The standard deviation of the building heights is 5.34 meters. We assume "
      "that the distribution is normal. What is the mean value of the building height distributions if 95% of all "
      "buildings are higher than 48.5 meters? Display the resulting float value on the screen, rounding to 2 decimal places.")
X = 48.5          # the height below which 5% of buildings are located
std_dev = 5.34    # standard deviation
print("\n   Z- value for 5%")
z_value = stats.norm.ppf(0.05)
print("\n   calculating the mean value")
mean_height = X - z_value * std_dev
print(round(mean_height, 2))

print("\n   In the United States, the average annual income of a college-educated worker is $78,970 with a standard "
      "deviation of $13,230, while that of a worker without a college degree is $46,650 with a standard deviation of "
      "$8,110. What is the probability that a randomly selected college-educated worker will have a higher annual income "
      "than a randomly selected worker without a college degree? Assume that the distributions are normal. Display the "
      "resulting float value, rounded to 5 decimal places.")
x1 = 78.97
y1 = 46.65
st_x1 = 13.23
st_y1 = 8.11
z = x1-y1
st_z = (st_x1**2 +st_y1**2)**.5
data = stats.norm(z,st_z)
P_z = data.sf(0)
print(round((P_z), 5))