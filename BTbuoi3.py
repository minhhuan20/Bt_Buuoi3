# BT3.1
# Ket qua hien thi: Hello Yo 7 
# Giai thich: 2 ham print ra Hello Yo
# ban dau x=5 sau x = 5+2 =7


# BT 3.2
import math
print("nhap nam sinh: ",end="")
ns=int(input())
def namsinh(n):
    print(f"Ban sinh nam {n}, nam nay {2020-n} tuoi")
namsinh(ns)

# BT3.3
def celcius(f):
    c=5*(f-32)/9
    print(c)
print("nhap nhiet do f: ",end="")
f=int(input())
celcius(f)

#BT3.4
def mua(thang):
    if thang < 4: 
        print("Mùa Xuân")
    elif thang <7:
        print("Mùa Hè")
    elif thang <10:
        print("Mùa Thu")
    else:
        print("Mùa Đông")
print("nhap thang: ",end="")
thang=int(input())
while thang<1 or thang>12:
    print("tháng không hợp lệ, nhập lại")
    thang=int(input("Nhap thang: "))
mua(thang)


#BT3.5
def max(*arr):
    max=0
    for i in arr:
        if i>max:
            max=i
    return max
print("nhap a:",end="")
a=int(input())
print("nhap b:",end="")
b=int(input())
print("nhap c:",end="")
c=int(input())
print(f"So lon nhat trong {a},{b},{c}: {max(a,b,c)}")


#BT3.6
def dttron(r):
    s=math.pi*r*r
    return s
r=int(input("Nhap ban kinh: "))
print(f"Dien tich hinh trong co ban kinh {r}: {dttron(r)}")

# Bai tap

# Tim so nghich dao
def timsodao():
  n= int(input("nhap n de nghich dao: "))
  print(str(n)[::-1])
timsodao()

# Tim giai thua
def giaithua():
  n= int(input("nhap n tinh giai thua: "))
  s = math.factorial(n)
  print(s)
giaithua()

# Tinh tong
def tinhtong():
  n= int(input("nhap n: "))
  x = 0
  for i in range(1, n):
    i+=1
    x += pow(i,3)
  print(x)
tinhtong()

# Tong le
def tongle():
  n= int(input("nhap so le: "))
  x = 0
  while n % 2 ==0:
    n= int(input("nhap lai: "))
  for i in range(n):
     i += 1
     if i % 2 != 0:
      x += i
  print(x)
tongle()

# Tong chan
def tongchan():
  n= int(input("nhap so chan: "))
  x = 0
  while n % 2 !=0:
    n= int(input("nhap lai: "))
  for i in range(n):
     if i % 2 == 0:
      x += i
  print(x)
tongchan()

# Tim so nguyen to
def timsonguyento():
  n = int(input("nhap 1 so bat ki: "))
  if n < 2:
    return False
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True
if timsonguyento():
  print("no la so nguyen to")
else:
  print("khong phai la so nguyen to")   

# Tim so chinh phuong
def sochinhphuong():
  n =  int(input("nhap n: "))
  i =0
  while i * i <= n:
    if i * i == n:
      print("so nay la so chinh phuong")
      return 0
    i+=1
  print("so nay khong phai la so chinh phuong")  
sochinhphuong()

# Tinh tong so nguyen to
def snt(n):
    if n<2:
        return 0
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
n=int(input("Nhap n:"))
if snt(n)==0:
    print(f"{n} khong phai snt")
else:
    print(f"{n} la snt")
def tongsnt(n):
    s=0
    for i in range(1,n+1):
        if snt(i):
            s+=i
    print(f"Tong cac so nguyen to: {s}")
n=int(input("Nhap n:"))
tongsnt(n)

# bangcuuchuong
def bangcuuchuong(n):
    for i in range(1,11):
        print(f"{i}*{n}={i*n}")
print("nhap n: ",end="")
n=int(input())
bangcuuchuong(n)

# Tinh so fibonacci thu n
def fibo(n):
    "Ham tinh so fibonacci"
    if n==1 or n==2:
        return 1
    return fibo(n-1) + fibo(n-2)
