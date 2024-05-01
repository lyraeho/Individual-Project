
def main():
  start = input("Would you like to begin the game? ").lower()
  if start == 'yes':
    health = 100
    age = 0
    IQ = 100
    EQ = 100
    print('Welcome to MyLife!'+ '\n' 'This is a game where you can make decisions and live your life. You will be given choices and based on your choices different outcomes will occur.' + '\n' + 'Your life will begin at age 0 and throughout the game you will age.')
    print('Your choices will determine your life expectancy. Your life expectancy is 100. If your life expectancy is less than your age then you die. You can win by reaching 150. Good luck!')
    print('''        
        ,~'.~@~.`~.
       / : _..._ : \
      { :,"''\\`".: }
       `C) 9 _ 9 (--.._,-"""-.__
        (  )(@)(  )             `.
         `-.___.-'                \
         ,' \ /    ,`             ;`-._,-.
       ,'  ,'/   ,'           `---t.,-.   \_
     ,--.,','  ,'----.__\         _(   \----'
   '///,`,--.,'          `-.__.--'  `.  )
       '///,'                         `-`   
    ''')
    x = input("Type 'enter' to continue ")
    if x == 'enter':
       childhood()
  else:
    print('Goodbye!')
    exit()

class childhood:
  import random

  # Initial character stats
  stats = {
      "health": 100,
      "IQ": 100,
      "EQ": 100,
      "age": 1,
      "friends": 0,
      "relationship": 0,
      "job": 0,
      "education": 0
  }

  def display_stats():
      print(f"Age: {stats['age']}")
      print(f"Health: {stats['health']}")
      print(f"IQ: {stats['IQ']}")
      print(f"EQ: {stats['EQ']}")
      print(f"Friends: {stats['friends']}")
      print(f"Relationships: {stats['relationship']}")
      print(f"Jobs: {stats['job']}")
      print(f"Education: {stats['education']}")
      print()

  def make_choice(choices):
      while True:
          print("Choose an action:")
          for i, choice in enumerate(choices):
              print(f"{i+1}: {choice['text']}")
          choice_index = input("Enter your choice: ")
          if choice_index.isdigit() and 1 <= int(choice_index) <= len(choices):
              return choices[int(choice_index) - 1]
          else:
              print("Invalid choice. Please try again.")

  def handle_event(event):
      for stat, value in event.items():
          stats[stat] += value

  def try_action(action, success_message, failure_message, success_event=None, failure_event=None):
      if random.choice([True, False]):
          print(success_message)
          if success_event:
              handle_event(success_event)
          return True
      else:
          print(failure_message)
          if failure_event:
              handle_event(failure_event)
          return False

  # Main game loop
  while stats["age"] <= 18 and stats["health"] > 0 and stats["relationship"] <= 1:
      display_stats()

      # First set of choices
      choices_group1 = [
          {"text": "Eat healthy", "event": {"health": 10}},
          {"text": "Study late", "event": {"IQ": 5, "EQ": -5, "health": -5}},
          {"text": "Skip breakfast", "event": {"health": -10}}
      ]
      choice = make_choice(choices_group1)
      handle_event(choice["event"])

      # Second set of choices
      choices_group2 = [
          {"text": "Try to make friends", "event": {"friends": 1}},
          {"text": "Start a relationship", "event": {"relationship": 1}},
          {"text": "Get a job", "event": {"job": 1}}
      ]
      choice = make_choice(choices_group2)
      handle_event(choice["event"])

      # Third set of choices
      choices_group3 = [
          {"text": "Spend time with partner", "event": {"EQ": random.choice([-10, -5, 10, 15])}},
          {"text": "Ask someone out", "event": {}, "success_event": {"relationship": 1}},
          {"text": "Meet the parents", "event": {"EQ": random.choice([10, 5]) if stats["relationship"] > 0 else 0}}
      ]
      choice = make_choice(choices_group3)
      if choice["text"] == "Ask someone out":
          try_action(
              action="Ask someone out",
              success_message="Your crush said yes! You are now in a relationship.",
              failure_message="Your crush said no. Maybe next time!",
              success_event={"relationship": 1},
              failure_event=None
          )
      else:
          handle_event(choice["event"])

      # Additional actions based on previous choices
      if stats["relationship"] > 0:
          relationship_choices = [
              {"text": "Take partner on a date", "event": {"EQ": random.choice([10, 5])}},
              {"text": "Meet the parents", "event": {"EQ": random.choice([10, 5])}}
          ]
          choice = make_choice(relationship_choices)
          handle_event(choice["event"])

      # Age the character
      stats["age"] += 1

  if stats["age"] >= 18:
    adulthood_choices = [
        {"text": "Advance career", "event": {"job": 1}},
        {"text": "Further education", "event": {"education": 1}},
        {"text": "Start a family", "event": {"relationship": 1}}
    ]
    choice = make_choice(adulthood_choices)
    handle_event(choice["event"])
  # Game over
  if stats["health"] <= 0:
      print("Your health dropped to 0. Game over.")
  elif stats["relationship"] > 1:
      print("You are in a relationship. Game over.")
  else:
      print("You reached age 18. Game over.")
    
