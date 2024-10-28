'''
Write a program to count the number of times the given value is repeated.
Input Format:
First line of input consists of our list elements.
Second line of input consists of value to count.
Output Format:
Print thr number of times the given value is repeated in the list.
Sample Input:
10 20 10 40 10
10
Sample Output:
3
'''
lst = list(map(int,input().split()))
value = int(input())
count = 0
for i in lst:
  if i == value:
    count += 1
print(count)
