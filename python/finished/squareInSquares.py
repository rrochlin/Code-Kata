
def decompose(n):
    goal = n**2
    squareIt = lambda iter : list(map(lambda x:x**2,iter))
    squared = squareIt(list(range(n)))
    final = []
    final.append(n-1)
    loop1 = 0
    loop2 = 0
    loop3 = 0
    loop4 = 0


    while goal != sum(squareIt(final)):
        loop1 +=1
        runSum = sum(squareIt(final))
        for i in range(n)[1:]:
            print(i)
            print(final)
            loop4 +=1
            if goal < runSum + squared[i]:
                final.append(i-1)
                print('ran')
                break
        

        while len(final) != len(set(final)):
            loop2 +=1
            final.pop()
            final.pop()
            if len(final) == 0:
                return None
            final[-1] = final[-1]-1
        
        if sum(squareIt(final))*2 < goal:
            loop3 +=1
            return None


    print(final)
    return 'loop1 : ' + str(loop1) +'  ' + 'loop2 : ' + str(loop2) +'  ' + 'loop3 : ' + str(loop3) +'  ' + 'loop4 : ' + str(loop4)

        

    


print(decompose(12))
# print(decompose(6))
# print(decompose(50))
# print(decompose(44))
# print(decompose(625))
# print(decompose(5))
# print(decompose(7100))
# print(decompose(123456))
# print(decompose(1234567))
# print(decompose(7654321))
# print(decompose(4))
# print(decompose(7654322))