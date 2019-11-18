from decimal import Decimal
import decimal, random, numpy


def GibbsSampling():
    # initialize probabilities, but only where B = b1
    a0b1 = 5
    a1b1 = 10
    b1c0 = 1
    b1c1 = 100
    c0d0 = 1
    c0d1 = 100
    c1d0 = 100
    c1d1 = 1
    d0a0 = 100
    d0a1 = 1
    d1a0 = 1
    d1a1 = 100

    a0b1c0d0 = a0b1 * b1c0 * c0d0 * d0a0
    a0b1c0d1 = a0b1 * b1c0 * c0d1 * d1a1
    a0b1c1d0 = a0b1 * b1c1 * c1d0 * d0a0
    a0b1c1d1 = a0b1 * b1c1 * c1d1 * d1a0
    a1b1c0d0 = a1b1 * b1c0 * c0d0 * d0a1
    a1b1c0d1 = a1b1 * b1c0 * c0d1 * d1a1
    a1b1c1d0 = a1b1 * b1c1 * c1d0 * d0a1
    a1b1c1d1 = a1b1 * b1c1 * c1d1 * d1a1

    # normalize probabilities
    sum = a0b1c0d0 + a0b1c0d1 + a0b1c1d0 + a0b1c1d1 + a1b1c0d0
    + a1b1c0d1 + a1b1c1d0 + a1b1c1d1

    normalize_a0b1c0d0 = Decimal(a0b1c0d0) / Decimal(sum)
    normalize_a0b1c0d1 = Decimal(a0b1c0d1) / Decimal(sum)
    normalize_a0b1c1d0 = Decimal(a0b1c1d0) / Decimal(sum)
    normalize_a0b1c1d1 = Decimal(a0b1c1d1) / Decimal(sum)
    normalize_a1b1c0d0 = Decimal(a1b1c0d0) / Decimal(sum)
    normalize_a1b1c0d1 = Decimal(a1b1c0d1) / Decimal(sum)
    normalize_a1b1c1d0 = Decimal(a1b1c1d0) / Decimal(sum)
    normalize_a1b1c1d1 = Decimal(a1b1c1d1) / Decimal(sum)

    # '0' = a0b1c0d0, a0b1c0d1, a0b1c1d0, a0b1c1d1 (where A = a0)
    # '1' = a1b1c0d0, a1b1c0d1, a1b1c1d0, a1b1c1d1 (where A = a1)
    arr = [0, 0, 0, 0, 1, 1, 1, 1]

    # probability associated with each entry in arr
    probs = [normalize_a0b1c0d0, normalize_a0b1c0d1, normalize_a0b1c1d0,
            normalize_a0b1c1d1, normalize_a1b1c0d0, normalize_a1b1c0d1,
            normalize_a1b1c1d0, normalize_a1b1c1d1]

    # normalize probs so they sum to 1 to avoid ValueError with numpy
    probs = numpy.array(probs)
    probs /= probs.sum()

    Sampling(arr, probs, 1)
    Sampling(arr, probs, 10)
    Sampling(arr, probs, 100)
    Sampling(arr, probs, 1000)
    Sampling(arr, probs, 10000)
    Sampling(arr, probs, 100000)
    Sampling(arr, probs, 1000000)


def Sampling(arr, probs, size):
    # we will resample non-evidence variables using a random order
    randomSample = numpy.random.choice(arr, size, p=probs)

    # Print results for frequency of seeing A = a1
    print(Decimal(randomSample.sum())/Decimal(size))

GibbsSampling()