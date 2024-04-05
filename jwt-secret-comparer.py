import os
import hashlib
import hmac
import base64
from tqdm import tqdm

# Path of the folder containing the files
folder_path = "C:/tmp/pruebas"

jwt = input("Enter the JWT token:\r\n")
jwt_cleaned = jwt.strip()

header, payload, signature = jwt_cleaned.split('.')

file_list = os.listdir(folder_path)

match_found = False

# Iterate over each file in the list
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    # Check if the element is a file
    if os.path.isfile(file_path):
        print(f"Searching in file: {file_name}")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                # Get the number of lines in the file
                total_lines = sum(1 for _ in file)
                file.seek(0)
                # Create the progress bar
                progress_bar = tqdm(total=total_lines, desc="Progress", unit=" word")
                
                for line in file:
                    secret = line.strip().encode('utf-8')
                    
                    # Concatenate the header, payload, and period to calculate the HMAC-SHA256 signature
                    data = (header + '.' + payload).encode('utf-8')
                    
                    # Generate the HMAC-SHA256 signature
                    generated_signature = hmac.new(secret, msg=data, digestmod=hashlib.sha256).digest()
                    
                    # Check if the generated signature matches the original signature of the JWT token
                    if base64.urlsafe_b64encode(generated_signature).decode().rstrip('=') == signature:
                        progress_bar.close()
                        print("\r\n")
                        print("The generated signature matches the original signature of the JWT token.")
                        print("JWT: " + jwt_cleaned)
                        print("\033[1m" + "Secret: " + line.strip() + "\033[0m")  # Print in bold
                        print("\r\n")
                        match_found = True
                        break
                    progress_bar.update(1)  # Increment the progress bar
                
                progress_bar.close()
            
            if match_found:
                break
        
        except UnicodeDecodeError as e:
            print(f"Error decoding file {file_name}: {e}")
            continue  # Move to the next file if a decoding error occurs

if not match_found:
    print("\r\n")
    print("No match found in any file.")
    print("\r\n")
