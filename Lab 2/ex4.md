Q1
Assume the sign is read we would already know if our room is contained in list given by the sign. It is unknown to us if the rooms are sorted. Therefore, the first step is to turn left and check the room number. If the room number is equal to target room number you found the room. Else go check the next room. Repeat until the room is found.  

Q2
It would take 15 steps. Each step is the check if the current room you are at is the room you are looking for.   

Q3
This is would be neither case as its not the worse-case or the best-case.

Q4
The worst-case being the target room being the very last room there to check. Meaning the first room if you went to the right. And the best case is that it would be the first room we check being the target. 

 Q5
 We make variable left and set it equal to abs(target - 100), make another variable right and set it equal to abs(target - 138). Then compare the 2 variables, which ever is lower decides the direction we first take. If left or right == 0, then best case scenario, else take smallest between left and right and divide by 2, then set equal to variable direction. Think of the rooms as an array, you then want to skip over by passing by (direction - 1) number of rooms.