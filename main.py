# Write a function that takes in a non-empty string and returns its run-length
# encoding.
# From Wikipedia, "run-length encoding is a form of lossless data compression " \
#                 "in which runs of data are stored as a single data value and " \
#                 "count, rather than as the original run."
# For this problem, a run of data is any sequence of consecutive,
# identical characters. So the run "AAA" would be run-length-encoded as "3A"
# To make things more complicated, however, the input string can contain
# all sorts of special characters, including numbers. And since encoded data
# must be decodable, this means that we can't naively run-length-encode long runs.
# For example, the run "AAAAAAAAAAAA" (12 A s), can't naively be encoded ' \
# as "12A", since this string can be decoded as either "AAAAAAAAAAAA" or "IAA" .
# Thus, long runs (runs of 10 or more characters) should be encoded in a split fashion;
# the aforementioned run should be encoded as "9A3A"
# Sample Input
# string = "AAAAAAAAAAAAABBCCCCDD"
# Sample Output
# "9A4A2B4C2D"

def runLengthEncoding(string):
    new_str = ""
    count = 1
    ptr = 0

    # print("the string is currently: ", string, "------------")

    while ptr < (len(string) - 1):
        if string[ptr] == string[ptr + 1]:
            if count < 9:
                count += 1
            else:
                # count is 9, so add the character to the string and set count to 1
                # add 9 to the string
                # add the character to the string
                new_str = add_to_string(string, new_str, 9, ptr)
                count = 1
        else:
            new_str = add_to_string(string, new_str, count, ptr)
            count = 1
        ptr += 1

    # this is the last character, so add the count & character to the string
    new_str = add_to_string(string, new_str, count, ptr)

    return new_str

    pass

def add_to_string(string, new_str, counter, pointer):
    new_str += chr(counter + ord('0'))
    new_str += string[pointer]
    return(new_str)
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("The result is: ", runLengthEncoding('ABC'))
    print("The result is: ", runLengthEncoding('bbb'))
    print("The result is: ", runLengthEncoding('AAAAAAAAAAAAABBCCCCDD'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
