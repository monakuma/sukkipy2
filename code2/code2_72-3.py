# A_one_hobby=str(input("Aさん一つ目の趣味を入力してください"))
# A_two_hobby=str(input("Aさん二つ目の趣味を入力してください"))
# A_three_hobby=str(input("Aさん三つ目の趣味を入力してください"))
# A_four_hobby=str(input("Aさん四つ目の趣味を入力してください"))
# A_five_hobby=str(input("Aさん五つ目の趣味を入力してください"))

# one_person_hobby={A_one_hobby,A_two_hobby,A_three_hobby,A_four_hobby,A_five_hobby}

# B_one_hobby=str(input("Bさん一つ目の趣味を入力してください"))
# B_two_hobby=str(input("Bさん二つ目の趣味を入力してください"))
# B_three_hobby=str(input("Bさん三つ目の趣味を入力してください"))
# B_four_hobby=str(input("Bさん四つ目の趣味を入力してください"))
# B_five_hobby=str(input("Bさん五つ目の趣味を入力してください"))

# one_person_hobby={A_one_hobby,A_two_hobby,A_three_hobby,A_four_hobby,A_five_hobby}

# two_person_hobby={B_one_hobby,B_two_hobby,B_three_hobby,B_four_hobby,B_five_hobby}
member_hobbies={
'A_Person':{'競馬','マラソン','散歩','映画','読書'},
'B_Person':{'読書','マラソン','カラオケ','ヨガ',"SNS"}
}
input("心の準備ができたらEnterキーを入力してください")
common_hobbies=member_hobbies['A_Person'] & member_hobbies['B_Person']

print(len(common_hobbies))

Compatibility=len(common_hobbies)

match Compatibility:

    case 0:
        print("相性0% 残念")
    case 1:
        print("相性25%")
    case 2:
        print("相性50% すごい")
    case 3:
        print("相性75% かなりすごい")
    case 4:
        print("相性100% 最高です")





