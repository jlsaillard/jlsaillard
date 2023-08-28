import csv
import hLepor
from nltk.translate.meteor_score import meteor_score
from nltk.tokenize import word_tokenize

# Check if punkt is downloaded
punkt_downloaded = True
try:
  nltk.data.find('tokenizers/punkt')
except LookupError:
  punkt_downloaded = False

if not punkt_downloaded:
  nltk.download('punkt')

def read_csv(csv_path, delimiter=','):
    references = []
    candidates = []
    
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delimiter)
        for row in csvreader:
            if len(row) == 2:  # Assuming two columns: reference and candidate
                references.append(word_tokenize(row[0]))  # Tokenize reference
                candidates.append(word_tokenize(row[1]))  # Tokenize candidate
    
    return references, candidates

csv_path = 'C:\\Users\\st_je\\OneDrive\\Documents\\Smartcat\\Tools\\BLEU Scores\\output2.txt'
references, candidates = read_csv(csv_path, delimiter='\t')  # Change delimiter if needed

total_hlepor_score = 0.0
num_samples = len(references)

for ref, cand in zip(references, candidates):
    hlepor_score = hLepor.calculate_score(ref, cand)
    total_hlepor_score += hlepor_score

average_hlepor_score = total_hlepor_score / num_samples
# print("Average hLepor score:", average_hlepor_score)

# Format as percentage
print(f"Average hLepor score: {average_hlepor_score * 100:.2f}%")
