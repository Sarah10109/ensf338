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
Once the second node reaches the end the first pointer should be pointing roughly in the center of the list.

ILL FINISH THIS LATER!!!!! I PROMISE