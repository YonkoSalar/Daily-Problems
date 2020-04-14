#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

lst = [5, 1, 15, 23]
lst2 = []
k = int(input("Tast inn for K: "))

def function():
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            lst2.append(lst[i]+lst[j])

    for b in range(len(lst2)):
        if(lst2[b] == k):
            return True
        else:
            return False

print(function())






