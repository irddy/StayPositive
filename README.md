# StayPositive
This was a HackerRank/codemotion challenge exercise.


 The program initially requests the user for the size of the array. 
 
 The second input requests the user to input a sequence of digits to populate the array. 

 The program will output a single number. 

### EXPLANATION ### 

Suppose that the array the user provided is something like the following. 

arr = [3, -5, 4, -3] 

We need to find the minimum number for which will make this array have only positive numbers. 

3 is positive 
-5 + 3 = -2 --> negative 
4 + (-2) = 2 --> positive
-3 + 2 = -1 --> negative 

in this case the solution would be 3. 

EXPLANATION 

If we add 3 to the array than every value will be positive. Meaning at least 1 

Proof: 

3 + 3 = 6 --> Positive
-5 + 6 = 1 --> Positive 
4 + 1 = 5 --> Positive 
-3 + 5 = 2 --> Positive 
