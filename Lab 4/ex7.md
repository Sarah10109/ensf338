### Question 1
The Complexity itself would be O(n^2) because the for loop itterates through the entire list from back to front. Then inside the forloop the
get_element function has to itterate through the list again so its basically a forloop inside a forloop. therefore n^2 complexity.

## Question 2
To make the funciton O(n) I just need to make the initial forloop start from front to back. store a variable to keep the previous node and make the current node then point to previous. Then make the current node point to its successor. All this should be in a while current is not None loop.
