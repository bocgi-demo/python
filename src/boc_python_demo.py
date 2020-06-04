
def my_sum(n):
    if n > 1:
        return my_sum(n - 2) + my_sum(n - 1)
    else:
        return 1


if __name__ == '__main__':
    print(my_sum(5))