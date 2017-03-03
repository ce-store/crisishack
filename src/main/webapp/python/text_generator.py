import numpy as np
import os
import random

sentence_dict = []
sentence_dict.append(['i','my','hi']) #nouns
sentence_dict.append(['neighbour','brother','sister']) #verbs
sentence_dict.append(['is','has','is not']) #adv
sentence_dict.append(['ebola','sick','worrying']) #adj

sentence_structures = dict()
sentence_structures['ebola'] = dict()
sentence_structures['sanitation'] = dict()
sentence_structures['roads'] = dict()

greeting = ("Hi", "Hello", "Hey", "") 
sentence_structures['ebola']['subject'] = ("","")
sentence_structures['ebola']['nouns'] = ("I am ", "My brother is", "My friend is", "We are")
sentence_structures['ebola']['verbs'] = ("sick", "ill", "unwell") 
#adv = ("sick", "ill", "in pain", , "barfs") 
sentence_structures['ebola']['adj'] = ("very", "really","","","")
sentence_structures['ebola']['frequency'] = 1000

#The toliet/loo/bog/WC/outhouse is (working fine) / is broken / is blocked/ is dirty / messy / full / overflowing/
sentence_structures['sanitation']['subject'] = ("The", "Our", "My", "The village", "The community")
sentence_structures['sanitation']['nouns'] = ("toilet", "toilets","loo", "bog", "WC" ,"outhouse")
sentence_structures['sanitation']['adj'] = ("very", "really","","","")
sentence_structures['sanitation']['verbs'] = ("is broken", "is blocked", "needs repairing", "is dirty", "is messy", "is full", "is overflowing", "needs cleaning")
sentence_structures['sanitation']['frequency'] = 2000
#adv = ("sick", "ill", "in pain", , "barfs") 

# The/This/Our road/main road/side road/track/path [through our town/by the river/] is broken/needs repairing/is dangerous/has potholes/is unusable
sentence_structures['roads']['subject'] = ("The", "Our", "My", "The village", "This")
sentence_structures['roads']['nouns'] = ("road", "main road","side road", "path", "street" ,"track","route")
sentence_structures['roads']['adj'] = ("through my town", "by the river","by my house","near the river","to work","to the toilets","to the factory","to the market","near the market")
sentence_structures['roads']['verbs'] = ("is broken", "is dangerous", "needs repairing", "is blocked", "is unusable", "is unsafe", "has potholes", "needs clearing")
sentence_structures['roads']['frequency'] = 3000

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
        sentences.append(sentence)

random.shuffle(sentences)
corpus = "\n".join(sentences)

corpus_file = os.open("corpus.csv", os.O_RDWR|os.O_CREAT)

ret = os.write(corpus_file, corpus)

print "the number of bytes written: "
print  ret

print "written successfully"

# Close opened file
os.close(corpus_file)
print "Closed the file successfully!!"