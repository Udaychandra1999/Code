def check_passwords(passwords):
    for i in range(len(passwords)):
        for j in range(i + 1, len(passwords)):
            if passwords[i].startswith(passwords[j]) or passwords[j].startswith(passwords[i]):
                print("BAD PASSWORD")
                return

    print("GOOD PASSWORD")

passwords = input().split()
check_passwords(passwords)