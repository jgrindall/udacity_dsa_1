import re

regexp_fixed_line = r'^\s*\(([0-9]+)\)([0-9]+)\s*$'
#area code is the first capured group

regexp_mobile = r'^\s*([7-9]{1})([0-9]{3,}) ([0-9]+)\s*$'
# mobile code is the first 4 digits, always starting with 7,8,9

regexp_tele = r'^\s*140([0-9]+)\s*$'
#start with code 140

class PhoneNumberClassifier():

    """
    classify phone numbers according to their type
    """

    @staticmethod
    def classify_number(num: str):
        """Return an object that describes a phone number"""
        groups = None
        if re.match(regexp_fixed_line, num):
            groups = re.findall(regexp_fixed_line, num)
            return {"type": "fixed", "area_code":groups[0][0], "number": groups[0][1]}
        elif re.match(regexp_mobile, num):
            groups = re.findall(regexp_mobile, num)
            code = groups[0][0] + groups[0][1]
            if len(code) >= 5:
                code = code[0:4]
            return {"type": "mobile", "code":code}
        elif re.match(regexp_tele, num):
            groups = re.findall(regexp_tele, num)
            return {"type": "tele", "number":groups[0]}
        
        # fail
        raise ValueError("Number is not classifiable")

