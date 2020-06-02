def fun(x):
    if x == 1:
        return 1
    return x * fun(x-1)
if __name__ == '__main__':
    print(fun(5))