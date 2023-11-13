A_Person={'競馬','マラソン','散歩','映画','読書'}
B_Person={'読書','マラソン','カラオケ','ヨガ',"SNS"}
input("心の準備ができたらEnterキーを入力してください")
common=A_Person & B_Person
total=A_Person | B_Person

Compatibility_rate=len(common)/len(total)*100
print(f"相性度は{Compatibility_rate}パーセントでした")