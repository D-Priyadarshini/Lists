'''
Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 
'''
lst = list(map(int,input().split()))
print(" ".join(map(str, lst[::-1])))
#print(*lst[::-1])
