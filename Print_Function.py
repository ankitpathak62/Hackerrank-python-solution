#The included code stub will read an integer, , from STDIN.
#
#Without using any string methods, try to print the following:
#
#
#Note that "" represents the consecutive values in between.
#
#Example
#
#Print the string .
#
#Input Format
#
#The first line contains an integer .
#
#Constraints
#
#
#Output Format
#
#Print the list of integers from  through  as a string, without spaces.
#
#Sample Input 0
#
#3
#Sample Output 0
#
#123
#Language
#Pypy 3
#More
#123
#if __name__ == '__main__':
#    n = int(input())
#    print(*[i for i in range(1,n+1)],sep="")
#Line: 3 Col: 45
#
#Test against custom input
#Python
#You have earned 20.00 points!
#You are now 35 points away from the 2nd star for your python badge.
#0%35/70
#Congratulations
#You solved this challenge. Would you like to challenge your friends?Share on FacebookShare on TwitterShare on LinkedIn
#
#Test case 0
#
#Test case 1
#
#Test case 2
#Compiler Message
#Success
#Input (stdin)
#3
#Expected Output
#123
#




if __name__ == '__main__':
    n = int(input())
    print(*[i for i in range(1,n+1)],sep="")
