#!/usr/bin/env python

from math import sqrt

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0,"Norah Jones": 4.5, 
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


def manhattam(rate1, rate2):

	distance = 0
	for key in rate1.keys():
		if key in rate2.keys():
			distance += abs(rate1[key] - rate2[key])

	return distance

def euclidian(rate1, rate2):
	distance = 0

	for key in rate1.keys():
		if key in rate2.keys():
			distance += pow(abs(rate1[key] - rate2[key]),2)

	return pow(distance,0.5)

def minkowski(rate1,rate2,r):
	distance = 0
	for title in rate1.keys():
		if title in rate2.keys():
			distance += pow(abs(rate1[title] - rate2[title]),r)

	return pow(distance, 1.0/r)

def computeNearestNeighbod(user_name,users):
	distances = []

	for user in users:
		if user_name != user:
			distance = euclidian(users[user], users[user_name])
			distances.append((user, distance))

	distances.sort()
	return distances

def recomend(user_name, users):

	nearest = computeNearestNeighbod(user_name,users)[0][0]
	#print nearest
	recomendations = []

	userRatings = users[user_name]
	neighboRating = users[nearest]

	for title in neighboRating:
		if not title in userRatings:
			recomendations.append((title, neighboRating[title]))

	return recomendations



















