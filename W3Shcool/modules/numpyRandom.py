print("---------------Random Numbers in NumPy-----------------")
from numpy import random
import numpy as np
print("---------------Random integer -----------------")
x = random.randint(100)
print(x)
print("---------------Generate Random Float-----------------")
x = random.rand()
print(x)
print("---------------Generate Random Array-----------------")
x=random.randint(100, size=(5))
print(x)
print("---------------Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:-----------------")
x = random.randint(100, size=(3, 5))
print(x)
print("---------------Generate Random Number From Array-----------------")
x = random.choice([3, 5, 7, 9])
print(x)
print("---------------Generate a 2-D array that consists of the values in the array -----------------")
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)
print("---------------Random Data Distribution-----------------")
# Data Distribution is a list of all possible values, and how often each value occurs.
# Such lists are important when working with statistics and data science.
# The random module offer methods that returns randomly generated data distributions.
# Random Distribution
# A random distribution is a set of random numbers that follow a certain probability density function.
# Probability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.
# We can generate random numbers based on defined probabilities using the choice() method of the random module.
# The choice() method allows us to specify the probability for each value.
# The probability is set by a number between 0 and 1, where 0 means that the value will never occur and 1 means that the value will always occur.
print("---------Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.---------")
# The probability for the value to be 3 is set to be 0.1
# The probability for the value to be 5 is set to be 0.3
# The probability for the value to be 7 is set to be 0.6
# The probability for the value to be 9 is set to be 0
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)
print("---------Same example as above, but return a 2-D array with 3 rows, each containing 5 values---------")
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)
print("---------Random Permutations---------")
# A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
# The NumPy Random module provides two methods for this: shuffle() and permutation()
print("---------Shuffling Arrays---------")
# The shuffle() method makes changes to the original array.
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)
print("---------Generating Permutation of Arrays---------")
# The permutation() method returns a re-arranged array (and leaves the original array un-changed).
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))
print("---------Visualize Distributions With Seaborn---------")
# Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
print("---------pip install seaborn---------")
print("---------Distplots---------")
# Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()
print("---------Plotting a Distplot Without the Histogram---------")
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()
# Note: We will be using: sns.distplot(arr, hist=False) to visualize random distributions in this tutorial.
print("---------Normal (Gaussian) Distribution---------")
# The Normal Distribution is one of the most important distributions.
# It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.
# It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.
# Use the random.normal() method to get a Normal Data Distribution.
# It has three parameters
# loc - (Mean) where the peak of the bell exists.
# scale - (Standard Deviation) how flat the graph distribution should be.
# size - The shape of the returned array.
x = random.normal(size=(2, 3))
print(x)
print("-----Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:----")
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)
print("---------Visualization of Normal Distribution--------")
sns.distplot(random.normal(size=1000), hist=False)
plt.show()
# Note: The curve of a Normal Distribution is also known as the Bell Curve because of the bell-shaped curve.
print("---------Binomial Distribution--------")
# Binomial Distribution is a Discrete Distribution.
# It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.
# It has three parameters:
# n - number of trials.
# p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
# size - The shape of the returned array.
# Discrete Distribution:The distribution is defined at separate set of events, e.g. a coin toss's result is discrete as it can be only head or tails whereas height of people is continuous as it can be 170, 170.1, 170.11 and so on
x = random.binomial(n=10, p=0.5, size=10)
print(x)
print("---------Visualization of Binomial Distribution--------")
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()
print("---------Difference Between Normal and Binomial Distribution--------")
# The main difference is that normal distribution is continous whereas binomial is discrete, but if there are enough data points it will be quite similar to normal distribution with certain loc and scale.
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()
print("---------Poisson Distribution--------")
# Poisson Distribution is a Discrete Distribution.
# It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?
# It has two parameters:
# lam - rate or known number of occurrences e.g. 2 for above problem.
# size - The shape of the returned array.
x = random.poisson(lam=2, size=10)
print(x)
print("---------Visualization of Poisson Distribution--------")
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()
print("---------Difference Between Normal and Poisson Distribution--------")
# Normal distribution is continuous whereas poisson is discrete.
# But we can see that similar to binomial for a large enough poisson distribution it will become similar to normal distribution with certain std dev and mean.
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
plt.show()
print("---------Difference Between Binomial and Poisson Distribution--------")
# Binomial distribution only has two possible outcomes, whereas poisson distribution can have unlimited possible outcomes.
# But for very large n and near-zero p binomial distribution is near identical to poisson distribution such that n * p is nearly equal to lam.
sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
plt.show()
print("---------Uniform Distribution--------")
# Used to describe probability where every event has equal chances of occuring.
# E.g. Generation of random numbers.
# It has three parameters:
# a - lower bound - default 0 .0.
# b - upper bound - default 1.0.
# size - The shape of the returned array.
x = random.uniform(size=(2, 3))
print(x)
print("---------Visualization of Uniform Distribution--------")
sns.distplot(random.uniform(size=1000), hist=False)
plt.show()
print("---------Logistic Distribution--------")
# Logistic Distribution is used to describe growth.
# Used extensively in machine learning in logistic regression, neural networks etc.
# It has three parameters:
# loc - mean, where the peak is. Default 0.
# scale - standard deviation, the flatness of distribution. Default 1.
# size - The shape of the returned array
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)
print("---------Visualization of Logistic Distribution--------")
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()
print("---------Difference Between Logistic and Normal Distribution--------")
# Both distributions are near identical, but logistic distribution has more area under the tails, meaning it represents more possibility of occurrence of an event further away from mean.
# For higher value of scale (standard deviation) the normal and logistic distributions are near identical apart from the peak.
sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')
plt.show()
print("---------Multinomial Distribution--------")
# Multinomial distribution is a generalization of binomial distribution.
# It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.
# It has three parameters:
# n - number of possible outcomes (e.g. 6 for dice roll).
# pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
# size - The shape of the returned array.
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)
# Note: Multinomial samples will NOT produce a single value! They will produce one value for each pval.
# Note: As they are generalization of binomial distribution their visual representation and similarity of normal distribution is same as that of multiple binomial distributions.
print("---------Exponential Distribution--------")
# Exponential distribution is used for describing time till next event e.g. failure/success etc.
# It has two parameters:
# scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
# size - The shape of the returned array.
x = random.exponential(scale=2, size=(2, 3))
print(x)
print("---------Visualization of Exponential Distribution--------")
sns.distplot(random.exponential(size=1000), hist=False)
plt.show()
# Relation Between Poisson and Exponential Distribution
# Poisson distribution deals with number of occurences of an event in a time period whereas exponential distribution deals with the time between these events.
print("---------Chi Square Distribution--------")
# Chi Square distribution is used as a basis to verify the hypothesis.
# It has two parameters:
# df - (degree of freedom).
# size - The shape of the returned array.
x = random.chisquare(df=2, size=(2, 3))
print(x)
print("---------Visualization of Chi Square Distribution--------")
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()
print("---------Rayleigh Distribution--------")
# Rayleigh distribution is used in signal processing.
# It has two parameters:
# scale - (standard deviation) decides how flat the distribution will be default 1.0).
# size - The shape of the returned array.
x = random.rayleigh(scale=2, size=(2, 3))
print(x)
print("---------Visualization of Rayleigh Distribution--------")
sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()
# Similarity Between Rayleigh and Chi Square Distribution
# At unit stddev and 2 degrees of freedom rayleigh and chi square represent the same distributions.
print("---------Pareto Distribution--------")
# A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).
# It has two parameter:
# a - shape parameter.
# size - The shape of the returned array.
x = random.pareto(a=2, size=(2, 3))
print(x)
print("---------Visualization of Pareto Distribution--------")
sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()
print("---------Zipf Distribution--------")
# Zipf distributions are used to sample data based on zipf's law.
# Zipf's Law: In a collection, the nth common term is 1/n times of the most common term. E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.
# It has two parameters:
# a - distribution parameter.
# size - The shape of the returned array
x = random.zipf(a=2, size=(2, 3))
print(x)
print("---------Visualization of Zipf Distribution--------")
x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)
plt.show()

