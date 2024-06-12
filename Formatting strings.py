team1_num = 5
team2_num = 6
team1_time = 18016
team2_time = 18015.2
score_1 = 40
score_2 = 42
task_total = 82
time_avg = 350.4
print('Количество людей в перыой команде: %d,' % team1_num, 'Количество людей во второй команде: %d!' % team2_num)
print('Итого сегодня в командах участников %d и %d!' % (team1_num, team2_num))
print(f'Команда Волшебники данных решила {score_2} задач!')
print('Волшебники данных решили задачи за {0:f} c!'.format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg} секунд на задачу')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print('Победа команды Мастера кода!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print('Победа команды Волшебники Данных!')
else:
    print('Ничья!')