name=[]
num=[]
s=input("請輸入班級人數")
s=int(s)

for i in range(s):
     b=input("請輸入名字")
     num.append(b)
     e=int(input("請輸入成績")) 
num.append(e)
print(num)
a=0
for i in range(s):
 a = a + num[i]

avg= a/s
print("平均分",avg)
biggest=0
indexbig=0
for i in range(s):
    if  num[i] > biggest:
        biggest = num[i]
        indexbig = i
print(name[indexbig],"最高分: ", biggest )        
smallest = 100
indexsmall = 0   
for i in range(s):
    if  num[i] < smallest:
        smallest = num[i]
        indexsmall = i
print(name[indexsmall], "最分: ", indexsmall )      