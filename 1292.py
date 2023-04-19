# 정수 A와 B를 입력받는다.
a, b = map(int, input().split())

# 수열을 담을 배열을 만든다.
# 편의를 위해 0번째 배열을 0으로 초기화한다.
array = [0]

# 수열을 만든다.
for i in range(1, b+1):
  for _ in range(i):
    array.append(i)

# 입력받은 A부터 B구간에 대한 수열의 합을 구한다.
sum = 0
for i in range(a, b+1):
  sum += array[i]

# 결과를 출력한다.
print(sum)