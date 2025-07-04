from data import *
from welcome import *
from linkedlist import LinkedList

# Print welcome message
print_welcome()

# Function to insert a list of types into a Linked List data structure
def insert_pokemon_types():
    poke_type_list = LinkedList()
    for poke_type in types:
        poke_type_list.insert_beginning(poke_type)
    return poke_type_list

# Function to insert Pokémon data into a nested Linked List data structure
def insert_pokemon_data():
    pokemon_data_list = LinkedList()
    for poke_type in types:
        poke_sublist = LinkedList()
        for pokemon in pokemon_data:
            if pokemon[0] == poke_type:
                poke_sublist.insert_beginning(pokemon)
        pokemon_data_list.insert_beginning(poke_sublist)
    return pokemon_data_list

# Define the Pokémon types and data as Linked Lists
gen1_types = insert_pokemon_types()
kanto_pokemon = insert_pokemon_data()

# Interactive input function
selected_type = ""

while True:
    # User interaction message
    user_type_input = input(
        "\nWhat type of Pokémon would you like to catch?\nType the beginning of that type (example: 'G' for 'Grass') and press enter to see if "
        "it's listed.\n").lower()

    # Search for user input in types linked list
    matching_types = []
    type_list_head = gen1_types.get_head_node()
    while type_list_head is not None:
        if type_list_head.get_value() and str(type_list_head.get_value()).startswith(user_type_input):
            matching_types.append(type_list_head.get_value())
        type_list_head = type_list_head.get_next_node()

    # Handle no matching types
    if not matching_types:
        print("No Pokémon types match your input. Please try again.")
        continue

    # Print matching types
    print("\nMatching types:")
    for poke_type in matching_types:
        print(poke_type)

    # If only one type was found, ask user to confirm
    if len(matching_types) == 1:
        user_confirm_input = input(
            f"\nThe only matching type is {matching_types[0]}. Continue? (y/n) "
        ).lower()
        if user_confirm_input == 'y':
            selected_type = matching_types[0]
        else:
            continue
    else:
        # If multiple types, ask user to select one
        selected_type = input(
            "\nPlease select one of the listed types by typing it exactly: "
        ).lower()
        if selected_type not in matching_types:
            print("Invalid type selected. Please try again.")
            continue

    # Retrieve and print Pokémon data for the selected type
    print(f"\nSelected Pokémon Type: {selected_type}")
    pokemon_list_head = kanto_pokemon.get_head_node()
    found = False
    while pokemon_list_head is not None:
        sublist = pokemon_list_head.get_value()  # Get the sublist (LinkedList)
        if sublist.get_head_node() and sublist.get_head_node().get_value()[0] == selected_type:
            found = True
            sublist_head = sublist.get_head_node()
            while sublist_head is not None:
                pokemon = sublist_head.get_value()
                print("--------------------------")
                print(f"Name: {pokemon[1]}")
                print(f"HP: {pokemon[2]}")
                print(f"Attack: {pokemon[3]}")
                print(f"Defense: {pokemon[4]}")
                print(f"Sp Attack: {pokemon[5]}")
                print(f"Sp Defense: {pokemon[6]}")
                print(f"Speed: {pokemon[7]}")
                print(f"Total: {pokemon[8]}")
                print(f"Location(s): {', '.join(pokemon[9])}")
                print("--------------------------\n")
                sublist_head = sublist_head.get_next_node()
        pokemon_list_head = pokemon_list_head.get_next_node()

    if not found:
        print(f"No Pokémon found for type {selected_type}.")

    # Ask user to search for other types
    repeat_question = input(
        "Would you like to search for other Pokémon types? (y/n) "
    ).lower()
    if repeat_question != 'y':
        break
