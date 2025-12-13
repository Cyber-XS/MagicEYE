import magic

print(r"""
 __       __                      __            ________                    
|  \     /  \                    |  \          |        \                   
| $$\   /  $$  ______    ______   \$$  _______ | $$$$$$$$__    __   ______  
| $$$\ /  $$$ |      \  /      \ |  \ /       \| $$__   |  \  |  \ /      \ 
| $$$$\  $$$$  \$$$$$$\|  $$$$$$\| $$|  $$$$$$$| $$  \  | $$  | $$|  $$$$$$\
| $$\$$ $$ $$ /      $$| $$  | $$| $$| $$      | $$$$$  | $$  | $$| $$    $$
| $$ \$$$| $$|  $$$$$$$| $$__| $$| $$| $$_____ | $$_____| $$__/ $$| $$$$$$$$
| $$  \$ | $$ \$$    $$ \$$    $$| $$ \$$     \| $$     \\$$    $$ \$$     \
 \$$      \$$  \$$$$$$$ _\$$$$$$$ \$$  \$$$$$$$ \$$$$$$$$_\$$$$$$$  \$$$$$$$
                       |  \__| $$                       |  \__| $$          
                        \$$    $$                        \$$    $$          
                         \$$$$$$                          \$$$$$$  

          The Hidden File Type Revealer
""")

print("Welcome to MagicEye 🧙‍♂️👁️\n")
print("MagicEye reveals the TRUE type of any file, beyond deceptive extensions!\n")

def identify_file_type(file_path):
    try:
        file_magic = magic.Magic(mime=True, uncompress=True)
        mime_type = file_magic.from_file(file_path.strip())
        
        print(f"✓ Detected: The file '{file_path}' is a → {mime_type.upper()}")

    except FileNotFoundError:
        print(f"✗ Error: File not found!\n   '{file_path}' does not exist. Double-check the path.")
    
    except PermissionError:
        print(f"✗ Error: Permission denied!\n   You don't have access to '{file_path}'.\n   Try running with 'sudo' if needed.")
    
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

if __name__ == "__main__":
    while True:
        user_input = input("\nEnter file path (or 'quit' to exit): ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye! MagicEye is closing...")
            break
        
        if user_input == "":
            print("⚠️ Please enter a valid file path.")
            continue
        
        identify_file_type(user_input)
    
    print("\nThank you for using MagicEye! ✨")