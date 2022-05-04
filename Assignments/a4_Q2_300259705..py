def two_length_run(l):
    '''
    (list) -> bool()
    takes a list of numbers as input parameter and returns True if the given list has at least one run
    (of length at least two), and False otherwise.
    '''
    i = -1
    d = -1
    while i < len(l) - 1 and d < len(l) - 2:
        i += 1
        d += 1
        if l[i] == l[d + 1]:
            return True
    return False

#main
a = input("Please input a list of numbers separated by space: ").strip().split()
print(two_length_run(list(a)))
