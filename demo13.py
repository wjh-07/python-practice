score_dict={'小明':85,'小红':92,'小李':78}
total=0
max_score=0
max_name=""
for name,score in score_dict.items():
    total=total+score
    if score>max_score:
        max_score=score
        max_name=name
avg=total/len(score_dict)
print(f"平均分:{avg}")
print(f"最高分同学:{max_name}，分数:{max_score}")
