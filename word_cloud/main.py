#!/usr/bin/python


text = open('job_recife.txt')

top_words = {}

def add_top_words(item):
	ignore = ['e','a','as','de','do','da','dos','das' 
			'no','nos','o','os','as','um','uma','como',
			'na','nas', 'para', 'com', 'que','em']

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
		words_line = line.split(' ')
		get_words_line(words_line)

text.close()

for key in top_words.keys():
	top_words.values().sort()
	if top_words[key] >= 3:
		print key + ": " + str(top_words[key]) + " times"


