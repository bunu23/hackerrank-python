import re

def fun(s):
  
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,10}$'
    

    return re.match(pattern, s) is not None

def filter_mail(emails):

    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input().strip())
    emails = [input().strip() for _ in range(n)]
    
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
