class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for a in asteroids:
            while st and st[-1] > 0 and a < 0:
                if st[-1] < -a:
                    st.pop()
                    continue
                if st[-1] == -a:
                    st.pop()

                break
            else:
                st.append(a)

        return st