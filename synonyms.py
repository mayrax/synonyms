# import pandas as pd
# import json

# excel_file_path = r"C:\Users\arturo\Desktop\Spinner_gpt.xlsx"
# pd.read_excel(excel_file_path, sheet_name=None)

from nltk.corpus import wordnet

def find_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return set(synonyms)

words = ["happy", "sad", "good"]
synonyms_dict = {}
for word in words:
    synonyms_dict[word] = find_synonyms(word)

print(synonyms_dict)

