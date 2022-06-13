import numpy as np

#Samples: X
corner_points = np.array([
    [0, 0, 177, 4, 189, 194, -20, 190],
[0, 0, 193, 6, 200, 120, -30, 113],
[0, 0, 177, 5, 189, 194, -20, 191],
[0, 0, 195, 6, 200, 120, -29, 113],
[0, 0, 178, 5, 189, 195, -20, 191],
[0, 0, 194, 7, 200, 120, -30, 113],
[0, 0, 176, 5, 188, 195, -21, 191],
[0, 0, 195, 7, 200, 120, -30, 113],
[0, 0, 178, 4, 190, 194, -19, 189],
[0, 0, 196, 6, 200, 120, -30, 113],
[0, 0, 178, 4, 189, 193, -19, 190],
[0, 0, 194, 6, 199, 120, -31, 113],
[0, 0, 177, 4, 189, 194, -20, 190],
[0, 0, 194, 6, 199, 120, -31, 113],
[0, 0, 178, 4, 190, 194, -19, 190],
[0, 0, 194, 6, 199, 120, -31, 113],
[0, 0, 177, 4, 189, 193, -21, 190],
[0, 0, 195, 6, 200, 120, -29, 113],
[0, 0, 177, 5, 189, 194, -19, 191],
[0, 0, 195, 7, 200, 120, -30, 113],
[0, 0, 178, 4, 190, 193, -19, 189],
[0, 0, 195, 7, 200, 120, -30, 113],
[0, 0, 177, 4, 189, 194, -20, 190],
[0, 0, 193, 7, 199, 120, -31, 113],
[0, 0, 177, 4, 189, 195, -21, 190],
[0, 0, 194, 6, 199, 120, -30, 113],
[0, 0, 177, 5, 189, 194, -20, 189],
[0, 0, 195, 7, 200, 120, -29, 113],
[0, 0, 177, 4, 189, 194, -20, 190],
[0, 0, 194, 7, 199, 121, -29, 114],
[0, 0, 177, 4, 189, 193, -21, 189],
[0, 0, 194, 7, 200, 120, -30, 113],
[0, 0, 129, 5, 161, 102, 16, 98],
[0, 0, 162, 7, 187, 84, 1, 79],
[0, 0, 129, 4, 162, 102, 15, 98],
[0, 0, 163, 5, 187, 83, 1, 78],
[0, 0, 130, 4, 163, 102, 17, 97],
[0, 0, 162, 7, 186, 84, -1, 79],
[0, 0, 131, 4, 163, 102, 18, 97],
[0, 0, 163, 7, 187, 84, 1, 79],
[0, 0, 131, 4, 162, 102, 19, 96],
[0, 0, 162, 7, 187, 84, 1, 79],
[0, 0, 130, 4, 162, 102, 18, 97],
[0, 0, 131, 5, 163, 102, 18, 97],
[0, 0, 163, 7, 187, 84, 1, 79],
[0, 0, 131, 4, 163, 102, 18, 97],
[0, 0, 130, 4, 163, 102, 19, 98],
[0, 0, 161, 6, 186, 84, 0, 79],
[0, 0, 131, 4, 162, 102, 19, 97],
[0, 0, 162, 7, 187, 84, 1, 79],
[0, 0, 131, 4, 163, 102, 18, 98],
[0, 0, 163, 7, 187, 84, 0, 79],
[0, 0, 130, 4, 162, 102, 18, 97],
[0, 0, 162, 7, 187, 84, 0, 79],
[0, 0, 131, 4, 163, 102, 18, 98],
[0, 0, 163, 7, 187, 84, 1, 79],
[0, 0, 131, 4, 163, 102, 18, 98],
[0, 0, 163, 7, 187, 84, 1, 79],
[0, 0, 130, 4, 163, 102, 19, 98],
[0, 0, 162, 6, 186, 84, 0, 79],
[0, 0, 131, 4, 162, 102, 20, 96],
[0, 0, 130, 4, 162, 102, 19, 97],
[0, 0, 129, 4, 162, 102, 17, 98],
[0, 0, 163, 7, 187, 84, 0, 79],
[0, 0, 130, 4, 162, 102, 16, 98],
[0, 0, 161, 7, 186, 84, 0, 79],
[0, 0, 129, 3, 123, 96, -22, 92],
[0, 0, 161, 6, 155, 80, -30, 75],
[0, 0, 128, 4, 121, 97, -22, 92],
[0, 0, 161, 6, 155, 80, -29, 75],
[0, 0, 128, 4, 122, 96, -22, 93],
[0, 0, 161, 6, 155, 80, -30, 75],
[0, 0, 129, 4, 123, 96, -23, 92],
[0, 0, 160, 6, 155, 80, -30, 75],
[0, 0, 129, 4, 123, 96, -21, 92],
[0, 0, 161, 6, 156, 80, -30, 75],
[0, 0, 129, 4, 122, 97, -22, 93],
[0, 0, 161, 6, 155, 80, -30, 75],
[0, 0, 129, 4, 122, 97, -21, 92],
[0, 0, 161, 6, 155, 80, -30, 75],
[0, 0, 129, 3, 123, 96, -22, 92],
[0, 0, 161, 6, 155, 80, -30, 75],
[0, 0, 127, 3, 122, 96, -23, 93],
[0, 0, 161, 6, 155, 80, -30, 75],
[0, 0, 129, 4, 123, 96, -23, 93],
[0, 0, 161, 6, 155, 80, -30, 75],
[0, 0, 129, 4, 123, 97, -22, 93],
[0, 0, 161, 6, 155, 80, -30, 75],
[0, 0, 129, 2, 123, 95, -20, 90],
[0, 0, 161, 6, 155, 80, -30, 75],
[0, 0, 129, 4, 123, 97, -21, 93],
[0, 0, 162, 6, 156, 80, -29, 75],
[0, 0, 128, 4, 122, 97, -23, 93],
[0, 0, 162, 6, 155, 80, -30, 75],
[0, 0, 129, 3, 122, 96, -21, 91],
[0, 0, 163, 6, 156, 80, -29, 75],
[0, 0, 129, 4, 123, 97, -23, 93],
[0, 0, 161, 6, 155, 80, -30, 75],
[0, 0, 129, 3, 123, 96, -22, 92],
[0, 0, 160, 6, 155, 80, -30, 75],
[0, 0, 201, 6, 192, 126, -47, 120],
[0, 0, 190, 2, 177, 211, -45, 207],
[0, 0, 200, 6, 192, 126, -47, 120],
[0, 0, 188, 2, 176, 211, -45, 207],
[0, 0, 201, 6, 192, 126, -47, 120],
[0, 0, 189, 2, 177, 211, -46, 207],
[0, 0, 201, 6, 192, 126, -47, 120],
[0, 0, 189, 2, 177, 211, -46, 207],
[0, 0, 200, 6, 192, 126, -47, 120],
[0, 0, 189, 2, 176, 212, -46, 207],
[0, 0, 199, 6, 191, 126, -48, 120],
[0, 0, 188, 3, 175, 213, -46, 208],
[0, 0, 201, 6, 192, 126, -47, 120],
[0, 0, 190, 2, 177, 211, -45, 207],
[0, 0, 200, 6, 192, 126, -47, 120],
[0, 0, 189, 2, 177, 211, -45, 207],
[0, 0, 200, 6, 192, 126, -47, 120],
[0, 0, 190, 2, 177, 211, -45, 206],
[0, 0, 201, 6, 192, 125, -46, 120],
[0, 0, 189, 2, 176, 211, -46, 206],
[0, 0, 201, 6, 192, 126, -47, 120],
[0, 0, 189, 2, 177, 211, -46, 208],
[0, 0, 201, 6, 192, 126, -47, 120],
[0, 0, 190, 1, 177, 211, -44, 206],
[0, 0, 200, 6, 192, 126, -47, 120],
[0, 0, 189, 2, 177, 211, -44, 206],
[0, 0, 200, 6, 192, 126, -47, 120],
[0, 0, 190, 2, 177, 211, -45, 207],
[0, 0, 201, 6, 192, 126, -47, 120],
[0, 0, 189, 2, 177, 211, -46, 207],
[0, 0, 200, 6, 191, 126, -47, 120],
[0, 0, 189, 2, 177, 212, -45, 207],
[0, 0, 201, 6, 192, 126, -48, 120],
[0, 0, 189, 1, 175, 211, -45, 206],
[0, 0, 179, 6, 229, 196, 20, 196],
[0, 0, 194, 6, 223, 121, -7, 116],
[0, 0, 179, 5, 228, 195, 21, 195],
[0, 0, 194, 6, 223, 122, -7, 116],
[0, 0, 179, 6, 228, 196, 21, 196],
[0, 0, 194, 6, 223, 122, -8, 115],
[0, 0, 178, 5, 228, 196, 21, 194],
[0, 0, 195, 6, 224, 122, -6, 116],
[0, 0, 178, 5, 228, 195, 20, 194],
[0, 0, 195, 6, 224, 122, -7, 115],
[0, 0, 179, 6, 229, 196, 21, 196],
[0, 0, 195, 6, 223, 122, -8, 115],
[0, 0, 180, 5, 229, 196, 21, 194],
[0, 0, 195, 6, 224, 121, -6, 116],
[0, 0, 179, 5, 229, 195, 21, 195],
[0, 0, 194, 6, 223, 121, -7, 116],
[0, 0, 179, 5, 229, 196, 20, 194],
[0, 0, 194, 6, 224, 122, -6, 116],
[0, 0, 178, 5, 228, 196, 20, 195],
[0, 0, 195, 6, 223, 121, -7, 116],
[0, 0, 178, 5, 228, 196, 20, 195],
[0, 0, 194, 6, 223, 122, -7, 116],
[0, 0, 179, 5, 228, 196, 21, 195],
[0, 0, 194, 6, 223, 122, -8, 116],
[0, 0, 179, 5, 229, 195, 21, 195],
[0, 0, 194, 6, 223, 122, -7, 116],
[0, 0, 179, 5, 228, 195, 21, 195],
[0, 0, 195, 6, 223, 122, -7, 116],
[0, 0, 178, 5, 227, 196, 21, 195],
[0, 0, 194, 6, 224, 122, -8, 115],
[0, 0, 179, 6, 229, 196, 21, 197],
[0, 0, 194, 6, 223, 122, -8, 116],
[0, 0, 178, 5, 228, 196, 20, 195],
[0, 0, 194, 6, 223, 122, -7, 116],
[0, 0, 178, 5, 228, 196, 20, 195],
[0, 0, 195, 6, 225, 122, -6, 116],
[0, 0, 179, 5, 229, 196, 20, 195],
[0, 0, 194, 6, 223, 122, -8, 116],

], dtype=np.float64)