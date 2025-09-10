# A 3-day tech workshop collected attendee registrations separately for each day. You are given three lists (day1, day2, day3) of email addresses — lists may contain duplicates (people registering multiple times) and email case may vary (Upper/Lower).
# Write a Python program that:

# Cleans each day's list (normalizes case, removes duplicates).
# Prints the total number of unique attendees across all days.
# Prints the list of attendees who attended all three days.
# Prints the list of attendees who attended exactly one day.
# Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
# Produces a final report with counts and sorted lists for each of the above outputs.


def clean(l1,l2,l3):
    l1 = set(email.lower() for email in l1)
    l2 = set(email.lower() for email in l2)
    l3 = set(email.lower() for email in l3)

    unique_attendees = l1|l2|l3
    print(f"Total no.of unique_attendees: {len(unique_attendees)}" )

    all_three_days=sorted(l1&l2&l3)
    print(f"Attendees who attended all the three days:\n{all_three_days}\ncount is {len(all_three_days)}")

    exactly_one_day = (l1 - l2 - l3) | (l2 - l1 - l3) | (l3 - l1 - l2)
    print(f"Attendees who attended exactly one day:\n{sorted(exactly_one_day)}\ncount is {len(exactly_one_day)}")


    print(f"pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3): {len(l1&l2)}, {len(l2&l3)} & {len(l1&l3)}")


# Example input
day1 = ["a@example.com", "b@example.com", "c@example.com", "d@example.com"]   # d only in day1
day2 = ["a@example.com", "b@example.com", "c@example.com", "e@example.com"]   # e only in day2
day3 = ["a@example.com", "b@example.com", "f@example.com"]                     # f only in day3

clean(day1,day2,day3)