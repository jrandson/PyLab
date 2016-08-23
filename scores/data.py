def get_scores():
	
	file = open('dados.txt','r')
	lista = []
	for line in file:
		if len(line.rstrip()) > 0:
			lista.append(line.rstrip())	

	dados_brutos = [(lista[i],lista[i+1]) for i in range(0,len(lista)-1,2)]

	scores = {}
	for data in dados_brutos:
		scores[data[0]] = str_to_float(data[1])

	return scores

def str_to_float(str):
	f = str.split(",")
	return float(f[0])

def get_histogram(notas):
	histogram = {}
	for n in notas:
		if n in histogram.keys():
			histogram[n] += 1
		else:
			histogram[n] = 1

	
	return histogram

scores = get_scores()
notas = scores.values()
matriculas = scores.keys()
print matriculas
histogram = get_histogram(notas)

qtdAprovados = 0
total = 0

for nota in histogram.keys():
	total += histogram[nota]
	if nota >= 5:
		qtdAprovados += histogram[nota]

	print histogram[nota], nota


print "Total: "  + str(total)
print "Total de aprovados: " + str(qtdAprovados)
print "Total de reprovados: " + str(total - qtdAprovados)
print "Min: "+ str(min(notas))
print "Max: " + str(max(notas))
