height=float(input("请输入您的身高(m) "))
weight=float(input("请输入您的体重(kg) "))
BMI=weight/(height*height)
if BMI<18.5:
    print("偏瘦")
elif 18.5<=BMI<24:
    print("正常")
else:
    print("偏胖")