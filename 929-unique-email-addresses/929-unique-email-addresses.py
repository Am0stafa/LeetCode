class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for i in emails:
            localName = i.split('@')[0]
            domainName = i.split('@')[1]
            while '.' in localName:
                localName = ''.join(localName.split('.'))
            while '+' in localName:
                localName = localName.split('+')[0]
            unique.add((localName, domainName))
            
        return len(unique)
      