class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj_list = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj_list[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            curr_word, steps = queue.popleft()
            if curr_word == endWord:
                return steps
            
            for i in range(len(curr_word)):
                pattern = curr_word[:i] + "*" + curr_word[i+1:]
                for neighbor in adj_list[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps+1))
                
                adj_list[pattern] = []
        return 0
