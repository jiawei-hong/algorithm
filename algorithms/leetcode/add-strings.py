class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
      num1_len = len(num1)
      num2_len = len(num2)

      main, sub = num1 if num1_len > num2_len else num2, num2 if num1_len > num2_len else num1

      if main == "0" or sub == "0":
        return "0"

      n = len(main)
      res = [0] + [int(x) for x in list(main)]
      diff_zero = n - len(sub) + 1
      sub = '0' * diff_zero + sub

      for i in range(len(sub)-1,-1,-1):
        res[i] += int(sub[i])

      for i in range(len(res)-1,1,-1):
        if res[i] >= 10:
          add = res[i] // 10
          res[i] = res[i] % 10
          res[i-1] += add

      if res[0] == 0:
        res.pop(0)

      return ''.join([str(x) for x in res])

