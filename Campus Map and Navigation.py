import webbrowser

# Class to manage campus map and navigation
class CampusMap:
    def __init__(self):
        # Predefined campus locations
        self.locations = {
            "Library": "https://maps.app.goo.gl/AW5nvbvaaiL9CNhD8",
            "Volley Ball Court": "https://maps.app.goo.gl/i7j7cwUcLooVtZiVA",
            "Main Building": "https://maps.app.goo.gl/gHzyhpKhfkv159yx9",
            "Mechanical Workshop": "https://maps.app.goo.gl/MeFVwzJRQq2FRNAu5",
            "Electrical Department": "https://maps.app.goo.gl/5qu4XjKhuy9Dmz789",
            "ATM":"https://maps.app.goo.gl/y4o4KEpawUEd2RwG8",
            "Hostel": "https://maps.app.goo.gl/PMbpHb76udsx2joA6"
        }

    # Add a new location
    def add_location(self):
        name = input("Enter the name of the location: ")
        url = input(f"Enter the Google Maps URL for {name}: ")
        self.locations[name] = url
        print(f"Location '{name}' added successfully!")

    # View all available locations
    def view_locations(self):
        if not self.locations:
            print("No locations available.")
        else:
            print("\nAvailable Locations:")
            for idx, (location, url) in enumerate(self.locations.items(), 1):
                print(f"{idx}. {location} - {url}")

    # Open a location in Google Maps
    def open_location(self):
        if not self.locations:
            print("No locations available to navigate to.")
        else:
            self.view_locations()
            choice = int(input("Enter the number of the location to open: "))
            if 0 < choice <= len(self.locations):
                location_name = list(self.locations.keys())[choice - 1]
                print(f"Opening Google Maps for {location_name}...")
                webbrowser.open(self.locations[location_name])
            else:
                print("Invalid choice!")

    # Remove a location
    def remove_location(self):
        if not self.locations:
            print("No locations available to remove.")
        else:
            self.view_locations()
            choice = int(input("Enter the number of the location to remove: "))
            if 0 < choice <= len(self.locations):
                location_name = list(self.locations.keys())[choice - 1]
                del self.locations[location_name]
                print(f"Location '{location_name}' removed successfully!")
            else:
                print("Invalid choice.")

# Main menu for the campus map navigation tool
def main_menu():
    campus_map = CampusMap()

    while True:
        print("\n--- Campus Map and Navigation ---")
        print("1. Open Location in Google Maps")
        print("2. Add a new Location")
        print("3. Remove a Location")
        print("4. View all the Locations")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '2':
            campus_map.add_location()
        elif choice == '4':
            campus_map.view_locations()
        elif choice == '1':
            campus_map.open_location()
        elif choice == '3':
            campus_map.remove_location()
        elif choice == '5':
            print("Exiting Campus Map and Navigation. Safe travels!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
