import pathlib
def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
                lines=[el.strip() for el in file.readlines()] # прочитати всі рядки одразу
                list=[]
                for i in lines:
                    s=i.split(",") # розділити за комами 
                    dic={"id": s[0], "name":s[1], "age": s[2]}
                    list.append(dic)#передати по індексу інформацію в словник і додати словник в список
    except Exception as e:
        print(f'Seems to be some error: {e}. \nPlease, check it one more time') 
    return list
current_dir = pathlib.Path(__file__).parent #отримуємо шлях поточного файлу
path=(current_dir/"cats_info.txt") #отримуємо шлях до текстового файла
cats_info = get_cats_info(path)
print(cats_info)