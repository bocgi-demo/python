import math
import flask


def my_sum(n):
    if n > 1:
        return my_sum(n - 2) + my_sum(n - 1)
    else:
        return 1


def my_sum2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif n == 4:
        return 5
    elif n > 5:
        res = {
            -1: 1,
            0: 1,
            1: 1,
            2: 2,
            3: 3,
            4: 5,
            5: 8
        }
        for i in range(1, n):
            res[i] = res[i - 1] + res[i - 2]
        return res[i]


def I_will_destory_code_style(n):
    I_m_smart= [sum((range(i))) for i in range(n)][-1]

    return I_m_smart


if __name__ == '__main__':
    print(my_sum2(20))
    print(my_sum(20))
    print(I_will_destory_code_style(10))
