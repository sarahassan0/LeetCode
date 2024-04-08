class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        if sorted(students) == sorted(sandwiches):
            return 0

        for s in sandwiches:
            if s not in students:
                return len(students)
            students.remove(s)


        return 0
            

            


        
        