def classifica(n):
    classe=""

    #reflexiva

    for i in range(0,16,5):
        if n & 1<<i == 1<<i:
            classe+="R"
            break

    #transitiva

    return classe

n=int(input())
c=classifica(n)
print(c)
