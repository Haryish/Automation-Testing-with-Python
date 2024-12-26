def timeConversion(s):
    # Extract the period (AM/PM)
    period_ind = s[-2:]
    # Extract hour, minute, and second, excluding the last 2 characters (AM/PM)
    hour, minute, second = map(int, s[:-2].split(":"))

    # Convert hour based on the period
    if period_ind == "PM" and hour != 12:  # Convert PM times except 12 PM
        hour += 12
    elif period_ind == "AM" and hour == 12:  # Convert 12 AM to 0
        hour = 0

    # Return the military time in "HH:MM:SS" format
    return f"{hour:02}:{minute:02}:{second:02}"


if __name__ == "__main__":
    s = input()  # Take input in the format "hh:mm:ssAM/PM"
    result = timeConversion(s)
    print(result)  # Output the converted time
