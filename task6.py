

def check():
    chetnie = 0 
    nechetnie = 0 
    num = [33 , 44 , 66, 77, 88]
    for i in num:
        if i % 2 == 0:
            chetnie += 1
        else:
            nechetnie += 1
    return chetnie , nechetnie
print (check())