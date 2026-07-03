class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_id = {}
        email_to_name = {}
        id_cnt = 0

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = id_cnt
                    email_to_name[email] = name
                    id_cnt += 1
                
        parent = list(range(id_cnt))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        for account in accounts:
            first_email = account[1]
            first_id = email_to_id[first_email]

            for other_email in account[2:]:
                other_id = email_to_id[other_email]
                union(first_id, other_id)
        
        components = defaultdict(list)
        for email, email_id in email_to_id.items():
            root_id = find(email_id)
            components[root_id].append(email)
        
        res = []
        for root_id, email_list in components.items():
            name = email_to_name[email_list[0]]
            res.append([name] + sorted(email_list))
        return res
            