def emoji_converter(message):
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
    return output


message = input(">")
print(emoji_converter(message))
