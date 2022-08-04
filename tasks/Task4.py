
class Task4():
    @staticmethod
    def process(calls, texts):
        numbers_that_make_calls = list(map(lambda call: call[0], calls))
        numbers_that_receive_calls = list(map(lambda call: call[1], calls))
        numbers_that_send_texts = list(map(lambda text: text[0], texts))

        possible_tele = list(set(numbers_that_make_calls) - set(numbers_that_send_texts) - set(numbers_that_receive_calls))

        print('These numbers could be telemarketers:')

        for num in sorted(possible_tele):
            print(num)
