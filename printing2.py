import time


# def main1():
#     print("I am in script 2")
#     for i in range(5):
#         print(f"Script 2: Index {i}")
#         time.sleep(2)

def main2():
    with open('printing1.txt', 'a') as file:
        for i in range(10):
            file.write(f"Script 2: {i}")
    file.write("EOF Script 2")


# if __name__ == '__main__':
#     print("I am in script 2")
#     for i in range(200):
#         print(f"Script 2: Index {i}")

# main()
print("In script 2")