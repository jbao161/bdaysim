bdaysim
=======

     A simulation for randomly placing k indistinguishable items into n distinct boxes,
     so that no box remains empty.

 birthday_sim(n,k,t,s,v)
  
     main variables:
     n = number of boxes
     k = number of items (0 for as many as it takes for all boxes to have at least one item)
     t = number of trials

     parameters:
     s = 1 to show boxes (warning: may take a long time for large numbers!), 0 to hide boxes
     v = 1 to show status messages, 0 to hide messages

     output:
     returns a list where each element is the number of items needed to fill all boxes for a trial,
     or if all k items are used before each box is filled, the element is zero instead.
