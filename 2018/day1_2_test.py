import day1_2


def test_read():
    freq = day1_2.process_freqs('data/day1-2-test.txt')
    assert freq == 10
