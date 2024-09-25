if __name__ == 'main':
    n = int(input("enter a value to find the runner up score:" ))
    arr = map(int_raw_input().split())

    a = max(arr)
    c=arr.count(a)
    for i in range(c):
        arr.remove(a)
    print(max(arr))