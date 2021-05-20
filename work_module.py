def list_to_dict(mas) -> dict:
    return {i:mas.count(i) for i in mas}

def string_intersec(str1, str2) -> set:
    return set(str1).intersection(str2)

def longest_ascending_seq(int_mas) -> list:
    L = []
    M = []
    j = 1
    
    while j < len(int_mas):
        i = j
        N = int_mas[:]
        while i < len(N)-1:
            if N[i] < N[i+1]: 
                M.append(N[i])
                i += 1
            else:
                N.pop(i+1)
        
        j+=1
        if len(L) < len(M):
            L = M
        M=[]
    
    if int_mas[-1] > L[-1]:
        L.append(int_mas[-1])
    
    if int_mas[0] < L[0]:
        L.insert(0, int_mas[0])
    
    return L

if __name__ == '__main__':
    print(list_to_dict([1, 2, 3, 4, 5, 5, 4, 3, 2, 0]))
    print(string_intersec("string", "stria",))
    print(longest_ascending_seq([1, 2, 3, 4, 5, 5, 4, 3, 2, 0, 6]))