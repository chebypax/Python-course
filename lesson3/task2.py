def user_info(first_name, last_name, birth_year, city, email, tel):
    return f'{first_name} {last_name} родился в {birth_year} году, живет в {city}. ' \
           f'Для связи использовать емэйл {email} или телефон {tel}'


print(user_info(tel=1245, first_name='Valery', last_name='K', city='Moscow', birth_year=1987, email='mail@mail.ru'))
