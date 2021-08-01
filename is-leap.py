def is_leap(year):
    if year % 4 != 0 :
        return 'False,是平年'
    elif year %100 != 0 :
        return 'True,是閏年'
    elif year  % 400 != 0 :
        return 'False,是平年'
    elif year % 3200 != 0:
        return 'True,是閏年'
        
print(is_leap(int(input('請輸入年份:'))))
