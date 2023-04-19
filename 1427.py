# 정렬하려는 수 n을 입력받는다.
n = int(input())

# 정렬함수를 쓰기 위해 n의 각 자리수를 배열에 집어 넣는다.
array = []  # 배열 초기화
for i in str(n):
  array.append(int(i))

# 정렬 - 내림차순 !
array.sort(reverse=True)

# 정렬된 배열을 한줄로 출력한다.
for i in array:
  print(i, end="")