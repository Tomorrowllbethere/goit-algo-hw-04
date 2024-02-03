import pathlib
def total_salary(path):
    try:
         with open(path, "r") as salary_data:   # функція  приймає текстовий файл
        # перебираємо кожен рядок, створюємо список рядків
            lines = [el.strip() for el in salary_data.readlines()]
            num=0 #лічильник ітерацій
            total=0 #змінна, що отримає суму чисел
            for i in lines: # перебираємо рядок в списку рядків
                s=i.split(',') # розділяємо через кому рядок
                a=int(s[1]) #отримуємо число через індекс
                total+=(a) #додаємо число в суму
                num+=1 #додаємо ітерацію в лічильник
            average=int(total/num) #функція рахує середню зарплату і приводить її в ціле число   
            return (total, average) #повертаємо значення
    except Exception:
        print(" ______________\nSorry, we couldn't find your file. Maybe, is not file exist?\n_____________ ")
current_dir = pathlib.Path(__file__).parent #отримуємо шлях поточного файлу
path=(current_dir/"salary.txt") #отримуємо шлях до текстового файла з даними про зп
total, average = total_salary(path) #витягуємо змінні з функції
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}") #виводимо значення 