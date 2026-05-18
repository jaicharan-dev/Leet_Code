class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_order = {char : idx for idx, char in enumerate(order)}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            for j in range( min(len(w1), len(w2)) ):
                if w1[j] != w2[j]:
                    if alien_order[w1[j]] > alien_order[w2[j]]:
                        return False
                    break
            
            else:
                if len(w1) > len(w2):
                    return False
            
        return True



