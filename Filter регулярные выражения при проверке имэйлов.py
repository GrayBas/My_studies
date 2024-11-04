import re

pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
def mail_check(mail):
    if re.match(pattern, mail):
        return mail




print(*filter(mail_check, input().split()))
