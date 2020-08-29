# rotating matrix in anti-clock wise direction
# let input be a N*N Matrix
# First transpose and then reverse the columns to get final answer

def rotate(matrix): 
    # performing a transpose
    N = len(matrix)
    for i in range(N):
        for j in range(i,N):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for j in range(N):
        for i in range(N//2):
            matrix[i][j],matrix[N-i-1][j] = matrix[N-i-1][j],matrix[i][j]
    return matrix
