"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts, receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

numbers_that_make_calls = list(map(lambda call: call[0], calls))
numbers_that_receive_calls = list(map(lambda call: call[1], calls))
numbers_that_send_texts = list(map(lambda text: text[0], texts))

possible_tele = list(set(numbers_that_make_calls) - set(numbers_that_send_texts) - set(numbers_that_receive_calls))

print('These numbers could be telemarketers:')

for num in sorted(possible_tele):
    print(num)