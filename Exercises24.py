# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/18

'''
求1+2！+3！+4！……+20!的和
'''
s=0

for i in range(1,21):
    n=1
    for j in range(1,i+1):
        n*=j
    s+=n
print(s)