# Continue
var = 10  # Initialize variable

while var > 0:  # Iterate loop
    var = var - 1  # Decrement variable

    if var == 5:  # Condition 1
        continue  # Skip the rest of the loop iteration

    # Display result (since continue skipped the rest)
    print("\nCurrent variable value:", var)

print("\nGood bye!")