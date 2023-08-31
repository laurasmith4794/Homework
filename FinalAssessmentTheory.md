# Final Assessment - Section 1: Theory Questions

### 1.1 The deque module is part of which python library?
The deque module is a double-ended queue and is part of the collections library.

### 1.2 What are 2 differences that distinguish a tree from a graph?
A tree has a hierarchical structure where each node has one parent and any number of children.
A graph has a network structure where each node can have any number of edges connecting it to other nodes.
A tree has a single root node that is used as the starting point for traversing the tree but a graph does not necessarily have a root node.

### 1.3 Give the definitions of time complexity and space complexity.
Time complexity is a measure of how fast an algorithm runs. It helps to define the effectiveness of an algorithm and to evaluate its performance.
Space complexity is a measure of how much auxiliary memory an algorithm takes up. It helps to determine how much extra space would be needed by the algorithm with change in the input size.
The Big 0 notation is used to describe the time complexity and space complexity of algorithms.

### 1.4 Describe the bubble sort algorithm and its complexity. What is guaranteed at the end of the first pass?
The bubble sort algorithm works by repeatedly swapping adjacent elements in an array if they are in the wrong order.
The algorithm starts from the left end of the array and compares each pair of elements until it reaches the right end. If the left element is larger than the right element then they are swapped.
This process is repeated until no more swaps are needed, which means the array is sorted.

Bubble sort repeatedly passes through the unsorted part of the list so it has a worst case time complexity of O(n^2), where N is the number of elements in the array.
This is because the algorithm has to make n-1 passes over the array, and each pass involves n-1 comparisons and swaps.
The space complexity of bubble sort is O(1) as it only uses a constant amount of extra space for temporary variables.

At the end of the first pass, bubble sort guarantees that the largest element in the array is placed at its correct position which is at the rightmost end of the array.
This is because every time a larger element is encountered, it is swapped with its adjacent element until it reaches the end.
For example, if the input array is [5, 3, 2, 4, 1], then after the first pass, the array will be [3, 2, 4, 1, 5], as 5 is the largest element.

### 1.5 Explain what LIFO and FIFO are and how each works in practice with a named data structure.
LIFO and FIFO are techniques for maintaining data in a data structure. They determine the sequence of entry/exit of data into a data structure.

LIFO stands for Last In, First Out and uses a stack data structure. In a LIFO data structure, the newest/last element added to the stack is processed first.

A stack is a linear data structure that follows the principle of LIFO. The operations of a stack are:
push (adds an element to the top of the stack);
pop (removes and returns the element from the top of the stack);
peek (returns the element from the top of the stack without removing it);
isEmpty (checks if the stack is empty or not).

FIFO stands for First In, First Out and uses a queue data structure. In a FIFO data structure, the first element added to the queue is processed first.

A queue is a linear data structure that follows the principle of FIFO. The operations of a queue are:
enqueue (adds an element to the rear of the queue);
dequeue (removes and returns the element from the front of the queue);
front (returns the element from the front of the queue without removing it);
rear (returns the element from the rear of the queue without removing it);
isEmpty (checks if the queue is empty or not).

### 1.6 What is a Balanced Binary Tree and what would be the best root? Walkthrough how you search using this structure.
A balanced binary tree is a binary tree in which the left and rightsubtrees of every node differ in height by no more than 1 and the left and right subtree of that node is also balanced.
Binary trees are used to manipulate hierarchical data and make information easier to search.

The best root for a balanced binary tree is the one that minimizes the height of the tree.
A way to determine this would be to use the median of the sorted values as the root then recursively construct the left and right subtrees from the remaining values as in in the example below:

![image](https://github.com/laurasmith4794/Homework/assets/137213894/b6767728-f0ec-4cf1-91c1-69bd080dca8e)

To search for a value in a balanced binary tree, we can use a recursive algorithm that compares the value with the root then moves to the left or right subtree depending on whether the value is smaller or larger.
If the value is equal to the root, we have found it. If we reach a null node, we have not found it.

If we are searching for 5 in the example above then 5 would be compared with the root, which is 4. As 5 is larger than 4, we move to the right subtree.
5 is then compared with the root of the right subtree, which is 6. As 5 is smaller than 6, we move to the left subtree.
5 is then compared with the root of the left subtree, which is 5 and since they are equal, we have found it.
