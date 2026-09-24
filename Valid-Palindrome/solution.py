class Solution(object):
    def isPalindrome(self, s):

        if s == ' ':
            return True

        for i in s:
            if i.isalnum()==False:
                s = s.replace(i,'')

        s=s.lower()

        if s[::1] == s[::-1]:
            return True
        return False
