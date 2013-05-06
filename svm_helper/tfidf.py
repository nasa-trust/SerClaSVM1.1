import os
import sys
import math

#         Train the related file and the non-related file
#            get the value of tfidf
#            test the test file
#            record the coordinate.

def tfidf( is_kind, is_not_kind, test, method = "p", alpha = 0.4 , directory = 'sequence_Directory'):

#        New a dictionary
    # data = open(directory, 'r')
    data = open( directory ).readlines()
    count = 0
    dict_new = dict()
    for each_line in data:
		count = count +1
		# term = each_line.strip()
		term, num = each_line.split()
		# print term
		dict_new[term] = count
		# print "OK111"

    N = 0
    word_dict = {}
    vector = ""
    for path in (is_kind, is_not_kind, test):
        N += len( os.listdir( path ) )
        # print N

        for f in os.listdir( path ):
            if os.path.isdir( path + "/" + f ):
                continue
            # print "reading:" + f
            try:
            	content = open( path + "/" + f ).readlines()
            	# open the file, with the directory
            	for line in content:
                	word, count = line.split()
                	word_dict.setdefault( word, 0 )
                	word_dict[ word ] += 1
                	
            except BaseException, e:
            	print "error:", e
            	print "continue"
            	continue
                      
                
    vector_index = word_dict.keys()
    vector_index.sort()
    n = 0
    print "OK222"
	
    for path in (is_kind, is_not_kind):
    	print path
        for f in os.listdir( path ):
            if os.path.isdir( path + "/" + f ):
                continue
            # print "generating traing:" + f
            content = open( path + "/" + f ,'r')
            tfidf_dict = {}
            max_tfidf = 0
#        Highlight the keywords
            for line in content:
                word, count = line.split()

#        Calculate the value of the train files' tfidf
                raw_tfidf = int(count)* math.log( N * 1.0 / word_dict[ word ])
                if max_tfidf < raw_tfidf:
                    max_tfidf = raw_tfidf
                tfidf_dict[ vector_index.index(word) ] = raw_tfidf
                doc_index = tfidf_dict.keys()
                doc_index.sort()
            vector += str( n ) + " "
            if method == "0":
                for k in doc_index:
                    vector += str( k ) + ":" + str(tfidf_dict[k]) + " "
            elif method == "1":
                for k in doc_index:
                    vector += str( k ) + ":" + str(alpha + (1 - alpha) * tfidf_dict[k] / max_tfidf) + " "
                    

            vector += "\n"
        n += 1
	# print vector
    f = open( "svm_helper\\train.txt", "w" )
    f.write(vector)
    f.flush()
    f.close()

    vector = ""
    for f in os.listdir( test ):
        if os.path.isdir( test + "/" + f ):
                continue
       	# print "generating testing:" + f
        content = open( test + "/" + f ).readlines()
        tfidf_dict = {}
        max_tfidf = 0
        for line in content:
                word, count = line.split()
                raw_tfidf = int(count)* math.log( N * 1.0 / word_dict[ word ])
                """if raw_tfidf >=1:
                        raw_tfidf = 0.99"""
                if max_tfidf < raw_tfidf:
                        max_tfidf = raw_tfidf
                tfidf_dict[ vector_index.index(word) ] = raw_tfidf
                doc_index = tfidf_dict.keys()
                doc_index.sort()
        vector += "0 "
        if method == "0":
                for k in doc_index:
                        vector += str( k ) + ":" + str(tfidf_dict[k]) + " "
        elif method == "1":
                for k in doc_index:
                        vector += str( k ) + ":" + str(alpha + (1 - alpha) * tfidf_dict[k] / max_tfidf) + " "

        vector += "\n"
            
    f = open( "svm_helper\\test.txt", "w" )
    f.write(vector);
    f.flush()
    f.close()
    print "OK444"

if len(sys.argv) != 7:
	print "Error!"
	sys.exit(1)
	
is_path = sys.argv[ 1 ]
is_not_path = sys.argv[ 2 ]
test_path = sys.argv[ 3 ]
kind = sys.argv[ 4 ]
alpha = float(sys.argv[ 5 ])
directory = sys.argv[ 6 ]

tfidf( is_path, is_not_path, test_path, kind, alpha , directory)
print "OK"
                     
