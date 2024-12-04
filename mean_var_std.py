import numpy as np

def calculate(list):
    
    if len(list)!=9:
        raise ValueError('List must contain nine numbers.')
    else:
        matrix = np.array(list).reshape(3,3)
    mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), float(matrix.mean())]
    var = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), float(matrix.var())]
    std = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), float(matrix.std())]
    max = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), float(matrix.max())]
    min = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), float(matrix.min())]
    sum = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), float(matrix.sum())]
   
    calculate = {
        "mean": mean,
        "variance": var,
        "standard deviation": std,
        "max": max,
        "min": min,
        "sum": sum,
    }
    return calculate
