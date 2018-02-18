import csv
import re

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

with open('csclub-comment.csv', "rt") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	emailscsv = open('emails.csv', 'w', newline='')
	writer = csv.writer(emailscsv)
	for row in spamreader:
		if row:
			email = emoji_pattern.sub(r'', row[0])
			if re.match(r"[^@]+@[^@]+\.[^@]+", email):
				writer.writerow([email])

