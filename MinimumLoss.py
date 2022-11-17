"""https://www.hackerrank.com/challenges/minimum-loss/problem"""


def minimumLose(price):
    minimum=float("inf")   #defined inf number. Becase dont know how biggest number will come in price list.
    for i in price:
        for j in price:
            if price.index(i)<price.index(j) and (i-j) >0:
                minimum=min(minimum,(i-j))
            else:
                continue

    return minimum


