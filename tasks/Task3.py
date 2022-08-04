from classifiers import PhoneNumberClassifier

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

class Task3():
    @staticmethod
    def process(calls, texts):

        bangalore_data = get_receiving_from_area(BANGALORE_AREA_CODE, calls)

        #For part A, we need to get the codes
        bangalore_codes = list(map(get_code, bangalore_data))

        # remove duplicates
        bangalore_codes_uniq = list(set(bangalore_codes))

        print("The numbers called by people in Bangalore have codes:")
        #sorted, one per line
        for c in sorted(bangalore_codes_uniq):
            print(c)

        # For part B, we filter the array to get those that are made to Bangalore
        calls_to_bangalore = list(filter(is_fixed_area_code_bangalore, bangalore_data))

        percent = 100 * len(calls_to_bangalore) / len(bangalore_codes)

        print('{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(percent))


