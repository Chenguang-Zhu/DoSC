# This file is a template python script for compiling the source code and running test cases.
# To run DeltaPartitioner on new projects, for each functionality of interest, the user needs to write such a python script, specifying the methods of compilation and tests execution on that unctionality.
# There is no need to change the framework of this script. The user just need to focus the lines with comments and follw the instructions in those comments.
# With simple modifications, this template can be applied to run DeltaPartitioner on other open source projects.

import os
import os.path
import sys
import csv
import subprocess as sub

def isexec (fpath):
    if fpath == None: return False
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK) 

def which(program):
    fpath, fname = os.path.split(program)
    if fpath:
        if isexec (program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if isexec (exe_file):
                return exe_file
    return None

if __name__ == '__main__':
    option = sys.argv[1]
    repopath = sys.argv[2]
    mvn = which('mvn')
    os.chdir(os.path.join(repopath, 'core')) # This line is to specify the directory of compiling code and running tests. Please provide the directory as an argument for os.chdir('') function.
    
    if option == 'compile':
        ret = sub.call ([mvn, 'compiler:compile']) # Put your command of compliling code in this line. For projects based on maven, the command is usually "mvn compiler:compile" as we show here. 
        if ret == 0:
            sys.exit(0)
        else:
            sys.exit(1)
    elif option == 'test':
        # ----------------
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=TestClass1#testMethod1']) # Put your command of running test case in this line. If your test suite contains multiple test methods (like this example), then copy & paste the code segment between the dash lines, using each such segment for running per test method.
        print ret
        if ret == 1:
            sys.exit(1)
        # ----------------
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=TestClass1#testMethod2'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=TestClass2#testMethod1'])
        print ret
        if ret == 0:
            sys.exit(0)
        else:
            sys.exit(1)
