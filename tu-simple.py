def throwtheball(receiver, seconds):
    index = 1

    r = seconds
    if len(receiver) < seconds:
        r = round(seconds*(1-len(receiver)/seconds))
    for i in range(r):
        index = receiver[index-1]
        print(index)