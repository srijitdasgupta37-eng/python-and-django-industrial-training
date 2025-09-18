dept1_guests = ["Alice", "Bob", "Charlie"]
dept2_guests = ["Bob", "David", "Eva"]


combined_guests = list(set(dept1_guests + dept2_guests))


combined_guests.sort()


print("Final guest list:")
for guest in combined_guests:
    print(guest)