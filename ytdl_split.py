import os
import csv

# list of files
path = r'C:\\Users\...'
files = os.listdir(path)
#print("Files at {}: {}". format(path,files))

columns = ['channel', 'title', 'date', 'duration',
           'view_count', 'like count']
rows = [part.split("-ghj-") for part in files]

for row in rows:
    # row[3] = str(int(row[3])//60)
    year = row[2][:4]
    month = row[2][4:6]
    day = row[2][6:]
    row[2] = '-'.join([year, month, day])
    row[7] = row[7].split('.')[0]

print(rows)

with open('FILENAME.csv', 'w', encoding='utf8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    writer.writerows(rows)
