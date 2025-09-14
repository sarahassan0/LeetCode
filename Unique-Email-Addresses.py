class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        for i , e in enumerate(emails):
            name, domain = e.split('@')
            name = name.split('+')[0]
            name = name.replace('.','')
            emails[i] = name + '@' + domain
            
        return len(set(emails))
