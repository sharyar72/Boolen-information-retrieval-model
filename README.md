# Boolen-information-retrieval-model
The repository contains implementation of a Boolean Retrieval model to showcase classic Information Retrieval

The Python code implements a boolean retrieval model with proximity queries, boolean queries and
phrase queries up to 3 terms. The code reads a folder containing text documents For this repo the dataset is in the Dataset Folder, preprocesses the documents, 
creates inverted and positional indexes and stores them in PICKLE format. It also provides a GUI interface for the user
to enter boolean and proximity queries and get the search results. To run the model only run the main.py code the rest of the code files are imported into this
and individual functions are used from each code file.

The boolean retreival model has 3 python files with functions explained as follows: 
1) preprocessing.py: 
has 2 functions

. preprocess(): This function takes the text from file, reads the stopwords text file which contains the stop words to be
removed from each file, removes digits, punctuation and stems the words using porter stemmer.

. create_indexes(): This function takes the path of the folder containing the text files,
preprocesses it using the preprocess() function and then creates inverted and positional indexes.
if both indexes have already been created then this function will not be called else it will
be called and will create both indexes and store them in pickle format inside the folder containing
the text documents.

2) query.py:
has 2 functions

. evaluate_boolean_query(): takes query and inverted index, preprocesses the query and finds documents
matching the query with inverted index and returns a set.

. evaluate_proximity_query(): takes query and positional index, preprocesses the query and finds documents
matching the query with positional index and returns a set. 

3) main.py: 

is the main function with the GUI implemetation and driver code.
WHen the main in run GUI will display a text box a display box and 4 buttons(choosefolder, clear, enter, exit)
. Choose folder is used to choose the folder containing the documents to be preprocessed or to look for already made indexes and just loads them.
. enter to confirm query once it is written in text box here the query is checked if query has a / then evaluate_proximity_query is called else evaluate_boolean_query is called.
. clear is used to clear the text box input.
. exit is to end the program.
has 7 functions

. load indexes(): loads the indexes if already made else calls the create_indexes() function.
. choose_folder(): to choose the path of the folder of the documents.
. run_function(): to display a loading screen which halts the code until preprocessing or loading of indexes has not been finished.
. clear_text(): to clear the textbox so that new input can be inserted.
. evaluate_query(): checks which query is entered if query has / then evaluate_proximity_query() is called else evaluate_boolean_query is called().
. perform_operation(): when enter is pressed takes the query as input fetched the result and displays the documents if any have been fetched else prints 'NO documents found'.
. exit_program(): terminates the code.

RESUlTs of the query as shown in the video: 
BOOLEAN QUERIES: 

1) cricket AND caption 
	1,3,6,9,14,20,21,29,25,29

2) good and chase
	2,16,27,28,30

3) BAtter ANd BOwler
	2,3,9,16,18,19,22,23,25,27

4) cricket AND melbourn AND pakistan
	1,2

5) impossible
	2,4

6) help AND hate
	No documents

7) psl AND pCb
	4,11

8) psl OR pcb
	4,11,29

proximity queries: 

1) pakistan india /2
	No documents

2) pakistan india /3
	12,18

3) pakistan india /4
	12,18
