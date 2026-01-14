class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
# 1. 리스트는 앞부분 삽입, 제거는 한칸씩 밀으니 n임-> 큐에넣고, 하나씩 pop하면서 찾아가야하나
    # 아주 맨 끝에 답이 있을수있는경우 시간 초과(최악의 상황을 가정하지 못해서 놓친 포인트)
# 2. 중복제거해서, 정렬해 target이후보다 큰값들중 제일 작은 인덱스를 찾아보는 형식으로 가야겠다
    # 찾은후 삭제연산을 진행해도, 초반시점에서 정렬한 값보다 큰값에 대한 모든 인덱스를 일일히 살펴봐야하므로  N^2의 시간초과가 난다.
# 3. 스택을 활용하자 매순간 모든 데이터를 조사하는게 아니라 한번의 순회로 여러개를 처리하자.
    # 스택의 top에 마지막 날짜가 오도록 담아두고, 리스트를 순회해, 리스트의 요소가 높다면 반복적으로 pop과 함께 날짜 차이 계산
    #마지막 날이나 100도인 날이 본인의 답이 필요 없다고 해서 루프를 건너뛰어 버리면 그 날만 기다리던 과거의 데이터들을 구출해 줄 기회조차 사라짐
        answer = [0] * len(temperatures)
        notFindYet= deque()
        for i,current in enumerate(temperatures):
            while notFindYet and current>temperatures[notFindYet[-1]]:
                index= notFindYet.pop()
                answer[index]=i-index
            notFindYet.append(i)
        return answer