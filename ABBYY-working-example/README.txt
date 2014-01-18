Example of parsing Financial Disclosure tables using the ABBYY Cloud OCR SDK. 
Note that this is the result of extremely limited experimentation without a 5 hour period.

N00029139_2012.pdf - example PDF file

curl_recognize.sh - bash script provided by ABBYY to convert file using their API.
Look inside for usage, but you need to set your Application ID and Password in environment variables.
Example usage is ./curl_recognize.sh N00029139.pdf output.txt -f txt, which converts the 
example file into txt format.

output.txt - output from above command

parse.py - Python script to strip unnecessary pages and data, and write tab delimited. Opens
output.txt and writes output.csv. Don't look inside if you don't like bad code. It is
VERY hard coded to the example PDF, and should only serve as a general prototype for 
developing a general solution.

output.tsv - output from parse.py (renamed to .tsv extension for Excel) showing what
can be done to parse Financial Disclosure data. 
