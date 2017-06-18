import csv
import re
from nltk.corpus import stopwords
from nltk.corpus import words
from nltk.corpus import brown

import string

file = open('writehere-test2.txt','w') #for writing the clean,filtered tweets

with open('tweetsfinal-tsv.txt','r') as tsv: #opening the file which has the twets
    f_list = [line.strip().split('\t') for line in tsv] #making the tabbed tweets in a list #lists within a list of id,tweet,type
    print f_list[1]
    
    for i in range (len(f_list)):
        f_list[i] = filter(None, f_list[i]) #removing empty characters
        
        if (len(f_list[i])>1): #cleaning the tweets and removing urls
            clean_tweet = re.match('(.*?)http.*?\s?(.*?)', f_list[i][1])
            if clean_tweet: 
                f_list[i][1]=clean_tweet.group(1) #reassigning the clean tweet back to list

            split_list=f_list[i][1].split() #splitting the tweet content into separate words-usually at index 1
            filtered_word_list =split_list[:]  #make a copy of the split_list
            filtered_word_list= [''.join(c for c in s if c not in string.punctuation) for s in filtered_word_list] #removing punctuations from individual words
            filtered_word_list=map(lambda x:x.lower(),filtered_word_list) #lowercasing
            for word in filtered_word_list: # iterate over filtered_word_list
              if (word not in brown.words()) or (word in stopwords.words('english')):
                #print word
                filtered_word_list.remove(word) # remove word from filtered_word_list if it is a stopword
            filtered_word_list=string.join(filtered_word_list)
            f_list[i][1]=filtered_word_list
            
        if (len(f_list[i])>2):
            list=f_list[i][2].split()
            f_list[i][2]= [''.join(c for c in s if c not in string.punctuation) for s in list] #removing punctuations from individual words
            print f_list[i][2]
        

        for j in range (len(f_list[i])):
            print f_list[i][j]
            file.write(f_list[i][j])
            file.write('\t')

        file.write('\n')

        

print f_list[1]
