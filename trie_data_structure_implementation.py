# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 23:33:47 2020

@author: Anjani K Shiwakoti

Synopsis: Implement a Trie data structure class in Python
"""

class Trie():
    """ Trie Class Definition"""
    
    def __init__(self):
        self.trie = dict()
        self._end = '*'
        
    
    
    def make_trie(self,*words):
        
        ### initialize root trie (dict)
        trie = dict() 
        for word in words:
            ### create sub tries based off of root trie
            sub_trie = trie
            for letter in word:
                sub_trie = sub_trie.setdefault(letter,{})
                
            ### when the word is finished, add a '*' to both the key and the value
            ### to demarcate the end of the word, and repeat until all words are finished
            sub_trie[self._end] = self._end
        
        return trie
        
        
    def search_trie(self, word):
        sub_trie = self.trie

        for letter in word:
            if letter in sub_trie:
                sub_trie = sub_trie[letter]
            else:
                return False
        else:
            if self._end in sub_trie:
                return True
            else:
                return False

    def add_trie(self, word):
        
        if self.search_trie(word):
            print ("The word [" + word + "] already exists!")
            return self.trie
        
        
        temp_trie = dict(self.trie)  # deepcopy 
        #print(temp_trie)
        for letter in word:
            if letter in temp_trie:
                temp_trie = temp_trie[letter]
                print(self.trie[letter])
            else:
                temp_trie = temp_trie.setdefault(letter, {})
                print(self.trie)
        temp_trie[self._end] = self._end
        
        print("The word ["+word+"] has been added to the Trie.")
         
        return temp_trie
        
        
    def delete_trie(self, trie):
        pass
    
    def prepend_trie(self, word):
        pass
    
    def __str__(self):
        print("Print Trie: ", self.trie)
        
    def __repr__(self, trie):
        return repr("REPR Trie: ", self.trie)

def main():
    """
    Trie
    """
    words = ["world", "wide", "web"]
    my_trie = Trie()
    print(my_trie.make_trie(["world", "wide", "web"]))  
    
    print(my_trie.add_trie("network"))   
    print(my_trie.add_trie("computer")) 
    print(my_trie.add_trie("internet")) 
    print(my_trie.search_trie("webb"))
    print(my_trie.search_trie("wide"))
    
    
if __name__ == "__main__":
    main()
    
