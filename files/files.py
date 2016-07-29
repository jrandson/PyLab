from os import path as p

def diskUsage(path):
	size = p.getsize(path)

	if p.isdir(path):
		listDir = p.listdir(path)
		for item in listDir:
			childPath = p.join(path,item)
			print childPath
			size += diskUsage(childPath)
	
	return size

path = raw_input("Inform um diretorio: ");
print diskUsage(path)
