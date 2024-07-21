from nltk.stem import PorterStemmer
import re
from collections import defaultdict

# Define function to evaluate simple Boolean queries
def evaluate_boolean_query(query,inverted_index):
    # Split query into terms and operators
    ps=PorterStemmer()
    terms = [ps.stem(term) for term in query.split()]
    operators = []
    for term in terms:
        if term in {'and', 'or', 'not'}:
            operators.append(term)
            terms.remove(term)
    # Evaluate query using Boolean logic
    result = set(inverted_index.get(terms[0], set()))
    not_docs=[str(i) for i in range(1,31)]
    for i, operator in enumerate(operators):
        if operator == 'and':
            result &= set(inverted_index.get(terms[i+1], set()))
        elif operator == 'or':
            result |= set(inverted_index.get(terms[i+1], set()))
        elif operator == 'not':
            if len(terms)==1:
                result=[i for i in not_docs if i not in result]
            else:
                result -= set(inverted_index.get(terms[i+1], set()))
    # Return documents that satisfy query
    return result


# Define function to evaluate simple proximity queries
def evaluate_proximity_query(query,positional_index):
#     #preprocess the query and split the proximity part and query part
#     ps=PorterStemmer()
#     terms,k=query.split('/')
#     k=int(k)
#     terms = [ps.stem(term) for term in terms.split()]
#     docs = set(positional_index.get(terms[0], {}).keys())
#     for term in terms[1:]:
#         docs &= set(positional_index.get(term, {}).keys())

# #evaluate the relevant documents
#     result = []
#     for doc in docs:
#         positions = []
#         for term in terms:
#             positions.append(positional_index.get(term, {}).get(doc, []))

#         for i in range(len(positions[0])):
#             for j in range(1, len(terms)):
#                 if not any(abs(positions[k][i] - positions[0][i]) <= k for k in range(1, j+1)):
#                     break
#             else:
#                 result.append(doc)
#                 break
# #return documents that satisfy the query
#     return result
    ps=PorterStemmer()
    terms = re.findall(r'\w+', query)
    term1 = ps.stem(terms[0])
    term2 = ps.stem(terms[1])
    k = int(terms[2])

    results = defaultdict(list)
    for doc1, positions1 in positional_index[term1].items():
        if term2 in positional_index and doc1 in positional_index[term2]:
            positions2 = positional_index[term2][doc1]
            for pos1 in positions1:
                for pos2 in positions2:
                    if abs(pos1 - pos2) <= k:
                        results[doc1].append((pos1, pos2))

    result=[]
        # print results
    # print(f"Results for proximity query '{query}':")
    if results:
        for doc, positions in results.items():
            result.append(doc)
            # print(f"Document '{doc}' contains '{term1}' and '{term2}' within {k} words of each other:")
            # for pos1, pos2 in positions:
            #     print(f"  '{term1}' at position {pos1}, '{term2}' at position {pos2}")
    else:
        print("No documents found for query")
    return result


