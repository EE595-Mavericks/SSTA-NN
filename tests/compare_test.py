import subprocess
import random
from math import fabs
import csv

def get_error(num, mc) -> float:
    sum_num = 0
    sum_mc = 0
    for i in range(10):
        sum_mc += float(mc[i])
        sum_num += float(num[i])
    return (sum_num - sum_mc) / sum_mc

def generate_test():
    #pairs = [(random.randint(1, 100), random.randint(1, 100)) for i in range(n)]
    mux = random.uniform(0, 10)
    varx = random.uniform(0, 100)
    muy = random.uniform(0, 10)
    vary = random.uniform(0, 100)
    return mux, varx, muy, vary

def main():

    rows = []

    for x in range(100):
        mux, varx, muy, vary = generate_test()
        result1 = subprocess.run(['../build/normal_rv_num_test', str(mux), str(varx), str(muy), str(vary)], stdout=subprocess.PIPE)
        #subprocess.call(["python", "/Users/paradox/vscode/Normal-RVs/tests/normal_rv_test.py", str(mux), str(varx), str(muy), str(vary)])
        row = list(range(10))
        output_first = result1.stdout.decode().split(' ')
        row[0], row[1], row[2], row[3] = mux, varx, muy, vary
        row[4] = round(float(output_first[0]), 10)
        row[5] = round(float(output_first[1]), 10)

        result2 = subprocess.check_output(
            ["python3", "normal_rv_test.py", str(mux), str(varx), str(muy),
             str(vary)])
        output_second = result2.strip().decode('utf-8').split(' ')
        row[6] = round(float(output_second[0]), 10)
        row[7] = round(float(output_second[1]), 10)
        row[8] = '{:.10%}'.format(fabs((row[6] - row[4]) / row[6]))
        row[9] = '{:.10%}'.format(fabs((row[7] - row[5]) / row[7]))

        rows.append(row)

    with open('normal_mc_test.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['x_mean', 'x_var', 'y_mean',
                         'y_var', 'z1_mean', 'z1_var',
                         'z2_mean', 'z2_var', 'mean error', 'var error'])
        for row in rows:
            writer.writerow(row)
    #result = subprocess.run(['/Users/paradox/vscode/595hw/compute', "1", "1", "1", "1"], stdout=subprocess.PIPE)

    # Num_mean = []
    # Num_var = []
    # Num_skew = []
    # MC_mean = []
    # MC_var = []
    # MC_skew= []
    #
    # f_Num = open('result_Num.txt', 'r')
    # lines = f_Num.read().splitlines()
    # f_Num.close()
    # for line in lines:
    #     Num_mean.append(line.split(' ')[4])
    #     Num_var.append(line.split(' ')[5])
    #     Num_skew.append(line.split(' ')[6])
    #
    # f_Num = open('result_MC.txt', 'r')
    # lines = f_Num.read().splitlines()
    # f_Num.close()
    # for line in lines:
    #     MC_mean.append(line.split(' ')[4])
    #     MC_var.append(line.split(' ')[5])
    #     MC_skew.append(line.split(' ')[6])
    #
    # error_mean = get_error(Num_mean, MC_mean)
    # error_var = get_error(Num_var, MC_var)
    # error_skew = get_error(Num_skew, MC_skew)
    #
    # with open("output.txt", "w") as file:
    #     for x, y, z, a, b, c in zip(Num_mean, MC_mean, Num_var, MC_var, Num_skew, MC_skew):
    #         file.write(str(x) + " " + str(y) + "     " + str(z) + " " + str(a) + "     " + str(b) + " " + str(c) + "\n")
    #
    #     file.write("Error for means:" + str(error_mean) + "\n")
    #     file.write("Error for vars:" + str(error_var) + "\n")
    #     file.write("Error for skews:" + str(error_skew) + "\n")
    #
    # print(Num_skew)


if __name__ == "__main__":
    main()