import re
"""1)
Validate Email Addresses
Write a Python program to validate a list of email addresses using regular expressions.
 A valid email address should have the format username@domain.extension"""


'''regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      print("Valid email")
    else:
      print("Invalid email")
list_email=["name.surname@gmail.com",
"anonymous123@yahoo.co.uk",
"anonymous123@...uk",
"...@domain.us",
"sohaardah@gmail.com"]
for email in list_email:
    isValid(email)
'''

"""
2)Extract Phone Numbers
Write a Python program to extract phone numbers from a list of strings using regular expressions.
 Phone numbers should have the format xxx-xxx-xxxx
"""
'''regex=re.compile(r"\d{3}-\d{3}-\d{4}")
def vaild_phone_number(phone):
    all_phone=[]
    search=re.findall(regex,phone)
    if search!=[]:
        all_phone.append(search)
        # print(re.findall(regex,phone))
        print("valid number")
    else:
        print("invalid number")
    for phone in all_phone:
        print(phone)
list_phone=['My phone number is 123-456-7890.123-345-2345 Please call me.', 'Call me at 555-123-4567.', 'Invalid phone number','1928-291-982']
for phone in list_phone:
    # print(phone)
    vaild_phone_number(phone)'''
"""
3)Replace Text

Write a Python program to replace all occurrences of a word in a string with a replacement word using regular
 expressions.
"""
'''
def replacewordtoword(word1,word2,allsentance):
    print(re.sub(word1,word2,allsentance))
sentance="This is the best python course I have been enrolled to"
replacewordtoword("course","training",allsentance=sentance)'''

"""
4)Extract URLs

Write a Python program to extract URLs from a list of strings using regular expressions. URLs should have the 
format http(s)://domain.extension.
"""
''' regex=re.compile(r"(https?)://(www.)?(\w+)\.(\w+):?(\d+)?/?(.+)")
def extract_url(url):
   search=re.search(regex,url)
    if search!=None:
        print(search.group()," vailed url")
    else:
        print("invailed url")

strings = ['Visit our website at https://example.com', 'Invalid url', 'https://www.google.com/search?q=regex']
for url in strings:
    extract_url(url)
print(re.search(r'^Eat', "Eat cake!").group())

## However, the code below will not give the same result. Try it for yourself:
# print(re.search(r'^eat', "Let's eat cake!").group())
statement = 'Please contact us at: support123@datacamp.com'
match = re.search(r'([\w\.-]+)@([\w\.-]+)', statement)
if statement:
  print("Email address:", match.group()) # The whole matched text
  print("Username:", match.group(1)) # The username (group 1)
  print("Host:", match.group(2)) # The host (group 2)
pattern = "cookie"
sequence = "Cake and cookie"

rr=re.search(pattern, sequence)
print(rr.group())
pattern = "C"
sequence1 = "IceCream"
sequence2 = "Cake"

# No match since "C" is not at the start of "IceCream"
print("Sequence 1: ", re.match(pattern, sequence1))
print("Sequence 2: ", re.match(pattern,sequence2).group())'''


"""
Validate IP Addresses

Write a Python program to validate a list of IP addresses using regular expressions. A valid IP address
 should have the format xxx.xxx.xxx.xxx, where each x is a number between 0 and 255.
"""
'''regex=re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
print(re.match(regex,"127.0.0.1").group())
ips = ['192.168.0.1', '10.0.0.1', 'invalid.ip.address', '255.255.255.256']
for ip in ips:
    try:
        print(re.match(regex, ip).group())
    except:print("invailed ip ")'''