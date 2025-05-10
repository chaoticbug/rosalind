#Rabbits and Recurrence Relations
def get_alcohol_estimate():
    # Define drinking levels
    drinking_levels = {
        "light": 2,   # Light drinker: ~2 drinks per event
        "moderate": 4, # Moderate drinker: ~4 drinks per event
        "heavy": 6     # Heavy drinker: ~6+ drinks per event
    }
    
    num_guests = int(input("Enter the number of guests: "))
    total_drinks = 0
    
    for i in range(num_guests):
        name = input(f"Enter guest {i+1} name (or skip): ")
        drink_level = input(f"Enter {name}'s drinking level (light, moderate, heavy): ").strip().lower()
        events = int(input(f"How many events will {name} drink at? (1-2): "))
        
        if drink_level in drinking_levels:
            total_drinks += drinking_levels[drink_level] * events
        else:
            print(f"Invalid input for {name}, skipping.")
    
    # Convert to bottles
    liquor_bottles = total_drinks / 16  # 750ml bottle = 16 drinks
    wine_bottles = total_drinks / 5     # 750ml bottle = 5 drinks
    beer_cases = total_drinks / 24      # 1 case (24 bottles) = 24 drinks
    
    print("\nEstimated Alcohol Needed:")
    print(f"Liquor Bottles: {round(liquor_bottles, 1)}")
    print(f"Wine Bottles: {round(wine_bottles, 1)}")
    print(f"Beer Cases: {round(beer_cases, 1)}")
    
# Run the function
get_alcohol_estimate()