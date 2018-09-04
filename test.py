areas = ["Area 1", 123, "Area 2", 123]

area1Value = areas[1]
area2Value = areas[3]

print(area1Value)
print(area2Value)

sumOfAreas = area1Value + area2Value
yourOldSumOfAreas = [area1Value + area2Value]

yourOldSumOfAreas.append(123)

print(sumOfAreas)
print(yourOldSumOfAreas)