import os

def extract_errors(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' not found.")
        return
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if 'INFO' in line:
                outfile.write(line)
            
        
if __name__ == "__main__":
    extract_errors('system.log', 'info.log')