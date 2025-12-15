class matrix:
    def __init__(self,x,y,arr = None):
        if arr == None:
            self.__arr = [[None]*x]*y
        else:
            self.__arr = arr
        self.__x = x
        self.__y = y

    def row(self,x):
        return self.__arr[x]
    
    
    def col(self,y):
        temp = []
        for i in self.__y:
            temp.append(self.__arr[i][y])

        return temp
    
    def det(self):

        if self.__x != self.__y:
            return -1
        
        n = self.__x
        mat = self.__arr
        # Base case: if the matrix is 1x1
        if n == 1:
            return mat[0][0]
        
        # Base case for 2x2 matrix
        if n == 2:
            return mat[0][0] * mat[1][1] - \
                mat[0][1] * mat[1][0]
        
        # Recursive case for larger matrices
        res = 0
        for col in range(n):
        
            # Create a submatrix by removing the first 
            # row and the current column
            sub = [[0] * (n - 1) for _ in range(n - 1)]
            for i in range(1, n):
                subcol = 0
                for j in range(n):
                
                    # Skip the current column
                    if j == col:
                        continue
                    
                    # Fill the submatrix
                    sub[i - 1][subcol] = mat[i][j]
                    subcol += 1
            
            # Cofactor expansion
            sign = 1 if col % 2 == 0 else -1
            res += sign * mat[0][col] * self.det(sub, n - 1)
        
        return res
    
    def x(self):
        return self.__x
    
    def y(self):
        return self.__y
    
    def __dir__(self):
        return self.__arr
    
class matrixCalucation:
    def __init__(self,mat1:matrix,mat2:matrix):
        self.__mat1 = mat1
        self.__mat2 = mat2

    def add(self):
        new_matrix = []
        if len(dir(self.__mat1))>len(dir(self.__mat2)):
            new_matrix = dir(self.__mat1)
            add_matrix =  self.__mat2
        else:
            add_matrix  = self.__mat1
            new_matrix=  dir(self.__mat2)
        
        for i in range(add_matrix.x()):
            for j in range(add_matrix.y()):
                new_matrix[i][j] += dir(add_matrix)[i][j]

        return new_matrix

        



