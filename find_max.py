def find_max_recursive(list, n): # n 은 list 의 마지막 인덱스
    # 나를 뺀 나머지랑 비교 -> else 의 경우
    if n==1: # list 가 2개 요소밖에 없을 때는 둘이 비교
        return list[0] if list[0] > list[1] else list[1]
    else: # list 에 여러 요소 있을 때는, 함수의 목적 생각해서 뭉뚱그려서 생각하기
        return list[0] if list[0] > find_max_recursive(list[1:], n-1) else find_max_recursive(list[1:], n-1)

def find_max_iterative(list):
    max = -10000000
    for element in list:
        if element > max:
            max = element
    return max

print("10개의 숫자를 입력하시오")


numbers = list(map(int, input().split()))

result1 = find_max_recursive(numbers, len(numbers)-1)
result2 = find_max_iterative(numbers)

print("최대값:", result1)
print("최대값:", result2)
