import requests  # εισαγωγή της βιβλιοθήκης

#άσκηση
def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


#get url from user
url = input("Enter a URL: ")

if not url.startswith("http://"):
    url = "http://" + url


with requests.get(url) as response:  # το αντικείμενο response
    html = response.text
    more(html)

#server detection
server = response.headers.get("Server")

if server:
    print(f"The server is: {server}")
else: print("No sever found")

#cookies
cookies = response.headers.get("Set-Cookie")

if cookies:
    print(f"The cookies are {cookies}")

    # Iterate over each cookie and print its name and expiry time
    # Get cookie information from the response

    cookies = response.cookies
    for cookie in cookies:
        print("Cookie Name:", cookie.name)
        print("Expiry Time (UNIX timestamp):", cookie.expires)
else:
    print("No cookies found")