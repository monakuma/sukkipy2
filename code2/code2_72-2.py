national_Language=int(input("国語の点数を入力してください"))
Math=int(input("数学の点数を入力してください"))
society=int(input("社会の点数を入力してください"))
English=int(input("英語の点数を入力してください"))
Science=int(input("理科の点数を入力してください"))
scores=[national_Language,Math,society,English,Science]
total=sum(scores)
avg=total/ len(scores)
print(total)
print(avg)