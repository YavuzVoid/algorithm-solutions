def processCouponStackOperations(operations):
    stack = []
    min_stack = []
    result = []
    for op in operations:
        if op.startswith('push'):
            val = int(op.split()[1])
            stack.append(val)
            min_stack.append(min(val, min_stack[-1]) if min_stack else val)
        elif op == 'pop':
            stack.pop()
            min_stack.pop()
        elif op == 'top':
            result.append(stack[-1])
        elif op == 'getMin':
            result.append(min_stack[-1])
    return result
