import numpy as np

def main():
    heading()
    limit = get_limit()
    simulation_count = 100_000
    matching_count = run_sim(limit, simulation_count)
    display_results(limit, simulation_count, matching_count)

def heading():
    print("Birthday Paradox")

def get_limit():
    print("\nHow many birthdays shall I generate? (Max 100)")
    num = input("> ")

    if num.isdigit() and 1 <= int(num) <= 100:
        return int(num)
    else:
        print("Please enter a valid number between 1 and 100.")
        return get_limit()

def run_sim(limit, simulation_count):
    matching_count = 0

    for i in range(simulation_count):
        birthdays = np.random.randint(0,365, size=limit)

        if len(np.unique(birthdays)) < limit:
            matching_count += 1

        if (i + 1) % 10_000 == 0:
            print(f"{i + 1} simulations run")

    return matching_count

def display_results(limit, simulation_count, matching_count):
    probability = (matching_count / simulation_count) * 100

    print(f"\nOut of {simulation_count} simulations of {limit} people, there was a matching birthday "
          f"in that group {matching_count} times.")
    print(f"This means that {limit} people have a {probability:.2f}% chance of having a matching "
          f"birthday in their group.")
    print("That's probably more than you would think!")

if __name__ == '__main__':
    main()
