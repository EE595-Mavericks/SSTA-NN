import subprocess
import random
import csv

def generate_test():
    #pairs = [(random.randint(1, 100), random.randint(1, 100)) for i in range(n)]
    # mux = random.uniform(0, 100)
    mux = 0.0
    varx = random.uniform(0, 100)
    skx = random.uniform(-1, 1)
    muy = random.uniform(0, 5)
    vary = random.uniform(0, 100)
    sky = random.uniform(-1, 1)
    return mux, varx, skx, muy, vary, sky


if __name__ == "__main__":
    rows = []

    for x in range(100):
        row = list(range(10))
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
        row[9] = float(output[9])
        rows.append(row)
    
    with open('../build/skewed_pdf_integral.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['integral', 
                         'x_mean', 'x_variance', 'x_skewness', 
                         'y_mean', 'y_variance', 'y_skewness',
                         'z_mean', 'z_variance', 'z_skewness'])
        
        for row in rows:
            writer.writerow(row)