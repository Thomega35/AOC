import hashlib
IN = "yzbqklnj"
hashihasha = hashlib.md5(IN.encode()).hexdigest()
print(hashihasha[0:5])
i=0
while hashihasha[0:6] != "000000" :
    hashihasha = hashlib.md5((IN + str(i)).encode()).hexdigest()
    i+=1
print(hashihasha,i-1)