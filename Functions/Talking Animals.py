def speak(animal= "dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    elif animal == " ":
        return "woof"
    else:
        return "?"

print(speak("pig"))
print(speak("duck"))
print(speak("dog"))
print(speak("cat"))
print(speak(" "))
print(speak(5))
