class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        def rec(number):
            if number <= 0:
                return ''

            number -= 1
            c = chr((number%26)+65)

            return rec((number//26)) + c

        return rec(columnNumber)