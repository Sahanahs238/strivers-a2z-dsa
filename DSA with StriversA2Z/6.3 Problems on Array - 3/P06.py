def merge(intervals):
    intervals.sort(key=lambda i : i[0])
    output = [intervals[0]]
    for start,end in intervals[1:]:
        lastend = output[-1][1]
        if start <= lastend:
            output[-1][1]=max(lastend,end)
        else:
            output.append([start,end])
    return output
raw_numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
intervals = [raw_numbers[i:i+2] for i in range(0, len(raw_numbers), 2)]
print("Merged intervals:", merge(intervals))
