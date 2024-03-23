import inflect

p = inflect.engine()

num = 22_500_000

print("The plural of ", num, " is", p.number_to_words(num))
