# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, limiter=','):
    list1 = group1.split(limiter)
    list2 = group2.split(limiter)
    common = set(list1).intersection(list2)
    return sorted(list(common))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_list = find_common_participants(participants_first_group, participants_second_group, '|')

print(f"Общие участники: {common_list}")