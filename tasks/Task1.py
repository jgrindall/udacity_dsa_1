
class Task1():
    @staticmethod
    def process(calls, texts):
        numbers_that_make_calls = list(map(lambda call: call[0], calls))
        numbers_that_receive_calls = list(map(lambda call: call[1], calls))
        numbers_that_send_texts = list(map(lambda text: text[0], texts))
        numbers_that_receive_texts = list(map(lambda text: text[1], texts))

        numbers = list(set(numbers_that_make_calls) | set(numbers_that_receive_calls) | set(numbers_that_send_texts) | set(numbers_that_receive_texts))

        print('There are: {} different telephone numbers in the records'.format(len(numbers)))
