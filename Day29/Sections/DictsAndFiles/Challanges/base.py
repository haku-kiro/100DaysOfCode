def WordCount(path):
    dictOfWordCounts = {}
    with open(path, "r") as f:
        for line in f:
            for word in line.split(): # splitting all whitespace (I think newlines count as whitespace - probably)
                if word.lower() in dictOfWordCounts:
                    dictOfWordCounts[word.lower()] += 1
                else:
                    dictOfWordCounts[word.lower()] = 1
    return dictOfWordCounts


data = WordCount(r"C:\Users\mdjco\Desktop\100DaysOfCode\Day29\Sections\DictsAndFiles\Challanges\small.txt")
for key in data.keys():
    print(f"{key} > {data[key]}")
print(sorted(data))    