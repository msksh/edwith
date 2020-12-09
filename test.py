#!/usr/local/bin/python3
print("Content-Type: text/html")
print()

x =0.6
x = x = 3.9 * x * (1 - x)
print(x) # 0.936 출력됨.
          #3.9 * 0.6 * (1 - 0.6)
x = 3.9 * x * (1 - x )
print(x) # 0.2336256 출력됨.
          #3.9 * 0.936 * (1 - 0.936)
ddd = 1 + 4
print(ddd) # 5로 출력됩니다.

eee = 'hello ' + ' there'
print(eee) # hello there로 출력됩니다.
'''
eee = eee + 1 #문자열 타입과 정수형 타입을 더하려 했기 때문에 에러가 발생합니다.
eee = 'hello' + ' world'
print(eee) # hello world
'''
type(eee) # class 'str' 문자열 클레스 타입
type(1) # 정수 클레스 타입
i = 42
type( i ) # int 타입
f = float( i ) # float 타입으로 변환
print( f ) # 42.0으로 출력

type( f ) # float 타입
sval = '123'
type(sval) # str 타입


ival = int(sval)
type(ival) # int 타입
print(ival + 1) # int 타입 간 연산이기 때문에 오류 발생하지 않는다. 124로 출력됨
nam = input('Who are you? ') #Who are you? 라고 물어 볼 것이고 사용자는 입력값을 넣습니다.
print('Welcome', nam) # 해당 입력값을 nam이라는 변수에 할당한 다음 Welcome이라는 문자열과 함께 출력합니다.
