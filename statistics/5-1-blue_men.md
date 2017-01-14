[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> **Problem Statement**

>> Determine the percentage of the male population eligible to join Blue Man Group, according to the group's height criteria (between 5' 10" and 6' 1").   

>> **Method**

>> Based on the National Center for Chronic Disease Prevention and Health Promotion's 2008 Behavioral Risk Factor Surveillance
System (BRFSS) survey, assumed height is roughly normally distributed with µ = 178 cm and σ = 7.7 cm for men. Generated a normal distribution with those parameters using scipy's stats libary.
```python
import scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
```

>> Wrote a function to convert cm to in, then calculated the difference in cdfs for the ends of the acceptable height range for Blue Man Group.
```python
def to_cm(len_ft, len_in):
    len_cm = len_ft*30.48 + len_in*2.54
    return len_cm

range_min = to_cm(5, 10)
range_max = to_cm(6, 1)

dist.cdf(range_max) - dist.cdf(range_min)
```

>> **Solution**

>> The difference in cdfs above represents the difference between the percentage of men who are 5' 10" or shorter and the percentage of men who are 6' 1" or shorter. This difference represents the percentage of men whose height falls within the Blue Man Group's height criteria, which is 34%.
