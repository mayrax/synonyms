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

