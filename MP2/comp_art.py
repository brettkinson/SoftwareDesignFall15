# -*- coding: utf-8 -*-
"""
comp_art.py
Brett Atkinson
Software Design FA15

Creates art through random mathematical function generation.
"""

from PIL import Image
import random
import math


def build_random_function(min_depth, max_depth):
    """ Uses random number generator to create a function of a depth between the function inputs
    """
    # input: min and max desired depth of function
    # output: list of the function names to include

    rand_num = random.randint(0,6)
    
    if max_depth == 0:
        return [random.choice(["x","y"])]
        
    elif min_depth <= 0 and random.randint(0,1):
        return [random.choice(["x","y"])]
        
    elif rand_num == 0: #"prod" -> a*b
        return ["prod", build_random_function(min_depth-1,max_depth-1), build_random_function(min_depth-1,max_depth-1)]
    elif rand_num == 1: #"cos" -> cos(pi*a)
        return ["cos", build_random_function(min_depth-1,max_depth-1)]
    elif rand_num == 2: #"sin" -> sin(pi*a)
        return ["sin", build_random_function(min_depth-1,max_depth-1)]
    elif rand_num == 3: #"avg" -> 1/2*(a+b)
        return ["avg", build_random_function(min_depth-1,max_depth-1), build_random_function(min_depth-1,max_depth-1)]
    elif rand_num == 4: #"sq" -> a**2
        return ["sq", build_random_function(min_depth-1,max_depth-1)]
    elif rand_num == 5: #"thrd" -> a**3
        return ["thrd", build_random_function(min_depth-1,max_depth-1)]
    elif rand_num == 6: #"sqrt" -> a**1/2
        return ["sqrt", build_random_function(min_depth-1,max_depth-1)]



def evaluate_random_function(f, x, y):
    """ Uses build_random_function to create a function and evaluates it with two numeric inputs
    """

    if f[0] == "x": #function for X
        return x

    elif f[0] == "y": #function for Y
        return y

    elif f[0] == "prod": #multiplies two inputs
        return (evaluate_random_function(f[1], x, y) * evaluate_random_function(f[2], x, y))

    elif f[0] == "cos": #computes cosine of input
        return math.cos(math.pi*evaluate_random_function(f[1], x, y))

    elif f[0] == "sin": #computes sine of input
        return math.sin(math.pi*evaluate_random_function(f[1], x, y))

    elif f[0] == "avg": #takes average of two inputs
        return (0.5 * (evaluate_random_function(f[1], x, y) + evaluate_random_function(f[2], x, y)))

    elif f[0] == "sq": #squares input
        return (evaluate_random_function(f[1], x, y) ** 2)

    elif f[0] == "thrd": #raise input to third power
        return (evaluate_random_function(f[1], x, y) ** 3)

    elif f[0] == "sqrt": #take square root of input
        return (abs(evaluate_random_function(f[1], x, y)) ** (0.5))



def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    """

    input_range = float(input_interval_end) - float(input_interval_start)
    output_range = float(output_interval_end) - float(output_interval_start) 
    val_pos = val - float(input_interval_start)
    relative_pos = val_pos / input_range

    return (relative_pos * output_range) + output_interval_start



def color_mapping(val):
    """ Uses remap_interval to convert the input to a color code
    """

    color = remap_interval(val,-1,1,0,255)

    return int(color)



def generate_art(filename, x_size, y_size):
    """ Generate computational art and save as an image file.
        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions
    """

    minDepth = 8
    maxDepth = 12

    # Function generation for each color
    red = build_random_function(minDepth, maxDepth)
    green = build_random_function(minDepth, maxDepth)
    blue = build_random_function(minDepth, maxDepth)

    print red
    
    # Generate image and loop color mapping on each pixel
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            #print(x)
            pixels[i, j] = (
                    color_mapping(evaluate_random_function(red, x, y)),
                    color_mapping(evaluate_random_function(green, x, y)),
                    color_mapping(evaluate_random_function(blue, x, y))
                    )

    #for i in [-1,-0.5,0,0.5,1.0]:
    #   for j in [-1,-0.5,0,0.5,1.0]:
    #      print(evaluate_random_function(["sqrt", ["y"]], i, j))
    im.save(filename)

generate_art('test1.png',500,500)