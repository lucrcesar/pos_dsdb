from multiprocessing import Process
import time
### n=100.00.000

def pi_naive(start, end, step):
    #marca o inicio
    print ("Start: ", str(start))
    #marca o fim
    print ("End: ", str(end))
    #inicia a soma em 0
    sum = 0.0
    #para cada retangulo
    for i in range(start, end):
        #calcula a altura do retangulo pelo paço, que é também a largura
        x = (i+0.5) * step
        #atualiza isso na soma (o  que esse 4 faz?)
        sum = sum + 4.0/(1.0+x*x)
    print ("Valor Pi: %.10f" %sum)
    return sum

if __name__ == '__main__':
    procs = []
    #haverão 100 milhões de passos, ou seja, 100 milhões de retangulos
    num_steps = 100 #100.000.000 (10+e8) = 17.1 seg.
    n_process = 4
    inicio = 0
    for i in range(n_process):
        tamanho_processo = num_steps/n_process
        inicio = int( i * (tamanho_processo))
        fim = int((tamanho_processo * (i+1))-1)

        step = 1.0/num_steps
        
        tic = time.time() # Tempo Inicial
        
        p = Process(target = pi_naive, args = (inicio, fim, step, ))
        procs.append(p)
        procs[i].start()

        toc = time.time() # Tempo Final
        #pi vai ser 1/numero de passos * essa soma local
        #prints
        print ("Tempo Pi: %.8f s" %(toc-tic))
    
    #print('hello, sou', 'bob pai')
    
    ##TEM QUE SER SEPARADO PORQUE SENÃO PIORA O CÓDIGO
    ##VIRA SEQUENCIAL COM O CUSTO DO PARALELISMO
   # for i in range():
   #     procs[i].start()
    for i in range(n_process):
        procs[i].join()
   # print('hello, sou bob pai, soma=', soma)