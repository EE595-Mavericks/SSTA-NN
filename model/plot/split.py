import pandas as pd
import os
import glob
import csv

if __name__ == "__main__":
    # Define the number of rows per file
    rows_per_file = 103

    folder_path = "../../epoch=300"
    file_pattern = '*.csv'

    # 获取当前文件夹下所有符合模式的文件路径
    file_paths = glob.glob(os.path.join(folder_path, file_pattern))

    # 从文件路径中提取文件名
    file_names = [os.path.basename(file_path) for file_path in file_paths]

    min_rows = []

    print(file_names)  # 输出文件名列表

    for file_name in file_names:
        print(file_name)
        data = pd.read_csv(folder_path + "/" + file_name)
        # Split the data frame and save each group to a separate CSV file
        for i, chunk in enumerate(data.groupby(data.index // rows_per_file)):
            # if i == 1:
            #     break
            structure = file_name.split('.')[0]

            act_func = chunk[1].iloc[1]["Epoch"]
            opti = chunk[1].iloc[1]["train error mean"]
            l_rate = chunk[1].iloc[1]["train error variance"]
            bch_size = chunk[1].iloc[1]["train error skewness"]

            min_index = chunk[1]["test error variance"].iloc[2:102].astype(float).idxmin() - i * 103
            print(min_index)
            print(len(chunk[1]))
            min_row = chunk[1].iloc[min_index].to_dict()
            min_row['Arch.'] = structure
            min_row['Opt.'] = opti
            min_row['Activation'] = act_func
            min_row['LR'] = l_rate
            min_row['Batch'] = bch_size

            print(min_row)
            min_rows.append(min_row)
            output_name = structure + '-' + opti + '-' + act_func + '-' + l_rate + '-' + bch_size
            chunk[1].to_csv(output_name + '.csv', index=False)

    header = ['Arch.', 'Opt.', 'Activation', 'LR', 'Batch', 'Epoch', 'train error mean', 'train error variance',
              'train error skewness', 'test error mean',
              'test error variance', 'test error skewness']

    with open("best.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for min_row in min_rows:
            tmp = []
            for name in header:
                tmp.append(min_row[name])
            writer.writerow(tmp)

        f.close()
