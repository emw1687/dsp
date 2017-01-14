[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> **Problem Statement**

>> Demonstrate the class size paradox by using NSFG respondent data to compute the actual and biased distributions of number of children under 18 in a households.  

>> **Method**

>> Imported Cycle 6 of the National Survey of Family Growth (NSFG), collected from January 2002 to March 2003 by the US Centers for Disease Control and Prevention (CDC) using code provided in Allen Downey's ThinkStats2 repository
```python
import nsfg
import thinkstats2
resp = nsfg.ReadFemPreg()
```

>> Created an unbiased probability mass function using the number of children under 18 in a household, as reported by the respondents. This represents the actual distribution of children because the respondents are not part of the distribution itself.
```python
actual_pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')
```

>> Simulated the distribution of the number of children under 18 in a household that would have been reported if the children of the household were asked by creating a biased probability mass function.
```python
biased_pmf = BiasPmf(actual_pmf, label='biased')
```

>> **Solution**

>> As shown in the plot below, if children has been asked to report the number of children under 18 in their household, the distribution would not accurately reflect the actual distribution. Families with no children would not have any children to report that no children were present in the family, which families with five children would have five children to report that five children are present in the family. This is further reflected in the means of the distributions: the actual mean is 1.0 children per household while the biased mean is 2.4 children per household.

>> ![NumKids](/statistics/3-1numkids.png)
