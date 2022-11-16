def isValid(s):

    liste=[]
    liste2=[]
    dict={}
    dict2={}

    for i in s:
        dict[i]=s.count(i)
    for j in dict.values():
        liste2.append(j)
    for k in liste2:
        dict2[k]=liste2.count(k)

    if len(dict2) ==1:
        return "YES"
    if len(dict2) > 2:
        return "NO"
    if 1 in dict2.values() and (dict2[min(dict2.keys())] or (max(dict2.keys()) - min(dict2.keys())==1)):
        return "YES"
    else:
        return "NO"
