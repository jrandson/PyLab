#!/usr/bin/python


text = open('assay1.txt')

top_words = {}

# words to ignore
def add_top_words(item):
	ignore_pt = ['e','a','as','de','do','da','dos','das' 
			'no','nos','o','os','as','um','uma','como',
			'na','nas', 'para', 'com', 'que','em']

	ignore_en = ['and','to','a','an', 'the','for', 'from','in','of','on','this','these','that','is','are']

	ignore = ignore_pt + ignore_en

	if not item in ignore:
		if item in top_words.keys():
			top_words[item] += 1
		else:
			top_words[item] = 1

def get_words_line(line):
	for item in words_line:
		add_top_words(item)


for line in text:
	if not line == '':
		words_line = line.split()
		get_words_line(words_line)

text.close()

#show the occurrence of the words
treshould = 3 
i = 0;
for key in top_words.keys():
	top_words.values().sort()
	if top_words[key] >= treshould:
		print str(i) + ": " + key + ": " + str(top_words[key]) + " times"
		i += 1



