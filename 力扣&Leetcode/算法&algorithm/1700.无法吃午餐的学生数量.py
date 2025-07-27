class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = deque(students)
        sa = deque(sandwiches)
        while st:
            n = len(st)
            swap = False
            for i in range(n):
                if st[0] != sa[0]:
                    st.rotate(-1)
                else:
                    st.popleft()
                    sa.popleft()
                    swap = True
            if swap:
                continue
            else:
                break
        return len(st)
