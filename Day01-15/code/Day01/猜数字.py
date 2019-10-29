import random

answer= random.randint(1,100)
counter= 0
while True:
    counter +=1
    nuber= int(input('请猜一个1~100的数字：'))
    if nuber <0 and nuber>100:
        print ('请输入正确数值')
    elif nuber < answer:
	    print ('猜小了')
    elif nuber > answer:
        print ('猜大了')
    else:
	    print ('恭喜你猜对了')
	    break
print ('你总共猜了%d次' %counter)