import numpy as np
import plotly.figure_factory as ff


def sample_normal_distributed_value(samples_to_average=12):
    """
    2.1 One-dimensional normal distributed sample
    :param samples_to_average:
    :return:
    """
    samples = np.random.random(samples_to_average)
    return np.average(samples) - 0.5


def sample_normal_distributed_values(samples_to_generate=1, samples_to_average=12, offset=0.0):
    """
    2.2 Normal distributed samples
    :param samples_to_generate:
    :param samples_to_average:
    :param offset:
    :return:
    """
    result = []
    for _ in range(0, samples_to_generate):
        result.append(sample_normal_distributed_value(samples_to_average) + offset)
    return result


def plot():
    """
    2.3 Plot normal distributions
    :return:
    """
    for sample_size in [500, 1000, 5000, 10000]:
        x1 = sample_normal_distributed_values(samples_to_average=sample_size, samples_to_generate=4, offset=0.0)
        x2 = sample_normal_distributed_values(samples_to_average=sample_size, samples_to_generate=4, offset=0.25)
        x3 = sample_normal_distributed_values(samples_to_average=sample_size, samples_to_generate=4, offset=0.5)
        x4 = sample_normal_distributed_values(samples_to_average=sample_size, samples_to_generate=4, offset=0.75)

        group_labels = ['offset 0.0', 'offset 0.25', 'offset 0.5', 'offset 0.75']
        colors = ['slategray', 'magenta', 'red', 'green']
        fig = ff.create_distplot([x1, x2, x3, x4], group_labels, bin_size=.5,
                                 curve_type='normal',
                                 colors=colors)

        # Add title
        fig.update_layout(title_text='sample_size ' + str(sample_size))
        fig.show()


def main():
    print('I am assignment 1.')
    plot()


if __name__ == '__main__':
    main()
