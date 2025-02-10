# Page Replacement Algorithms

This program simulates and evaluates the performance of various page replacement algorithms for demand-paging scenarios in operating systems. It provides a clear understanding of page faults and their impact on memory management.

## Getting Started
This program is written in Python and simulates the following algorithms:
- **FIFO (First-In-First-Out)**
- **LRU (Least Recently Used)**
- **Optimal Page Replacement**

The program accepts user input for page values and frame numbers and outputs the steps, faults, and page table for each algorithm.

## Prerequisites
- **Python 3.10 or above**: The program was written in Python 3.12.1, but it is compatible with Python 3.10 or newer.
- No additional libraries are required as it uses Python's built-in functionality.

## Installation
1. Clone the repository to your local machine:
   
   ```bash
   git clone https://github.com/Nemesis-12/page-replacement.git
   ```
   
2. Navigate to the directory containing the script:

   ```console
   cd page-replacement
   ```

## Usage
Run the program in the terminal or an IDE:

```console
python page_algo.py
```

## Example

### Input

```console
Enter sample values (without commas): 1 2 3 4 1 2 5 1 2 3 4 5
Enter no of frames: 4
```

### Output

```console
LRU Algorithm:

Step 1: Page fault (1) - Page Table: [1], Frames: [1], Faults: 1
Total faults: 1
Step 2: Page fault (2) - Page Table: [1, 2], Frames: [2], Faults: 2
Total faults: 2
...
Total faults: 8
```

## Contributing
This project is an educational tool and welcomes contributions. To contribute:
- Fork the repository.
- Make your changes.
- Submit a pull request with a description of your updates.
Feel free to open an issue for suggestions or bugs.

## License
This project is licensed under the [MIT License](LICENSE).
