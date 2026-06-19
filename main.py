import requests

print("Mr.fuzz MADE BY aCoDeR")
print("UNDER MIT LIECENCE")
print("///////////\\\\\\\\\\\\")
wordlist = input("GIVE A FULL ADDRESS OF A TXT WORDLIST(your wordlist should be .txt, and in every line, it should be JUST ONE word): ")
target = input("GIVE THE TARGET URL(WITH FUZZ): ")

print("/////")
print("This tool is intended for educational purposes and authorized security testing only. Only use it against systems you own or have explicit written permission to test. The author is not responsible for misuse.")
print("/////")

with open(wordlist, "r") as f:
    for line in f:
        word = line.strip()
        url = target.replace("FUZZ", word)
        response = requests.get(url)
        
        print(f"{word} sent, respond: {response.status_code}")
