temp=float(input('请输入要转换的温度:'))
unit=input('请输入单位: C/F')

if unit=='C':
    F=temp*9/5+32
    F=round(F,2)
    print('经转换后的华氏温度是'+str(F)+'F')
elif unit=='F':
    C=(temp-32)*5/9
    C=round(C,2)
    print('经转换后的摄氏温度是'+str(C)+'C')
else:
    print('您输入的温度单位有误')