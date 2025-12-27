```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #값 인덱스리스트 형태로 저장
        #처음부터 순회해, target에서 뺀값을 key로 찾아 인덱스를 저장한다
        #이때의 인덱스는 자신과 다른 인덱스여야함

# 파이썬에는 dict뿐이므로
# 1.리스트를 value로 갖는 dict에 저장한다 (이러면, 중복된 값을 제거하면서도, 인덱스도 관리 가능)
        dict1= {}
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]]=[] #값이 없다면 리스트 초기화
            dict1[nums[i]].append(i) #값을 추가

# 2. 처음부터 순회해, target- 현재 요소인 키를 뒤에서부터 찾는다.
        vales=dict1.values()
        index=[0,0]
        for key, value in dict1.items():
            index[0] = value.pop()
            find = dict1.get((target - key), None)
            #뒤에서부터 찾는걸 어떻게 구현하지?
            if find is not None and len(find)!=0:
                index[1] = find.pop()
                break
        return index

```
