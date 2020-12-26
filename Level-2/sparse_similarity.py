#!/usr/bin/python

# Date: 2020-12-26
#
# Description:
# The similarity of two documents (each with distinct words) is defined to be
# the size of the intersection divided by the size of the union. For example,
# if the documents consist of integers, the similarity of {1, 5, 3} and
# {1, 7, 2, 3} is 4 because the intersection has size 2 and the union has size
# 5.
# We have a long list of documents (with distinct values and each with an
# associated ID) where the similarity is believed to be "sparse". That is, any
# two arbitrarily selected documents are very likely to have similarity O.
# Design an algorithm that returns a list of pairs of document IDs and the
# associated similarity.
# Print only the pairs with similarity greater than O. Empty documents should
# not be printed at all. For simplicity, you may assume each document is
# represented as an array of distinct integers.
# EXAMPLE
# Input:
#   13: {14, 15, 100, 9, 3}
#   16: {32, 1, 9, 3, 5}
#   19: {15, 29, 2, 6, 8, 7}
#   24: {7, 10}
# Output:
#   ID1, ID2 SIMILARITY
#   13,  19  0.1
#   13,  16  0.25
#   19,  24  0.14285714285714285
#
# Approach:
# Consider each pair of documents and compute similarity, if similarity comes
# out to be more than 0, add it the output list.
# Computing similarity b/w 2 document can be done in O(A + B)
# - Keep one one document in a set and iterating over other and checking if
#   a word is present in set or not, this will give intersection
# - To find union, union = A + B - intersection
#
# Complexity:
# O(D^2 * W)
# D = Number of documents
# W = Max words in a document
#
# NOTE: Slightly better approach given in CTCI, refer that. Worst case
# complexity remains same in that approach also but most of the time runs
# better than this one


class Document:
    def __init__(self, doc_id, words):
        self.doc_id = doc_id
        self.words = words

    def get_id(self):
        return self.doc_id

    def get_words(self):
        return self.words

    def get_size(self):
        return len(self.words)

class DocPair:
    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2

def compute_similarity(doc1, doc2):
    words1 = doc1.get_words()
    set1 = set(words1)

    intersection = 0
    for w in doc2.get_words():
        if w in set1:
            intersection += 1

    union = doc1.get_size() + doc2.get_size() - intersection
    return intersection / union

def compute_similarities(documents: list) -> float:
    similarities = {}
    for i in range(len(documents)):
        for j in range(i + 1, len(documents)):
            d1 = documents[i]
            d2 = documents[j]
            sim = compute_similarity(d1, d2)
            if sim > 0:
                pair = DocPair(d1.get_id(), d2.get_id())
                similarities[pair] = sim
    return similarities
            

def main():
    docs = []
    input_docs = {
        13: [14, 15, 100, 9, 3],
        16: [32, 1, 9, 3, 5],
        19: [15, 29, 2, 6, 8, 7],
        24: [7, 10]
    }
    for doc_id in input_docs:
        docs.append(Document(doc_id, input_docs[doc_id]))

    similarities = compute_similarities(docs)
    for doc_pair in similarities:
        print(f'{doc_pair.id1}, {doc_pair.id2} -> {similarities[doc_pair]}')

if __name__ == '__main__':
    main()
