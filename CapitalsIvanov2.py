Capitals={}
Capitals["Estonia"]="Tallinn"
Capitals["Albania"]="Tirana"
Capitals["Belgium"]="Brussels"
Capitals["Germany"]="Berlin"
Capitals["Poland"]="Warsaw"
Capitals["Portugal"]="Lisabon"
Capitals["France"]="Paris"
Capitals["Finland"]="Helsinki"
Capitals["Czechia"]="Praha"
Countries=["Estonia","Albania","Belgium","Czechia","Poland","Portugal","Finland","France","Germany"]
for country in Countries:
    country=input("Напиши страну: ")
    if country in Capitals:
        print("Столица страны "+country+": " +Capitals[country])
    else:
        print("В базе данных нет страны с названием " +country)
        v=input("Хочешь написать" +country+ " в базу данных?: ")
        if o=="Да":
            ca=input("Напиши столицу"+country)
            Capitals.update({country: ca})
        elif n=="Нет":
            print("Удачи тебе!")
            break
