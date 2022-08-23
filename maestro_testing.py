import os
from multiprocessing import Pool
# import printing1, printing2, printing3

processes = ("printing1.py", "printing2.py", "printing3.py")


def run_process(process):
    print("In run_process()")
    os.system('python {}'.format(process))

if __name__ == '__main__':
    print("Running maestro main")
    with Pool(processes=4) as pool:
        print("In pool")
        try:
            pool.map(run_process, processes)
        except Exception as excpt:
            print(excpt)