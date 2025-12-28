# 모든 배열, 한명뺀 배열을 받고 그 한명을 찾아라
# 같은이름이더라도, 각각 기록한다.

#먼저 10의 6승의 입력이므로, NlogN이하의 시간복잡도를 사용해야한다.(정렬가능)
#없다는 걸 알려면, 결국 완주자명단과 전체명단을 비교해야한다.
#sort로 정렬한다면, 무조건 nlogn이다 좀더 줄일순 없을까?

#전체명단을 테이블에 넣고 완주자 명단으로 접근한다면
    #삭제연산으로 비교를 진행하고, 최종적으로 남은걸 반환
#완주자명단을 테이블에 넣고 전체명단으로 접근한다면
    #동일인이 있는경우에만 삭제연산을 진행한다
    # 테이블에 이름이 없다면 반환,
#전체 명단으로 접근하는게 끝까지 계산 안할 가능성이 존재한다.

def solution(participant, completion):
    dictcompletion={}
    answer = ''
#1.받은 완주자배열을 키는 이름, 값은 인원으로 테이블에 저장한다
    for name in completion:
        if name in dictcompletion:
            dictcompletion[name]+=1
        else: dictcompletion[name]=1
#2.전체명단을 순회하여, 완주자테이블과 비교한다.
    for i, name in enumerate(participant): 
    #만일 일치하지 않는다면, 반환해 종료
        if name not in dictcompletion:
            answer = name
            break 
    #만약 일치한다면 1일땐 삭제, 2이상일땐 감소
        elif 1<dictcompletion[name]:
            dictcompletion[name]-=1
        else: dictcompletion.pop(name)
    return answer
