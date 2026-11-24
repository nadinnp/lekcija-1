tasks = ["homework", "studying", "cleaning"]

# Adding training to the end of the list
tasks.append("training")
print(tasks)

# Inserting shopping at the second position
tasks.insert(1, "shopping")
print(tasks)

# Removing studying from the list
tasks.remove("studying")
print(tasks)

# Changing the first task to math homework
tasks[0] = "math homework"
print(tasks)