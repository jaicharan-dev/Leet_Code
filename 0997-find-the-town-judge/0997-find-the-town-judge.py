class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        Finds the town judge in a community of 'n' people based on a list of trust pairs.

        --- ALGORITHM STRATEGY: INDEGREE & OUTDEGREE NET TRUST SCORE ---
        This problem can be modeled as a directed graph where each person is a node, and 
        a trust pair [a, b] represents a directed edge from person 'a' to person 'b'.
        
        The rules state that the town judge must satisfy two properties:
        1. The town judge trusts nobody (Outdegree must be 0).
        2. Everybody else trusts the town judge (Indegree must be n - 1).

        Instead of maintaining two separate tracking arrays for outdegree and indegree, 
        this approach uses a single array, 'people', to track each person's NET score:
        - When person 'a' trusts someone, they lose a point (people[a] -= 1). This disqualifies 
          them from being the judge because their score can now never reach n - 1.
        - When person 'b' is trusted by someone, they gain a point (people[b] += 1).

        Ultimately, the judge must have a perfect net score of exactly (n - 1) - 0 = n - 1.

        --- TIME & SPACE COMPLEXITY ---
        - Time Complexity: O(T + N), where T is the number of trust pairs (len(trust)) and 
          N is the number of people. We iterate through the trust array once to populate scores, 
          and then loop through the people array once to check for the judge.
        - Space Complexity: O(N) auxiliary space to store the trust score array of size N + 1.
        """
        
        if len(trust) < n-1:
            return -1
        
        trust_count = [0] * (n+1)

        for a, b in trust:
            trust_count[a] -= 1
            trust_count[b] += 1
        
        for i in range(1, n+1):
            if trust_count[i] == n-1:
                return i
        
        return -1
        

        
        # if the number of edges is less than people
        # there can never be a judge 
        # as we need (n-1) inwards and zero outwards for a judge
        # here is dont say "len(trust) != n-1" since other people also cna have inwards
        # lets keep a count of till n+1 since this is 1-indexed
        # this ith person maps to idx 'i'
        # there is not person with index '0'
        # total 'n' people + '0' = n+1
        # if a trusts someone - reduce to -1 
        # he is not the judge, 
        # the trusted person "b" increase by one
        # has a chance of being the judge
        # for all the people present, the one with n-1 trusts
        # that is everyone except himself
        # he is the judge
        # the question gaurantees that there is surely atmost only 1 person like this
        # else we can return -1 
        # there is no judge
