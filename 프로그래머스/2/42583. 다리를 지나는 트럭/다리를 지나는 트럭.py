from collections import deque
def solution(bridge_length, weight, truck_weights):
    time=0
    # 다리 자체를 큐로 만든다
    bridge = deque([0] * bridge_length)
    # 대기 트럭도 큐로 만들어 효율성 높임
    waiting_trucks = deque(truck_weights)
    currentWeight = 0
    # 다리 위에 트럭이 있거나 대기 트럭이 있는 동안 반복
    while bridge:
        time+=1
        # 다리 끝에서 트럭(혹은 0)이 나감
        out_truck = bridge.popleft()
        currentWeight -=out_truck
        # 대기 중인 트럭이 있다면 진입 시도
        if waiting_trucks:
            # 다음 트럭이 다리에 진입할 수 있는지 판단
            if currentWeight+ waiting_trucks[0]<=weight:
                new_truck = waiting_trucks.popleft()
                bridge.append(new_truck)
                currentWeight += new_truck
            else:
                # 무게 초과 시 0을 넣어 트럭을 전진시킴
                bridge.append(0)
    return time 