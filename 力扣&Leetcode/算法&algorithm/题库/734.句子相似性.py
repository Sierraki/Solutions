class Solution:
    def areSentencesSimilar(
        self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
    ) -> bool:
        cnt = defaultdict(list)
        for i in similarPairs:
            cnt[i[0]].append(i[1])
        if len(sentence1) == len(sentence2):
            for i in range(len(sentence1)):
                if sentence2[i] == sentence1[i]:
                    continue
                elif sentence2[i] in cnt[sentence1[i]]:
                    continue
                elif sentence1[i] in cnt[sentence2[i]]:
                    continue
                else:
                    return False
            return True
        return False
