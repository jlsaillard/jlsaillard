import csv
import difflib
from difflib import HtmlDiff

# Read the CSV file and store its content in a list of lists
csv_file_path = 'C:\\Users\\st_je\\OneDrive\\Documents\\Smartcat\\Tools\\BLEU Scores\\output2.txt'
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    rows = [row for row in reader]

# Transpose the rows to get columns
columns = zip(*rows)

# Initialize the HTMLDiff object
html_diff = HtmlDiff()

# Generate HTML with differences highlighted for each column
output_html = ""
for column in columns:
    original = list(column)
    compared = list(column)  # This is where you would have your updated data
    diff_html = html_diff.make_table(original, compared)
    output_html += diff_html

# Save the HTML output to a file
output_file_path = 'C:\\Users\\st_je\\OneDrive\\Documents\\Smartcat\\Tools\\BLEU Scores\\output2.html'  # Specify the desired file path here
print("Output file path:", output_file_path)  # Print the path for debugging
try:
    with open(output_file_path, 'w') as output_file:
        output_file.write(output_html)
    print("Output file created successfully.")
except Exception as e:
    print("Error:", e)
