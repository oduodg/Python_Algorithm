# 2와 5의 인수를 가지고 있으면 뒷자리 0이 생긴다.
# 인수 2는 짝수일 때마다 하나씩 증가하므로 무조건 인수 5의 개수보다 많다.
# 인수 5의 개수를 기준으로 뒷자리 0의 개수를 구하면 된다.
# 5의 배수인 경우 인수 5를 여러 개 가지므로 n을 5로 나누어 준 값으로 갱신시키면서 while문을 돌린다.
n = int(input())
cnt = 0
while n >= 5:
    cnt += n//5  # 5로 나누어지는 수의 개수 구함
    n //= 5  # 5의 배수들은 5를 여러 개 가지므로 n을 5로 나누어주면서 while문 돌기
print(cnt)
