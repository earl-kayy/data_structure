from listStack import *
from changeOrder import *

# 입력받은 문자열이 좌우 대칭인지 확인하는 함수
def checkReverse(string):
    
    sub_str1 = string.split('$')[0]
    sub_str2 = string.split('$')[1]

    return sub_str2 == reverse(sub_str1)

string = input("문자열을 입력 : ")
print(checkReverse(string))