class adulthood:
  import random
  # Will use stats from end of childhood()
  def handle_event(event):
    for stat, value in event.items():
        stats[stat] += value
    stats["events"].append(event)

    # Update stats based on events from childhood
    for event in stats["events"]:
        for stat, value in event.items():
            if stat in stats and stat != "events":
                stats[stat] += value
  def display_stats():
    print(f"Age: {stats['age']}")
    print(f"Health: {stats['health']}")
    print(f"IQ: {stats['IQ']}")
    print(f"EQ: {stats['EQ']}")
    print(f"Friends: {stats['friends']}")
    print(f"Relationships: {stats['relationship']}")
    print(f"Jobs: {stats['job']}")
    print(f"Education: {stats['education']}")
    print()

  def make_choice(choices):
    while True:
        print("Choose an action:")
        for i, choice in enumerate(choices):
            print(f"{i+1}: {choice['text']}")
        choice_index = input("Enter your choice: ")
        if choice_index.isdigit() and 1 <= int(choice_index) <= len(choices):
            return choices[int(choice_index) - 1]
        else:
            print("Invalid choice. Please try again.")

  def handle_event(event):
    for stat, value in event.items():
        stats[stat] += value
    stats["events"].append(event)

  # Main game loop
  while stats["health"] > 0:
    display_stats()

    # Apply events from childhood
    for event in stats["events"]:
        handle_event(event)

    # First set of choices
    choices_group1 = [
        {"text": "Eat healthy", "event": {"health": 10}},
        {"text": "Study late", "event": {"IQ": 5, "EQ": -5, "health": -5}},
        {"text": "Skip breakfast", "event": {"health": -10}}
    ]
    choice = make_choice(choices_group1)
    handle_event(choice["event"])

    # Second set of choices
    choices_group2 = [
        {"text": "Try to make friends", "event": {"friends": 1}},
        {"text": "Start a relationship", "event": {"relationship": 1}},
        {"text": "Get a job", "event": {"job": 1}}
    ]
    choice = make_choice(choices_group2)
    handle_event(choice["event"])

    # Third set of choices
    choices_group3 = [
        {"text": "Spend time with partner", "event": {"EQ": random.choice([-10, -5, 10, 15])}},
        {"text": "Ask someone out", "event": {}, "success_event": {"relationship": 1}},
        {"text": "Meet the parents", "event": {"EQ": random.choice([10, 5]) if stats["relationship"] > 0 else 0}}
    ]
    choice = make_choice(choices_group3)
    if choice["text"] == "Ask someone out":
        if random.choice([True, False]):
            print("Your crush said yes! You are now in a relationship.")
            stats["relationship"] = 1
        else:
            print("Your crush said no. Maybe next time!")

    if stats["relationship"] > 0:
        relationship_choices = [
            {"text": "Take partner on a date", "event": {"EQ": random.choice([10, 5])}},
            {"text": "Meet the parents", "event": {"EQ": random.choice([10, 5])}}
        ]
        choice = make_choice(relationship_choices)
        handle_event(choice["event"])

    # Age the character
    stats["age"] += 1

    if stats["age"] >= 18:
        adulthood_choices = [
            {"text": "Advance career", "event": {"job": 1}},
            {"text": "Further education", "event": {"education": 1 if stats["IQ"] >= 120 else 0}},
            {"text": "Start a family", "event": {"relationship": 1}}
        ]
        choice = make_choice(adulthood_choices)
        handle_event(choice["event"])

        if choice["text"] == "Further education":
            college_questions = [
                {"question": "What is your GPA?", "correct_answer": "4.0"},
                {"question": "What extracurricular activities have you participated in?", "correct_answer": "Debate club, Science Olympiad"},
                {"question": "Why do you want to attend this college?", "correct_answer": "To pursue my passion for computer science"}
            ]
            print("College Admittance Questionnaire:")
            for question in college_questions:
                answer = input(question["question"] + " ")
                if answer.lower() != question["correct_answer"].lower():
                    print("Your application was rejected.")
                    break
            else:
                print("Congratulations! You got into college.")
                stats["education"] += 1

        marriage_choices = [
            {"text": "Get married", "event": {"relationship": 1}},
            {"text": "Stay single", "event": {}}
        ]
        choice = make_choice(marriage_choices)
        handle_event(choice["event"])

  # Game over
  if stats["health"] <= 0:
    print("Your health dropped to 0. Game over.")
  else:
    print("You have reached the end of your life. Game over.")

  

main()

