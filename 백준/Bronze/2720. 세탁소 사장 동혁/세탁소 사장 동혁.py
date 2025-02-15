t = int(input())
for i in range(t):
    case = int(input())
    print(case//25, case%25//10, case%25%10//5, case%25%10%5)