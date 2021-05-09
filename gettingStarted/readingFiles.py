sample_file = open("D:\Web_Development\Python\gettingStarted\sample.txt", "r")
print(sample_file.readable())  # Check if the file is readable
# print(sample_file.read())  # Read File
# Read oneline and the cursor is moved to the next line in the file
# print(sample_file.readline())
# Read oneline and the cursor is moved to the next line in the file
# print(sample_file.readline())  # result read line 2
# print(sample_file.readlines())  # read all lines and result in array
# print(sample_file.readlines()[0])  # read lines in specific array

for line in sample_file.readlines():  # Read array using array
    print(line)

sample_file.close()

# Untuk parameter kedua ada beberapa pilihan yang bisa dipilih
"""
    r => read, buat baca doang
    w => write, mengubah data atau bener bener buat ulang atau ngubah total
    a => append, menambahkan tapi gabisa ubah apa yang udah ada
    r+ => read and write, membaca dan mengubah file
"""
