#!/usr/bin/env python

from math import sqrt

import codecs

users = {
	"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0,"Norah Jones": 4.5, 
		"Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, 
		"Vampire Weekend": 2.0},
	
	"Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0,
	 	"Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
	
	"Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0,
	 		"Phoenix": 5, "Slightly Stoopid": 1.0}, "Dan": {"Blues Traveler": 3.0, 
	 		"Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, 
	 		"The Strokes": 4.0, "Vampire Weekend": 2.0},
	
	"Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0,
	 		"Vampire Weekend": 1.0},
	
	"Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, 
	 		"Slightly Stoopid": 4.5,"The Strokes": 4.0, "Vampire Weekend": 4.0},
	
	"Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0,
	 		"Slightly Stoopid": 4.0, "The Strokes": 5.0},
	
	"Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0,"Phoenix": 4.0, 
	 			"Sligghtly Stoopid": 2.5, "The Strokes": 3.0}}


class Recomender:

	def __init__(self, data, k=1, metric='pearson', n=5):
		
		self.k = k
		self.metric = metric
		self.n = n
		self.username2id = {}
		self.userid2name = {}
		self.productid2name = {}
		

		if self.metric == 'pearson':
			self.fn = self.pearson

		if type(data).__name__ == 'dict':
			self.data = data

	def convertProductID2Name(self, id):
		if id in self.productid2name:
			return self.productid2name[id]
		else:
			return id

	def userRatings(self, id, n):
		""" Return n top ratings """
		print "Rating for " + self.userid2name[id]
		ratings = self.data[id]
		print len(ratings)
		ratings = list(ratings.items())
		ratings = [(self.convertProductID2name(k), v) for (k,v) in ratings]

		ratings = ratings[:n]

		for rating in ratings:
			print "%s \t%i" % rating[0], rating[1]

	def loadBookBD(self, path ='BX-Dump/'):
		"""loads the BX book dataset. Path is where the BX files are located"""
 		self.data = {}
 		i = 0
		 #
		 # First load book ratings into self.data
		 #
 		f = codecs.open(path + "BX-Book-Ratings.csv", 'r', 'utf8')
 		for line in f:
 			i += 1		
		
		# separate line into fields
		fields = line.split(';')
		user = fields[0].strip('"')
		book = fields[1].strip('"')
		rating = int(fields[2].strip().strip('"'))
		if user in self.data:
 			currentRatings = self.data[user]
 		else:
 			currentRatings = {}

 		currentRatings[book] = rating
 		self.data[user] = currentRatings
 		f.close()
		
		#
		# Now load books into self.productid2name
		# Books contains isbn, title, and author among other fields
		#
 		f = codecs.open(path + "BX-Books.csv", 'r', 'utf8')
 		for line in f:
 			i += 1 		
	 		# separate line into fields
	 		fields = line.split(';')
	 		isbn = fields[0].strip('"')
	 		title = fields[1].strip('"')
	 		author = fields[2].strip().strip('"')
	 		title = title + ' by ' + author
	 		self.productid2name[isbn] = title
 		f.close()
		
		#
		# Now load user info into both self.userid2name and
		# self.username2id
		#
 		
 		f = codecs.open(path + "BX-Users.csv", 'r', 'utf8')
 		for line in f:
 			i += 1
 
 		# separate line into fields
 		fields = line.split(';')
 		userid = fields[0].strip('"')

		location = fields[1].strip('"')
 		if len(fields) > 3:
 			age = fields[2].strip().strip('"')
 		else:
 			age = 'NULL'
 		
 		if age != 'NULL':
 			value = location + ' (age: ' + age + ')'
 		else:
 			value = location
 		
 		self.userid2name[userid] = value
 		self.username2id[location] = userid
	 	f.close()
	 	
	 	print(i)

	def manhattam(self, rate1, rate2):

		distance = 0
		for key in rate1.keys():
			if key in rate2.keys():
				distance += abs(rate1[key] - rate2[key])

		return distance

	def euclidian(self, rate1, rate2):
		distance = 0

		for key in rate1:
			if key in rate2:
				distance += pow(abs(rate1[key] - rate2[key]),2)

		return pow(distance,0.5)

	def minkowski(self, rate1,rate2,r):
		distance = 0
		for title in rate1.keys():
			if title in rate2.keys():
				distance += pow(abs(rate1[title] - rate2[title]),r)

		return pow(distance, 1.0/r)

	def computeNearestNeighbod(self, username):
		distances = []

		for instance in self.data:
			if username != instance:
				distance = self.euclidian(self.data[instance], self.data[username])

				distances.append((instance, distance))

		distances.sort(key=lambda artistTuple: artistTuple[1], reverse=True)

		return distances

	def pearson(self,rate1, rate2):

		sum_xy = 0
		
		sum_x = 0
		sum_y = 0

		sum_x_2 = 0
		sum_y_2 = 0
		
		n = 0

		for title in rate1:
			if title in rate2:
				sum_xy += rate1[title] * rate2[title]

				sum_x += rate1[title]
				sum_y += rate2[title]
				n += 1.0

				sum_x_2 += rate1[title]**2
				sum_y_2 += rate2[title]**2


		num =  sum_xy - (sum_x*sum_y)/n
		den = sqrt(sum_x_2 - pow(sum_x,2)/n) * sqrt(sum_y_2 - pow(sum_y,2)/n)

		if den == 0:
			return 0
		else:
			return num / den

	def cossine(self,rate1, rate2):

		prod_xy = 0
		length_x = 0
		length_y = 0

		for title in rate1:
			length_x += rate1[title]**2
		
		length_x = sqrt(length_x)

		for title in rate2:		
			length_y += rate2[title]**2
		
		length_y = sqrt(length_y)

		for title in rate1:
			if title in rate2:
				prod_xy += rate1[title] * rate2[title]


		if not length_x * length_y == 0:
			return prod_xy / (length_x * length_y)
		else:
			return 0

	def recommend(self, user):
		"""Give list of recommendations"""
		#print nearest
		recomendations = {}
		# first get list of users ordered by nearness
		nearest = self.computeNearestNeighbod(user)
		#
		# now get the ratings for the user
		#
		
		userRatings = self.data[user]		
		# determine the total distance		
		total_distance = 0.0

		for i in range(self.k):
			total_distance += nearest[i][1]

		# now iterate through the k nearest neighbors
 		# accumulating their ratings

		for i in range(self.k):
			# compute slice of pie 
			weight = nearest[i][1] / total_distance
			# get the name of the person
			name = nearest[i][0]
			# get the ratings for this person
			neighborRatings = self.data[name]
			# get the name of the person
 			# now find bands neighbor rated that user didn't

 			for artist in neighborRatings:
 				if not artist in userRatings:
 					if not artist in recomendations:
 						recomendations[artist] = (neighborRatings[artist] * weight)
 					else:
 						recomendations[artist] = (recomendations[artist] +
 												neighborRatings[artist]*weight)

 		# now make list from dictionary

 		recomendations = list(recomendations.items())	
 		recomendations = [(self.convertProductID2Name(k), v)
 		 					for (k,v) in recomendations]

 		# finally sort and return
 		recomendations.sort(key=lambda artistTuple: artistTuple[1],
 		 						reverse = True)

 		# Return the first n items 		 
 		return recomendations[:self.n]




#=========================================================

def show_pearson():
	print peason(users['Angelica'], users['Bill'])
	print peason(users['Angelica'], users['Hailey'])
	print peason(users['Angelica'], users['Jordyn'])

#==========================================================



r = Recomender(users)
print r.recommend('Sam')
#r.loadBookBD()
#r.recommend('171118') 
#r.userRatings('171118', 5) 
















