option_counts = {'A': 0, 'B': 0}  # Initialize counters for options A and B
num_questions = 5  # Set the number of questions


for i in range(1, num_questions + 1):
    response = input(f"Enter response for question {i} (A/B): ").upper()  # Get user input for each question
    if response in option_counts:
        option_counts[response] += 1  # Increment the count for the selected option

# Print the counts
for option, count in option_counts.items():
    print(f"Option {option} count: {count}")
