import csv
import Levenshtein

def read_csv(csv_path, delimiter=','):
    references = []
    candidates = []
    
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delimiter)
        for row in csvreader:
            if len(row) == 2:  # Assuming two columns: reference and candidate
                references.append(row[0])  # Reference
                candidates.append(row[1])  # Candidate
    
    return references, candidates

csv_path = 'C:\\Users\\st_je\\OneDrive\\Documents\\Smartcat\\Tools\\BLEU Scores\\Fillable CDS Authorizations - AM Google.txt'
references, candidates = read_csv(csv_path, delimiter='\t')  # Change delimiter if needed

total_levenshtein_distance = 0
num_samples = len(references)

for ref, cand in zip(references, candidates):
    levenshtein_distance = Levenshtein.distance(ref, cand)
    total_levenshtein_distance += levenshtein_distance

average_levenshtein_distance = total_levenshtein_distance / num_samples
# Round the Levenshtein distance to two decimal places
average_levenshtein_distance_rounded = round(average_levenshtein_distance, 2)

print("Average Levenshtein distance (rounded to 2 decimals):", average_levenshtein_distance_rounded)
