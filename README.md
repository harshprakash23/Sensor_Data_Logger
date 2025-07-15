# Sensor Data Logger

This project simulates and logs data from four types of temperature sensors:

- **Thermoresistive (RTD/Thermistor)**
- **Thermoelectric (Thermocouple)**
- **Thermo-Optical (Infrared Sensor)**
- **Thermo-Acoustic (Ultrasonic-based)**

## Features
- Simulates 1200 readings for each sensor type.
- Logs data to CSV files for easy analysis.
- Provides operational status (Fan On, Heater On, Stable) based on temperature.
- User can select sensor type and years of operation.

## How to Build and Run
1. Ensure you have [MinGW](http://www.mingw.org/) or another GCC compiler installed.
2. Open the project folder in VS Code.
3. Build the project using the provided build task or run:
   ```sh
   gcc 22BCT0098_main.c -o 22BCT0098_main.exe
   ```
4. Run the executable:
   ```sh
   ./22BCT0098_main.exe
   ```
5. Follow the prompts to select sensor type and years of operation.

## Output
- The program generates the following CSV log files:
  - `thermoresistive_log.csv`
  - `thermoelectric_log.csv`
  - `thermo_optical_log.csv`
  - `thermo_acoustic_log.csv`
- Each file contains simulated sensor data and operational status.

## File Structure
- `22BCT0098_main.c` - Main program file
- `_22BCT0098_thermoresistive.h` - RTD/Thermistor calculations
- `_22BCT0098thermo_acoustic.h` - Ultrasonic sensor calculations
- `_22BCT0098thermoelectric.h` - Thermocouple calculations
- `_22BCT0098thermo_optical.h` - Infrared sensor calculations
- `*.csv` - Output log files

## Author
Harsh Prakash (22BCT0098)

---

For more details, see the code and generated CSV files.
