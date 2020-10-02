

from collections import OrderedDict
import re

def findTopNCompetitors(numCompetitors, topNCompetitors, competitors, numReviews, reviews):
                        
    """ Output: A list of top N competitor names """
    ### initialize variables
    
    result = []
    word_list = []
    competitor_dict = dict.fromkeys(sorted(competitors),0)
    sorted_competitor_dict = dict()
    
    ### iterate over each quote in the reviews
    for quote in reviews:
        #print(quote)
        print("-"*50)
        
        ### keep track of words already seen in the single quote
        ### reset visited word for each iteration of quote
        visited_word = []  
        
        ### iterate over each word in the list and check to see if the word is
        ### name of one of the competitors in the given list of competitors
        word_list = re.sub(r'[^\w=]', ' ',quote)
        word_list = word_list.split()
        
        for word in word_list:
            print(word)
            if word in competitors:
                print(">>"+word)
                
                if word not in visited_word:
                    competitor_dict[word] += 1
                    visited_word.append(word)
    
    print(competitor_dict)
    ### sort the competitor_dict by value, the transformed result will be list of tuples
    sorted_competitor_dict = OrderedDict(sorted(competitor_dict.items(), key=lambda x: x[1], reverse=True))
    
    ### TODO: implement sort by key (competitor name) if the count values are the same
    
    if len(sorted_competitor_dict) < topNCompetitors:
        return list(sorted_competitor_dict)
    else:
        return list(sorted_competitor_dict)[:topNCompetitors]


numCompetitors = 6
topNCompetitors = 3
competitors = ["Google", "Microsoft", "Facebook", "Apple", "LinkedIn", "NetFlix"]
numReviews = 3 
reviews = ["I don't know about you but I like Apple better than Google. Apple has better employee satisfaction than Google.",
           "Microsoft is also a great place to work but I sometimes don't like their policies. I'd prefer NetFlix if I could choose between FAANGs.",
           "Facebook is also one of my dream places to work. I admire Facebook's employee compensation plans but lately I am hesitant to apply at Facebook because of thier political involvement regarding consumer privacy.",
           "Microsoft and Amazon are among my top 5 places to work, but if I were given a choice, I would choose one from Google, Apple, LinkedIn, and NetFlix.",
           "Apple is definitely the best place to work for me because I personally like and use their products and Apple has always stood out as a cool company."]

print(findTopNCompetitors(numCompetitors, topNCompetitors, competitors, numReviews, reviews))