import json
import os


class VedaTechnology:

    def __init__(self):
        self.filename = "veda_data.json"

        self.data = {
            "programs": [],
            "services": [],
            "training": [],
            "internships": [],
            "customers": [],
            "inquiries": [],
            "requests": []
        }

        self.load_data()

    # Load data from JSON file
    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    self.data = json.load(file)
            except (json.JSONDecodeError, OSError):
                print("Error loading file. Starting with empty data.")

    # Save data into JSON file
    def save_data(self):
        try:
            with open(self.filename, "w") as file:
                json.dump(self.data, file, indent=4)
        except OSError:
            print("Error saving data.")

    # Add a new record
    def add_record(self, category):
        try:
            name = input("Enter name/title: ").strip()
            if not name:
                raise ValueError("Name cannot be empty.")

            description = input("Enter description: ").strip()
            status = "Active"

            record = {
                "id": len(self.data[category]) + 1,
                "name": name,
                "description": description,
                "status": status
            }

            self.data[category].append(record)
            self.save_data()

            print("Record added successfully!")

        except ValueError as e:
            print("Invalid input:", e)

    # Display records
    def display_records(self, category):
        records = self.data[category]

        if not records:
            print("No records found.")
            return

        print("\n---", category.upper(), "---")

        for record in records:
            print("\nID:", record["id"])
            print("Name:", record["name"])
            print("Description:", record["description"])
            print("Status:", record["status"])

    # Search records
    def search_records(self, category):
        keyword = input("Enter name or keyword to search: ").strip().lower()

        if not keyword:
            print("Search keyword cannot be empty.")
            return

        found = False

        for record in self.data[category]:
            if (keyword in record["name"].lower()
                    or keyword in record["description"].lower()
                    or keyword in record["status"].lower()):

                print("\nID:", record["id"])
                print("Name:", record["name"])
                print("Description:", record["description"])
                print("Status:", record["status"])
                found = True

        if not found:
            print("No matching records found.")

    # Filter records by status
    def filter_records(self, category):
        status = input("Enter status to filter (Active/Completed/Pending): ").strip().lower()

        found = False

        for record in self.data[category]:
            if record["status"].lower() == status:
                print(record)
                found = True

        if not found:
            print("No records found with this status.")

    # Update record status
    def update_status(self, category):
        try:
            record_id = int(input("Enter record ID: "))

            for record in self.data[category]:
                if record["id"] == record_id:
                    new_status = input("Enter new status: ").strip()

                    if not new_status:
                        raise ValueError("Status cannot be empty.")

                    record["status"] = new_status
                    self.save_data()

                    print("Status updated successfully!")
                    return

            print("Record not found.")

        except ValueError as e:
            print("Invalid input:", e)

    # Main menu
    def menu(self):

        categories = {
            "1": "programs",
            "2": "services",
            "3": "training",
            "4": "internships",
            "5": "customers",
            "6": "inquiries",
            "7": "requests"
        }

        while True:

            print("\n================================")
            print(" VEDA TECHNOLOGY MANAGEMENT")
            print("================================")
            print("1. Technology Programs")
            print("2. Digital Services")
            print("3. Training Programs")
            print("4. Internship Programs")
            print("5. Customers")
            print("6. Customer Inquiries")
            print("7. Service Requests")
            print("8. Exit")

            choice = input("\nSelect category: ").strip()

            if choice == "8":
                print("Thank you for using Veda Technology!")
                break

            if choice not in categories:
                print("Invalid choice. Try again.")
                continue

            category = categories[choice]

            while True:

                print("\n---", category.upper(), "MENU ---")
                print("1. Add Record")
                print("2. Display Records")
                print("3. Search Records")
                print("4. Filter by Status")
                print("5. Update Status")
                print("6. Back to Main Menu")

                option = input("Enter your choice: ").strip()

                if option == "1":
                    self.add_record(category)

                elif option == "2":
                    self.display_records(category)

                elif option == "3":
                    self.search_records(category)

                elif option == "4":
                    self.filter_records(category)

                elif option == "5":
                    self.update_status(category)

                elif option == "6":
                    break

                else:
                    print("Invalid option. Please try again.")


# Run application
if __name__ == "__main__":

    app = VedaTechnology()

    # Add sample data for first-time execution
    if not any(app.data.values()):

        app.data["programs"].append({
            "id": 1,
            "name": "AI Development",
            "description": "Artificial Intelligence solutions",
            "status": "Active"
        })

        app.data["services"].append({
            "id": 1,
            "name": "Web Development",
            "description": "Website design and development",
            "status": "Active"
        })

        app.data["training"].append({
            "id": 1,
            "name": "Python Training",
            "description": "Python programming course",
            "status": "Active"
        })

        app.data["internships"].append({
            "id": 1,
            "name": "Software Internship",
            "description": "Practical software development training",
            "status": "Active"
        })

        app.data["customers"].append({
            "id": 1,
            "name": "Rahul",
            "description": "Customer interested in web development",
            "status": "Active"
        })

        app.data["inquiries"].append({
            "id": 1,
            "name": "Course Inquiry",
            "description": "Inquiry about Python training",
            "status": "Pending"
        })

        app.data["requests"].append({
            "id": 1,
            "name": "Website Support",
            "description": "Customer requested website maintenance",
            "status": "Pending"
        })

        app.save_data()

    app.menu()
