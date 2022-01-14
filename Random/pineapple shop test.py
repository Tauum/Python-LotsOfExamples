answer = input("Enter buy or sell: ")
if answer == "buy":
    # Do this.
or answer == "sell":
    # Do that.

    answer = None
    while answer not in ("buy", "sell"):
        answer = input("Enter buy or sell: ")
        if answer == "buy":
        # Do this.
        elif answer == "sell":
        # Do that.
        else:
            print("Please enter buy or sell.")

