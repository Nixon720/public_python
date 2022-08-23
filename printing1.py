import subprocess
import time
print("In script 1")

# def main1():
#     print("I am in script 1")
#     for i in range(3):
#         print(f"Script 1: Index {i}")
#         time.sleep(1)

# def main2():
if __name__ == '__main__':
    with open('printing1.txt', 'a') as file:
        for i in range(15):
            print(f"Script 1: {i}\n")
            file.write(f"Script 1: {i}\n")
        print("EOF Script 1\n")
        file.write("EOF Script 1\n")


# if __name__ == '__main__':
#     print("I am in script 1")
#     for i in range(1000):
#         print(f"Script 1: Index {i}")
# main()

# subprocess.run(["dir"], shell=True)
