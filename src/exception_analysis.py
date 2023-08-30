import re
import sys
from collections import Counter


def extract_exceptions(log_file_path, pattern_before_exception):
    exceptions = []

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = re.search(fr'{pattern_before_exception}.*?Exception: (.+)', line)
            if match:
                exception_message = match.group(1)
                exception_parts = exception_message.split(":")
                if len(exception_parts) > 1:
                    exceptions.append(':'.join(exception_parts[1:]))

    return exceptions


if __name__ == "__main__":
    default_log_file_path = "<default-file-path>"
    default_pattern_before_exception = "<default-prefix-pattern>"

    if len(sys.argv) > 1:
        log_file_path = sys.argv[1]
    else:
        log_file_path = default_log_file_path

    if len(sys.argv) > 2:
        pattern_before_exception = sys.argv[2]
    else:
        pattern_before_exception = default_pattern_before_exception

    print(f"Log File: {log_file_path}\n")  # Print the log file name

    exceptions = extract_exceptions(log_file_path, pattern_before_exception)
    exceptions_counter = Counter(exceptions)

    total_exceptions = len(exceptions)
    print(f"Total exceptions: {total_exceptions}\n")

    print("Different exceptions and their counts (highest count first):")
    sorted_exceptions = sorted(exceptions_counter.items(), key=lambda x: x[1], reverse=True)
    for exception, count in sorted_exceptions:
        print(f"{count} - {exception}")
