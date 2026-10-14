text="hello python hello world python python hi hello python"
word_list=text.split()
count_dict={}
for word in word_list:
    if word in count_dict:
        count_dict[word]+=1
    else:
        count_dict[word]=1
sorted_items=sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
Top5=sorted_items[:5]
print("词频前五: ")
for word,num in Top5:
    print(word,num)

