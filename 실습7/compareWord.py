from listQueue import *

# 입력으로 들어온 문자열이 w$w 의 문자열의 원소인지 확인

def compareWord(string):
    sub_str1 = string.split('$')[0]
    sub_str2 = string.split('$')[1]

    if (len(sub_str1) != len(sub_str2)):
        return False
    queue = ListQueue()


    for i in range(len(sub_str1)):
        queue.enqueue(sub_str1[i])
    
    for i in range(len(sub_str2)):
        if (queue.dequeue() != sub_str2[i]):
            return False
    return True

string = input("문자열을 입력하시오: ")
print(compareWord(string))