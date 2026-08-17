class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # Find the # char
            while s[j] != '#':
                j += 1

            # Get the length nd extract word
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            # Move pointer i to the start of the next word's length
            i = j + 1 + length

        return res