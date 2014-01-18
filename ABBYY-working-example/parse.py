import re
import csv

# headings = {1:"Asset Code", 2:"Asset and/or Income Source", 3:"Year-End Value of Asset", 4:"Type of Income",
#	    5:"Amount of Income", 6:"Transaction"}

heading = ["Asset Code", "Asset and/or Income Source", "Year-End Value of Asset", "Type of Income", "Amount of Income", "Transaction"]

csv_output = open("output.csv", "w")
writer = csv.writer(csv_output, dialect = 'excel-tab')
writer.writerow(heading)

source = open("output.txt").read()
# Strip the beginning pages that we don't care about
strip_source = re.sub(r'UNITED STATES .* reporting year.', "", source, 0, re.DOTALL|re.MULTILINE)
# Strip the rest on tabs
tabs = re.split(r'\t*', strip_source, 0, re.DOTALL)
row = []
for item in tabs:
	if "\r\n" in item:
		writer.writerow(row)
		block = 1
		row = []
		print ""
	if item is not '\r\n' and item is not "r" and item is not " ' " and item.lstrip() is not "0":
		if "SCHEDULE" not in item and "Page" not in item and "Name" not in item and """ ' """ not in item:
			#print headings[block] + ": " + item
			row.append(item)
			block += 1	

csv_output.close()
