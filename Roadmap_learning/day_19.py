""" Day 19: Working with Files (Read/Write) """

# with open("sample.txt", "a") as f:
#     f.write("\nHello File times 6" * 2)  

# print("File written successfully.")


with open("sample.txt", "rb") as f:
    content = f.read()
    print(content)  # Output: Hello File

# # ============================================================================
# # SECTION 2: FILE OPERATIONS
# # ============================================================================
# print("\n=== FILE OPERATIONS ===")  
# # Open a file for writing (creates if not exists)
# with open("example.txt", "w") as file:
#     file.write("This is an example file.\n")
#     file.write("It contains multiple lines.\n") 
# # Open a file for reading
# with open("example.txt", "r") as file:
#     content = file.read()
#     print("File content:")
#     print(content)  # Output: This is an example file.\nIt contains multiple lines.\n



# open("Name of the file", "mode")
# # Modes:
# # "r" - Read (default)
# # "w" - Write (creates file if not exists, truncates if exists)
# # "a" - Append (creates file if not exists, appends to end if exists)
# # "b" - Binary mode (e.g., "rb", "wb")