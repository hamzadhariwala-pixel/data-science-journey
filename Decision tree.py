def ask(question, options):
    print("\n" + question)
    print("-" * len(question))
    
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    
    while True:
        choice = input("Enter choice (1-{}): ".format(len(options)))
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                return options[choice - 1]
        print("Invalid input. Please enter a valid number.")


def main():
    print("\n=== Daily Reflection ===")
    print("Hey—let’s take 2 minutes to look back at your day.\n")

    # -------- AXIS 1 --------
    rating = ask(
        "Q1: How would you rate your day?",
        ["Great", "Good", "Okay", "Bad"]
    )

    # -------- POSITIVE PATH --------
    if rating in ["Great", "Good"]:
        print("\nNice—that’s always good to hear.")
        print("Something clearly went right today.")

        cause = ask(
            "Q2: What contributed most to your good day?",
            ["Productivity", "People", "Routine", "Mindset"]
        )

        print("\nThat makes sense—that can really shape a good day.")

        if cause == "Productivity":
            detail = ask(
                "Q3: What drove your productivity?",
                ["Clear goals", "Deep focus", "Good time management"]
            )
        elif cause == "People":
            detail = ask(
                "Q3: What helped socially?",
                ["Support from others", "Meaningful conversations", "Teamwork"]
            )
        elif cause == "Routine":
            detail = ask(
                "Q3: What part of your routine helped?",
                ["Morning routine", "Consistency", "Daily planning"]
            )
        else:
            detail = ask(
                "Q3: What mindset helped you?",
                ["Positive thinking", "Confidence", "Calmness"]
            )

        print("\nThat’s actually a strong driver—keep that in mind.")

        print("\nLet’s dig a bit deeper into what led to this.")

        print("\nAlright—now let’s focus on tomorrow.")

        improvement = ask(
            "Q4: What will you do tomorrow?",
            ["Repeat same actions", "Optimize further", "Try something new"]
        )

        print("\nNice—building on a good day is powerful.")

    # -------- NEUTRAL PATH --------
    elif rating == "Okay":
        print("\nAlright, sounds like a mixed day.")
        print("Not bad, but not great either—let’s unpack it.")

        cause = ask(
            "Q2: What held your day back?",
            ["Distractions", "Low energy", "Poor planning", "Inconsistency"]
        )

        print("\nYeah, that can definitely slow things down.")

        if cause == "Distractions":
            detail = ask(
                "Q3: What distracted you most?",
                ["Phone", "People", "Noise"]
            )
        elif cause == "Low energy":
            detail = ask(
                "Q3: Why was your energy low?",
                ["Poor sleep", "Diet", "Mental fatigue"]
            )
        elif cause == "Poor planning":
            detail = ask(
                "Q3: What planning issue occurred?",
                ["No clear schedule", "Unclear goals", "Overplanning"]
            )
        else:
            detail = ask(
                "Q3: Where were you inconsistent?",
                ["Work", "Habits", "Focus"]
            )

        print("\nFixing just this could improve your whole day.")

        print("\nNow let’s understand the reason behind it.")

        print("\nLet’s turn this into something useful.")

        improvement = ask(
            "Q4: What will you improve tomorrow?",
            ["Plan better", "Reduce distractions", "Improve energy"]
        )

        print("\nGood—that’s a practical fix.")

    # -------- NEGATIVE PATH --------
    else:
        print("\nYeah, those days happen.")
        print("Let’s figure out what made it tough.")

        cause = ask(
            "Q2: What was the main issue?",
            ["Stress", "Conflict", "Low productivity", "Overwhelm"]
        )

        print("\nThat’s rough, but it’s useful to identify it.")

        if cause == "Stress":
            detail = ask(
                "Q3: What caused your stress?",
                ["Workload", "Deadlines", "Pressure"]
            )
        elif cause == "Conflict":
            detail = ask(
                "Q3: What kind of conflict?",
                ["Argument", "Miscommunication", "Expectation mismatch"]
            )
        elif cause == "Low productivity":
            detail = ask(
                "Q3: Why low productivity?",
                ["Procrastination", "No focus", "Lack of clarity"]
            )
        else:
            detail = ask(
                "Q3: Why did you feel overwhelmed?",
                ["Too many tasks", "No priority", "Time pressure"]
            )

        print("\nThat explains a lot.")

        print("\nNow let’s understand the reason behind it.")

        print("\nLet’s turn this into something useful.")

        improvement = ask(
            "Q4: What is your recovery step?",
            ["Rest", "Plan fresh", "Talk to someone", "Start small"]
        )

        print("\nGood step—that’s how you reset.")

    # -------- FINAL --------
    print("\nJust one last thing.")

    confidence = ask(
        "Q5: How do you feel about tomorrow?",
        ["Confident", "Neutral", "Uncertain"]
    )

    print("\nFair enough—take it one step at a time.")

    print("\nHere’s a quick recap of your day:")

    print("\n========== SUMMARY ==========")
    print(f"Day Rating: {rating}")
    print(f"Key Factor: {cause}")
    print(f"Detail: {detail}")
    print(f"Plan: {improvement}")
    print(f"Confidence: {confidence}")
    print("================================")

    print("\nThat’s it for today—see you tomorrow.\n")


if __name__ == "__main__":
    main()