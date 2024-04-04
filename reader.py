import csv

# Adjust the file path below to point to your actual CSV file
file_path = '/Users/zachjohnson/Desktop/Kindle /The St_ Gallen Mafia_ Exposing the Secret Reformist Group Within the Church-Notebook.csv'

try:
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        sample = csvfile.read(2048)
        csvfile.seek(0)
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(sample)
        has_header = sniffer.has_header(sample)
        reader = csv.reader(csvfile, dialect)
        
        # If the file has a header, extract it. Otherwise, assume the first row is data.
        if has_header:
            headers = next(reader)
            print(f"Detected headers: {headers}")
            annotation_index = headers.index('Annotation') if 'Annotation' in headers else -1
        else:
            print("No headers detected, assuming fixed column order.")
            annotation_index = 3  # 'Annotation' is the fourth column
        for row in reader:
            if annotation_index >= 0:
                print(row[annotation_index].strip())
            else:
                print("No 'Annotation' column found. Please check the CSV format.")
except Exception as e:
    print(f"An error occurred: {e}")
