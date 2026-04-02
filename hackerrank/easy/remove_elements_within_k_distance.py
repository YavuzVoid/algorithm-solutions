def debounceTimestamps(timestamps, K):
    if not timestamps:
        return 0
    write = 1
    for i in range(1, len(timestamps)):
        if timestamps[i] - timestamps[write - 1] >= K:
            timestamps[write] = timestamps[i]
            write += 1
    return write
