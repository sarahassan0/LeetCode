class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            local_part, domain_part = email.split('@')
            
            local_part = local_part.split('+')[0]

            local_part = local_part.replace('.', '')

            unique_email = local_part + '@' + domain_part

            unique.add(unique_email)

        return len(unique)


        