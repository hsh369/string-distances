#cosine similarity.
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def CosineDist(a,b):
	# tokenization process
	X_list = word_tokenize(a.lower())
	Y_list = word_tokenize(b.lower())

	# get english stopwords 
	sw = stopwords.words('english')

	#list of numbers represents a vector of a and b
	l1 =[];l2 =[]

	# remove stopwords from the input
	X_set = {w for w in X_list if not w in sw}
	Y_set = {w for w in Y_list if not w in sw}

	# Union set 
	union_set = X_set.union(Y_set)

	# make vectors using sets for a and b respectively
	for w in union_set:
		if w in X_set: l1.append(1) 
		else: l1.append(0)
		if w in Y_set: l2.append(1)
		else: l2.append(0)

	
	# calculate cosine similarity
	# cos = (A*B)/(||A||*||B||)
	sum = 0
	for i in range(len(union_set)):
			sum+= l1[i]*l2[i]

	cosine = sum / float((sum(l1)**0.5)*(sum(l2)**0.5))

	return cosine
