fr = open("./test.txt", "r")
          
whole_txt = fr.read()
word_dict = {}

for word in whole_txt.split():
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] +=1
        
for key in word_dict:
    print(f'{key} {word_dict[key]}')
    
fr.close()