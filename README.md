# N-Queens
This is the second project that I did while learning AI algorithms.

Since most of the ground work was already done during learning Data Structures and CSP, this one was a breeze. 
All I had to do was import previously defined graph data structure in my python file and define an iterative CSP for
solving N-Queens problem. I am currently able to solve 1000 Queens under a minute.

The iterative CSP algorithm goes as follows:

1. Add all the variables of your problem (here the N Queens) as nodes in a graph.
2. Now randomly assign each variable an acceptable value; it doesn't have to be consistent at the moment. In this case
   our acceptable values were any integer (0-999) so I used randint() function for assignment
3. Now pass your graph and assignment to the iterative CSP function, which will randomly pick any variable from the assignment
   and assign it a value based on a heuristic. This process will continue till all the variables are properly assigned -- i.e.
   goal test is passed. The order of variable selection isn't as important as the selection of value of the variable is.
   
