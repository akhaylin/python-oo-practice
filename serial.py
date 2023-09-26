class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Initialize the starting number and current number."""

        self.start = start
        self.next = start
    #TODO: write a repr function

    def generate(self):
        """Return the next sequential number."""

        num = self.next
        self.next += 1
        return num

    def reset(self):
        """Reset the number back to the original start number"""

        self.next = self.start



