import matplotlib.pyplot as plt

def read_csv(file_name):
    data = []
    try:
        with open(file_name, 'r') as file:
            next(file)  # Skip header
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    try:
                        sensor_id, temperature, _, status = parts
                        data.append((float(temperature), status))
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f"File {file_name} not found. Skipping.")
    return data

def plot_temperature_trends():
    sensor_files = {
        "Thermoresistive": "thermoresistive_log.csv",
        "Thermoelectric": "thermoelectric_log.csv",
        "Thermo-Optical": "thermo_optical_log.csv",
        "Thermo-Acoustic": "thermo_acoustic_log.csv"
    }
    
    plt.figure(figsize=(12, 6))
    
    legend_labels = set()  # Track added labels

    for sensor_name, file_name in sensor_files.items():
        data = read_csv(file_name)
        if not data:
            continue
        
        time_index = list(range(len(data)))
        temperatures = [temp for temp, _ in data]
        statuses = [status for _, status in data]
        
        # Plot main temperature trend
        plt.plot(time_index, temperatures, label=sensor_name)
        
        # Identify Fan On / Heater On points
        fan_on = [(time_index[i], temperatures[i]) for i, status in enumerate(statuses) if status == 'Fan On']
        heater_on = [(time_index[i], temperatures[i]) for i, status in enumerate(statuses) if status == 'Heater On']
        
        # Scatter plot for Fan On
        if fan_on:
            x_fan, y_fan = zip(*fan_on)
            label_fan = f'Fan On ({sensor_name})' if f'Fan On ({sensor_name})' not in legend_labels else None
            plt.scatter(x_fan, y_fan, color='red', label=label_fan, s=10)
            legend_labels.add(f'Fan On ({sensor_name})')

        # Scatter plot for Heater On
        if heater_on:
            x_heater, y_heater = zip(*heater_on)
            label_heater = f'Heater On ({sensor_name})' if f'Heater On ({sensor_name})' not in legend_labels else None
            plt.scatter(x_heater, y_heater, color='blue', label=label_heater, s=10)
            legend_labels.add(f'Heater On ({sensor_name})')

    plt.xlabel("Time (Index)")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Trends from Different Sensors")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot_temperature_trends()
