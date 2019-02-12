def impcaracol(m, n, a) : 
    k = 0; l = 0
  
    ''' k - fila inicial
        m - corrimiento de fila 
        l - corrimiento columna inicial 
        n - corrimiento columna final 
        i - iterador '''
      
  
    while (k < m and l < n) : 
          
        # imprime la primera fila o sigiente  
        for i in range(l, n) : 
            print(a[k][i], end = " ") 
              
        k += 1
  
        #  imprime la ultima columna o sigiente  
        for i in range(k, m) : 
            print(a[i][n - 1], end = " ") 
              
        n -= 1
  
        # imprime la ultima fila o la sigiente 
        if ( k < m) : 
              
            for i in range(n - 1, (l - 1), -1) : 
                print(a[m - 1][i], end = " ") 
              
            m -= 1
          
        # imprima la primera columna o la sigiente 
        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                print(a[i][l], end = " ") 
              
            l += 1
  
# Matriz 
a = [ [1, 2, 3, 4, 5, 6], 
      [7, 8, 9, 10, 11, 12], 
      [13, 14, 15, 16, 17, 18] ] 
        
R = 3; C = 6
impcaracol(R, C, a)
