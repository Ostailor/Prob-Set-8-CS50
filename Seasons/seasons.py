import re
import sys
from datetime import date, timedelta
import inflect


def main():
    p = inflect.engine()
    dates = input('Date of Birth: ')
    if matches := re.search(r"([0-9]{4})-([0-9]{2})-([0-9]{2})", dates):
        diff = (p.number_to_words(difference(dates), andword='') + ' minutes').capitalize()
        print(diff)
    else:
        sys.exit("Invalid Date")


def difference(d):
    today_date = date.today()
    d = date.fromisoformat(d)
    if today_date < d:
        return "Invalid Date"
    else:
        diff = today_date-d
    divmod(diff.total_seconds(), 60)
    return int(diff/timedelta(minutes=1))


if __name__ == "__main__":
    main()
