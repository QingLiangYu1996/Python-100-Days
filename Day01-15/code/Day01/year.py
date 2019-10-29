year = int(input('请输入年份'))
is_leap= (year %4 == 0 and  year % 100 != 0 ) or \
          year %400 == 0
if is_leap == True:
    print('%s年是闰年' %year)
else:
    print('%s年不是闰年' %year)
    