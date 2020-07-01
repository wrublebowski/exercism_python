def slices(series, length):

    if length > len(series) or length <=0:
        raise ValueError("length must be <= len(series) and must be > 0")

    chunks = []
    for i in range(0,len(series)-length+1):
        chunks.append(series[int(i):(int(i)+length)])

    return chunks
