import sys
import nltk

class DetectPlag:
    def __init__(self):
        pass
    
    def run_main(self):
        sent_list = []

        for arg in sys.argv:
            sent_list.append(arg)
        #self.compare_sentences(sent_list[1], sent_list[2])
        self.find_most_similar_sentence(sent_list[1], sent_list[2])

        print "NOT NOT NOT word - word"

    def find_most_similar_sentence(self, sent1, sent2):

        similar_count = 0

        sent1_words_list = sent1.split(" ")
        sent2_sent = sent2.split(".") 
        
        for sent in sent2_sent:
            for word in sent.split(" "):
            
                if not word.strip():
                    continue
    
                if word in sent1_words_list:
                    similar_count += 1
           
                    if similar_count >= 7:
                        print "word to word plag"
                        exit(0)

                else:
                    similar_count = 0
              
 

    def compare_sentences(self, sent1, sent2):

        sent1_set = sent2_set = common_word_set = set()
        sent1_count = sent2_count =  common_words_count = 0
        sent1_sim = sent2_sim = 0


        sent1_set = set(sent1.split(" "))
        sent2_set = set(sent2.split(" "))

        stemmer = nltk.stem.PorterStemmer()

        sent1_set  = self.preprocess(sent1_set, stemmer)
        sent2_set  = self.preprocess(sent2_set, stemmer)


        sent1_count = len(sent1_set)
        sent2_count = len(sent2_set)

        common_word_set = sent1_set.intersection(sent2_set)

        common_words_count = len(common_word_set)        


        sent1_sim = (common_words_count/float(sent1_count)) * 100
        sent2_sim = (common_words_count/float(sent2_count)) * 100

        print "Sent-2 similarity %s" % (sent2_sim)
    

    def preprocess(self, sent_set, stemmer):

        new_sent_set = set()
        
    
        for word in sent_set:
            if word.strip():
                new_sent_set.add(stemmer.stem(word))

        return new_sent_set
        
            



if __name__ == "__main__":
    dp_obj = DetectPlag()
    dp_obj.run_main()
