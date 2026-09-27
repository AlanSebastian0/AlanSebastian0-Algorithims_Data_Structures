#print the numbers 1-10 recursively

def main():
    n=10
    recursion_print(10)

def recursion_print(n):
    if n == 0: #base case stop printing when n=0
        return
    print(n)
    return recursion_print(n-1)

if __name__ == "__main__":
    main()
