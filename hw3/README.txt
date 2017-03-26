This is the README file for A0144939R's submission

== Python Version ==

I'm using Python Version 2.7.6 for this assignment.

== General Notes about this assignment ==

For indexing, I iterate through all documents, and every term is added to the dictionary, while every doc_id is added to the postings list. The dictionary  keeps track of the (vector)length of each document, and the df of each term. The postings keeps track of both the doc_id and the tf of the term in each document. During indexing, both dictionary and postings are in memory. During the indexing, each term in the dictionary is associated with the number of documents that term appears in, as well as the row number of the postings list for that term in the postings object. This row number is later replaced by the byte offset in the postings file, once the file has been saved to disk.
The dictionary is serialised and deserialised using pickle. The postings is stored in a file with the postings list for every term on a different line.

For searching, I iterate through every term in the query string, and for every document in each query term's posting list, I compute the product of the weighted tf idf for the term using lnc-ltc and store the value, just like the algorithm in the lecture. I then use a heap to get the 10 most relevant documents.

== Files included with this submission ==

search.py: Contains code for performing search
index.py: Contains code for going through all documents and indexing them
dictionary.py: Code for the Dictionary class
postings.py: Code for the Postings class
searcher.py: Code for Searcher class that stores the dictionary and postings and has functions to perform search operations
dictionary.txt: Stored form of dictionary
postings.txt: Stored form of postings

== Statement of individual work ==

Please initial one of the following statements.

[X] I, A0144939R, certify that I have followed the CS 3245 Information
Retrieval class guidelines for homework assignments.  In particular, I
expressly vow that I have followed the Facebook rule in discussing
with others in doing the assignment and did not take notes (digital or
printed) from the discussions.  

[ ] I, A0144939R, did not follow the class rules regarding homework
assignment, because of the following reason:

<Please fill in>

I suggest that I should be graded as follows:

<Please fill in>

== References ==
I did not consult any external resource for this assignment.

EMAIL: e0009031@u.nus.edu