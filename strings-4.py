sentence = input ("Type a sentence")
sentenceA = sentence.count("a")
sentenceE = sentence.count("e")
sentenceI = sentence.count("i")
sentenceO= sentence.count("o")
sentenceU = sentence.count("u")
overall = sentenceA + sentenceE + sentenceI + sentenceO + sentenceU
print (f"There are {overall} vowels in that sentence")