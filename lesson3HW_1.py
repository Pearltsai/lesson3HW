import random
p=0
x=random.randint(1,10)
while p<1:
    g=input('猜數字')
    g=int(g)    
    if g!=x:
        print('你猜錯了')
    
    else:
        print('你猜對了')
        p=5
