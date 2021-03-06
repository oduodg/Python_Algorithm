import collections


class Solution:
    # 풀이 1. 재귀를 이용한 분리
    def removeDuplicateLetters(self, s: str) -> str:
        # 집합으로 정렬
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # 전체 집합과 접미사 집합이 일치할 때 분리 진행
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''

    # 풀이 2. 스택을 이용한 문자 제거
    def removeDuplicateLetters2(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 현재 문자가 이전 문자보다 앞선 문자이고, 이전 문자에 대해서 뒤에 붙일 문자가 남아 있다면 이전 문자를 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())  # (이전문자) seen에서도 stack에서도 제거

            stack.append(char)  # (현재문자) stack에 추가
            seen.add(char)  # (현재문자) seen에 추가
        return ''.join(stack)


# 결과 확인
s = "cbacdcbc"

slt = Solution()
print(slt.removeDuplicateLetters(s))
print(slt.removeDuplicateLetters2(s))
