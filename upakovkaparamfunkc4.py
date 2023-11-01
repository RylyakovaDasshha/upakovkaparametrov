wagon = [
    {1: 'м', 2: None, 3: None, 4: 'ж'},
    {1: None, 2: 'м', 3: 'ж', 4: 'ж'},
    {1: 'м', 2: 'м', 3: None, 4: None},
    {1: 'ж', 2: 'ж', 3: 'м', 4: None},
]

free_coupes = []
free_seats = []
free_lower_seats = []
free_upper_seats = []
free_male_seats = []
free_female_seats = []

for i, coupe in enumerate(wagon):
    is_free = True
    for seat in coupe.values():
        if seat is not None:
            is_free = False
            break
    if is_free:
        free_coupes.append(i+1)
    free_seats.extend([seat_num for seat_num, seat in coupe.items() if seat is None])
    free_lower_seats.extend([seat_num for seat_num, seat in coupe.items() if seat is None and seat_num % 2 != 0])
    free_upper_seats.extend([seat_num for seat_num, seat in coupe.items() if seat is None and seat_num % 2 == 0])
    if all(seat == 'м' for seat in coupe.values()):
        free_male_seats.extend([seat_num for seat_num, seat in coupe.items() if seat is None])
    if all(seat == 'ж' for seat in coupe.values()):
        free_female_seats.extend([seat_num for seat_num, seat in coupe.items() if seat is None])

print("Список полностью свободных купе:", free_coupes)
print("Список свободных мест в вагоне:", free_seats)
print("Список свободных нижних мест:", free_lower_seats)
print("Список свободных верхних мест:", free_upper_seats)
print("Список свободных мест в купе с исключительно мужской компанией:", free_male_seats)
print("Список свободных мест в купе с исключительно женской компанией:", free_female_seats)
