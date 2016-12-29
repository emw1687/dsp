"""
faculty_dict = {
    'Ellenberg':[
        ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],
        ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
        ],
    'Li':[
        ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],
        ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],
        ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
        ]
}

professor_dict = {
    ('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],
    ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],
    ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],
    ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],
    ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
}
"""

import csv
import re
import itertools

faculty_dict = dict()
professor_dict = dict()

def print3(x_dict):
    x = itertools.islice(x_dict.items(), 0, 3)
    for key, value in x:
        print key, ':', value

with open('faculty.csv') as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    for row in reader:
        fullname = row['name'].split(' ')
        firstname = fullname[0]
        lastname = fullname[-1]
        title = re.findall('([\w\s]*Professor)', row['title'])
        value = [row['degree'], title[0], row['email']]
        faculty_dict.setdefault(lastname, []).append(value)
        professor_dict[(firstname, lastname)] = value

#Q6. Print "first" 3 key-value pairs of faculty_dict
print3(faculty_dict)

#Q7. Print "first" 3 key-value pairs of professor_dict
print3(professor_dict)

#Q8. Print in alphabetical order by last name
prof_sorted_keys = sorted(professor_dict, key=lambda professor: professor[1])
for professor in prof_sorted_keys:
    print professor, ':', professor_dict[professor]
