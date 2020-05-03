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
    d1 = sample_normal_distributed_values(samples_to_average=12, samples_to_generate=500, offset=0.0)
    d2 = sample_normal_distributed_values(samples_to_average=12, samples_to_generate=1000, offset=0.25)
    d3 = sample_normal_distributed_values(samples_to_average=12, samples_to_generate=5000, offset=0.5)
    d4 = sample_normal_distributed_values(samples_to_average=12, samples_to_generate=10000, offset=0.75)

    group_labels = ['500 samples', '1000 samples', '5000 samples', '10000 samples']

    fig = ff.create_distplot([d1, d2, d3, d4], group_labels)
    fig.update_layout(title_text='2.3 Plot normal distributions')
    fig.show()


def main():
    print('I am assignment 1.')
    plot()


if __name__ == '__main__':
    main()
