def say_greeting():
  print("Welcome, I hope you slept")
def print_poor_sleep_days(days):
  if days:
    for day, score in days:
      print(f"{day}: {score}/10")
say_greeting()
weekday = []
day = weekday
poor_sleep_days = []
weekday = input("What day of sleep are we helping?")
day.append(weekday)
sleep = int(input("How did you sleep 1-10"))
if sleep == 9 or sleep == 10:
  print("You slept incredibly keep it up")
elif sleep == 7 or sleep== 8:
  print("focus on enhancing sleep hygiene,optimizing the bedroom enviorment, and managing late-night activities. Finally maintain a strict and consistent sleep schedule")
elif sleep == 6:
  print("Establish a 30-60min routine before bed, avoid screens, caffiene, and alcohol. Optimize your bedroom to be dark cool and quiet")
elif sleep == 5: 
  print("You should include physical activity throughout the day,If you haven't slept then get up and do a quiet and slow cool down routine before bed")
elif sleep == 4:
  print("Get sunlight in the morning and avoid phones, Avoid long naps in the afternoon, try low-dose melatonin")
elif sleep == 3:
  print("Remove screens an hour before bed, Keep naps under 30 minutes, Write down your worries, practice mindfulness/meditation to reduce anxiety")
elif sleep == 2:
  print(" Prevent any phone use 1hr before bed, practice deep breathing, don't eat heavy meals")
elif sleep == 1:
  print("Do stretching and reading 20 minutes before bed,Stay active throughout the day, Report to a doctor for continued issues")
else:
  print("Invalid Response")
if sleep <=6:
  poor_sleep_days.append((day, sleep))
  print_poor_sleep_days(poor_sleep_days)




