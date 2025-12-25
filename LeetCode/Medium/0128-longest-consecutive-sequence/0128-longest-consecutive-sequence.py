class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    #정렬되지 않은 정수형 배열 Nums 가지고 만들수있는 연속된 수의 갯수반환
        if not nums: return 0  # 빈 리스트 처리
        dictnums={}
        #1. 중복제거
        for num in nums:
            dictnums[num]=1
        #2. 정렬한다
        sortnums=sorted(dictnums)
        #3. 제일 큰 연속 반복수를 반환해야한다.
        maxrepeat=1
        count = 0
        length=len(sortnums)
        for i, num in enumerate(sortnums):
            count += 1
            # 연속되지 않았을때
            if num+1 not in dictnums:
                # 최대 횟수와 비교해 크다면, 최대 횟수 업데이트
                if maxrepeat < count:
                    maxrepeat = count
                # 만약, 다음요소가 최대반복수보다 적게 남았다면 즉시 종료
                if maxrepeat > (length - i): break
                # 횟수를 초기화한다
                count=0
        #4. 반환한다.
        return max(maxrepeat, count)
