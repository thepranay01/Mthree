def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    seq = fib(n - 1)
    seq.append(seq[-1] + seq[-2])
    return seq


num = int(input("Enter the number of terms: "))
print(" ".join(map(str, fib(num))))