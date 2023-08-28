import csv
import sacrebleu

def read_csv(csv_path, delimiter=','):
    references = [] 
    candidates = []
    
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delimiter)
        
        for row in csvreader:
            if len(row) == 2:
                references.append(row[0])  # Reference text
                candidates.append(row[1])  # Candidate text
                
    return references, candidates

csv_path = 'C:\\Users\\st_je\\OneDrive\\Documents\\Smartcat\\Tools\\BLEU Scores\\Test_document.csv'

references, candidates = read_csv(csv_path, delimiter='\t') 

lepors = []
for ref, cand in zip(references, candidates):
    score = sacrebleu.corpus_bleu(cand, [ref], force=True).score
    lepors.append(score)

total_lepor = sum(lepors) / len(lepors)
print(total_lepor)