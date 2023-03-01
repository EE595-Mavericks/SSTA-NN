import subprocess
import random
import os
import csv
from math import fabs

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
    mux = 0.0
    varx = random.uniform(10, 100)
    muy = random.uniform(0, 10)
    vary = random.uniform(0, 10)
    return mux, varx, muy, vary

def main():
    #n = input("How many test cases you want")

    if os.path.isfile('result_Num.txt'):
        os.remove('result_Num.txt')
    if os.path.isfile('normal_test.csv'):
        os.remove('normal_test.csv')

    rows = []

    for x in range(100):
        mux, varx, muy, vary = generate_test()
        result1 = subprocess.run(['../build/normal_rv_num_test', str(mux), str(varx), str(muy), str(vary)], stdout=subprocess.PIPE)
        row = list(range(14))
        output_first = result1.stdout.decode().split(' ')
        row[0], row[1], row[2], row[3] = mux, varx, muy, vary
        row[4] = round(float(output_first[0]), 10)
        row[5] = round(float(output_first[1]), 10)

        result2 = subprocess.run(['../week1/normal_rv_max', str(mux), str(varx), str(muy), str(vary)], stdout=subprocess.PIPE)
        output_second = result2.stdout.decode().split(' ')
        row[6] = round(float(output_second[0]), 10)
        row[7] = round(float(output_second[1]), 10)
        row[10] = '{:.10%}'.format(fabs((row[6] - row[4]) / row[6]))
        row[11] = '{:.10%}'.format(fabs((row[7] - row[5]) / row[7]))

        result3 = subprocess.check_output(
            ["python3", "normal_rv_test.py", str(mux), str(varx), str(muy),
             str(vary)])
        output_second = result3.strip().decode('utf-8').split(' ')
        row[8] = round(float(output_second[0]), 10)
        row[9] = round(float(output_second[1]), 10)
        row[12] = '{:.10%}'.format(fabs((row[8] - row[4]) / row[8]))
        row[13] = '{:.10%}'.format(fabs((row[9] - row[5]) / row[9]))

        rows.append(row)

    #result = subprocess.run(['/Users/paradox/vscode/595hw/compute', "1", "1", "1", "1"], stdout=subprocess.PIPE)


    with open('normal_total.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['x_mean', 'x_var', 'y_mean',
                         'y_var', 'zNum_mean', 'zNum_var',
                         'zAna_mean', 'zAna_var','zMC_mean','zMC_var',
                         'mean_error_Ana', 'var_error_Ana','mean_error_Mc', 'var_error_MC'])
        for row in rows:
            writer.writerow(row)

if __name__ == "__main__":
    main()