#This is Euclidean Distance
from math import sqrt
#look at how many things ppl ranked similarly then plot the different ratings/ppl on a charg

# A dictionary of movie critics and their ratings of a small set of movies provided in the book
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

print("This is the score of Lisa Rose for Lady in the water: " + str(critics['Lisa Rose']['Lady in the Water']))

# Returns a distance-based similarity score for person1 and person2 
def sim_distance(prefs,person1,person2):
 # Get the list of shared_items
 si={}
 for item in prefs[person1]:
     if item in prefs[person2]:
         si[item]=1
 # if they have no ratings in common, return 0
 if len(si)==0: return 0
 # Add up the squares of all the differences
 sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
 for item in prefs[person1] if item in prefs[person2]])
 #create formula to give higher values for ppl who are similar, add one to the function and invert it
 return 1/(1+sum_of_squares)

similarity = sim_distance(critics, 'Mick LaSalle', 'Toby')
print("The euclidean similarity score for Mick LaSalle and Toby is: " + str(similarity))
similarity2 = sim_distance(critics, 'Mick LaSalle', 'Jack Matthews')
print("The euclidean similarity score for Mick LaSalle and Jack Matthews is: " + str(similarity2))
similarity3 = sim_distance(critics, 'Lisa Rose','Gene Seymour')
print("The euclidean similarity score for Lisa Rose and Gene Seymour is: " + str(similarity3))
