# Page Replacement Algorithms

## Getting Started
This program simulates page replacement algorithms and is written in Python. The program asks the user for the sample values and frames as input and gives the steps, faults, and the page table as output. The following document will help you get started on setting up the program.

## Prerequisites
This program requires Python 3.10 to run and was written in 3.12.1. To download, go to python.org and download Python 3.10.x or above. You will not be required to install any additional libraries as we are using default libraries.

## Installation
Clone the repository or download the source code onto your local machine. Navigate to the directory of the script and run it through the terminal or an IDE.

## Usage
Run the following program on the terminal:

```console
python page_algo.py
```

When the program starts, you will be asked to enter the page values as well as the frame number as input. The functions then perform the page replacement based on the algorithms.

```python
# Take input of values
sampleInput = input("Enter sample values w/o commas (q to quit): ")

if sampleInput == 'q':
  quit()

pgSample = sampleInput.split()
pgSample = [int(i) for i in pgSample]

frames = int(input("Enter no of frames: "))
pgNo = len(pgSample)
```

After the program is executed, you should get the following output.

```console
Enter sample values (without commas): 1 2 3 4 1 2 5 1 2 3 4 5
Enter no of frames: 4

LRU Algorithm:

Step 1: Page fault (1) - Page Table: [1], Frames: [1], Faults: 1
Total faults: 1
Step 2: Page fault (2) - Page Table: [1, 2], Frames: [2], Faults: 2
Total faults: 2
Step 3: Page fault (3) - Page Table: [1, 2, 3], Frames: [3], Faults: 3
Total faults: 3
Step 4: Page fault (4) - Page Table: [1, 2, 3, 4], Frames: [4], Faults: 4
Total faults: 4
Step 5: Page fault (5) - Page Table: [2, 3, 4, 1], Frames: [4], Faults: 4
Total faults: 4
Step 6: Page fault (6) - Page Table: [3, 4, 1, 2], Frames: [4], Faults: 4
Total faults: 4
Step 7: Page fault (7) - Page Table: [4, 1, 2, 5], Frames: [4], Faults: 5
Total faults: 5
Step 8: Page fault (8) - Page Table: [4, 2, 5, 1], Frames: [4], Faults: 5
Total faults: 5
Step 9: Page fault (9) - Page Table: [4, 5, 1, 2], Frames: [4], Faults: 5
Total faults: 5
Step 10: Page fault (10) - Page Table: [5, 1, 2, 3], Frames: [4], Faults: 6
Total faults: 6
Step 11: Page fault (11) - Page Table: [1, 2, 3, 4], Frames: [4], Faults: 7
Total faults: 7
Step 12: Page fault (12) - Page Table: [2, 3, 4, 5], Frames: [4], Faults: 8
Total faults: 8


Optimal Algorithm:

Step 1: Page fault (1) - Page Table: [0], Frames: [1], Faults: 1
Total faults: 1
Step 2: Page fault (2) - Page Table: [0, 1], Frames: [2], Faults: 2
Total faults: 2
Step 3: Page fault (3) - Page Table: [0, 1, 2], Frames: [3], Faults: 3
Total faults: 3
Step 4: Page fault (4) - Page Table: [0, 1, 2, 3], Frames: [4], Faults: 4
Total faults: 4
Step 5: Page fault (5) - Page Table: [1, 1, 2, 3], Frames: [4], Faults: 5
Total faults: 5
Step 6: Page fault (6) - Page Table: [2, 1, 2, 3], Frames: [4], Faults: 6
Total faults: 6
Step 7: Page fault (7) - Page Table: [5, 1, 2, 3], Frames: [4], Faults: 7
Total faults: 7
Step 8: Page fault (8) - Page Table: [1, 1, 2, 3], Frames: [4], Faults: 8
Total faults: 8
Step 9: Page fault (9) - Page Table: [2, 1, 2, 3], Frames: [4], Faults: 9
Total faults: 9
Step 10: Page fault (10) - Page Table: [3, 1, 2, 3], Frames: [4], Faults: 10
Total faults: 10
Step 11: Page fault (11) - Page Table: [4, 1, 2, 3], Frames: [4], Faults: 11
Total faults: 11
Step 12: Page fault (12) - Page Table: [5, 1, 2, 3], Frames: [4], Faults: 12
Total faults: 12


FIFO Algorithm:

Step 1: Page fault (1) - Page Table: [1], Frames: [1], Faults: 1
Total faults: 1
Step 2: Page fault (2) - Page Table: [1, 2], Frames: [2], Faults: 2
Total faults: 2
Step 3: Page fault (3) - Page Table: [1, 2, 3], Frames: [3], Faults: 3
Total faults: 3
Step 4: Page fault (4) - Page Table: [1, 2, 3, 4], Frames: [4], Faults: 4
Total faults: 4
Step 5: Page fault (5) - Page Table: [1, 2, 3, 4], Frames: [4], Faults: 4
Total faults: 4
Step 6: Page fault (6) - Page Table: [1, 2, 3, 4], Frames: [4], Faults: 4
Total faults: 4
Step 7: Page fault (7) - Page Table: [2, 3, 4, 5], Frames: [4], Faults: 5
Total faults: 5
Step 8: Page fault (8) - Page Table: [3, 4, 5, 1], Frames: [4], Faults: 6
Total faults: 6
Step 9: Page fault (9) - Page Table: [4, 5, 1, 2], Frames: [4], Faults: 7
Total faults: 7
Step 10: Page fault (10) - Page Table: [5, 1, 2, 3], Frames: [4], Faults: 8
Total faults: 8
Step 11: Page fault (11) - Page Table: [1, 2, 3, 4], Frames: [4], Faults: 9
Total faults: 9
Step 12: Page fault (12) - Page Table: [2, 3, 4, 5], Frames: [4], Faults: 10
Total faults: 10
```

## Contributing
This project is an educational tool and is open to contributions. If you have suggestions or improvements, create a pull request by forking the repository.
