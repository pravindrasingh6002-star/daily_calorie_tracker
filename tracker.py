import datetime

print("==========================================================")
print("🧠 Welcome to the Daily Calorie Tracker CLI")
print("This program helps you record your meals and calorie intake,")
print("calculate total and average calories, and compare with your limit.")
print("==========================================================\n")


meal_names = []
meal_calories = []

try:
    num_meals = int(input("🍽️  How many meals do you want to log today? "))
except ValueError:
    print("⚠️  Invalid input! Please enter a number.")
    exit()

for i in range(num_meals):
    print(f"\nMeal {i+1}:")
    meal_name = input("Enter meal name: ").strip().title()
    try:
        calories = float(input("Enter calories consumed: "))
    except ValueError:
        print("⚠️  Invalid input! Please enter a number for calories.")
        exit()
    meal_names.append(meal_name)
    meal_calories.append(calories)

total_calories = sum(meal_calories)

average_calories = total_calories / len(meal_calories)

try:
    daily_limit = float(input("\n🔥 Enter your daily calorie limit: "))
except ValueError:
    print("⚠️  Invalid input! Please enter a valid number.")
    exit()


print("\n==========================================================")
print("📊 DAILY CALORIE SUMMARY")
print("==========================================================")
print("Meal Name\t\tCalories")
print("----------------------------------------------------------")
for meal, cal in zip(meal_names, meal_calories):
    print(f"{meal:<15}\t{cal:.2f}")
print("----------------------------------------------------------")
print(f"Total:\t\t\t{total_calories:.2f}")
print(f"Average per meal:\t{average_calories:.2f}")
print("----------------------------------------------------------")

if total_calories > daily_limit:
    print(f"⚠️  WARNING: You have exceeded your daily limit by {total_calories - daily_limit:.2f} calories!")
else:
    print(f"✅ Great job! You are within your daily limit by {daily_limit - total_calories:.2f} calories.")


save = input("\n💾 Do you want to save this session to a file? (yes/no): ").lower()
if save == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"calorie_log_{timestamp}.txt"
    with open(filename, "w") as file:
        file.write("Daily Calorie Tracker Report\n")
        file.write("====================================\n")
        file.write(f"Date & Time: {datetime.datetime.now()}\n\n")
        for meal, cal in zip(meal_names, meal_calories):
            file.write(f"{meal:<15} : {cal:.2f} cal\n")
        file.write("------------------------------------\n")
        file.write(f"Total Calories: {total_calories:.2f}\n")
        file.write(f"Average Calories: {average_calories:.2f}\n")
        file.write(f"Daily Limit: {daily_limit:.2f}\n")
        if total_calories > daily_limit:
            file.write("Status: ❌ Limit Exceeded\n")
        else:
            file.write("Status: ✅ Within Limit\n")
        file.write("====================================\n")
    print(f"✅ Session saved successfully as {filename}")
else:
    print("🗑️ Session not saved.")

print("\n🎯 Thank you for using Daily Calorie Tracker CLI!")
print("==========================================================")
