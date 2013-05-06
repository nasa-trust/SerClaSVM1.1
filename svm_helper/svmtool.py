from svmutil import *
import sys,os, shutil

if len(sys.argv) != 6:
	print "Error!"
	os.exit(1)

c = sys.argv[ 1 ]
gamma = sys.argv[ 2 ]
is_path = sys.argv[ 3 ]
is_not_path = sys.argv[ 4 ]
test_path = sys.argv[ 5 ]

train_y, train_x = svm_read_problem('svm_helper\\train.txt')
m = svm_train(train_y, train_x, '-c ' + c + " -g " + gamma )
test_y, test_x = svm_read_problem('svm_helper\\test.txt')
p_label, p_acc, p_val = svm_predict(test_y, test_x, m)

names = os.listdir(test_path)
is_name = os.path.basename(is_path)
is_not_name = os.path.basename( is_not_path )

if not os.path.exists( os.path.join( test_path, is_name )):
        os.mkdir( os.path.join( test_path, is_name ) )
	
if not os.path.exists( os.path.join( test_path, is_not_name )):
        os.mkdir( os.path.join( test_path, is_not_name ) )

for x in range( len(names)):
        if p_label[ x ] > 0:
                shutil.copy( os.path.join( test_path, names[ x ] ), os.path.join( test_path, is_not_name ) )
                #print "copy ", os.path.join( test_path, names[ x ] ), " to ",os.path.join( test_path, is_not_name )
	else:
                shutil.copy( os.path.join( test_path, names[ x ] ), os.path.join( test_path, is_name ) )
                #print "copy ", os.path.join( test_path, names[ x ] ), " to ",os.path.join( test_path, is_name )