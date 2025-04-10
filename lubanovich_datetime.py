import datetime


def write_file(file_name, date):
    with open(file_name, "w") as file:
        file.write(date)


def read_file(file_name):
    with open(file_name, "r") as file:
        text = file.read()
    return text


def format_string_in_date(string):
    """Преобразует строку в дату."""
    return datetime.datetime.strptime(string, "%Y-%m-%d")


if __name__ == "__main__":
    now = datetime.date.today().isoformat()
    today_string = read_file("today.txt")
    date = datetime.date(1997, 8, 14)
    days = datetime.timedelta(days=10000)
    weekday = date.isoweekday()  # день недели, где понедельник - 1, воскресенье - 7
