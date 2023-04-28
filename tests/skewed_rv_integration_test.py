import subprocess
import random
import csv

def generate_test():
    mux = 0.0
    varx = random.uniform(0, 1)
    skx = random.uniform(-0.99, 0.99)
    muy = random.uniform(0, 1)
    vary = random.uniform(0, 1)
    sky = random.uniform(-0.99, 0.99)
    return mux, varx, skx, muy, vary, sky


if __name__ == "__main__":
    rows = []

    for x in range(5100):
        row = list(range(9))
        mux, varx, skx, muy, vary, sky= generate_test()
        result1 = subprocess.run(['../build/skewed_rv_test', str(mux), str(varx), str(skx), str(muy), str(vary), str(sky),], stdout=subprocess.PIPE)
        output = result1.stdout.decode().split(' ')
        row[0] = float(output[0])
        row[1] = float(output[1])
        row[2] = float(output[2])
        row[3] = float(output[3])
        row[4] = float(output[4])
        row[5] = float(output[5])
        row[6] = float(output[6])
        row[7] = float(output[7])
        row[8] = float(output[8])
        if abs(row[8]) < 0.001 or row[7] < 0.001:
            continue
        rows.append(row)
    
    with open('../build/skewed_dataset.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([
                         'X_mean', 'X_variance', 'X_skewness', 
                         'Y_mean', 'Y_variance', 'Y_skewness',
                         'Z_mean', 'Z_variance', 'Z_skewness'])
        
        for row in rows:
            writer.writerow(row)