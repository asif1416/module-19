# Shutdown
def shutdown():
  user_input = input("Do you want to shut down the system? (Yes/No): ")

  if user_input.lower() == "yes":
    print("Shutting down...")
  elif user_input.lower() == "no":
    print("Abort shut down.")
  else:
    print("Sorry, I didn't understand that. Please enter 'Yes' or 'No'.")

shutdown()