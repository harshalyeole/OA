import random
import string

def solution(riddle):
  s = list(riddle)
  res = ""
  for i in range(len(riddle)):
        alpha = "".join(random.choice(string.ascii_letters) for x in range(1))
        print("alpha", alpha, riddle)
        alpha = alpha.lower()
        if (alpha in riddle or alpha in res):
            alpha = "".join(random.choice(string.ascii_letters) for x in range(1))
            alpha = alpha.lower()
        res += alpha
        if s[i] == '?':
            if i > 0 and i < len(s)-1:
                if s[i+1] != alpha:
                    s[i] = alpha
                elif s[i-1] != alpha:
                    s[i] = alpha
                else:
                    i=i
            else:
                if i == 0:
                    if s[1] != alpha:
                        s[i] = alpha
                    else:
                        i = i
                else:
                    if s[i-1] != alpha:
                        s[i] = alpha
                    else:
                        i = i
  riddle = ""
  for ele in s:
      riddle+=ele
  return riddle
print(solution("ab?ac?"))

