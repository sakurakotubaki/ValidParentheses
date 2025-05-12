### Function ##################################################################

def solve(num=0):
    solver = Solution().isValid

    if 1 <= num <= Input().input:
        id_LIST = [num]
    else:
        id_LIST = [id + 1 for id in range(Input().input)]

    for id in id_LIST:
        data = Input(id)
        ans = solver(data.s)
        result = "OK" if ans == data.ans else "NG"
        print(f"[{str(id).zfill(3)}] {result}")


### Class #####################################################################

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
            1 <= s.length <= 104
            s[i]: '(', ')', '[', ']', '{', '}'
        :rtype: bool
        """

        if len(s) % 1 == 1: return False
        print(f"lenの中身 ${s}")

        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for char in s:

            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element: return False

            else:
                stack.append(char)

        return not stack


# ==============================================================================

class Input:

    def __init__(self, num=0):

        if num == 1:
            self.s = "()"
            self.ans = True

        elif num == 2:
            self.s = "()[]{}"
            self.ans = True

        elif num == 3:
            self.s = "(]"
            self.ans = False

        else:
            self.input = 3


### Main ######################################################################

if __name__ == "__main__":
    solve()

###############################################################################