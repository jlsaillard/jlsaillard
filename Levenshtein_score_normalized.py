import csv
import Levenshtein
import statistics


def read_csv(csv_path, delimiter=','):
    pairs = []
    
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delimiter)
        for row in csvreader:
            if len(row) == 2:  # Assuming two columns: string1 and string2
                pairs.append((row[0], row[1]))
    
    return pairs

def normalized_levenshtein_similarity(string1, string2):
    levenshtein_distance = Levenshtein.distance(string1, string2)
    max_length = max(len(string1), len(string2))
    normalized_similarity = 1 - (levenshtein_distance / max_length)
    return normalized_similarity

csv_path = 'C:\\Users\\st_je\\OneDrive\\Documents\\Smartcat\\Tools\\BLEU Scores\\Consent of Mother - GPT Legal.txt'
pairs = read_csv(csv_path, delimiter='\t')  # Change delimiter if needed

total_normalized_score = 0
num_pairs = len(pairs)

for string1, string2 in pairs:
    normalized_similarity = normalized_levenshtein_similarity(string1, string2)
    normalized_levenshtein_score = round(1 - normalized_similarity, 2)
    total_normalized_score += normalized_levenshtein_score

average_normalized_score = total_normalized_score / num_pairs
# Round the average Levenshtein distance to two decimal places
average_levenshtein_distance_rounded = round(average_normalized_score, 2)

print("Average Levenshtein distance (rounded to 2 decimals):", average_levenshtein_distance_rounded)