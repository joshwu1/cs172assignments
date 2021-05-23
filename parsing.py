import re
import os
import zipfile
import sys
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
#helper function for stemming
stemmer = PorterStemmer()

token_regex = re.compile("\w+([\,\.]\w+)*")

# Regular expressions to extract data from the corpus
doc_regex = re.compile("<DOC>.*?</DOC>", re.DOTALL)
docno_regex = re.compile("<DOCNO>.*?</DOCNO>")
text_regex = re.compile("<TEXT>.*?</TEXT>", re.DOTALL)

#with zipfile.ZipFile("ap89_collection_small.zip", 'r') as zip_ref:
   # zip_ref.extractall()

#function to remove stopwords,punctionuation,stem,and tokenize the document dictionary
def tokenizing():
    stop_word = []
    document_dictionary={}
    with open('stopwords.txt', 'r') as file:
        for word in file:
            word = word. split('\n')
            stop_word.append(word[0])


    # Retrieve the names of all files to be indexed in folder ./ap89_collection_small of the current directory
    for dir_path, dir_names, file_names in os.walk("ap89_collection_small"):
        allfiles = [os.path.join(dir_path, filename).replace("\\", "/") for filename in file_names if (filename != "readme" and filename != ".DS_Store")]

    for file in allfiles:
        with open(file, 'r', encoding='ISO-8859-1') as f:
            filedata = f.read()
            result = re.findall(doc_regex, filedata)  # Match the <DOC> tags and fetch documents

            for document in result[0:]:
                # Retrieve contents of DOCNO tag
                docno = re.findall(docno_regex, document)[0].replace("<DOCNO>", "").replace("</DOCNO>", "").strip()
                # Retrieve contents of TEXT tag
                text = "".join(re.findall(text_regex, document))\
                          .replace("<TEXT>", "").replace("</TEXT>", "")\
                          .replace("\n", " ")

                # step 1 - lower-case words, remove punctuation, remove stop-words, etc.
                text = text.lower()
                nosw_text = []
                text_stemmed = []
                #use finditer to implement the regex, looks for the start of each word and end then adds to no stop word list
                for match in re.finditer(token_regex, text):
                    text = match.group()
                    nop_text = text.replace('_','')
                    nosw_text.append(nop_text)

                #https://www.geeksforgeeks.org/create-inverted-index-for-file-using-python/
                #stemming that takes the current list and removes stop words
                text = [i for i in nosw_text if not word in stop_word]
                #helper function to stem words
                for word in text:
                    stem_word =stemmer.stem(word)
                    text_stemmed.append(stem_word)
                    document_dictionary[docno] = text_stemmed

    return document_dictionary

#step 3 build index

#function to get term frequency and number of documents with the term
def term_stats(term):

    term_dictionary = {} 
    doc_tempdic = tokenizing()
    #iterate through the dictionary and appends/counts

    for word, count in doc_tempdic.items():
       
        for text_stemmed in count:
            if text_stemmed in term_dictionary:
                term_dictionary[text_stemmed] = term_dictionary[text_stemmed] + 1
            else:
                term_dictionary[text_stemmed] = 1

    doc_tempdic = term_dictionary
    
    termID= 1
    for i in doc_tempdic:
        if term == i:
                termID += 1

    return term_dictionary[text_stemmed],term_dictionary[text_stemmed], termID

#function to get unique document id and number of terms in the document
def doc_stats(docID):
    count = 1000
    term_total= 0
    DOCID = 0
    doc_tempdic = tokenizing()

    for document_dictionary in doc_tempdic: #processes the terms in the document and enumurates the total terms, and document id
        if docID == document_dictionary: 
            DOCID = count
            term_total = len(doc_tempdic.get(docID))
            break
        count = count + 1
    return term_total, DOCID







