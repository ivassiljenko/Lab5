#!/usr/bin/env python3
# Author ID: Ivan Vassiljenko

import os

def read_file_string(file_name):
   # Takes file_name as string for a file name, returns its entire contents as a string
   file_path = os.path.abspath(file_name)
   with open(file_path, 'r') as f:
       return f.read()

def read_file_list(file_name):
   # Takes a file_name as string for a file name,
   # return its entire contents as a list of lines without new-line characters
   file_path = os.path.abspath(file_name)
   with open(file_path, 'r') as f:
       lines = f.readlines()
       # Strip new-line characters from each line
       lines = [line.strip() for line in lines]
       return lines

def append_file_string(file_name, string_of_lines):
   # Takes two strings, appends the string to the end of the file
   file_path = os.path.abspath(file_name)
   with open(file_path, 'a') as f:
       f.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
   # Takes a string and list, writes all items from list to file where each item is one line
   file_path = os.path.abspath(file_name)
   with open(file_path, 'w') as f:
       for line in list_of_lines:
           f.write(line + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
   # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
   file_path_read = os.path.abspath(file_name_read)
   file_path_write = os.path.abspath(file_name_write)
   
   with open(file_path_read, 'r') as read_file:
       with open(file_path_write, 'w') as write_file:
           line_number = 1
           for line in read_file:
               write_file.write(f"{line_number}:{line}")
               line_number += 1

if __name__ == '__main__':
   file1 = 'seneca1.txt'
   file2 = 'seneca2.txt'
   file3 = 'seneca3.txt'
   string1 = 'First Line\nSecond Line\nThird Line\n'
   list1 = ['Line 1', 'Line 2', 'Line 3']
   
   # Remove existing files if they exist from previous runs
   for file in [file1, file2, file3]:
       if os.path.exists(file):
           os.remove(file)
   
   append_file_string(file1, string1)
   print(read_file_string(file1))
   
   write_file_list(file2, list1)
   print(read_file_string(file2))
   
   copy_file_add_line_numbers(file2, file3)
   print(read_file_string(file3))

