import csv
from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius


def convert_temperatures(input_file, output_file, target_unit):
    with open(input_file, 'r', encoding='utf-8-sig') as f_in, open(output_file, 'w', newline='', encoding='utf-8') as f_out:
        reader = csv.DictReader(f_in)
        writer = csv.DictWriter(f_out, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            temperature = float(row['Reading'][:-2])
            unit = row['Reading'][-2:]
            if unit == '°C' and target_unit == 'F':
                temperature = int(celsius_to_fahrenheit(temperature))
                row['Reading'] = f"{temperature}°F"
            elif unit == '°F' and target_unit == 'C':
                temperature = int(fahrenheit_to_celsius(temperature))
                row['Reading'] = f"{temperature}°C"
            writer.writerow(row)


convert_temperatures('data.csv', 'output.csv', 'F')
