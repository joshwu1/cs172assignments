import parsing
from parsing import tokenizing
from parsing import doc_stats
from parsing import term_stats
import sys

if(len(sys.argv) == 3):
    if(sys.argv[1] == '--term'):
        term_statistics = term_stats(sys.argv[2])
        print("Listing for term: ", sys.argv[2])
        print("TERMID: ", term_statistics[2])
        print("Number of documents containing term: ", term_statistics[1])
        print("Term frequency in corpus: ", term_statistics[0])


    if(sys.argv[1] == '--doc'):
        document_statistics = doc_stats(sys.argv[2]) 
        print("Listing for document: ", sys.argv[2])
        print("DOCID: ", document_statistics[1])
        print("Total terms: ", document_statistics[0])

#else:
    #if(len(sys.argv) == 5):
        #if(sys.argv[1] == '--term' and sys.argv[3] == '--doc')
        #print("Inverted list for term: ", sysargv[2])
        #print("In document: ", sys.argv[4])
        #print("TERMID: ", )
        #print("DOCID: ", )
        #print("Term
   #not implemented...