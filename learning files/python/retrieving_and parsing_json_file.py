import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "http://py4e-data.dr-chuck.net/comments_1067097.json"
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
new_data = json.loads(data)
contents = new_data["comments"]
print(contents)
content = []
for num in contents:
    nums = int(num["count"])

    content.append(nums)

print(sum(content))
