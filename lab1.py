import requests  # εισαγωγή της βιβλιοθήκης
import datetime

# unix_timestamp = 1614370123  # Example timestamp

def convertTime(unix_timestamp):
    # Convert Unix timestamp to a datetime object
    datetime_obj = datetime.datetime.utcfromtimestamp(unix_timestamp)

    # Convert datetime object to a formatted string
    formatted_date = datetime_obj.strftime('%Y-%m-%d %H:%M:%S UTC')

    return("Formatted Date:", formatted_date)

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
        #format time if Value != None
        time = convertTime(cookie.expires) if cookie.expires !=None else cookie.expires;
        print("Expiry Time (UNIX timestamp):",time )
else:
    print("No cookies found")