import numpy as np
import os
import random

#sentence_dict = []
#sentence_dict.append(['i','my','hi']) #nouns
#sentence_dict.append(['neighbour','brother','sister']) #verbs
#sentence_dict.append(['is','has','is not']) #adv
#sentence_dict.append(['ebola','sick','worrying']) #adj

sentence_structures = dict()
sentence_structures['ebola'] = dict()
sentence_structures['sanitation'] = dict()
sentence_structures['roads'] = dict()
sentence_structures['water'] = dict()
sentence_structures['heat'] = dict()

greeting = ("Hi", "Hello", "Hey", "") 
sentence_structures['ebola']['subject'] = ("","")
sentence_structures['ebola']['nouns'] = ("I am ", "My brother is", "My sister is", "My mother is", "My father is", "The priest is", "The Imam is", "My friend is", "We are", "My wife is", "My husband is")
sentence_structures['ebola']['verbs'] = ("very", "really","","","","")
#adv = ("sick", "ill", "in pain", , "barfs") 
sentence_structures['ebola']['adj'] = ("sick", "ill", "unwell", "feeling bad", "fever", "bleeding") 
sentence_structures['ebola']['frequency'] = 1000

#The toliet/loo/bog/WC/outhouse is (working fine) / is broken / is blocked/ is dirty / messy / full / overflowing/
sentence_structures['sanitation']['subject'] = ("The", "Our", "My", "The village", "The community", "The mosque", "The church", "The market")
sentence_structures['sanitation']['nouns'] = ("toilet is", "toilets are", "loo is", "bog is", "WC is" ,"outhouse is", "can is")
sentence_structures['sanitation']['adj'] = ("very", "really","","","")
sentence_structures['sanitation']['verbs'] = ("broken", "blocked", "in need of repairing", "dirty", "messy", "full", "overflowing", "in need of cleaning")
sentence_structures['sanitation']['frequency'] = 1500
#adv = ("sick", "ill", "in pain", , "barfs") 

# The/This/Our road/main road/side road/track/path [through our town/by the river/to mosque/to church] is broken/needs repairing/is dangerous/has potholes/is unusable
sentence_structures['roads']['subject'] = ("The", "Our", "My", "This")
sentence_structures['roads']['nouns'] = ("road", "main road","side road", "path", "street" ,"track","route","village road","town road","main route","main path")
sentence_structures['roads']['adj'] = ("through my town", "by the river","by my house","near the river","to work","to the toilets","to the factory","to the market","near the market", "to mosque", "to church")
sentence_structures['roads']['verbs'] = ("is broken", "is dangerous", "needs repairing", "is blocked", "is unusable", "is unsafe", "has potholes", "needs clearing")
sentence_structures['roads']['frequency'] = 2000

# The church/mosque/village/town pump/water pump/water/well/water supply/drinking water/water well/tap/water tap/drinking water tap is broken/is not working/is contaminated/has failed/is not right/is dirty/is mucky/give bad water/pumps bad water/pumps dirty water
sentence_structures['water']['subject'] = ("The church", "The mosque", "Our church's","Our mosque's","My church's","My mosque's","My village","The village","Our village's", "The community", "My", "Our", "The")
sentence_structures['water']['nouns'] = ("pump", "water", "well", "water supply", "drinking water", "water well", "tap", "water tap", "drinking water tap")
sentence_structures['water']['adj'] = ("really","totally","","","","")
sentence_structures['water']['verbs'] = ("is broken","is not working","is contaminated","has failed","is not right","is dirty","is mucky","gives bad water","pumps bad water","pumps dirty water","is nasty")
sentence_structures['water']['frequency'] = 3000

sentence_structures['heat']['subject'] = ("","")
sentence_structures['heat']['nouns'] = ("I", "My brother", "My sister", "My mother", "My father", "The priest", "The Imam", "My friend", "My wife", "My husband")
sentence_structures['heat']['verbs'] = ("","")
#adv = ("sick", "ill", "in pain", , "barfs") 
sentence_structures['heat']['adj'] = ("is overheating", "is dehydrated", "has collapsed", "collapsed from heat", "has a fever", "is exhausted", "collapsed from overheating") 
sentence_structures['heat']['frequency'] = 1000

idx = random.randrange(0, len(greeting))
print()

sentences = []
for key in sentence_structures.keys():
    for ii in range(sentence_structures[key]['frequency']):
        # sentence = [sentence_dict[position][np.random.randint(0,3,1)] for position in range(len(sentence_dict))]
        # sentence = ",".join(sentence)
        sentence = "{} {} {} {} {}".format(random.choice(greeting), 
                                         random.choice(sentence_structures[key]['subject']),
                                         random.choice(sentence_structures[key]['nouns']),
                                         random.choice(sentence_structures[key]['adj']),
                                         random.choice(sentence_structures[key]['verbs']))
        sentences.append(sentence.strip())

random.shuffle(sentences)
corpus = "\n".join(sentences)

corpus_file = os.open("corpus2.csv", os.O_RDWR|os.O_CREAT)

ret = os.write(corpus_file, corpus)

#print "the number of bytes written: "
#print  ret

#print "written successfully"

# Close opened file
os.close(corpus_file)
print("Closed the file successfully!!")