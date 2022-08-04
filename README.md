## Running the project:

Note: python3 -> 'py' for Windows


- To install:
                        
            > git clone https://github.com/jgrindall/udacity_dsa_1.git


- To run some unit tests:

            > python3 -m doctest -v tests.txt


- Task0

            > python3 Task0.py

This is O(1)


- Task2
            
            > python3 Task1.py

Creating the lists is O(n).
Performing the set union is also O(n) since checking if elements exist in a Python set is O(1)
Overall, this is O(n)


            
- Task 2

            > python3 Task2.py

Creating the 'count' object is O(n)
Creating the .items() list is O(n)
Sorting the array is O(n logn)
Overall, this is O(n logn)


- Task 3
            
            > python3 Task3.py
            
            
            > python3 Task4.py


numbers_that_make_calls = list(map(lambda call: call[0], calls))
numbers_that_receive_calls = list(map(lambda call: call[1], calls))
numbers_that_send_texts = list(map(lambda text: text[0], texts))
numbers_that_receive_texts = list(map(lambda text: text[1], texts))

numbers = list(set(numbers_that_make_calls) | set(numbers_that_receive_calls) | set(numbers_that_send_texts) | set(numbers_that_receive_texts))

print('There are: {} different telephone numbers in the records'.format(len(numbers)))
