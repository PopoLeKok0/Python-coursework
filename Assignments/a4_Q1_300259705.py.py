def number_divisible(l,n):
    '''
    (list,int) -> (int)
    returns the number of elements in the list that are divisible by n
    '''
    count=0
    for i in range(len(l)):
        if int(l[i])%int(n)==0:
            count+=1
    return count

#main
a = input("Please input a list of numbers separated by space: ").strip().split()
n=input('Please input an integer: ')
print('The number of elements divisible by '+ n + ' is '+ str(number_divisible(list(a),n)))
