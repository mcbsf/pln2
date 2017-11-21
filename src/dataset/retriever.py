"""
Subset of reuters 21578, "ModApte", considering only received categories.

util: 
- http://www.nltk.org/book/ch02.html
- https://miguelmalvarez.com/2015/03/20/classifying-reuters-21578-collection-with-python-representing-the-data/

might be useful:
- http://www.nltk.org/howto/corpus.html
- https://miguelmalvarez.com/2016/11/07/classifying-reuters-21578-collection-with-python/
"""


from nltk.corpus import floresta, treebank
import os, nltk.test
from itertools import islice
from nltk.grammar import PCFG, induce_pcfg, toy_pcfg1, toy_pcfg2

class Floresta:


    """
    Initializes the collection considering only the received categories.

    :param categories: [str] list of categories names
    """

    def simplify_tag(self, t):
        if "+" in t:
            return t[t.index("+")+1:]
        else:
            return t

    def simpifly_tree_tag(self, t):
        
        if(type(t)!=type('as')):
            t.set_label(self.simplify_tag(t._label))
            if(t.height()!=0):
                for child in t:
                    if child:
                        self.simpifly_tree_tag(child)

        return t


    def __init__(self):
        self.sentences = floresta.parsed_sents()
        productions = []

        for fileid in floresta.fileids()[:2]:
            for t in floresta.parsed_sents(fileid):
                t = self.simpifly_tree_tag(t)
                t.chomsky_normal_form()
                productions += t.productions()

        # for e, t in enumerate(self.sentences):
        #     if(t):
        #         #print("\taqui carai", t)
        #         #print(type(t))
        #         t = self.simpifly_tree_tag(t)
        #         #print(t)
        #         t.chomsky_normal_form()
        #         productions += t.productions()
        #         if(e==4):
        #             break
            
        print(productions)
        
        np = nltk.Nonterminal('np')
        grammar = induce_pcfg(np, productions)
        print(grammar)
        
        

    def get_words(self, document_id):
        return floresta.words()

