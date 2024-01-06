import os

os.chdir("../Datasets")
json_file_path = os.path.join(os.getcwd(), "Digital_Music.json")
n = 150_000
suffix = str(n//1000) + "k"
output_file_path = json_file_path[:-5] + "_" + suffix + ".json"

with open(json_file_path, 'r') as input_file:
    with open(output_file_path, 'w') as output_file:
        for i in range(n):
            # BE SURE THAT EACH OBJECT OCCUPIES *EXACTLY* ONE LINE
            output_file.write(input_file.readline())
