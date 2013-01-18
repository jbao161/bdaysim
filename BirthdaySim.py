#!/usr/bin/env python
'''
Created on Dec 31, 2012
#
# birthday_sim(n,k,t,s,v)
#
#     A simulation for randomly placing k indistinguishable items into n distinct boxes
#  
#     main variables:
#     n = number of boxes
#     k = number of items (0 for as many as it takes for all boxes to have at least one item)
#     t = number of trials
#
#     parameters:
#     s = 1 to show boxes (warning: may take a long time for large numbers!), 0 to hide boxes
#     v = 1 to show status messages, 0 to hide messages
#
#     output:
#     returns a list with number of elements equal to the number of trials,
#     where each element is the number of items it took to fill all boxes (or 0 if some box is unfilled) for that trial
#
# Example 1: If there are 365 days in a year and each person is equally likely to be born on any day of the year,
# how many people do you need to pick at random to have at least one person born on each day of the year?
# try: birthday_sim(365,0,1,1,1) for one experiment
#
# Example 2: If there are 2,800 people in a group, what is the probability that every day is somebody's birthday in the group?
# try: print(check_percent(birthday_sim(365,2800,10**3,0,0))) and repeat several times
# (note: this is an estimate of the probability based on 1,000 trials, not an exact calculation of the probability!)
#
#
# @author: Jonathan Bao
#          jbao161@gmail.com
'''

import random


# start of simulation program

# main execution
def birthday_sim(n,k,t,s,v):
    result=[]
    while t>0: #for t trials
        b=create_buckets(n) #create n empty boxes
        result.append(iterate(b,n,k,s,v)) #fill the boxes and record results
        t=t-1
    return result

# returns a list of n empty boxes
def create_buckets(n):
    buckets=[]
    for i in range (0,n):
        buckets.append(0)
    return buckets

# takes a list of boxes, b, and displays the number of items in each box
# (set s to 0 and it does nothing!)
def print_buckets(b,s):
    if s==0:
        return
    text='|'
    for i in b:
        text+=str(i)+'|'
    print(text)

# takes a list of n empty boxes, b, and adds an item to a random box 
# until k iterations (or when k=0, until all boxes are filled )
# and returns the number of iterations until all boxes are filled
# (or returns 0 if not all boxes have been filled)       
def iterate(b,n,k,s,v):
    count=n #how many boxes are empty
    t=0 #how many items used
    
    #Case 1: run until all boxes filled
    if k==0: 
        if v==1:
            print("Running simulation until all boxes are filled:")
        
        #randomly fill the boxes  
        while count>0:
            p=random.randrange(0, n) #choose a random box
            if b[p]==0:
                count=count-1 #update count if box is empty
            b[p]+=1 #add one item to the box
            print_buckets(b,s)
            t+=1
            
        if v==1:
            print("     to fill all "+str(n)+" boxes, "+str(t)+ " items were required.")
            
        return t #records the number of iterations to fill all boxes
    
    #Case 2: run until k iterations
    else: 
        if v==1:
            print("Simulating "+str(k)+" iterations")
            
        #randomly fill the boxes    
        while k>0:
            p=random.randrange(0, n) #choose a random box
            if b[p]==0:
                count=count-1 #update count if box is empty
            b[p]+=1 #add one item to the box
            print_buckets(b,s)
            if count==0: 
                x=t #remember the number of iterations to fill all boxes
                count=count-1 #don't count subsequent iterations
            t+=1
            k=k-1
        
        #record results
        if count<=0:
            if v==1:
                print("Sucess: all boxes filled at "+str(x)+' iterations!')
                
            return x #records the number of iterations to fill all boxes
        else:
            if v==1:
                print("Failure: "+str(count)+" boxes remain unfilled!")
                
            return 0 #records failure

# end of simulation program
        

# start of data analysis tools:     

# takes a list and returns the number of nonzero entries in the list
def check_freq(data):
    count=0
    for i in data:
        if i!=0:
            count+=1
    return count

# takes a list and returns the frequency of nonzero entries in that list
# as a percentage of the number of entries in the list
def check_percent(data):
    return check_freq(data)/len(data)


# end of data analysis tools


##
## sample code: delete the leading '#' or enter your own values below!
##

#birthday_sim(5,0,1,1,1)

#birthday_sim(365,0,1,1,1)

#birthday_sim(365,0,10,0,1)

#print(check_percent(birthday_sim(365,2000,10**3,0,0)))

#print(check_percent(birthday_sim(365,2800,10**3,0,0)))

#print(check_percent(birthday_sim(365,3300,10**3,0,0)))

##
## end of sample code
##


