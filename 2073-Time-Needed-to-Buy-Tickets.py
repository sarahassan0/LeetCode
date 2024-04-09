class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        person = tickets[k]
        time = 0

        for i in range(len(tickets)):
            if tickets[i] < person:
                time += tickets[i]
                
            else:
                if i > k: 
                    time += person-1
                else:
                    time += person


        return time

        