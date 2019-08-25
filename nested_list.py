if __name__ == '__main__':
    n = int(input())

    nestedList = []
    scoreList = []
    secondLowestNames = []
    uniqueScoreList = []
    for _ in range(0, n):
        name = input()
        score = float(input())
        nameScore = [name, score]
        nestedList.append(nameScore)
    
    for i in range(0, n):
        scoreList.append(nestedList[i][1])
    
    ScoreList = set(scoreList)
   
    for j in ScoreList:
        uniqueScoreList.append(j)
    
    uniqueScoreList.sort()
    secondLowest = uniqueScoreList[1]

    for i in range(0, n):
        if(nestedList[i][1] == secondLowest):
            secondLowestNames.append(nestedList[i][0])
    
    secondLowestNames.sort()

    for i in range(0, len(secondLowestNames)):
        print(secondLowestNames[i])
