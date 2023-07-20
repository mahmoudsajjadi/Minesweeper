import settings


def height_percent(percentage):
    return (settings.HEIGHT) * (percentage / 100)


def width_percentage(percentage):
    return (settings.WIDTH) * (percentage / 100)
