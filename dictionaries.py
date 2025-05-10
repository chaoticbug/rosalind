#assignment: dictionaries
#split the string into a list of words
#count how many times each word appears
#print each word along with its count

s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

# x = s.split()
# print(x)

test = {}
for word in s.split(' '): #word variable created here
    if word in test:
        test[word] = test[word] + 1 #increase count if word already exists
    else:
        test[word] = 1 #add word with count 1 if its new

for word, count in test.items():
    print(word, count)

