This is the README file for A0000000X's submission

== Python Version ==

I'm using Python Version 2.7.6 for this assignment.

== General Notes about this assignment ==

For indexing, I iterate through all documents, and every term is added to the dictionary, while every doc_id is added to the postings list. During indexing, both dictionary and postings are in memory. During the indexing, each term in the dictionary is associated with the number of documents that term appears in, as well as the row number of the postings list for that term in the postings object. This row number is later replaced by the byte offset in the postings file, once the file has been saved to disk.
The dictionary is serialised and deserialised using pickle. The postings is stored in a file with the postings list for every term on a different line. The first line of the postings file has a list of all the documents, which is useful for NOT queries.

For searching, I implemented the shunting yard algorithm to parse queries. While evaluating queries, the postings lists for each term are loaded into list data strucutres, after which list operations are performed on them. To implement skip pointers, instead of building a skip list, I simply skip by the square root of the length of each list while taking the intersection.

== Files included with this submission ==

search.py: Contains code for performing search
index.py: Contains code for going through all documents and indexing them
dictionary.py: Code for the Dictionary class
postings.py: Code for the Postings class
utils.py: Some extra utility functions, like the shunting yard algorithm and list merging algorithms
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

I had to look at some past year's github projects to get myself started, especially on how to structure my project. However, I wrote every line of code by myself. Following is a list of the repos I consulted:

https://github.com/ymichael/cs3245-hw
https://github.com/ashrayjain/CS3245
https://github.com/akshatd/InformationRetreival/tree/master

In addition, I referred to various answers on stack overflow for python related questions.