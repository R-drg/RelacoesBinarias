def classifica(n):

    #reflexiva
    classe=''
    for i in range(0,16,5):
        if n & 1<<i == 1<<i:
            classe+='R'
            break





    return classe

def imprime_relacao(r,c):
    b = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    b[3][3] = r & 32768 == 32768
    b[3][2] = r & 16384 == 16384
    b[3][1] = r & 8192 == 8192
    b[3][0] = r & 4096 == 4096
    b[2][3] = r & 2048 == 2048
    b[2][2] = r & 1024 == 1024
    b[2][1] = r & 512 == 512
    b[2][0] = r & 256 == 256
    b[1][3] = r & 128 == 128
    b[1][2] = r & 64 == 64
    b[1][1] = r & 32 == 32
    b[1][0] = r & 16 == 16
    b[0][3] = r & 8 == 8
    b[0][2] = r & 4 == 4
    b[0][1] = r & 2 == 2
    b[0][0] = r & 1 == 1
    resp = '{'
    for i in range(4):
        for j in range(4):
            if b[i][j]:
                resp += "("+ str(i+1) + "," + str(j+1)+")"
    resp += '}'
    file.write(resp + " " + c +'\n')


file=open('relacoesbinarias.txt','w')
for n in range(65535):
    c=classifica(n)
    imprime_relacao(n,c)
