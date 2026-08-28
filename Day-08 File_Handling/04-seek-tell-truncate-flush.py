# seek() — Move file pointer
#seek() file pointer ko kisi specific position par move karta hai.
file = open("rahul.txt", "r")
content = file.read()
#print(content)
file.seek(7)          # pointer ko position 7 par le jao
content = file.read() # position 7 se aage read karo
print(content)
file.close()

# tell() — Check file pointer position
# tell() batata hai ki file pointer currently kis position par hai.
file = open("readme.txt", "r")
print(file.tell())  # tell() returns the current position of the file pointer
content = file.read(5)  # Read the first 5 characters
print(content)
print(file.tell())  # Check the current file pointer position
file.close()


# truncate() — Reduce file content
# truncate() file ko specified size tak truncate karta hai.
file = open("readme.txt", "r+")  # Open the file in read and write mode ("r+")
file.truncate(10)  # truncate() keeps only the first 10 bytes/characters of the file
file.close()  

# flush() — Force buffered data to file
# flush() memory buffer mein jo data pending hai usko file par write karne ke liye force karta hai.
file = open("readme.txt", "w")
file.write("Hello Python")  # Write content into the file buffer
file.flush()  # Force the buffered content to be written to the file
file.close() 
