def multiplication_table(num):
    if num == 0:
        return []
    else:
        return [[i + j if i == 0 or j == 0 else i * j for j in range(num + 1)] for i in range(num + 1)]
        
