for number in range(1, 101):
    if number % 7 == 0 or str(number).find('7') != -1:
        continue;
    print(number);
