import numpy as np

#Samples: X
corner_points = np.array([
    #0,0,0
    [0, 0, 144, -4, 142, 140, 1, 141],
    [0, 0, 178, 0, 177, 175, -2, 178],
    [0, 0, 284, 4, 282, 283, -3, 282],
    
    #30,0,0
    [0, 0, 174, -9, 178, 190, -13, 199],
    [0, 0, 189, -7, 192, 180, -19, 188],
    [0, 0, 225, 1, 213, 263, -40, 258],
    
    #45,0,0
    [0, 0, 203, 1, 190, 237, -50, 235],
    [0, 0, 217, 6, 207, 144, -51, 138],
    [0, 0, 108, 4, 103, 67, -15, 63],
    
    
        
    ], dtype=np.int64)

answers = np.array([
    #0,0,0
    [0,0,0],
    [0,0,0],
    #30,0,0
    [30,0,0],
    [30,0,0],
    
    #45,0,0
    [45,0,0],
    [45,0,0],
    
    
        
    ], dtype=np.int64)