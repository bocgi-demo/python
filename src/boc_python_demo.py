
def my_sum(n):
    if n > 1:
        return my_sum(n - 2) + my_sum(n - 1)
    else:
        return 1


def terrible_code():
    for i in range(1000):
        if i % 3 < 2:
            for j in range(i):
                x = int(str(j)+ str(i))
                if x % 2:
                    break
            else:
                x = 0
        else:
            for k in range(x):
                x += k
        res = x
    return res


if __name__ == '__main__':
    print(my_sum(5))