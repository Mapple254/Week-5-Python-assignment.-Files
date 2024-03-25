try:
    with open("my_file.txt", "w") as file:
        file.write("My name is Paul Muguro\n")
        file.write("07546788948\n")
        file.write("Python file handling is fun! I love it. Can't wait to get it all in.\n")
    print("File created and initial content written successfully.")
    with open("my_file.txt", "a") as file:    
        file.write("Paul was born in Kenya and he loves it here.\n")
        file.write("030897\n")
        file.write("Well, I've heard of Appending but I sure can't explain it. Lol!\n")
    print("Additional content appended successfully.")
    with open("my_file.txt", "r") as file:     
        contents = file.read()
        print("Contents of my_file.txt:")
        print(contents)
except FileNotFoundError:
    print("File not found. Please ensure the file path is correct.")
except PermissionError:
    print("Permission denied. Please check file permissions.")
finally:
    print("File handling process completed.")
