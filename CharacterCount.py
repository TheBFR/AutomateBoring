import pprint

message = 'It was a bight cold day in April, and the clocks wewre stricking thirteen.'
count = {}
for character in message.upper():
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count)