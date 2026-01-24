class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        dic = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
        }
        a = []
        b = []
        for i in words:
            print(i)
            for j in i:
                if j in dic:
                    b.append(dic[j])

            c = "".join(b)
            b = []
            a.append(c)

        return len(set(a))
