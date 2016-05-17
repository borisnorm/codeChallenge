G-Unit Interview Questions

#Given a number, remove one of the digits the digit must be part of a consecutive run,
 #where it returns the max value of that number, (dont be concerend with run time),
    -The value you return must be less if you remove a digitS

    soln
        -Find all runs, and then remove the right most run, 2 is good enough for a run so no
        -need to dp the problem
        -At the end of the day they will all be shifted back the same, want to remove smallest
        -number?
        -IF there is a run of sevens there is no difference to what you remove

        naive solution:
            -Remove every numbre



#given a file directory described by a string, return the sum of the length of all of the directory path strings that, terminate in a valid img file
a1
 a2
  file.txt
b1
 file2.txt


"a1\n a2\n  file.txt"

"/a1/a2/file.txt"


    soln
        -
        -



#give a list of numbers, return an index of that list, sum of all number before
#index is equal to sum of numbers after that index, if multiple instances can return any
#return -1


#Symetric, do an iterative DFS, modified on the left and right subtrees and then
compare their results
