import csv

with open('faculty.csv') as facultycsv:
    emails = list() #all email addresses

    for line in facultycsv:
        line = line.split(',')
        if line[0] == 'name' : continue
        try:
            email = line[3].rstrip()
            emails.append(email)
        except:
            continue

with open('emails.csv', 'w') as emailcsv:
    writer = csv.writer(emailcsv, quoting=csv.QUOTE_MINIMAL)
    for email in emails:
        writer.writerow([email])
