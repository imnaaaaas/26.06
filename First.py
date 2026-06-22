
file_lines =[]

with open("/home/imna/Documents/FirstCda/Files/file.txt" , "r") as folder_file:
    all_lines = folder_file.readlines()



for line in all_lines:
    clean_line = line.strip()
    if clean_line.startswith("# "):
        actual_text = clean_line[2:]
        parsed_line = f"<h1>{actual_text}</h1>"
    else:
        parsed_line = f"<h5>{clean_line}</h5>"
    file_lines.append(parsed_line)

final_html_content = "\n".join(file_lines)

with open("/home/imna/Documents/FirstCda/Files/First.html" , "w") as new_file:
    new_file.write(final_html_content) 

print("successfully converted to html")