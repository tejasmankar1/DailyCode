import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there! My name is Tejas"

encoded = enc.encode(text)
print("Encoded text: ",encoded)

decoded = enc.decode(encoded)
print("Decoded text: ",decoded )