def longest_run(l):
    '''
    (list) -> (int)
    returns the length of the longest run.
    '''
    i = -1
    d = -1
    count=0
    if l==[]:
        return 0
    else:
        while i < len(l) - 1 and d < len(l) - 2 :
            i += 1
            d += 1
            if int(float(l[i]))==int(float(l[i+1])):
                count+=1
        if count==0:
            return 1
        else:
            return count
#main
a = input("Please input a list of numbers separated by space: ").strip().split()
print(longest_run(list(a)))
