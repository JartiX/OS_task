import numpy as np

def linux():
    cmd = " ".join([f"{char:.2f}" for char in np.linspace(0, 10, 100)])
    return cmd
