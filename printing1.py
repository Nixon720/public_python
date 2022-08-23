import subprocess
import time


# def main1():
#     print("I am in script 1")
#     for i in range(3):
#         print(f"Script 1: Index {i}")
#         time.sleep(1)

def main2():
    with open('printing1.txt', 'a') as file:
        for i in range(15):
            file.write(f"Script 1: {i}")
    file.write("EOF Script 1")


# if __name__ == '__main__':
#     print("I am in script 1")
#     for i in range(1000):
#         print(f"Script 1: Index {i}")
# main()
print("In script 1")
# subprocess.run(["dir"], shell=True)
