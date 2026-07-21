class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj_list[pattern].append(word)
        
        q = deque([(beginWord, 1)])
        visit = set([beginWord])

        while q:
            curr, steps = q.popleft()
            if curr == endWord:
                return steps

            for i in range(len(curr)):
                pattern = curr[:i] + "*" + curr[i+1:]
                for neighbor in adj_list[pattern]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        q.append((neighbor, steps+1))
                adj_list[pattern] = []
        
        return 0