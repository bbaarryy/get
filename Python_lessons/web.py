import requests

from hashlib import sha256
from time import time

# Define the target URL
#url = 'https://lightyellow-pink-printer--stepanlokonov.replit.app/future-block'
#url = 'https://nocturnal-cool-namebinding--moiseevpd.replit.app/future-block'
url = 'https://understated-revolving-scope--savelykoptsev.replit.app/future-block'

while True:
    # Send a GET request
    response = requests.get(url)
    #if(response.text == ''):
    #   break
    # Check if the request was successful
    if response.status_code == 200:
        # Get the HTML content as text
        html_content = response.text
        print(html_content)

        if(html_content == ""):
            break
            
        html_content += ":Dima:"

        ind = html_content.find(":")

        n = html_content[0:ind]
        print(n)

        ans=0
        while(ans < 16**(int(n)+1)):
            ans+=1
            curr = html_content + str(hex(ans))[2::].zfill(int(n))

            get_256 = lambda x: sha256(x.encode('utf-8')).hexdigest()

            curr_hesh = get_256(curr)

            if(curr_hesh[0:int(n)] == "0"*int(n)):

                print(curr)
                print(curr_hesh)
                payload = "block="+str(curr)
                print(payload)

                headers = {
                    "Content-Type": "application/x-www-form-urlencoded"
                }

                response = requests.post(url, data=payload, headers=headers)
                #response = requests.post(url, data=payload)

                # Выводим статус и ответ сервера
                print("Status code:", response.status_code)
                print("Response body:", response.text)

                break

    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")



