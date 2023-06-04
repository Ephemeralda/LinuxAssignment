import subprocess
import time
import matplotlib.pyplot as plt

def generate_data(num_records):
    start_time = time.time()
    subprocess.run(['./generate-dataset.sh', 'dataset.txt', str(num_records)])
    end_time = time.time()
    return end_time - start_time

def sort_data(filename):
    start_time = time.time()
    subprocess.run(['./sort-data.sh', filename])
    end_time = time.time()
    return end_time - start_time

num_records_list = [1000, 100000, 10000000]
generate_time_list = []
sort_time_list = []

for num_records in num_records_list:
    generate_time = generate_data(num_records)
    sort_time = sort_data('dataset.txt')
    generate_time_list.append(generate_time)
    sort_time_list.append(sort_time)

# Plotting the graph
plt.plot(num_records_list, generate_time_list, label='Generate Time')
plt.plot(num_records_list, sort_time_list, label='Sort Time')
plt.xlabel('Number of Records')
plt.ylabel('Time (seconds)')
plt.title('Time Taken to Generate and Sort Data')
plt.legend()
plt.show()
