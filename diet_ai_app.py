import streamlit as st

# --------------------- Basic Info ---------------------
st.set_page_config(page_title="Smart Diet Coach", layout="centered")
st.title("🍽️ Smart Diet Coach")
st.subheader("Get your custom 7-day meal plan — no AI key needed!")

# --------------------- User Inputs ---------------------
goal = st.selectbox("What is your goal?", ["Lose Fat", "Maintain", "Gain Muscle"])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", 10, 100, 20)
height = st.number_input("Height (cm)", 100, 250, 170)
weight = st.number_input("Weight (kg)", 30, 200, 70)
activity = st.selectbox("Activity Level", [
    "Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"
])
food_pref = st.selectbox("Diet Preference", ["Vegetarian", "Non-Vegetarian", "Vegan"])

# --------------------- BMR & Calorie Logic ---------------------
def calc_bmr(gender, weight, height, age):
    if gender == "Male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

activity_levels = {
    "Sedentary": 1.2,
    "Lightly Active": 1.375,
    "Moderately Active": 1.55,
    "Very Active": 1.725,
    "Extra Active": 1.9
}

bmr = calc_bmr(gender, weight, height, age)
calories = bmr * activity_levels[activity]

if goal == "Lose Fat":
    calories -= 500
elif goal == "Gain Muscle":
    calories += 300

calories = int(calories)

# --------------------- Static Meal Plan Generator ---------------------
def generate_meal_plan(cals, food_pref):
    # Example simple meal plan structure
    breakfast = {
        "Vegetarian": "Oats with almond milk + fruits",
        "Non-Vegetarian": "Boiled eggs + toast + banana",
        "Vegan": "Tofu scramble + avocado toast"
    }

    lunch = {
        "Vegetarian": "Dal, roti, mixed sabzi, curd",
        "Non-Vegetarian": "Grilled chicken, rice, salad",
        "Vegan": "Quinoa bowl with chickpeas and veggies"
    }

    dinner = {
        "Vegetarian": "Paneer stir-fry + brown rice",
        "Non-Vegetarian": "Egg curry + roti + salad",
        "Vegan": "Lentil soup + whole wheat bread"
    }

    snacks = {
        "Vegetarian": "Nuts, Greek yogurt, fruits",
        "Non-Vegetarian": "Protein shake, boiled egg",
        "Vegan": "Fruit smoothie, hummus + carrots"
    }

    plan = []
    for day in range(1, 8):
        plan.append({
            "day": f"Day {day}",
            "breakfast": breakfast[food_pref],
            "lunch": lunch[food_pref],
            "dinner": dinner[food_pref],
            "snacks": snacks[food_pref]
        })
    return plan

# --------------------- Show Meal Plan ---------------------
if st.button("Generate Weekly Diet Plan"):
    st.success(f"🎯 Your daily calorie goal is: {calories} kcal")
    st.write("---")
    plan = generate_meal_plan(calories, food_pref)

    for day in plan:
        st.markdown(f"### 📅 {day['day']}")
        st.markdown(f"- **Breakfast**: {day['breakfast']}")
        st.markdown(f"- **Lunch**: {day['lunch']}")
        st.markdown(f"- **Dinner**: {day['dinner']}")
        st.markdown(f"- **Snacks**: {day['snacks']}")
        st.write("---")
