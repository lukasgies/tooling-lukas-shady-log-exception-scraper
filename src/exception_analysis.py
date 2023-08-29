import re
import sys
from collections import Counter


def extract_exceptions(log_file_path, pattern_before_exception):
    additional_info = []

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = re.search(fr'{pattern_before_exception}.*?Exception: (.+)', line)
            if match:
                exception_message = match.group(1)
                exception_parts = exception_message.split(":")
                if len(exception_parts) > 1:
                    additional_info.append(':'.join(exception_parts[1:]))

    return additional_info


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

    additional_info = extract_exceptions(log_file_path, pattern_before_exception)
    additional_info_counter = Counter(additional_info)

    total_info = len(additional_info)
    print(f"Total exceptions: {total_info}\n")

    print("Different exceptions and their counts (highest count first):")
    sorted_info = sorted(additional_info_counter.items(), key=lambda x: x[1], reverse=True)
    for info, count in sorted_info:
        print(f"{count} - {info}")
