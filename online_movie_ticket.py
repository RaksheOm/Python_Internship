# ### **2️⃣ Online Movie Ticket Booking**

# **Problem Statement:**

# Create a function to book movie tickets.

# **Requirements:**

# - Take number of tickets as input
# - Max allowed tickets = **6**
# - Ticket price = **₹250**
# - Calculate total price
# - Handle cases where:
#     - User enters non-numeric value
#     - User enters more than 6 tickets
#     - User enters zero or negative tickets

# **Concepts to use:**

# - Function
# - Exception handling
# - Conditional logic

def book_movie_tickets():
    TICKET_PRICE = 250
    MAX_TICKETS = 6

    try:
        tickets = int(input("Enter number of tickets: "))

        if tickets <= 0:
            print("Invalid number of tickets. Must be greater than 0.")

        elif tickets > MAX_TICKETS:
            print("You can book a maximum of 6 tickets only.")

        else:
            total_price = tickets * TICKET_PRICE
            print("Tickets booked successfully!")
            print("Number of tickets:", tickets)
            print("Total amount: ₹", total_price)

    except ValueError:
        print("Invalid input! Please enter a numeric value.")


# Function call
book_movie_tickets()
