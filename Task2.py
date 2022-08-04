"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

count = {}

for call in calls:
    calling_num = call[0]
    receiving_num = call[1]
    count[calling_num] = (count[calling_num] + 1) if (calling_num in count) else 1
    count[receiving_num] = (count[receiving_num] + 1) if (receiving_num in count) else 1
    

sorted_count = sorted(count.items(), key = lambda item: -item[1])

print(sorted_count[0])
