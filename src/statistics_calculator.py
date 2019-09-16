import sys
import os
import re
import statistics

NUMBER_PATTERN = re.compile(r"^\-?\d+(\.|,)?\d*$")

filename = None
FILE = None
operation = None
compOp = None
refValue = None
compOpsInputted = False
numbers = []
calc_result = None

args = sys.argv


def validateInput(inputArgs):
    args_length = len(inputArgs)

    if validateFile(inputArgs[1]):
        if (args_length == 3):
            if not (validateOp(inputArgs[2])):
                sys.stderr.write("Inputted operation '{0}'\
                    is not allowed".format(inputArgs[2]))
                exit()

        elif (args_length == 5):
            if not (validateOp(inputArgs[2])
                    and validateCompOp(inputArgs[3])
                    and validateRefValue(inputArgs[4])):

                sys.stderr.write(
                    "There is something wrong with inputted values '{0}', '{1}'\
                        and '{2}'".format(inputArgs[2],
                                        inputArgs[3],
                                        inputArgs[4])
                                        )
                exit()
    else:
        showUsage()


def validateFile(f):
    try:
        with open(f) as fileStream:
            return fileStream.readable()
    except OSError:
        return False


def validateOp(operation):
    return (operation == "sum" or operation == "avg" or operation == "median")


def validateCompOp(compOp):
    return (compOp == "lt" or compOp == "gt" or compOp == "eq")


def validateRefValue(refValue):
    try:
        f = float(refValue)
        return (type(f) is float)
    except ValueError:
        print("Error: value '{0}' of n is not a number".format(refValue))
        return False


def showUsage():
    print(
        """
          Usage:   {} <file_name> <sum|avg|median> [<gt|lt|eq> <n>

          file_name       file that contains numbers on each row
          sum|avg|median  calculation operation
          gt|lt|eq        comparison operator (optional)
          n               reference value that is used to compare numbers to
                          (needed when comparison operator is defined)
        """.format(os.path.basename(__file__))
        )


def read_numbers(file):
    with open(file, "r") as dataFile:
        numbers = []

        for line in dataFile:
            if (re.match(NUMBER_PATTERN, line)):
                number = float(line)
                numbers.append(number)

    return numbers


def calculate_sum(numbers):
    return sum(numbers)


def calculate_avg(numbers):
    return calculate_sum(numbers) / len(numbers)


def calculate_median(numbers):
    return statistics.median(numbers)


# operation selection
def select_operation(opCode, data):
    result = None

    if opCode == "sum":
        result = calculate_sum(data)
        print("Sum is", result)
    elif opCode == "avg":
        result = calculate_avg(data)
        print("Average is", result)
    elif opCode == "median":
        result = calculate_median(data)
        print("Median is", result)
    return result


# comparison operations
def compare(comp_operator, number, refValue):
    if comp_operator == "lt":
        if number < refValue:
            print(number, "is less than", refValue)
        else:
            print(number, "is not less than", refValue)
    elif comp_operator == "gt":
        if number > refValue:
            print(number, "is greater than", refValue)
        else:
            print(number, "is not greater than", refValue)
    elif comp_operator == "eq":
        if number == refValue:
            print(number, "equals with", refValue)
        else:
            print(number, "does not equal with", refValue)


if __name__ == "__main__":
    args_len = len(args)

    if (args_len == 3):
        validateInput(args)
        filename = args[1]
        operation = args[2]
        numbers = read_numbers(filename)
        select_operation(operation, numbers)

    elif (args_len == 5):
        validateInput(args)
        filename = args[1]
        operation = args[2]
        compOp = args[3]
        refValue = float(args[4])
        numbers = read_numbers(filename)
        calc_result = select_operation(operation, numbers)
        compare(compOp, calc_result, refValue)
    else:
        showUsage()
        exit()
