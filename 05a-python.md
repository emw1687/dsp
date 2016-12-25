# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both groups of values, which are indexed by integers. However, lists changes be changed (i.e. they are mutable) while tuples cannot (i.e. they are immutable).

>> For this reason, tuples will work as keys in dictionaries while lists will not. Dictionaries are unordered groups of key-value pairs; key-value pairs are associated with each other using a hash function. Keys are passed to a hash function, which returns a hash value. The hash value is then used to quickly find the value of the key.

>> The issue arises due to the mutability of lists. If a key in the list of keys is changed, then the hash function may not return the correct hash value and the key's value may not be found.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both groups of values. List, however, are ordered and indexed but integers, while sets are unordered. Lists may contain duplicate values but lists only contain unique values.

>> A list could store the individual pieces of fruit that are in the fridge:
```python
>>> fruits = ['grape', 'grape', 'grape', 'apple', 'peach', 'kiwi', 'kiwi']
```

>> A set could store the unique types of fruit that are in the fridge:
```python
>>> fruit_type = set(fruits)
>>> print(fruit_type)
set(['grape', 'apple', 'peach', 'kiwi'])
```

>> Sets perform better than lists for finding an element, because sets use hash tables while lists do not. To find an element in a list, each item must be checked sequentially. The speed therefore depends on the size of the list, and performance decreases as the length of the list increases.

>> To find an element in a set, however, only the element's position in the hash table is checked. Therefore the speed of this operation does not depend on the size of the set, and performance does not decrease as the length of the set increases.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is Python's anonymous function construct. Lambda functions may contain only one expression and always return a value. Lambda functions are useful in situations when a single function is needed just once; rather than define a named function and call it, a lambda function may be defined and used directly at the point where the function is needed.

>>A lambda function could be used with the built-in `sorted` function to change which parameter is used for sorting. For example, the following list stores tuples of the names of the months and their corresponding number.
```python
>>> months = [
  (1, 'January'),
  (2, 'February'),
  (3, 'March'),
  (4, 'April'),
  (5, 'May'),
  (6, 'June'),
  (7, 'July'),
  (8, 'August'),
  (9, 'September'),
  (10, 'October'),
  (11, 'November'),
  (12, 'December'),
]
```
>>Calling `sorted` without a `key` function returns a list sorted by the first item in each tuple.
```python
>>> sorted(months)
[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]
```
>> A lambda function could be used in the `key` argument to sort the list alphabetically by the name of the months, or the second item in each tuple.
```python
>>> sorted(months, key=lambda month: month[1])
[(4, 'April'), (8, 'August'), (12, 'December'), (2, 'February'), (1, 'January'), (7, 'July'), (6, 'June'), (3, 'March'), (5, 'May'), (11, 'November'), (10, 'October'), (9, 'September')]
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)
