months = {
    "january":1,
    "february":2,
    "march":3,
    "april":4,
    "may":5,
    "june":6,
    "july":7,
    "august":8,
    "september":9,
    "october":10,
    "november":11,
    "december":12
}

while True:
    try:
        date = input("date: ").strip()
        
        if "," in date:
            month,day,year = date.split(" ")
            month = months[month.lower()]
            year = int(year)
            day = int(day.replace(",", ""))
              
        else:
            month,day,year = map(int, date.split("/"))
            
        if not 1 <= month <= 12 or not 1 <= day <= 31:
            continue
        
        print(f"{year}-{month:02}-{day:02}")
        break

    except (ValueError,NameError, KeyError):
        pass