filename = input("Enter log file name (for example, sample_log.txt): ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    print("\n--- Log File Contents ---")
    for line in lines:
        print(line, end="")

    print("\nTotal log entries/lines:", len(lines))

    error_lines = [line.strip() for line in lines if "ERROR" in line.upper()]
    print("\nNumber of error entries:", len(error_lines))
    if error_lines:
        print("Error entries:")
        for line in error_lines:
            print(line)
except FileNotFoundError:
    print("File not found. Check the file name and try again.")