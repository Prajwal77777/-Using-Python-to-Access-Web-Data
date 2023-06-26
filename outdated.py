months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        month, days, year = date.split("/")
        if (int(days >= 1) and int(days <= 31) and int(month >= 1) and int(month <= 12)):
            break
    except:
        try:
            O_months, O_days, O_year = date.split(" ")
            for i in range(len(months)):
                if O_months == months[i]:
                    month = i + 1
            days = O_days.replace(",", "")
            if (int(days >= 1) and int(days <= 31) and int(month >= 1) and int(month <= 12)):
                break
        except:
            print()
            pass
print(f"{year}-{int(month):02}-{int(days):02}")
