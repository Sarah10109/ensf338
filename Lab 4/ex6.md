|           | Arrays                                                   | Linked Lists                                          |
|-----------|----------------------------------------------------------|-------------------------------------------------------|
| **Pros**  | - Easy to Implement                                      | - Expandable                                          |
|           | - Retrival and Replacment are a complexity of O(1)       | - Dont need to worry about overwriting memory         |
|           |                                                          |                                                       |
| **Cons**  | - Adding / Removing Elements from Arrays can be awkward  | - Non Indexable. Requires O(n) for retrival           |
|           | - Having fixed sizes can lead to wasted/limited space    |                                                       |
|           | - If you choose to copy array it has complexity of O(n)  |                                                       |
**2** 
- Assuming we know which index we wish to perform these actions
- We can replace the location of the index with a NULL value instead of actually deleting the space. Then we wont be moving all the elements over by one
- causing an O(n) operation. Then we can simply replace the location of the NULL value with the new value.

**3**
### INSERTION
Yes it is fesible.
Since you can access the node before and after. it is easy to traverse the list looking for the spot meant for the node
Then you can move the pointers to point to the new node and the change the nodes before and after pointers as well
### MERGE
It is possible but a bit more tedious
To divide the linked list we need two pointers. One moves at one node at a time while the second moves two nodes.
Once the second node reaches the end the first pointer should be pointing roughly in the center of the list. From there you can have your two pointers. The middle pointer and the initial pointer.
Send those through the same merge sort function for the orignial node and middle pointers.
then return the merged array of the left and right arrays by putting it through a merge function which orderes the list from smaller and greater than the middle element.



**4**
The expected complexity refers to the average case for each style.
DOUBLY LINKED LISTS
For insertion it would be a complexity of O(1) since you only need the one step no matter the position but thats if its unordered. Ordered youd have an 
O(n) since you have to itterate through the list to find the position needed.

For Merge Sort
It seems a lot harder to determine. complexity as it has to go through half of the list to find the middle over and over. with each division of the lists, it need to itterate through the list to order it O(n). Since Merge is Divide and Conquer This prompts a O(nlog(n))
