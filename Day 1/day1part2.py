with open ('input.txt') as file:
    frequency_reached_twice = False
    current_frequency = 0
    list_of_previous_frequencies = []

    frequency_change_list = []
    for line in file:
        frequency_change_list.append(int(line))

    while frequency_reached_twice is False:
        for change in frequency_change_list:  # da je file umjesto liste, postane file prazan (potrošen) i petlja ide u nedogled
            current_frequency += change

            if current_frequency in list_of_previous_frequencies:
                frequency_reached_twice = True
                print(current_frequency)
                break
            else:
                list_of_previous_frequencies.append(current_frequency)