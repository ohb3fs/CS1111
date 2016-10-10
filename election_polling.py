# Olivia Bicks ohb3fs


def read_data_file(filename):
    data = []
    file = open(filename, "r")
    for line in file:
        organized_data = line.split(',')
        poll = organized_data[0]
        date = organized_data[1]
        number_polled = int(organized_data[2])
        margin_of_error = int(organized_data[3])
        cruz = int(organized_data[4])
        kasich = int(organized_data[5])
        rubio = int(organized_data[6])
        trump = int(organized_data[7])
        data += [[poll, date, number_polled, margin_of_error, cruz, kasich, rubio, trump]]
    return data


def poll_winner(poll_to_examine):
    winner = max(poll_to_examine[4], poll_to_examine[5], poll_to_examine[6], poll_to_examine[7])
    if winner == poll_to_examine[4]:
        name = "Cruz"
        poll_to_examine.remove(winner)
        runner_up = max(poll_to_examine[4], poll_to_examine[5], poll_to_examine[6])
        margin = winner - runner_up
        if margin != 0:
            value = "+" + str(margin)
            return name, value
        elif margin == 0:
            value = "TIE"
            return value
    if winner == poll_to_examine[5]:
        name = "Kasich"
        poll_to_examine.remove(winner)
        runner_up = max(poll_to_examine[4], poll_to_examine[5], poll_to_examine[6])
        margin = winner - runner_up
        if margin != 0:
            value = "+" + str(margin)
            return name, value
        elif margin == 0:
            value = "TIE"
            return value
    if winner == poll_to_examine[6]:
        name = 'Rubio'
        poll_to_examine.remove(winner)
        runner_up = max(poll_to_examine[4], poll_to_examine[5], poll_to_examine[6])
        margin = winner - runner_up
        if margin != 0:
            value = "+" + str(margin)
            return name, value
        elif margin == 0:
            value = "TIE"
            return value
    if winner == poll_to_examine[7]:
        name = "Trump"
        poll_to_examine.remove(winner)
        runner_up = max(poll_to_examine[4], poll_to_examine[5], poll_to_examine[6])
        margin = winner - runner_up
        if margin != 0:
            value = "+" + str(margin)
            return name, value
        elif margin == 0:
            value = "TIE"
            return value


def latest_poll_winner_by_state(state):
    data = read_data_file(state)
    poll_to_examine = data[0]
    return poll_winner(poll_to_examine)


def average_of_polls(state, number_of_polls=5):
    margin = 0
    cruz = 0
    kasich = 0
    rubio = 0
    trump = 0
    number_polled = 0
    data = read_data_file(state)
    i = 0
    while 0 <= i < number_of_polls:
        number_polled += int(data[i][2])
        margin += int(data[i][3])
        cruz += int(data[i][4])
        kasich += int(data[i][5])
        rubio += int(data[i][6])
        trump += int(data[i][7])
        i+=1
    number_polled_average = number_polled // number_of_polls
    margin_average = margin // number_of_polls
    cruz_average = cruz // number_of_polls
    kasich_average = kasich // number_of_polls
    rubio_average = rubio // number_of_polls
    trump_average = trump // number_of_polls
    average_list = ['Average Poll', number_of_polls, number_polled_average, margin_average, cruz_average,
                    kasich_average, rubio_average, trump_average]
    return average_list