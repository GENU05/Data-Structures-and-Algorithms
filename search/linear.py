def linear(a,n):
    for i in range(len(a)):
        if a[i] == n :
            return True 
    return False 

a = [1,0,-1,9,8,4,9]
print("is number 5 in list? :",linear(5))