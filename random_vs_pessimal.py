#!/usr/bin/env python3
"""
Demo the modules.
"""

from sequence import Sequence


def buck_the_trend(seq):
    """Number of trends in opposite direction."""
    trend_list = seq.collect_and_merge()
    forward_trends = len(trend_list)  # number of trends in random sequence
    trend_list.rotate_and_merge()  # rotate to single trend

    # how many in the opposite direction?
    seq = Sequence(trend_list[0].trend())  # make it a sequence
    seq.reverse()  # turn it around
    backward_trends = len(seq.collect_and_merge())  # trends in opposite direction
    return (forward_trends, backward_trends)


def main():
    """The whole enchilada."""

    years = 70  # the Biblical "three score and ten"
    fwd = 0
    bkwd = 0  # in pessimal forward lives
    days = 365 * years
    trials = 100
    for _ in range(trials):  # multiple trials
        seq = Sequence(days)
        (forward_trends, backward_trends) = buck_the_trend(seq)
        fwd += forward_trends
        bkwd += backward_trends

    mean_forward_trends = fwd / trials
    mean_backward_trends = bkwd / trials

    print("Average number of upward trends in a random life: ", mean_forward_trends)
    print("Average number of upward trends in a pessimal life: ", mean_backward_trends)
    print(
        "Average upward trend length in a random life: {} years".format(
            years / mean_forward_trends
        )
    )
    print(
        "Average upward trend length in a pessimal life: {} years".format(
            years / mean_backward_trends
        )
    )


if __name__ == "__main__":
    main()
