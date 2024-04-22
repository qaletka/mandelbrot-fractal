import numpy as np
import matplotlib.pyplot as plt


def calculate_mandelbrot_iterations(c, max_iterations):
    z = 0
    iteration = 0
    while abs(z) <= 2 and iteration < max_iterations:
        z = z ** 2 + c
        iteration += 1
    return iteration


def generate_row_iterations(imaginary_part, real_values, max_iterations):
    return [calculate_mandelbrot_iterations(complex(real_value, imaginary_part), max_iterations) for real_value in
            real_values]


def generate_mandelbrot_set_iterations(xmin, xmax, ymin, ymax, width, height, max_iterations):
    real_values = np.linspace(xmin, xmax, width)
    imaginary_values = np.linspace(ymin, ymax, height)
    return np.array(
        [generate_row_iterations(imaginary_part, real_values, max_iterations) for imaginary_part in
         imaginary_values])


def plot_mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iterations):
    mandelbrot_set = generate_mandelbrot_set_iterations(xmin, xmax, ymin, ymax, width, height, max_iterations)
    plt.imshow(mandelbrot_set, extent=(xmin, xmax, ymin, ymax))
    plt.show()


if __name__ == "__main__":
    plot_mandelbrot_set(-2.0, 1.0, -1.5, 1.5, 1000, 1000, 256)
