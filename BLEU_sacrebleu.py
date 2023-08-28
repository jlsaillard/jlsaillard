import csv
import sacrebleu

def read_csv(csv_path, delimiter='\t'):
    references = []
    candidates = []
    
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delimiter)
        for row in csvreader:
            if len(row) == 2:  # Assuming two columns: reference and candidate
                references.append([row[0]])  # Wrap reference in a list
                candidates.append(row[1])  # Leave candidate as-is
    
    return references, candidates

csv_path = 'C:\\Users\\st_je\\OneDrive\\Documents\\Smartcat\\Tools\\BLEU Scores\\Fillable CDS Authorizations - KO Microsoft.txt'
references, candidates = read_csv(csv_path, delimiter='\t')  # Change delimiter if needed

bleu = sacrebleu.corpus_bleu(candidates, references)
rounded_bleu = round(bleu.score, 8)
print("Rounded BLEU score:", rounded_bleu)
