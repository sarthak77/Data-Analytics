import nltk
from nltk.corpus import stopwords 
import csv
from apyori import apriori

stop_words = stopwords.words('english')

#remove stopwords
data=[]
with open("knock.txt") as f:
    for line in f:
        line=line.strip().split(" ")
        row=[]
        for word in line:
            if word not in stop_words:
                    word=word.strip(",.?!")
                    word=word.lower()
                    row.append(word)
        data.append(row)



#create dictionary of words
words=[]
for line in data:
    for word in line:
            if word not in words:
                words.append(word)



#create bv
bv=[]
for line in data:
    row=[]
    for i in range(len(words)):
        if words[i] in line:
            row.append(words[i])
            # row.append(1)
        else:
            # row.append(0)
            row.append('NaN')
    bv.append(row)



#find frequency of each word
count=[]
for word in words:
        temp=0
        for line in data:
                if word in line:
                        temp+=1
        count.append(temp)



#find frequent items
frequent=[]
for i in range(len(count)):
    if(count[i]>=.9*len(data)):
        # print(words[i])
        frequent.append(i)



#remove frequent items from bv
bv2=[]
for line in bv:
        row=[]
        for i in range(len(words)):
                if i not in frequent:
                        row.append(line[i])
        bv2.append(row)

#apriori
association_rules = apriori(bv,min_support=0.1,min_confidence=0.1,min_lift=1,max_length=2)
association_results = list(association_rules)
minlen=1

nor=0
for i in association_results:

    #preprocess
    i=list(i)
    rule=list(i[0])
    sup=i[1]
    other=i[2]

    #print
    if(len(rule)>minlen and str(rule[0])!='NaN' and str(rule[1])!='NaN'):
        nor+=1
        print("------------------------------------------")
        print("Rule: "+str(rule[0])+" -> "+str(rule[1]))    
        print("Support: "+str(sup))
        print("Confidence: "+str(other[0][2]))
        print("Lift: "+str(other[0][3]))
        print("------------------------------------------")

print(nor)