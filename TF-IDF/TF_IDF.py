'''
Created on 2014-12-4

@author: you_shoubian
'''

import glob
import math

def tf_idf():
    # find the files in filedir
    wordlist = []
    # the directory of the documents,ensure that there are no characters
    filedir = "D:\\Desktop\\doc"
    filenames = glob.glob( filedir + "\*" )
    for filename in filenames:
        filename_list.append( filename )
        with open( filename, "r" ) as tempInputData:
            word = tempInputData.read()
            wordlist.append( word.split( ' ' ) )

    # Calculate TF
    for doc in wordlist:
        doc_tf_dict = {}
        for word in doc:
            if word not in doc_tf_dict:
                doc_tf_dict[word] = 1.0 / len( doc )
            else:
                doc_tf_dict[word] += 1.0 / len( doc )
            idf_dict[word] = 0
        tf_list.append( doc_tf_dict )

    # Calculate IDF
    N = len( tf_list )
    for doc in tf_list:
        for item in idf_dict:
            if item in doc:
                idf_dict[item] += 1
    for item in idf_dict:
        idf_dict[item] = math.log( ( N * 1.0 ) / idf_dict[item] )

def query():
    # input the query word
    query_word = raw_input( "please input the word:" )
    q_list = query_word.split( ' ' )

    # calculate the tfidf of each doc
    tf_idf_dict = {}
    for i in range( len( tf_list ) ):
        tf_idf = 0
        for word in q_list:
            if word in tf_list[i]:
                tf_idf += tf_list[i][word] * idf_dict[word]
        tf_idf_dict[filename_list[i]] = tf_idf

    # sorted by value  descending
    tf_idf_dict = sorted( tf_idf_dict.items(), key = lambda d:d[1], reverse = True )

    # output the result
    print 'the result is:'
    for item in tf_idf_dict:
        if item[1] != 0:
            print item[0]
    print '\nover'

if __name__ == '__main__':
    filename_list = []
    tf_list = []
    idf_dict = {}

    tf_idf()
    query()
