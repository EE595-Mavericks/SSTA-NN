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
    mux = 0.0
    varx = random.uniform(0, 1)
    muy = random.uniform(0, 1)
    vary = random.uniform(0, 1)
    return mux, varx, muy, vary

def main():
    #n = input("How many test cases you want")

    if os.path.isfile('result_Num.txt'):
        os.remove('result_Num.txt')
    if os.path.isfile('result_Week1.txt'):
        os.remove('result_Week1.txt')

    for x in range(100):
        mux, varx, muy, vary = generate_test()
        result1 = subprocess.run(['../build/normal_rv_num_test', str(mux), str(varx), str(muy), str(vary)], stdout=subprocess.PIPE)
        #subprocess.call(["python", "/Users/paradox/vscode/Normal-RVs/tests/normal_rv_test.py", str(mux), str(varx), str(muy), str(vary)])
        # result2 = subprocess.call(
        #     ["python", "normal_rv_test.py", str(mux), str(varx), str(muy),
        #      str(vary)])
        #print(result.stdout.decode())

        result2 = subprocess.run(['../week1/normal_rv_max', str(mux), str(varx), str(muy), str(vary)], stdout=subprocess.PIPE)


        with open("result_Num.txt", "a") as f:
            f.write(result1.stdout.decode())

        with open("result_Week1.txt", "a") as f:
            f.write(result2.stdout.decode())

    #result = subprocess.run(['/Users/paradox/vscode/595hw/compute', "1", "1", "1", "1"], stdout=subprocess.PIPE)

    Num_mean = []
    Num_var = []
    Num_skew = []
    MC_mean = []
    MC_var = []
    MC_skew= []

    f_Num = open('result_Week1.txt', 'r')
    lines = f_Num.read().splitlines()
    f_Num.close()
    for line in lines:
        Num_mean.append(line.split(' ')[4])
        Num_var.append(line.split(' ')[5])
        #Num_skew.append(line.split(' ')[6])

    f_Num = open('result_Num.txt', 'r')
    lines = f_Num.read().splitlines()
    f_Num.close()
    for line in lines:
        MC_mean.append(line.split(' ')[4])
        MC_var.append(line.split(' ')[5])
        # MC_skew.append(line.split(' ')[6])

    # error_mean = get_error(Num_mean, MC_mean)
    # error_var = get_error(Num_var, MC_var)
    # #error_skew = get_error(Num_skew, MC_skew)
    #
    # with open("output.txt", "w") as file:
    #     for x, y, z, a, b, c in zip(Num_mean, MC_mean, Num_var, MC_var, Num_skew, MC_skew):
    #         file.write(str(x) + " " + str(y) + "     " + str(z) + " " + str(a) + "     " + str(b) + " " + str(c) + "\n")
    #
    #     file.write("Error for means:" + str(error_mean) + "\n")
    #     file.write("Error for vars:" + str(error_var) + "\n")
    #     #file.write("Error for skews:" + str(error_skew) + "\n")
    #
    # print(Num_skew)


if __name__ == "__main__":
    main()