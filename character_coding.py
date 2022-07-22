"""
    ASCII - American Standard Code for Information Interchange

    - each character is represented by a number between 0 and 256 stored in 8 bits of memory
    - the ord() function tells us the numeric value of a simple ASCII character.
"""

print(ord('H'))

"""
    Multi-Byte characters

    - to represent the wide range of characters computers must handle we represent
    characters with more than one byte:
        - UTF-16 is fixed length 2 bytes
        - UTF-32 is fixed length 4 bytes
        - UTF-8 is variable length 1-4 bytes
            - upwards compatible with ASCII
            - automatic detection between ASCII and UTF-8
            - UTF-8 is recommended parctice for encoding data to be exchanged between systems
    
    - in Python 3 all strings internally are UNICODE
    - working with string variables in Python programs and reading data from files usually "just works"
    - when we talk to a network resource using sockets or talk to a database we have to encode and decode
      data, usually to UTF-8
"""

import socket

while True :
    data = my_socket.recv(512)

    if (len(data) < 1) :
        break

    mystring = data.decode() # by default it assumes UTF-8 or ASCII which are compatible.
    print(mystring)
