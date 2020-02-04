
cals = [1+1,1-1,2*3,3/1,3**4]
desc = ['加法','减法','乘法','除法','乘方']
for index,cal in enumerate(cals):
    r = cal
    print(desc[index], "计算结果[{0}]".format(r), "类型", type(r))











