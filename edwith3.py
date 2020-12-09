#!/usr/local/bin/python3
#시급 계산기 try 와 except 구문쓰기

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error,Please enter number input")
    quit()
print(fh,fr)
if fh > 40 :
    print("Overtime ")
    reg = fr * fh
    otp = (fh - 40.0) * (fr *0.5)
    print(reg,otp)
    xp = reg + otp
else:
    print("Regulartime")
    xp = fh * fr
print("pay:",xp)
