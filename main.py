import nltk

# Dependensi untuk nltk.download() :
#   DO THIS BELOW FIRST
# a. download NLTK
# b. download package NLTK dengan cara :
#nltk.download('punkt')

import operator
import re
from nltk.corpus import brown
from nltk.probability import *
from nltk.corpus import wordnet


# 1. menghitung frekuensi dari korpus BROWN
words = FreqDist()
for sentence in brown.sents():
    for word in sentence:
        words[word] += 1
# ---------------------------------------
def freq(word):
	return words.freq(word)

#----------------------------------------
# meminta masukan berupa kalimat/paragraf
string = input("Enter a string :\n")

# tokenisasi menjadi kalimat
sents = nltk.sent_tokenize(string)
#print(sents)

# tokenisasi kata
final_word = {}
for sent in sents:
	# $print(sent)
	tokens = nltk.word_tokenize(sent)
	# pemeringkatan top sekian infrequent token
	freqToken = [None]*len(tokens)
	for index, token in enumerate(tokens):
	 	freqToken[index] = freq(token)
	# print(tokens)
	# print(freqToken)
	sortedtokens = [f for (t,f) in sorted(zip(freqToken,tokens))]
	n = int(0.3 * len(tokens))
	#print(n)
	difficultWords = []
	for i in range(0, n):
		difficultWord = sortedtokens[i]
		difficultWords.append(difficultWord)
		#print("kata susah ", difficultWord)
		#print(wordnet.synsets(difficultWord))
		calon_pengganti = {}
		for synset in wordnet.synsets(difficultWord):
			for lemma in synset.lemmas():
				calon_pengganti[lemma.name()] = freq(lemma.name())
		#$print(calon_pengganti)
		if len(calon_pengganti) > 0 :
			final_word[difficultWord] = max(calon_pengganti, key=lambda i: calon_pengganti[i])
	#print(final_word)		
	# $print(tokens)
	for token in tokens:
		# $print(token)
		# if idx != len(tokens):
		# 	print(idx, len(tokens))
		# 	if not(re.match('[a-zA-Z0-9]',token[idx+1])):
		# 		print('hmm')
		if token in difficultWords and token in final_word:
			print(final_word[token], end=' ')
		else:
			print(token, end=' ')
	# $print()
