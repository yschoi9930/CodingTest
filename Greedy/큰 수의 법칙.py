# n개의 숫자들을 중복포함 m번 더해서 가장 큰 수를 만든다
# but k번 초과하여 중복되서는 안된다

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 오름차순 정렬
print(data)
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k + m % (k+1)
last = m - count

result = first * count + second * last
print(result)

# 모범답안
count = int(m / (k+1)) * k
count += m % (k+1)
result = 0
result += count * first
result += (m-count) * second
print(result)