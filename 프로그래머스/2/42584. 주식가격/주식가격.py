from collections import deque
def solution(prices):
    length=len(prices)
    answer = [0] * length
    notFindYet= deque()
    for i,current in enumerate(prices):
        while notFindYet and (current<prices[notFindYet[-1]] or i==length-1) :
            index= notFindYet.pop()
            answer[index]=i-index
        notFindYet.append(i)
    return answer