#Program to find generators in cyclic multiplicative group

def calculate(a, x, n):
    exponent = bin(x).replace("0b", "")

    solution = a
    for i in range(1, len(exponent)):
        if(exponent[i] == "1"):
            solution = (solution * solution) % n
            solution = (solution * a) % n

        if(exponent[i] == "0"):
            solution = solution * solution % n

    return solution


def main():
    array = []
    count = 0
    
    a = 0
    n = 4973
    while(a < n-1):
        a += 1
        for x in range(1, n-1):
            answer = calculate(a, x, n)
            if(answer in array):
                array.clear()
                break
            if(answer not in array):
                array.append(answer)
                
            if(len(array) == n - 2):
                print(f"{a} is a primitive root of {n}")
                count += 1
                array.clear()
    print(f"There are {count} primitive roots in Z*{n}")

if __name__ == "__main__":
    main()