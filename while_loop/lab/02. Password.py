username = input()
password = input()
insert_password = input()
while insert_password != password:
    insert_password = input()
print(f"Welcome {username}!")
