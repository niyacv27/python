import csv
with open('file3.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print("ID Name")
 print("--------------------")
 for row in data:
   print(row['Id'], row['Name'])
