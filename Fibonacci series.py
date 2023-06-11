
def fibonacci(i):

    if i <= 0:
        print("Please enter a positive integer")
        return

    elif i == 1:
        return 0

    elif i == 2:
        return 1

    else:
        return fibonacci(i-1) + fibonacci(i-2)




# main function
n = 35
fibonacci_seq = []
for i in range(1,n+1):
    fibonacci_seq.append(fibonacci(i))

print(fibonacci_seq)