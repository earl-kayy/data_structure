from listStack import *

# 양쪽 괄호의 균형이 맞는지 (정상적으로 괄호가 닫혔는지) 를 확인하는 함수
def paranBalance(expression):
    st = ListStack()
    for i in range(len(expression)):
        if expression[i] == '(':
            st.push(expression[i])
        
        elif expression[i] == ')':
            if st.isEmpty(): return False
            st.pop()
    return st.isEmpty()

def main():
    input1 = "((800/(3+5)*2)"
    input2 = "(82+2) / 4)"
    input3 = "(91 * (40-35) +2)"
    print(input1, ":", paranBalance(input1))
    print(input2, ":", paranBalance(input2))
    print(input3, ":", paranBalance(input3))

if __name__ == "__main__":
    main()