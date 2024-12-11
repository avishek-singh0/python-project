with open('story.txt','r') as f:
    story = f.read()

# words = []
# we use set for unique element in list
words = set()
start_word = -1

start_target='<'
end_target = '>'

for i,char in enumerate(story):
    if char == start_target:
        start_word = i

    if char == end_target and start_word != -1:
        # to get  slice or we get specific string
        word =  story[start_word: i+1]  
        # words.append(word)
        words.add(word)
        start_word = -1

# empyt dicitoary  act as unordered 
answers = {}

for word in words:
    answer = input('Enter a word for' + word + ':')
    answers[word] = answer

for word in words:
   story =  story.replace(word,answers[word])

print(story)

