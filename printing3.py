import time

print("In script 3")
# def main1():
#     print("I am in script 3")
#     for i in range(3):
#         print(f"Script 3: Index {i}")


# def main2():
if __name__ == '__main__':
    with open('printing1.txt', 'a') as file:
        for i in range(5):
            print(f"Script 3: {i}\n")
            file.write(f"Script 3: {i}\n")
            time.sleep(1)
        print("EOF Script 3\n")
        file.write("EOF Script 3\n")

# if __name__ == '__main__':
#     print("I am in script 3")
#     for i in range(200):
#         print(f"Script 3: Index {i}")

# main()
