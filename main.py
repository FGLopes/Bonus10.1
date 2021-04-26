with open("intel.csv", 'r') as intel_file:
    content = intel_file.read().splitlines()

    for row in content:
        row_data = row.split(",")
        print(f"{row_data[0]} tem {row_data[1]} anos e vem de {row_data[2]}")