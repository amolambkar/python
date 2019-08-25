if __name__ == '__main__':
    N = int(input())
    L = []

    for i in range (N):
      
        inputCommand = input()
        command = inputCommand.split(' ')   

        if(command[0]=='insert'):
            L.insert(int(command[1]), int(command[2]))
        if(command[0]=='print'):
            print (L)
        if(command[0]=='remove'):
            L.remove(int(command[1]))
        if(command[0]=='append'):
            L.append(int(command[1]))
        if(command[0]=='sort'):
            L.sort()
        if(command[0]=='pop'):
            L.pop()
        if(command[0]=='reverse'):
            L.reverse()
