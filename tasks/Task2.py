
class Task2():
    @staticmethod
    def process(calls, texts):
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
