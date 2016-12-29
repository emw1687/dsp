import string
import re

degrees = list() #degrees and frequencies
titles = list() #titles and frequencies
emails = list() #all email addresses
domains = set() #unique email domains

def count_list(things):
    count_dict = dict()
    for thing in things:
        count_dict[thing] = count_dict.get(thing,0)+1
    return count_dict

def print_counts(count_dict):
    for item in sorted(count_dict):
        print item, count_dict[item]

def print_list(things):
    for thing in things:
        print thing

with open("faculty.csv") as facultycsv:
    for line in facultycsv:
        line = line.split(',')
        if line[0] == 'name' : continue
        try:
            degree = line[1].translate(None, string.punctuation)
            degrees.extend(re.findall('\s*([A-Za-z]+)\s*', degree))
            title = re.findall('([\w\s]*Professor)', line[2])
            titles.append(title[0])
            email = line[3].rstrip()
            emails.append(email)
            domain = re.findall('\S+@(\S+)', email)
            domains.add(domain[0])
        except:
            continue

degrees_count = count_list(degrees)
titles_count = count_list(titles)

print 'Q1. Degrees and frequencies'
print_counts(degrees_count)
print 'Q2. Titles and frequencies'
print_counts(titles_count)
print 'Q3. Emails'
print_list(emails)
print 'Q4. Unique Domains'
print_list(domains)
