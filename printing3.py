# def main1():
#     print("I am in script 3")
#     for i in range(3):
#         print(f"Script 3: Index {i}")
import time


def main2():
    with open('printing1.txt', 'a') as file:
        for i in range(5):
            file.write(f"Script 3: {i}")
            time.sleep(1)
    file.write("EOF Script 3")

# if __name__ == '__main__':
#     print("I am in script 3")
#     for i in range(200):
#         print(f"Script 3: Index {i}")

# main()

print("In script 3")