import csv


def write_holiday_cities(first_letter):
    visited_cities = set()
    wished_cities = set()

    with open('travel-notes.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            name, visited, wished = row[0], row[1].split(';'), row[2].split(';')
            if name.startswith(first_letter):
                visited_cities.update(visited)
                wished_cities.update(wished)

    never_been_cities = wished_cities - visited_cities

    visited_cities = sorted(visited_cities)
    wished_cities = sorted(wished_cities)
    never_been_cities = sorted(never_been_cities)

    first_city_to_visit = never_been_cities[0] if never_been_cities else "None"

    with open('holiday.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Посетили"] + visited_cities)
        writer.writerow(["Хотят посетить"] + wished_cities)
        writer.writerow(["Никогда не были в"] + never_been_cities)
        writer.writerow(["Следующим городом будет"] + [first_city_to_visit])


write_holiday_cities('R')
