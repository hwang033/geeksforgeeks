# geeksforgeeks 
Python code for geeksforgeeks

1. merge sort can be used on sorting linkedlist, stable, o(n) space

2. merge sort and quick sort is widely used 

3. Interpolation search: the input is ordered. similar to binary search.
    mid = low + (key - arr[low])*((high - low)/(arr[high] - arr[low]))
    O(log(log(n))) when the array is unifomly distributed

4. stable sort: insertion sort, merge sort, bubble sort
    unstable sort: heap sort, quick sort

5. worst case for quick sort id O(n^2) but heapsort and merge
    sort are O(nlogn) 

6. cycle sort: for each element count how many element is less than it
    and put it to the right place. Cycle sort makes leat number of write.

7. range from 0 to n^2 -1 can be represented using base n(two digits).
    45 using base 7 = 63 

8. counting sort, count the number first, then for each i,
    count[i] += count[i-1], get the position of the number

9. huffman code(compression): compute probability of each parrten, 
   sum less probability together and get huffman tree. prefix code.

10. recursive call is the last thing excuted by the function is called tail recursion. tail recursion is considered better than non tail recursive functions. non tail recursive fucntions can be changed to tain tecursive function by adding new parameter.

11. detect cycle in a directed graph using back edge. dectect cycle in an undirected graph using union find. Because undirected graph more than one grey vertice will be found. 

12. will be used in job sequence problem. Union by rank: a quick method to find the parent.

13. greedy algorithm can give approximation of some NP problem 

14. Longest increasing subsequence has O(nlogn) method using binary search



