message = input(">")
words = message.split(" ")

emojis = {
    ":)" : "😀",
    ":(" : "🙁",
    ":D" : "😁",
    ":/" : "🫤",
    "XD" : "😆",
    ">:(" : "😡",
    ":3" : "😸",
    ">:)" : "😈",
    ";)" : "😉",
    ":O" : "😦",
    ":p" : "😋"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)
