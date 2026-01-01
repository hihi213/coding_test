def solution(nums):
    noRepeat={}
    #일일히 중복제거를 한다
    for num in nums:
        noRepeat[num]=True
    numskey=noRepeat.keys()
    length=len(numskey)
    if length>(len(nums)//2):
        return len(nums)//2
    else: return length
