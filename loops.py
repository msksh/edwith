#!/usr/local/bin/python3

#루프를 사용하여 개수세기

zork = 0
print('Before', zork)
numbers = [9, 41, 12, 3, 74, 15] # 강의와는 달리 numbers라는 int를 원소로 가지는 list를 선언하였습니다.
for thing in numbers :
    zork = zork + 1
    print(zork, thing)
print('After', zork)


#루프를 이용하여 합계구하기
#zork = 0
print('Before', zork)
numbers = [9, 41, 12, 3, 74, 15] # 강의와는 달리 numbers라는 int를 원소로 가지는 list를 선언하였습니다.
for thing in numbers :
    zork = zork + thing
    print(zork, thing)
print('After', zork)


#루프를 이용하여 평균구하기
count = 0 # 평균을 전체 원소의 수로 나누기 위해 total number를 확인합니다.
sum = 0
print('Before', count, sum)
numbers = [9, 41, 12, 3, 74, 15] # 강의와는 달리 numbers라는 int를 원소로 가지는 list를 선언하였습니다.
for value in numbers :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)


#루프를 이용하여 필터링 하기
print('Before')
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers :
    if value > 20:
        print('Large number', value)
print('After')

#부울값을 사용하여 특정 값을 검색하기
found = False
print('Before', found)
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers :
    if value == 3 :
        found = True
        print(found, value)
        break # 특정 값을 찾았을때 해당 루프를 종료하는 것이 더욱 적절해 보입니다.
print('After', found)

#가장 작은 수를 찾는 코드 완성하기

smallest = None
print('Before')
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)
