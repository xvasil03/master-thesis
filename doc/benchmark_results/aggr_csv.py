
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
output_rows_cnt = int(sys.argv[3])

input_rows_cnt = 0
for row in open(input_file):
    input_rows_cnt += 1

agg_batch_size = int(input_rows_cnt / output_rows_cnt)
print("agg batch size:{}".format(agg_batch_size))

with open(input_file) as input:
    with open(output_file, "w") as output:
        input_reader = csv.reader(input, delimiter=' ')
        output_writer = csv.writer(output, delimiter=' ')
        # header
        output_writer.writerow(["row", "ram", "cpu"])
        output_row_id = 1
        ram_agg = 0.0
        cpu_agg = 0.0
        row_count = 0
        for row in input_reader:
            row_count += 1
            if row_count == 1:
                continue
            ram_agg += float(row[1])
            cpu_agg += float(row[2])
            if row_count % agg_batch_size == 0:
                ram_agg = '{:.2f}'.format(ram_agg / float(agg_batch_size))
                cpu_agg = '{:.2f}'.format(cpu_agg / float(agg_batch_size))
                output_writer.writerow([output_row_id, ram_agg, cpu_agg])
                ram_agg = 0.0
                cpu_agg = 0.0
                output_row_id += 1
