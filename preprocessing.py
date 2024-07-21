import os
import re
import pickle
from nltk.stem import PorterStemmer


# Preprocessing function
def preprocess(text,stop_words_path='Stopword-List.txt'):
    # read the stopwords from the text file
    stop_word_list=[]
    f=open(stop_words_path,"r")
    lines=f.readlines()

    for line in lines:
        stop_word_list.append(line.strip())

    ps=PorterStemmer()
    # remove all digits from text
    text=re.sub(r'\d+', '', text)

     # Remove non-alphanumeric characters and split into terms
    terms = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower().split()

    # Remove stop words and apply stemming
    terms = [ps.stem(term) for term in terms if term not in stop_word_list]
    # return the terms from the document
    return terms


# Define function to create inverted and positional indexes
def create_indexes(folder_path):
    # Initialize indexes
    inverted_index = {}
    positional_index = {}
    # Loop through files in folder
    for file_name in os.listdir(folder_path):
        # Read file contents
        with open(os.path.join(folder_path, file_name), 'r') as f:
            text = f.read()
        # # Preprocess file contents
        # Split file contents into terms
        terms = preprocess(text)
        file_name=file_name.replace('.txt','')
        # Loop through terms in file
        for i, term in enumerate(terms):
            # Add term to inverted index
            if term not in inverted_index:
                inverted_index[term] = set()
            inverted_index[term].add(file_name)
            # Add term to positional index
            if term not in positional_index:
                positional_index[term] = {}
            if file_name not in positional_index[term]:
                positional_index[term][file_name] = []
            positional_index[term][file_name].append(i)
    # Save indexes to file
    file_path_1=folder_path+'\\inverted_index.pkl'
    file_path_2=folder_path+'\\positional_index.pkl'
    with open(file_path_1, 'wb') as f:
        pickle.dump(inverted_index, f)
    with open(file_path_2, 'wb') as f:
        pickle.dump(positional_index, f)

    return inverted_index,positional_index
