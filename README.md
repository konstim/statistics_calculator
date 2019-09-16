# StatisticsCalculator
   
   Calculates summation, average or median of numbers. It is also possible to
   compare result of this mathematical calculation with a statement and reference
   number.

1. Install Python with official instructions at [Python Setup and Usage](https://docs.python.org/3/using/index.html)

   Make sure that you install Python version 3.

2. Go to directory where 'statistics_calculator.py' exists

3. Create a text file that has at least one number. Two or more numbers should
   be separated with newline.

4. Call the statistics_calculator module with arguments:
  * file.txt with numbers (',' is not currently supported in number definitions)
  * sum | avg | median
  * optional argument: statement 'lg', 'gt' or 'eq' with reference number

## About arguments

   First argument 'file.txt' should point to a file that has numbers - each separated with
   newline ('\n'). Program only knows about absolute references to files so it
   is recommended to be used. Second argument is choice of summation, average or median
   calculation that follows respective mathematical result. Optional argument
   should be combined with a reference number that is used basis for comparison
   with result of 'sum', 'avg' or 'median' calculation. Calculation of median
   follows traditional way of calculating median [Wikipedia site of
   median](https://en.wikipedia.org/wiki/Median#Finite_set_of_numbers)


## Example usage:

  * Sum of numbers: Run 'python statistics_calculator.py sum text_file' to get
    sum of numbers in text_file.
  * Average of numbers: Run 'python statistics_calculator.py avg text_file' to
    get average of numbers in text_file.
  * Median of numbers: Run 'python statistics_calculator.py median text_file' to
    get median of numbers in text_file.
  * Sum of numbers and comparison with reference number '999': Run 'python
    statistics_calculator.py sum text_file eq 999' to get sum of numbers in
    text_file. Program also outputs result of comparison between sum and number
    '999'.
## How to get help

   Run python statistics_calculator.py to get more help with program.
