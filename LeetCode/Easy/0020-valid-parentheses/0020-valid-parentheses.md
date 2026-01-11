### 소스 코드 (LeetCode/Easy/0020-valid-parentheses/0020-valid-parentheses.py)

```python
class Solution:
    def isValid(self, s: str) -> bool:

    #key로 여는괄호 value로 닫는괄호
        mapping= {"(": ")", "{": "}", "[": "]"}
        openstack=[]
        # 하나만 있을때는 false반환
        slength=len(s)
        if slength==1: return False
        #하나씩 전진해
        for i, part in enumerate(s):
            #앞으로 남은 괄호보다, 현재 담은괄호가 많다면 false리턴
            if (slength-i)<len(openstack):
                return False
            # 여는 괄호를 발견하면 담는다
            if part in mapping:
                openstack.append(part)
            #닫는 괄호를 발견하면 제거한다.
            else :
                if openstack:
                    close=openstack.pop()
                    # 다른 쌍이라면 거짓
                    if mapping[close]!=part:
                        return False
                else : return False  #존재하지 않는다면 false반환
        #끝까지 갔는데 남는게 있다면 false 반환
        if len(openstack)==0 : return True
        return False
```
