#Greets user
print("Hello! I am so excited for the opportunity to run for a leadership position!")
input("Press enter to continue\n")


#Introduces breach
print("Would you like to learn why Addison Lewis would make a great Social Media Manager, Workshop Coordinator, or Membership Chair?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) Why I want to run, (b) Past Experience, or (c) Skills and Strengths, (d) None")
  topic = input()

  if topic.lower() == "a":
    print("I am passionate about computer science and deeply committed to creating a positive and inclusive environment for girls interested in coding. My love for technology, particularly in areas like cybersecurity, drives me to explore new challenges and continuously improve my skills. I am excited to pursue a future in cybersecurity, where I hope to contribute to protecting individuals and organizations from cyber threats. By taking on a leadership role in our Girls Who Code club, I aim to inspire and support other girls as they explore the world of coding, helping them build confidence in their abilities and discover their own passions within tech.")

  elif topic.lower() == "b":
    print("I have various leadership positions in the past! I am currently the Student Council President and where I foster a sense of community within the school. I am passionate about Computer Science. Recently, I have been interning for Eleven-0 Pickleball where I am in charge of creating their webiste! I am currently in the final stages of creating my own app. I also have my own nonprofit called STEM Sisters Corp. where I inspire elementary school girls to pursue their passions in STEM. This summer I attended a two week Data Science camp where I learned the basics of Python and SQL! I also particpated in the Girls who Code Summer Immersion Program. I have past experience with making instagram posts for Student Council and for KP Cares!")

  elif topic.lower() == "c":
    print("I have various leadership positions in the past! I am currently the Student Council President and where I foster a sense of community within the school. I am passionate about Computer Science. Recently, I have been interning for Eleven-0 Pickleball where I am in charge of creating their webiste! I am currently in the final stages of creating my own app. I also have my own nonprofit called STEM Sisters Corp. where I inspire elementary school girls to pursue their passions in STEM. This summer I attended a two week Data Science camp where I learned the basics of Python and SQL! I also particpated in the Girls who Code Summer Immersion Program. I have past experience with making instagram posts for Student Council and for KP Cares!")

  elif topic.lower() == "d":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you vote me, Addison Lewis to be your Social Media Manager, Workshop Coordinator, or Membership Chair!")