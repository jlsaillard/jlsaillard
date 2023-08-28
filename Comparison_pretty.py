import csv
import difflib
from difflib import HtmlDiff
import re

# Read the CSV file with tab delimiter and store its content in a list of lists
csv_file_path = 'C:\\Users\\st_je\\OneDrive\\Documents\\Smartcat\\Tools\\BLEU Scores\\output2.txt'
with open(csv_file_path, 'r', newline='') as file:
    reader = csv.reader(file, delimiter='\t')
    rows = [row for row in reader]

# Extract data from columns
column1_data = [row[0] for row in rows]
column2_data = [row[1] for row in rows]

# Initialize the HTMLDiff object
html_diff = HtmlDiff()

# Generate legend 
legend = '<div class="legend">Legend:</div>'

# Initialize HTML 
output_html = "<table>" 

# Insert legend before table
output_html = legend + output_html  

# Loop through rows
for original, compared in zip(column1_data, column2_data):

  # Generate diff HTML
  diff_html = html_diff.make_file([original], [compared])

  # Remove legend
  diff_html = diff_html.replace('<div class="legend">Legend:</div>', '')

  # Add diff HTML to table
  output_html += f"<tr><td>{diff_html}</td></tr>"

output_html += "</table>"

# Save the HTML output to a file
with open('C:\\Users\\st_je\\OneDrive\\Documents\\Smartcat\\Tools\\BLEU Scores\\output11.html', 'w') as output_file:
    output_file.write(output_html)
