# Read complex binary
# open filename and return the contents as a column vector treating
# them as 32 bit complex numbers

import numpy as np


filename = r"C:\Users\patel\PycharmProjects\read_complex_binary\print_test2.dat"
content = np.fromfile(open(filename), dtype=np.float32)
a_file = open("test.txt", "w+")
print(content, a_file)
np.savetxt(a_file, content)

