# https://cs50.harvard.edu/python/psets/1/meal/

def main():
    entrada = input('What time is it? ')
    time_convert = convert(entrada)
    if 7.0 <= time_convert <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_convert <= 13.0:
        print("lunch time")
    elif 18.0 <= time_convert <= 19.0:
        print("dinner time")
    else:
        print('')


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + (minutes/60)


if __name__ == "__main__":
    main()
