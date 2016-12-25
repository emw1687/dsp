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

>> List comprehensions programmatically create lists. For example, the following list comprehension creates a list of integers from 1 to 5.
```python
>>> nums = [x for x in range(1,6)]
>>> print(nums)
[1, 2, 3, 4, 5]
```

>> List comprehensions are also commonly used to create a new list from an existing list, applying the given function to each element of the existing list. (Note that `nums` in the examples below could be replaced with its definition above, thereby creating the "existing" list in the same line of code as creating the "new" list.) The equivalent can be done using `map`, which applies the given function parameter to each element of the iterable parameter. For example, `nums_comp` below is created using list comprehensions while `nums_map` is created using `map`.
```python
>>> nums_comp = [5*x for x in nums]
>>> nums_map = list(map(lambda x: 5*x, nums))
>>> print(nums_comp)
[5, 10, 15, 20, 25]
>>> print(nums_map)
[5, 10, 15, 20, 25]
```

>> Similarly, list comprehensions can create a list equivalent to one created by using both `map` and `filter`. For example, `tens_comp` below is created using list comprehensions while `tens_mf` is created using both `map` and `filter`.
```python
>>> tens_comp = [5*x for x in nums if 5*x%10 == 0]
>>> tens_mf = list(filter(lambda x: x%10 == 0, (map(lambda x: 5*x, nums))))
>>> print(tens_comp)
[10, 20]
>>> print(tens_mf)
[10, 20]
```

>> Set and dictionary comprehensions can also be used to programmatically creates sets and dictionaries, respectively, as shown below.
```python
>>> nums_set = {x for x in nums}
>>> print(nums_set)
set([1, 2, 3, 4, 5])
>>> nums_dict = {x: 5*x for x in nums}
>>> print(nums_dict)
{1: 5, 2: 10, 3: 15, 4: 20, 5: 25}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

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
