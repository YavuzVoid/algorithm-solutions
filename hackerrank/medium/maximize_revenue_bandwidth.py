def allocateBandwidthMaxRevenue(N, sizes, revenues, B):
    items = sorted(range(N), key=lambda i: revenues[i] / sizes[i], reverse=True)
    total = 0.0
    remaining = B
    for i in items:
        if remaining <= 0:
            break
        if sizes[i] <= remaining:
            total += revenues[i]
            remaining -= sizes[i]
        else:
            total += revenues[i] * (remaining / sizes[i])
            remaining = 0
    return total
