from datetime import date, timedelta

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
        
today = date(year, month, day)
tomorrow = today + timedelta(1)
        
print(f"Tomorrow's date: Day: {tomorrow.day} Month: {tomorrow.month} Year: {tomorrow.year}")
    


