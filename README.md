# tooling-lukas-shady-log-exception-scraper
In essence, this script helps you quickly analyze exception messages in a log file and identify the most common additional information snippets associated with those exceptions. The script can be run from the command line, allowing you to provide custom log file paths and patterns for different types of log files.

## Usage
Call the script like this:

```bash
$ py exception_analysis.py /path/to/log/file.log prefix_pattern
```

- **path**: The path to the log file that should be scraped
- **prefix pattern**: A string that should occur before the 'Exception' keyword in the log line

## Output
This script should output the total amount of lines to contain exceptions and the amount of each individual exception 
somewhat like this:

````asciidoc
Total exceptions: 207

Different exceptions and their counts (highest count first):
60 -  JDBC exception executing SQL [select a FROM b]
55 -  must not be null
50 -  Could not commit transaction.
35 -  End-of-File, expected line at offset 0
7 -  Conflict
````

## Disclaimer
This script was quickly hacked together in is in no means something like 'production ready'. The only goal was to provide
a quick tool for myself to analyze big log files and group the occuring exceptions somewhat together. This does not have
to be perfekt at all. Future refinements of the analyzer may happen.