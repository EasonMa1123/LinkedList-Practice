class matrix:
    def __init__(self,arr):
        
        self.__arr = arr
        self.__y = len(self.__arr)
        self.__x = len(self.__arr[0])
        self.__dim = f'{str(self.__x)} {str(self.__y)}'

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
        new_martix_list = 0
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
            new_martix_list += sign * mat[0][col] * self.det(sub, n - 1)
        
        return new_martix_list
    
    def x(self):
        return self.__x
    
    def y(self):
        return self.__y
    
    def matrix(self):
        return self.__arr
    
    def dim(self):
        return self.__dim
    
class matrixCalucation:
    def __init__(self):
        pass

    def add(self,mat1:matrix,mat2:matrix):
        if mat1.dim() != mat2.dim():
            return -1
        
        
        new_martix_list = [[0 for _ in range(mat1.x())] for _ in range(mat1.y())]
        for i in range(mat1.x()):
            for j in range(mat1.y()):
                
                new_martix_list[i][j] = mat1.matrix()[i][j]+mat2.matrix()[i][j]
                

        new_martix = matrix(new_martix_list)
        return new_martix
    
    def minus(self,mat1:matrix,mat2:matrix):
        if mat1.dim() != mat2.dim():
            return -1
        
        
        new_martix_list = [[0 for _ in range(mat1.x())] for _ in range(mat1.y())]
        for i in range(mat1.x()):
            for j in range(mat1.y()):
                
                new_martix_list[i][j] = mat1.matrix()[i][j]-mat2.matrix()[i][j]
                

        new_martix = matrix(new_martix_list)
        return new_martix
    
    def multiply(self,mat1:matrix,mat2:matrix):
        mat1_y = mat1.y()
        mat1_x = mat1.x()
        mat2_y = mat2.y()
        mat2_x = mat2.x()

        if mat1_x != mat2_y:
            print("Invalid Input")
            return None

       
        new_martix_list = [[0] * mat2_x for _ in range(mat1_y)]

        
        for i in range(mat1_y):
            for j in range(mat2_x):
                for k in range(mat1_x):
                    new_martix_list[i][j] += mat1.matrix[i][k] * mat2.matrix[k][j]

        new_martix = matrix(new_martix_list)

        return new_martix
