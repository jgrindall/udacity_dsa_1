"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from classifiers import PhoneNumberClassifier

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

BANGALORE_AREA_CODE = "080"

def is_fixed_area_code(area_code):
    def F(classification):
        """ is this from a fixed line with the given area code?"""
        return classification["type"] == "fixed" and classification["area_code"] == area_code
    return F

is_fixed_area_code_bangalore = is_fixed_area_code(BANGALORE_AREA_CODE)

def get_receiving_from_area(area_code, calls):
    """ get the classifications of all numbers that were called from a fixed line in the given area """
    data = []
    for call in calls:
        calling_num = call[0]
        receiving_num = call[1]
        calling_classification = PhoneNumberClassifier.classify_number(calling_num)
        if is_fixed_area_code_bangalore(calling_classification):
            data.append(PhoneNumberClassifier.classify_number(receiving_num))
    return data


def get_code(classification):
    return classification["area_code"] if classification["type"] == "fixed" else classification["code"]



bangalore_data = get_receiving_from_area(BANGALORE_AREA_CODE, calls)

#For part A, we need to get the codes we want to print
bangalore_codes = list(map(get_code, bangalore_data))

# remove duplicates
bangalore_codes_uniq = list(dict.fromkeys(bangalore_codes))

print("The numbers called by people in Bangalore have codes:")
#print sorted, one per line
for c in sorted(bangalore_codes_uniq):
    print(c)


# For part B, we filter the array to get those that are made to Bangalore
calls_to_bangalore = list(filter(is_fixed_area_code_bangalore, bangalore_data))

percent = 100 * len(calls_to_bangalore) / len(bangalore_codes)

print('{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(percent))





