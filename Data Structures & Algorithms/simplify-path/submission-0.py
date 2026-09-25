class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')

        st = []
        print(dirs)

        for d in dirs:
            if d == "" or d == ".":
                continue

            if d == "..":
                if st:
                    st.pop()

            else:
                st.append(d)

        return '/' + '/'.join(st)