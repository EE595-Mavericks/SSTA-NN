import csv
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

    rows = []
    while len(rows) < 10000:
        mux, varx, muy, vary = generate_test()
        result1 = subprocess.run(['../build/normal_rv_num_test', str(mux), str(varx), str(muy), str(vary)], stdout=subprocess.PIPE)

        row = list(range(7))
        output = result1.stdout.decode().split(' ')
        row[0], row[1], row[2], row[3] = mux, varx, muy, vary
        row[4] = round(float(output[4]), 10)
        row[5] = round(float(output[5]), 10)
        row[6] = round(float(output[6]), 10)

        # print(result1.stdout.decode())
        if row[6] < 1e-3:
            continue

        rows.append(row)

    with open('generate_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        for row in rows:
            writer.writerow(row)

        # with open("generate_data.csv", "a") as f:
        #     f.write(result1.stdout.decode())

    #result = subprocess.run(['/Users/paradox/vscode/595hw/compute', "1", "1", "1", "1"], stdout=subprocess.PIPE)



if __name__ == "__main__":
    main()