import re
def find_email(plain_text):
pattern=r"([\w\.-]+)(\@[\w\.-]+)(\.[\w]+)"
match=re.findall(pattern,plain_text)
match=re.findall(pttern,plain_text)
found_email_list=[]
if match:
for char in match:
char_list=list(char)
email="".join(char_list)
found_email_list.append(email)
return found_email_list
else:
return 0

$
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/samples.mailgun.org/messages",
        auth=("api", "key-3ax6xnjp29jd6fds4gc373sgvjxteol0"),
        data={"from": "Excited User <excited@samples.mailgun.org>",
              "to": [find_email(str)],
              "subject": "Hello",
              "text":$ curl https://api.punkapi.com/v2/beers/random
			  }
			  )