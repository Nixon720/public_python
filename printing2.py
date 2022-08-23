import time
print("In script 2")

# def main1():
#     print("I am in script 2")
#     for i in range(5):
#         print(f"Script 2: Index {i}")
#         time.sleep(2)

# def main2():
if __name__ == '__main__':
    with open('printing1.txt', 'a') as file:
        for i in range(10):
            print(f"Script 2: {i}\n")
            file.write(f"Script 2: {i}\n")
        print("EOF Script 2\n")
        file.write("EOF Script 2\n")


# if __name__ == '__main__':
#     print("I am in script 2")
#     for i in range(200):
#         print(f"Script 2: Index {i}")

# main()
