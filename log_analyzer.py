import os
import sys
from typing import List
def most_used_test_type(log_lines):
    """
    Finds the most used type of test

    :param log_lines: list of string log lines 
    :return: string name of the kind of most used test

    TODO: implement this
    """
    tests_count = {
        "Performance": 0,  
        "Functional": 0,
        "System": 0, 
    }
    unique_tests = list(tests_count.keys())
    for log_lines in log_lines:
        for test in unique_tests:
            if test in log_lines:
                tests_count[test] += 1
    print(tests_count)
    return max(tests_count,key=lambda x: tests_count[x])
 



def failure_map(log_lines):
    """
    Count the failures per test type. A test failure has the word "FAIL" in 
    the test output.

    :param log_lines: list of string log lines
    :return: dictionary mapping test type (string) to number of failures

    Currently, returns count of 0 for each type
    TODO: implement this correctly
    """
    failures = {
        "Performance": 0,  
        "Functional": 0,
        "System": 0, 
    }
    unique_tests = list(failures.keys())
    for log_lines in log_lines:
        for test in unique_tests:
            if (test in log_lines)  and ("FAIL" in log_lines):
                
                failures[test] += 1
    return failures

def count_tests(log_lines):
    return len(log_lines)

def format_failures(results):
    """
    Format the failure counts table

    :param results: Dict mapping types to failure counts
    :return: string formatted table of failures 
    """

    table = [f"Type\t\tCount"]
    for test_type, count in results.items():
        table.append(f"{test_type}  \t{count}")
    return "\n".join(table)


def count_phrase(log_lines, phrase):
    """
    Count the occurrences of a phrase in the log lines

    :param log_lines: list of string log lines
    :param phrase: string phrase to match
    :return: integer count of lines that match the phrase
    """
    count = 0
    for test_line in log_lines:
        if phrase in test_line:
            count += 1
    return count


def analyze_logs(log):
    """
    Analyze the lines of the log file

    :param log: string with all the log lines
    :return: string summary of analysis
    """
    log_lines = log.splitlines()
    phrase = "component"
    test_count = count_tests(log_lines)
    most_used_type = most_used_test_type(log_lines)
    failure_table = failure_map(log_lines)
    phrase_count = count_phrase(log_lines, phrase)

    return f"""Number of tests: {test_count}
Most used type of test: {most_used_type}
Tests related to \"{phrase}\": {phrase_count}

Failures:
{format_failures(failure_table)}
"""

def write_stats(report, destination):
    """
    Write the report to a destination file
    """
    with open(file=destination, mode='w') as dest:
        dest.write(report)


if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python log_analyzer.py [input_file] [output_file]")
        exit()

    input_filename = sys.argv[1]
    with open(input_filename) as f:
        report = analyze_logs(f.read())
    if len(sys.argv) == 2:
        print(report)
    elif len(sys.argv) == 3:
        output_file = sys.argv[2] 
        write_stats(report, output_file)

# collaborated with victor and chris to get this done.