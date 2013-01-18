#!/usr/bin/env python
'''
Created on Dec 31, 2012
Analysis tools for the simulation of k indistinguishable items randomly placed in n distinct boxes
@author: jbao
         jbao161@gmail.com
'''
import BirthdaySim


# takes a list [[number of items,simulation results],...] and returns the list [[number of items,probability of filling all boxes],...]
def list_percent(result):
    for entry in result:
        entry[1]=BirthdaySim.check_percent(entry[1])
    return result

# for the simulation of k indistinguishable items randomly placed in n distinct boxes
# creates a list [[number of items, simulation results],...]
# where n is the number of boxes, t is the number of trials
# k is the number of items and u is the unit increment of k between k1 and k2

# ex: for 365 boxes, {2000,2100,2200,...4000} items and 10^3 trials
# use create_distribution(365,10**3,2000,4000,100)

def create_distribution(n,t,k1,k2,u):
    result=[]
    for i in range (int(k1/u),int(k2/u)+1):
        data=BirthdaySim.birthday_sim(n,i*u,t,0,0)
        result.append([i*u,data])
    return result


#sample code:

#d=create_distribution(365,10**1,2000,4000,100)
#print (list_percent(d))
