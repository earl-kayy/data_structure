from listStack import *

#스택이 정상적으로 동작하는지 확인하는 임시 테스트 코드

st1 = ListStack()
st1.push(100)
st1.push(200)
print("Top is", st1.top())

st1.pop()
st1.push("Monday")
st1.printStack()
print("isEmpty", st1.isEmpty())
