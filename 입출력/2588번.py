A = input()
B = input()

z = (int(A[0])*int(B[2])*100)+(int(A[1])*int(B[2])*10)+(int(A[2])*int(B[2]))
x = (int(A[0])*int(B[1])*100)+(int(A[1])*int(B[1])*10)+(int(A[2])*int(B[1]))
c = (int(A[0])*int(B[0])*100)+(int(A[1])*int(B[0])*10)+(int(A[2])*int(B[0]))

print(z)
print(x)
print(c)
print(int(z)+(int(x)*10)+(int(c)*100))