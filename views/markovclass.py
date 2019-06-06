try:
	import sys
	import random
	import string
	import math
	import nltk
except ImportError:
   	print('ugh')

class markov:
	def __init__(self,file):
		self.og = file
		self.file = file.replace("\n"," ").split(" ")
		self.words = dict()
		self.starters = []

	def construct_dict(self, order):
		previous = False
		punctuation = ['.','?','!']
		for i in range(0, len(self.file)-order):
			ngram = []
			for j in range(i, i+order):
				ngram.append(self.file[j])
			# print(ngram)
			# print(i, len(self.file), self.file[i-1])
			if i == 0 or self.file[i-1][len(self.file[i-1])-1] in punctuation:
				self.starters.append(ngram)
			if self.file[i] not in self.words.keys():
				self.words[' '.join(ngram)] = []
			if i < len(self.file)-order:
				newGram =[]
				for j in range(i, i+order):
					if j+order < len(self.file):
						if self.file[j+order][len(self.file[j + order])-1] in punctuation:
							newGram.append(self.file[j+order])
							break
						else:
							newGram.append(self.file[j+order])
				self.words[' '.join(ngram)].append(newGram)
		# print(self.words)
	def generate(self):
		punctuation = ['.','?','!']
		sentences = nltk.sent_tokenize(self.og)
		randStart = ' '.join(self.starters[random.randint(0, len(self.starters)-1)])
		currentGram = randStart
		result = randStart
		path = {}
		while result[len(result) -1] not in punctuation:
			#print(self.words[currentGram])
			path[currentGram] = self.words[currentGram]
			currentGram = ' '.join(self.words[currentGram][random.randint(0, len(self.words[currentGram])-1)])
			result += " " + currentGram
		if result not in sentences:
		 	# path[currentGram] = []
		 	# return chain(path, result, [randStart])
		 	print(result)
		else:
			self.generate()

# class chain:
# 	def __init__(self, path, string, starter):
# 		self.path = path
# 		self.string = string
# 		self.starter = starters
# 	def breed(self, otherChain):
# 		combinedPath = {}
# 	def generate(self):
# 		punctuation = ['.','?','!']
# 		randStart = ''.join(self.starter[random.randint(0, len(self.starter)-1)])
# 		currentGram = randStart
# 		result = randStart
# 		while result[len(result) -1] not in punctuation:
# 			# print(currentGram)
# 			# print(currentGram + ": " + str(self.path[currentGram]))
# 			# print("\n \n")
# 			currentGram = ' '.join(self.path[currentGram][random.randint(0, len(self.path[currentGram])-1)])
# 			result += " " + currentGram
# 		print(result)

with open(sys.argv[1], "r") as file:
	text = file.read()
# 	mtg_cards = json.load(file)
# for keys in mtg_cards:
# 	for i in range(0, len(mtg_cards[keys]["cards"])):
# 		if("text" in mtg_cards[keys]["cards"][i].keys()):
# 			print(mtg_cards[keys]["cards"][i]["text"])


markovify = markov(text)
markovify.construct_dict(int(sys.argv[2]))
# # # chain1 = markovify.generate()
# # # chain2 = markovify.generate()

# # # newChain = chain1.breed(chain2)
# # # newChain.generate()
markovify.generate()
