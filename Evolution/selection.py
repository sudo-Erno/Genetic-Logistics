def selection(population, survivors, method='elite'):
    """
    times: List with all the times corresponding to each path.
    survivors: Number of items that will survive the seletion phase.
    method: Method use for selection of the paths.
    """

    if method == 'elite':
        return [p[0] for p in population][:survivors], [p[1] for p in population][:survivors]

    # TODO: Add more methods (in case)