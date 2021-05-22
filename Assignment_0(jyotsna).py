print("Qno. 1")
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]


for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)
print()

################################## QUESTION 2 ###################################################        

print("Qno. 2")		
color_1 = set(["White", "Black", "Red"])
color_2 = set(["Red", "Green"])

print(color_1.difference(color_2))

print()

################################# QUESTION 3: ###################################################

print("Qno. 3")
s=input('enter any string:')
alpha="abcdefghijklmnopqestuvwxyz"

flag=True
for char in alpha:
    if char not in s.lower():
        flag=False
if(flag==True):
    print("yaa!! its a pangaram string")
else:
    print("nahh!! its not a pangaram string")
print()

################################# QUESTION 4: ###################################################

print("Qno. 4")
num = int(input("input a number n: "))
temp = str(num)
t1 = temp + temp
t2 =temp + temp + temp
x = num + int(t1) + int(t2)
print("The Value of n+nn+nnn is : ",x)
print()

################################ QUESTION 5: ####################################################

print("Qno. 5")
num=input("Enter the input for list: ")
result=num.split('#')
list1=[int(i) for i in list(result[0].split())]
list2=[int(i) for i in list(result[1].split())]
print(list1)
print(list2)
print()

############################### QUESTION 6: #####################################################

print("Qno. 6")
words = input('ENTER comma saparated words:').split(',')
item = [i for i in words]
item.sort()
print(','.join(item))
print()

############################## QUESTION 7: ######################################################

print("Qno. 7")
dis={'student':[ 'Rahul' , 'kishore' , 'vidhya' ,'raakhi'],'marks':[57,87,67,79]}
idx = dis['marks'].index(max(dis['marks']))
print(dis['student'][idx])
print()

############################## QUESTION 8: ######################################################
 
print("Qno. 8")
sent = input("Enter a sentence : ")
alpha = 0
num = 0
for i in sent:
    if(i.isdigit()):
        num = num + 1
        
    elif(i.isalpha()):
        alpha = alpha + 1
print(" the number of digits are: ",num)
print(" The number of characters are: ",alpha)
print()

############################# QUESTION 9: #######################################################

print("Qno. 9")
data = {'Name': ['Akash', 'Soniy', 'Vishakha','Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

newdata = {'Name' : [],'Subject' :[], 'Ratings' : []}
inx = 0
for i in data['Subject']:
    if(i == 'Python'):
        newdata['Name'].append(data['Name'][inx])
        newdata['Ratings'].append(data['Ratings'][inx])
        newdata['Subject'].append(data['Subject'][inx])
    inx += 1     
print(newdata)
print()

############################ QUESTION 10: ######################################################

print("Qno. 10")
class generator :
    def __init__(num,r):
        num.n = r
  
    def gen_function(num) :
        for i in range(0,num.n + 1):
            if(not i%7):
                yield i
r = int(input('Enter the range: '))
gen = generator(r)
gen_list = list(gen.gen_function())
print('List of numbers divisible by 7 in the range 0 and ',r,' = ',gen_list)
print()

########################### QUESTION 11:########################################################

print("Qno. 11")
u = eval(input('UP : '))
d = eval(input('DOWN : '))
l = eval(input('LEFT : '))
r = eval(input('RIGHT : '))

net_up = abs(u - d)
net_right = abs(r - l)

distance = (net_up**2 + net_right**2)**0.5

print('walk distance = ',round(distance))
print()
print("@@@@@@@@@@@@@@@@@@ OVER!! @@@@@@@@@@@@@@@@@@")







