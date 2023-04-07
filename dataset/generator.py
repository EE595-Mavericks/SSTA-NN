import subprocess
import random
import os

def get_error(num, mc) -> float:
    sum_num = 0
    sum_mc = 0
    for i in range(10):
        sum_mc += float(mc[i])
        sum_num += float(num[i])
    return (sum_num - sum_mc) / sum_mc

def generate_test():
    #pairs = [(random.randint(1, 100), random.randint(1, 100)) for i in range(n)]
    # mux = random.uniform(0, 100)
    mux = random.uniform(0, 1)
    varx = random.uniform(0, 1)
    muy = random.uniform(0, 1)
    vary = random.uniform(0, 1)
    return mux, varx, muy, vary

def main():
    #n = input("How many test cases you want")

    if os.path.isfile('generate_data.csv'):
        os.remove('generate_data.csv')

    for x in range(5000):
        mux, varx, muy, vary = generate_test()
        result1 = subprocess.run(['../build/normal_rv_num_test', str(mux), str(varx), str(muy), str(vary)], stdout=subprocess.PIPE)


        with open("generate_data.csv", "a") as f:
            f.write(result1.stdout.decode())

    #result = subprocess.run(['/Users/paradox/vscode/595hw/compute', "1", "1", "1", "1"], stdout=subprocess.PIPE)



if __name__ == "__main__":
    main()