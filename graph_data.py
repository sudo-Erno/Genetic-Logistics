import matplotlib.pyplot as plt

def plot_times_average(times, fsize=(12, 8)):
    """
    times: List containing the average of time for the best paths.
    """

    fig, ax = plt.subplots(1, 1, figsize=fsize)
    ax.set_xlabel("Generations")
    ax.set_ylabel("Avg. Time")
    ax.plot(times)

    plt.show()

def plot_locations(coords, fsize=(12, 8)):
    fig, ax = plt.subplots(1, 1, figsize=fsize)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    for x, y in coords:
        ax.scatter(x, y, s=35)
    plt.show()