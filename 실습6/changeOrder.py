from listStack import *

# 인자로 받은 문자열의 순서를 뒤바꾸는 함수
def reverse(str):
    st = ListStack()
    for i in range(len(str)):
        st.push(str[i])
    out = ""
    while not st.isEmpty():
        out += st.pop()
    return out

def main():
    input = "Hong Ryoonki"
    answer = reverse(input)
    print("Input String :", input)
    print("Output String :", answer)

if __name__ == "__main__":
    main()