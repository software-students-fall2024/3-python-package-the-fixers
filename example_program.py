from codebreak.eye_exercises import eye_exercise
from codebreak.mental_exercises import mental_exercise
from codebreak.physical_exercise import Exercise
from codebreak.stretches import stretch_exercise

# Example usage of eye exercise function
print("Eye Exercise:", eye_exercise(10))

# Example usage of mental exercise function
print("Mental Exercise:", mental_exercise("creativity"))

# Example usage of Exercise class
jogging = Exercise("Jogging", "5 minutes", "10 minutes", "15 minutes", "Cardio")
jogging.output("medium")

# Example usage of stretch exercise function
print("Stretch Exercise:", stretch_exercise(8))
