"""
HackerRank Single Array Sum
https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true
"""

def compareTriplets(a, b):
    sumAlice = 0
    sumBob = 0
    for i in range(len(a)): # We could get len of b also. Because arrays(a,b) always have same lenght.
        if a[i]>b[i]:
            sumAlice=sumAlice+1
        elif a[i]<b[i]:
            sumBob=sumBob+1
        else:
            continue
    return sumAlice,sumBob

