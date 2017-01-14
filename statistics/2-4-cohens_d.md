[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> **Problem Statement**

>> Determine whether babies both first (first babies) are lighter or heavier than babies who are not born first (other babies).

>> **Method**

>> Imported Cycle 6 of the National Survey of Family Growth (NSFG), collected from January 2002 to March 2003 by the US Centers for Disease Control and Prevention (CDC) using code provided in Allen Downey's ThinkStats2 repository
```python
import nsfg
preg = nsfg.ReadFemPreg()
```

>> Created a dataframe of live births, then subseqently created additional dataframes for first births and other births
```python
#live births indicated by outcome = 1
live = preg[preg.outcome == 1]
#first babies indicated by birthord = 1
firsts = live[live.birthord == 1]
#other babies indicated by birthord other than 1
others = live[live.birthord != 1]
```

>> Wrote a function to calculate Cohen's effect size
```python
import numpy as np
#function to compute Cohen's D
def summary(group):
    mean = group.mean()
    std = group.std()
    var = group.var()
    return mean, std, var
def cohen_d(group_a, group_b):
    mean_a, std_a, var_a = summary(group_a)
    mean_b, std_b, var_b = summary(group_b)
    std_pooled = np.sqrt((std_a**2 + std_b**2)/2)
    d = (mean_a - mean_b)/std_pooled
    return d
```

>> Calculated Cohen's effect size for mean weight of first babies and the mean weight of other babies
```python
cohen_d(firsts.totalwgt_lb, others.totalwgt_lb)
```

>> **Solution**

>> Based on Cohen's d, the difference in means between first babies and other babies was calculated to be -0.089 standard deviations. The negative value can be interpreted to mean that first babies tend to be lighter than other babies; however, the absolute value is less than  0.2, indicating that the effect size is small. Therefore, first babies tend to be lighter, but not significantly so.
