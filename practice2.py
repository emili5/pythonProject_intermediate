def fibonacci(n):
    while n<=20:
        if n <= 1: 
            return n 
        else: 
            return(fibonacci(n-1) + fibonacci(n-2)) 
        
sum=0          
sum+=fibonacci(20)
print(sum)
