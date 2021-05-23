# CS172 - Assignment 1 (Tokenization)

## Team member 1 - Joshua Wu
## Team member 2 - Firstname Lastname

###### Provide a short explanation of your design
I first decided to process the text in the file by using the given starter code, importing a stemmer function, and adding the token_regex. I defined three functions: one to tokenize, one to get the term statistics of the document, and one to get the document statistics. I was able to remove the stopwords, punctuation,stem and tokenize the terms in the document.
The regex removes the punctuation and whitespace, and the stopword.txt file provided allowed me to remove the stopwords or ignore it. I then placed all of that text in a new dictionary and appended them together.
I am not sure if my term search and frequency is implemented correctly. The idea was to iterate through the dictionary and count the number of times the term selected would appear and then add it to the count. 
For the document ID and stats, I grabbed from the the already parsed dictionary and get the term total by getting the length of the document.
I was not able to get position and pass in both term and doc at the same time.
The read_index files uses system args, takes the input, and uses the functions in parsing.



###### Language used, how to run your code, if you attempted the extra credit (stemming), etc. 
I used Python3 and did not attempt the extra credit.

Example to get document information:
python3 .\read_index.py --doc AP890101-0001

Example to get term information:
python3 .\read_index.py --term asparagus