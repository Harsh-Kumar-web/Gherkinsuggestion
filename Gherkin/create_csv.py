import pandas as pd

data = {
    "user_input": [
        "go to the seats page",
        "decline insurance",
        "complete payment",
        "review fares",
        "enter passenger details",
        "select meals",
        "accept insurance",
        "search for flights",
        "select a business class seat",
        "select an economy class seat",
        "book a burger meal",
        "book a window seat",
        "do priority check-in",
        "cancel the booking"
    ],
    "gherkin_scenario": [
        "Given the user is on the home page\nWhen the user enters flight details\nAnd the user searches for flights\nThen the user is on the fare review page\nWhen the user reviews the fares\nThen the user is on the passengers page\nWhen the user enters passenger details\nThen the user is on the seats page\nWhen the user selects seats",
        "Given the user is on the home page\nWhen the user enters flight details\nAnd the user searches for flights\nThen the user is on the fare review page\nWhen the user reviews the fares\nThen the user is on the passengers page\nWhen the user enters passenger details\nThen the user is on the seats page\nWhen the user selects seats\nThen the user is on the meals page\nWhen the user selects meals\nThen the user is on the insurance page\nWhen the user declines insurance options",
        "Given the user is on the home page\nWhen the user enters flight details\nAnd the user searches for flights\nThen the user is on the fare review page\nWhen the user reviews the fares\nThen the user is on the passengers page\nWhen the user enters passenger details\nThen the user is on the seats page\nWhen the user selects seats\nThen the user is on the meals page\nWhen the user selects meals\nThen the user is on the insurance page\nWhen the user selects insurance options\nThen the user is on the payment page\nWhen the user completes the payment",
        "Given the user is on the home page\nWhen the user enters flight details\nAnd the user searches for flights\nThen the user is on the fare review page\nWhen the user reviews the fares",
        "Given the user is on the home page\nWhen the user enters flight details\nAnd the user searches for flights\nThen the user is on the fare review page\nWhen the user reviews the fares\nThen the user is on the passengers page\nWhen the user enters passenger details",
        "Given the user is on the home page\nWhen the user enters flight details\nAnd the user searches for flights\nThen the user is on the fare review page\nWhen the user reviews the fares\nThen the user is on the passengers page\nWhen the user enters passenger details\nThen the user is on the seats page\nWhen the user selects seats\nThen the user is on the meals page\nWhen the user selects meals",
        "Given the user is on the home page\nWhen the user enters flight details\nAnd the user searches for flights\nThen the user is on the fare review page\nWhen the user reviews the fares\nThen the user is on the passengers page\nWhen the user enters passenger details\nThen the user is on the seats page\nWhen the user selects seats\nThen the user is on the meals page\nWhen the user selects meals\nThen the user is on the insurance page\nWhen the user accepts insurance options",
        "Given the user is on the home page\nWhen the user enters flight details\nAnd the user searches for flights",
        "Given the user is on the home page\nWhen the user enters flight details\nAnd the user searches for flights\nThen the user is on the fare review page\nWhen the user reviews the fares\nThen the user is on the passengers page\nWhen the user enters passenger details\nThen the user is on the seats page\nWhen the user selects a business class seat",
        "Given the user is on the home page\nWhen the user enters flight details\nAnd the user searches for flights\nThen the user is on the fare review page\nWhen the user reviews the fares\nThen the user is on the passengers page\nWhen the user enters passenger details\nThen the user is on the seats page\nWhen the user selects an economy class seat",
        "Given the user is on the home page\nWhen the user enters flight details\nAnd the user searches for flights\nThen the user is on the fare review page\nWhen the user reviews the fares\nThen the user is on the passengers page\nWhen the user enters passenger details\nThen the user is on the seats page\nWhen the user selects seats\nThen the user is on the meals page\nWhen the user books a burger meal",
        "Given the user is on the home page\nWhen the user enters flight details\nAnd the user searches for flights\nThen the user is on the fare review page\nWhen the user reviews the fares\nThen the user is on the passengers page\nWhen the user enters passenger details\nThen the user is on the seats page\nWhen the user books a window seat",
        "Given the user is on the home page\nWhen the user enters flight details\nAnd the user searches for flights\nThen the user is on the fare review page\nWhen the user reviews the fares\nThen the user is on the passengers page\nWhen the user enters passenger details\nThen the user is on the seats page\nWhen the user selects seats\nThen the user is on the priority check-in page\nWhen the user does priority check-in",
        "Given the user is on the home page\nWhen the user enters flight details\nAnd the user searches for flights\nThen the user is on the fare review page\nWhen the user reviews the fares\nThen the user is on the passengers page\nWhen the user enters passenger details\nThen the user is on the seats page\nWhen the user selects seats\nThen the user is on the meals page\nWhen the user selects meals\nThen the user is on the insurance page\nWhen the user selects insurance options\nThen the user is on the payment page\nWhen the user completes the payment\nThen the user cancels the booking"
    ]
}

df = pd.DataFrame(data)
df.to_csv('C:\\Gherkin\\data\\gherkin_data.csv', index=False)
