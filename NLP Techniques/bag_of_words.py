sentence = "What is a bag of words and what does it do for me"
clean_text = sentence.lower().split(" ")
bow = {}
for item in clean_text:
    if item in bow:
        bow[item] += 1
    else:
        bow[item] = 1

print(bow)