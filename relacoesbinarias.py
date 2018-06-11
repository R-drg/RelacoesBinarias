def classifica(n):

    #reflexiva
    flags=0
    classe=''
    if n & 33825== 33825:
        classe+='R'



    #simetrica
    b = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    b[3][3] = n & 32768 == 32768
    b[3][2] = n & 16384 == 16384
    b[3][1] = n & 8192 == 8192
    b[3][0] = n & 4096 == 4096
    b[2][3] = n & 2048 == 2048
    b[2][2] = n & 1024 == 1024
    b[2][1] = n & 512 == 512
    b[2][0] = n & 256 == 256
    b[1][3] = n & 128 == 128
    b[1][2] = n & 64 == 64
    b[1][1] = n & 32 == 32
    b[1][0] = n & 16 == 16
    b[0][3] = n & 8 == 8
    b[0][2] = n & 4 == 4
    b[0][1] = n & 2 == 2
    b[0][0] = n & 1 == 1

    for i in range(4):
        for j in range(4):
            if (b[i][j] and b[j][i] == False):
                flags=1
                break

    if flags==0:
        classe+='S'

    #function or not

    flagf=0

    for i in range(4):
        for j in range(4):
            for x in range(4):
                if(j!=x):
                    if(b[i][j] and b[i][x]):
                        flagf=1
                        break


    if(flagf==0):
        classe+='F'

    resp = '{'
    for i in range(4):
        for j in range(4):
            if b[i][j]:
                resp += "("+ str(i+1) + "," + str(j+1)+")"
    resp += '}'
    file.write(resp + " " + classe +'\n')

file=open('relacoesbinarias.txt','w')
for n in range(65535):
    classifica(n)
