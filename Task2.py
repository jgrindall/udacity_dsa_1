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
    call_length = int(call[3])
    calling_num = call[0]
    receiving_num = call[1]
    count[calling_num] = (count[calling_num] + call_length) if (calling_num in count) else call_length
    count[receiving_num] = (count[receiving_num] + call_length) if (receiving_num in count) else call_length

# sort them
sorted_count = sorted(count.items(), key = lambda item: -item[1])

# this is the one with longest total duration
longest_time = sorted_count[0]

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(longest_time[0], longest_time[1]))