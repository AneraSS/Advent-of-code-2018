with open ('input.txt') as file:
    frequency_reached_twice = False
    current_frequency = 0
    previous_frequencies = set() # if it were a list, it would take up a lot of time (super slow check if in list)

    # taking out of the file, better for usage
    frequency_change_list = []
    for line in file:
        frequency_change_list.append(int(line))

    while frequency_reached_twice is False:
        for change in frequency_change_list:  # da je file umjesto liste, postane file prazan (potrošen) i petlja ide u nedogled
            current_frequency += change

            if current_frequency in previous_frequencies:
                frequency_reached_twice = True
                print(current_frequency)
                break
            else:
                previous_frequencies.add(current_frequency)

# result obtained: 77271