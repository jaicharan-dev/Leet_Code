class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        Verifies if a list of words is sorted lexicographically according to a custom alien alphabet.

        --- ALGORITHM STRATEGY: PAIRWISE LEXICOGRAPHICAL COMPARISON ---
        To verify if an entire array is sorted, we only need to ensure that every adjacent pair 
        of words is sorted correctly (i.e., words[i] <= words[i+1]). If every adjacent pair 
        passes the check, the entire list is transitively sorted.

        For each pair of words, we compare them character-by-character from left to right:
        1. If we find a mismatch, the custom alphabet rank determines their sorting order.
           - If the character in the first word has a higher index (comes later) than the second, 
             the list is out of order -> Return False immediately.
           - If it has a lower index, this pair is perfectly sorted -> Break early to check the next pair.
        2. If the inner loop finishes without hitting a mismatch (the 'for-else' trigger), it means 
           one word is a prefix of the other (e.g., "app" and "apple"). We then must ensure the 
           shorter word comes first.

        --- TIME & SPACE COMPLEXITY ---
        - Time Complexity: O(C), where C is the total number of characters across all words in the input. 
          In the worst case, we inspect every character of every word once. The hash map creation takes 
          O(1) time because the alphabet size is strictly fixed at 26 characters.
        - Space Complexity: O(1) auxiliary space, because the lookup dictionary size is bounded 
          by the size of the alphabet (exactly 26 key-value pairs).
        """
        
        # 1. CUSTOM DICTIONARY LOOKUP
        alien_dict = {char : idx for idx, char in enumerate(order)}
        
        # 2. PAIRWISE COMPARISON
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            
            # Compare characters up to the length of the shorter word
            for j in range(min( len(w1), len(w2) )):
                if w1[j] != w2[j]:
                    if alien_dict[w1[j]] > alien_dict[w2[j]]:
                        return False
                    break  

            else:
                if len(w1) > len(w2):
                    return False
        # all pairs are sorted  
        return True


        


        # lets make a dictionary like an oxford dictionary
        # this way we can know which word comes first
        # simple way is to assign an number to each of the characters is the same order
        # the number can be the index , best for comparing
        # now there can be more than 2 words
        # so lets take 2 words at a time
        # we have 2 situations in front of us
        # if the two words a not sorted, then we can immmediately return False
        # if they are sorted "we cannot tell true", we need to check other words as well
        # so just break our for this one iteration and proceed to the next iteration
        # i can see 2 for loops
        # one to pick the words, and the other to loop through characters
                    # the break statement tells
                    # ok we are sure this pair is sorted, no need to check other characters
                    # lets move to the next pair of words
            # the for-else loop: the else executes if the entire for loops runs
            # which means the words are same upto min length, after which
            # some extra characters are there in the longer word
            # this means the shorter word is smaller
            # and it has to be the "w1" if the words have to be sorted
                # incase w1 is the shorter one, this pair is correctly sorted
                # we can move to the next pair of words
        # all the pairs have been chacked and all of them are sorted
        # so we have the entire list in the correct order



