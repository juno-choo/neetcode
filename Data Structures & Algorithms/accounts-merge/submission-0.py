class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        graph = defaultdict(list)
        email_to_name = {}
        for account in accounts:
            anchor_email = account[1]
            email_to_name[anchor_email] = account[0]
            graph[anchor_email]
            for i in range(2, len(account)):
                email_to_name[account[i]] = account[0]

                graph[anchor_email].append(account[i])
                graph[account[i]].append(anchor_email)

        visited = set()
        
        # visit email, recursively visit neighbors if not yet seen
        def dfs(email, account):
            if email in visited:
                return

            visited.add(email)
            account.append(email)
            for nei in graph[email]:
                dfs(nei, account)

        res = []
        for email in graph:
            if email not in visited:
                merged = []
                dfs(email, merged)

                name = email_to_name[email]
                merged.sort()
                res.append([name, *merged]) # unpacks elements
        return res

