#!/usr/bin/env python3
"""
EDWED - A simple demonstration script
"""

def main():
    """Display EDWED message"""
    message = "EDWED"
    print(f"Welcome to {message}!")
    print(f"\n{message} is running successfully.")
    
    # Display EDWED in ASCII art style
    ascii_art = """
    ███████╗██████╗ ██╗    ██╗███████╗██████╗ 
    ██╔════╝██╔══██╗██║    ██║██╔════╝██╔══██╗
    █████╗  ██║  ██║██║ █╗ ██║█████╗  ██║  ██║
    ██╔══╝  ██║  ██║██║███╗██║██╔══╝  ██║  ██║
    ███████╗██████╔╝╚███╔███╔╝███████╗██████╔╝
    ╚══════╝╚═════╝  ╚══╝╚══╝ ╚══════╝╚═════╝ 
    """
    print(ascii_art)

if __name__ == "__main__":
    main()
