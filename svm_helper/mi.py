import os
import math
import sys

def MI( is_c_path, is_not_c_path ):

	if is_c_path[-1] != "/":
	    is_c_path += "/"
		
	if is_not_c_path[-1] != "/":
	    is_not_c_path += "/"
	    
        vocabulary = {}
        doc_count = {}

        N_1 = len( os.listdir( is_c_path ) )
        N_0 = len( os.listdir( is_not_c_path ) )
        N = N_0 + N_1


        for f in os.listdir( is_c_path ):
                print "Processing ", f
                content = open( is_c_path + f ).readlines()
                for line in content:
                        word, count = line.split()
                        vocabulary.setdefault( word, [] )
                        vocabulary[ word ].append( [ f, int(count) ] )
                        doc_count.setdefault( word, [0, 0] )
                        doc_count[ word ][1] += 1

        print "-------->IS Kind OK"
                        
        for f in os.listdir( is_not_c_path ):
                print "Processing ", f
                content = open( is_not_c_path + f ).readlines()
                for line in content:
                        word, count = line.split()
                        vocabulary.setdefault( word, [] )
                        vocabulary[ word ].append( [ f, int(count) ] )
                        doc_count.setdefault( word, [0, 0] )
                        doc_count[ word ][0] += 1
        print "--------->IS Not Kind OK" 
        rank = {}

        for x in doc_count.keys():
                N11 = doc_count[ x ][ 1 ]
                N10 = doc_count[ x ][ 0 ]
                N1_ = N11 + N10
                N01 = N_1 - N11
                N00 = N_0 - N10
                N0_ = N01 + N00
                
                MI = 0.0 
                if N11 != 0:
                        MI += math.log( float( N * N11 ) / ( N1_ * N_1 ), 2 ) * N11 / N
                
                if N10 != 0:
                     MI += math.log( float( N * N10 ) / ( N1_ * N_0 ), 2 ) * N10 / N
                
                if N01 != 0:
                         MI += math.log( float( N * N01 ) / ( N0_ * N_1 ), 2 ) * N01 / N
                
                if N00 != 0:
                         MI += math.log( float( N * N00 ) / ( N0_ * N_0 ), 2 ) * N00 / N
                
                rank[ x ] = MI

        selected = sorted( rank.items(), key = lambda d:d[ 1 ], reverse = True )
        print "Dictionary Length: ", len(selected)
        return [ x[0] for x in selected]

is_path = sys.argv[ 1 ]
is_not_path = sys.argv[ 2 ]
k = int( sys.argv[ 3 ] )
res_file = sys.argv[4]

mi_file = open( res_file, "w")
for x in MI( is_path, is_not_path )[:k]:
        mi_file.write( x + "\n")
mi_file.flush()
mi_file.close()

