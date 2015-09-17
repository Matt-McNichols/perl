
---
* AI 
  *  8/24/15
  *  Website: https://moodle.cs.colorado.edu/
  *  Assignment 1 due friday 9/4/15

---
A* todo:
 *  store location in node
 *  enter while loop
 *  if end node is in closed list
    * rebuild the shortest path from linked list  
 *  move current node from openlist to closed list
 *  function that returns adjacent nodes
 *  calculate G score for all edge nodes based on current node
 *  calculate the F score for each adjacent node
 *  call function that updates the openlist
    *  if the edge is already in openlist and the new_F score is lower than the node's F,
       * update the node.f to new_F and change the node's parent to the current node
    *  if the edge is already in the openlist and the new_F is greater than the nodes's F do nothing
    *  if the edge node is not in openlist, calculate the F score and set the parent then add node to openlist
    *  return
 *  sort the openlist and set c_node to be openlist[0]
 
 
