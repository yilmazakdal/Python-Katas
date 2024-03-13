def reduce_by_steps(func,iter,initial):
    result = initial
    for value in iter:
        result = func(result,value)
    return result
