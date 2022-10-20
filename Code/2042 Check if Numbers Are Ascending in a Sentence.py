class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # for i in s:
        #     if i.isdigit():
        #         temp.append(int(i))
        # print(temp)

        # ************** ALSO A Solution**************

        # for i in
        # x=[int(word) for word in s.split() if word.isnumeric()]
        # for i in range(len(x)-1):
        #     if x[i]>=x[i+1]:
        #         return False
        # return True

        prev = -1
        for w in s.split():
            if w.isdigit():
                if int(w) <= prev:
                    return False
                prev = int(w)

        return True
