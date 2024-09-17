# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils


def is_valid_email(email):

    pattern = r'^[a-zA-Z][\w.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, email)


n = int(input())


for _ in range(n):

    name, email_address = email.utils.parseaddr(input())
    

    if is_valid_email(email_address):
        print(email.utils.formataddr((name, email_address)))
