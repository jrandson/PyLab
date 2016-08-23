
def separate(source):
	
	words = []
	wordAcumulated = ""
	for c in source:
		wordAcumulated += c
		
		if belongs_to_dictionary(wordAcumulated):
			words.append(wordAcumulated)
			wordAcumulated = ""

	words.append(wordAcumulated)

	printWords(words)

	print printWords(words)

	#verificar "palvras" de uma única letra

def belongs_to_dictionary(word):
	dictionay = load_dicionary()
	if word in dictionay:
		return True
	else:
		return False

def printWords(words):

	frase = ""
	for word in words:
		frase += word + " "

	print frase

def load_dicionary():
	text = open("source_dictionary.txt","r")
	dictionay = []
	for line in text:
		words = line.split()
		for word in words:
			aux = word.strp()
			if not aux in dictionay :
				dictionay.append(aux)

	return dictionay

	
dic = load_dicionary()
print len(dic)

source = 'practiceandusethisgroupdiscussionexpressions'
separate(source)

