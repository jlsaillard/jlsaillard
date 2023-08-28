import csv
from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction

def read_csv(csv_path, delimiter='\t'):
    references = []
    candidates = []
    
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delimiter)
        for row in csvreader:
            if len(row) == 2:  # Assuming two columns: reference and candidate
                references.append(row[0].split())  # Split reference into tokens
                candidates.append(row[1].split())  # Split candidate into tokens
    
    return references, candidates

csv_path = 'C:\\Users\\st_je\\OneDrive\\Documents\\Smartcat\\Tools\\BLEU Scores\\Consent of Mother.txt'
references, candidates = read_csv(csv_path, delimiter='\t')  # Change delimiter if needed

bleu_score = corpus_bleu(references, candidates)
print("Average BLEU score:", bleu_score)