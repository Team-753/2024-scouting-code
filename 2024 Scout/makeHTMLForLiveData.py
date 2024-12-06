'''
step = 75
for i in range(75):
    startTD = "<td>{{"
    endTD = "}}</td>"
    i1 = str(i+step)
    print("<tr>")
    print(startTD,"team"+i1,endTD)
    print(startTD,"match"+i1,endTD)
    print(startTD,"coopertition"+i1,endTD)
    print(startTD,"amplified"+i1,endTD)
    print(startTD,"ringOne"+i1,endTD)
    print(startTD,"throOne"+i1,endTD)
    print(startTD,"ringTwo"+i1,endTD)
    print(startTD,"throTwo"+i1,endTD)
    print(startTD,"ringThree"+i1,endTD)
    print(startTD,"throThree"+i1,endTD)
    print(startTD,"notes"+i1,endTD)
    print("</tr>")
'''
step = 75
for i in range(75):
    i = i + step
    i1 = str(i)
    i2 = str(i + 1)
    print("team"+i1+" = teamList["+i2+"], match"+i1+" = pointList["+i2+"], coopertition"+i1+" = coopertitionList["+i2+"], amplified"+i1+" = amplifiedList["+i2+"], ringOne"+i1+" = ringOneList["+i2+"], throOne"+i1+" = throOneList["+i2+"], ringTwo"+i1+" = ringTwoList["+i2+"], throTwo"+i1+" = throTwoList["+i2+"], ringThree"+i1+" = ringThreeList["+i2+"], throThree"+i1+" = throThreeList["+i2+"],  notes"+i1+" = notesList["+i2+"], ")

