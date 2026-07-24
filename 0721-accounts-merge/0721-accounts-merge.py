class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_id = {}
        email_name = {}
        id_cnt = 0

        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                if account[i] not in email_id:
                    email_id[account[i]] = id_cnt
                    email_name[account[i]] = name
                    id_cnt += 1

        parent = list(range(id_cnt)) 
        rank = [1] * id_cnt
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                if rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                elif rank[root_j] < rank[root_i]:
                    parent[root_j] = root_i
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1
            
        for account in accounts:
            first_email = account[1]
            first_id = email_id[first_email]
            for i in range(2, len(account)):
                other_email = account[i]
                other_id = email_id[other_email]
                union(first_id, other_id)
        
        components = defaultdict(list)
        for email, idx in email_id.items():
            root_id = find(idx)
            components[root_id].append(email)

        res = []
        for root_id, email_list in components.items():
            name = email_name[email_list[0]]
            res.append([name] + sorted(email_list))
        return res