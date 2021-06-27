
print(int(3.5)      ) # 3
print(2e3           ) # 2000.0
print(float("1.6")  ) # 1.6
print(float("inf")  ) # 무한대
print(float("-inf") ) # -무한대
print(bool(0)       ) # False. 숫자에서 0만 False임,
print(bool(-1)      ) # True
print(bool("False") ) # True
a = None      # a는 None
print(a)
print(a is None)     # a가 None 이므로 True

print("복소수")
print("===================================")
v = 2 + 3j
print(v.real)
print(v.imag)

if a != 1:
    print("1이 아님")


a = 1
a = a * 10
a *= 10     # 위와 동일한 표현
print(a)