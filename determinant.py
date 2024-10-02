def find_determinant(a,b,c,d,e,f,g,h,i):
    det_A = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return det_A

#Enter Numbers Here to find 3 x 3 Determinant
print("Value Format: a,b,c,d,e,f,g,h,i")
value = int(input("Enter determinant number :"))
    ans = find_determinant(value)
    print(ans)