print("nhap n:",end="")
n=int(input())
print(f"So fibo thu {n}: {fibo(n)}")

# Bai tap ve nha

# Bai 1
print("max min")
def max_min(*numbers):
    print(f"Day so duoc truyen vao: {numbers}")
    return max(numbers),min(numbers)
max,min=max_min(1,3,15,10,2,50,100)
print(f"max: {max}, min: {min}")

# Bai 2
def reverse_string(str):
    return str[::-1]
str=input("Nhap so muon ngich daodao: ")
print(f"sau khi nghich dao: {reverse_string(str)}")

# Bai 3
print("so hoan hao")
def is_perfect(n):
    if(n<=0):
        return False
    if sum(i for i in range(1, n//2+1) if n%i==0)==n:
        return True
    else:
        return False
print("so muon kiem tra: ",end="")
n=int(input())
print(f"{n} True ") if is_perfect(n) else print(f"{n} False")


# Bai 4
print("Kiem tra so nguyen to")
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
print("Nhap so muon kiem tra: ",end="")
n=int(input())
if is_prime(n):
    print(f"{n} TrueTrue")
else:
    print(f"{n} False")

# Bai 5
print("Dem chu hoa va chu thuong")
def count_upper_lower(str):
    upper=lower=0
    for i in str:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print(f"So chu hoa: {upper}|So chu thuong: {lower}")
str=input("Nhap chuoi: ")
count_upper_lower(str)

# Bai 6
print("chuoi pangram")
def is_pangram(str, alphabet):
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
str=input("Nhap chuoi muon kiem tra: ")
alphabet="abcdefghijklmnopqrstuvwxyz"
if is_pangram(str,alphabet):
    print(f" \"{str}\" True")
else:
    print(f" \"{str}\" False")

# Bai 7
print("ma tran")
def create_matrix(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(i*j,end="\t")
        print()
n=int(input("so hang la: "))
m=int(input("so cot la: "))
create_matrix(n,m)

# Bai 8
print("Tinh BMI")
def body_mass_index(m,h):
    BMI=m/math.pow(h,2)
    return BMI
def bmi_information(m,h):
    bmi=body_mass_index(m,h)
    if bmi > 30:
        print("Beo phi")
    elif bmi >=25:
        print("Thua can")
    elif bmi >=18.5:
        print("Binh thuong")
    else:
        print("Gay")
m=float(input("Nhap can nang: "))
h=float(input("Nhap chieu cao: "))
while m<0 or h<0:
    print("Du lieu khong hop le\n Nhap lai")
    print("can nang la: ",end="")
    m=float(input())
    print("Chieu cao la: ",end="")
    h=float(input())
bmi_information(m,h)

# Bai 9
print("Chuyen chu hoa thanh thuong va nguoc lai")
def change_upper_lower(str):
    str=str.swapcase()
    print(f"Chuoi sau khi chuyen: {str}")
str=input("Nhap chuoi muon chuyen: ")
change_upper_lower(str)

# Bai 10
print("De quy tra ve nhung so le cua so n cho truoc")
i=0
def count_odd(n,i):
    if i==len(n) or n[i].isnumeric==False:
        return 0
    if int(n[i])%2!=0:
        return 1+count_odd(n,i+1)
    else:
        return 0+count_odd(n,i+1)

n=input("Nhap so can kiem tra: ")
print(count_odd(n,i))


# Bai 11
print("Tim day Fibonacci theo de quy")
def fibo_dequy(n):
    if n==1 or n==2:
        return 1
    return fibo_dequy(n-1) + fibo_dequy(n-2)
print("Tim Fibonacci khong theo de quy ")
def fibo_thuong(n):
    n1=0
    n2=1
    for i in range(n-1):
        temp=n1+n2
        n1=n2
        n2=temp
    return temp
print("nhap so fibo: ",end="")
n=int(input())
while n<=0:
    print("So khong hop le\n Nhap lai")
    print("nhap so fibo: ",end="")
    n=int(input())
print(f"De quy: {fibo_dequy(n)}")
print(f"Khong de quy: {fibo_thuong(n)}")