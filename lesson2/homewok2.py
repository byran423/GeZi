

# ﻿课后作业，实现如下方法(可2选1)
# def share_amount(total_amount=1000, weight=[5,5,5]):
#    ...
#    要求:
#        1. return 结果保留2位小数，加起来总和等于total_amount
#    return [333.33, 333.33, 333.34]
def share_amount(total_amount=1000, weights=[5,5,5]):
    sum_weight = sum(weights)
    list1 = []
    for index, weight in enumerate(weights):

        if index != len(weights)-1:
            rate = weights[index] / sum_weight
            r = round(total_amount * rate, 2)
            list1.append(r)
        else:
            r = round(total_amount - sum(list1), 2)
            list1.append(r)
    print(list1)


if __name__ == "__main__":
    share_amount(total_amount=1000, weights=[1,1,1])







