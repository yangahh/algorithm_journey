a, b = map(int, input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print("==")


#print(['><'[a < b],'=='][a==b])
