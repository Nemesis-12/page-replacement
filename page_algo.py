'''
This program implements different page replacement algorithms
in demand-paging scenarios and then analyze their performance
based on the page faults produced.
'''

from queue import Queue

# Define LRU Algorithm
def lruAlgorithm(frames, pgSample):
    # Define constants
    faults, hits, counter = 0, 0, 0
    page = []

    # Check for hits and faults in memory
    for i in pgSample:
        # Iterate through the sample pages that we gave
        # and if the sample page is present in the pages
        # list already (hit), remove it and add it at the end of
        # the list.
        if i in page:
            page.remove(i)
            page.append(i)
            hits += 1

        # If it is not present in the list, we have a page fault.
        # If the page list size is less than the number of
        # frames, add it to the list. If not, remove the first page
        # and add a new page to the list.
        else:
            faults +=1

            if (len(page) < frames):
                page.append(i)
            else:
                page.remove(page[0])
                page.append(i)
        
        # Print the results
        counter += 1
        print(f"Step {counter}: Page fault ({counter}) - Page Table: {page}, Frames: [{len(page)}], Faults: {faults}")
        print(f"Total faults: {faults}")
    
    print("\n")

# Define Optimal Algorithm
def optAlgorithm(frames, pgSample, pgNo):
    # Define constants
    faults, hits, counter = 0, 0, 0
    page = []

    # Check for hits and faults in memory
    for i in range(pgNo):
        # Iterate through the sample pages that we gave
        # and if the sample page is present in the pages
        # list already (hit), increase the hit counter
        if i in page:
            hits += 1

        # If it is not present in the list, we have a page fault.
        # If the page list size is less than the number of
        # frames, add it to the list. If not, find a page that
        # will not be accessed for a long time and replace that with
        # a new page.
        else:
            faults += 1

            if (len(page) < frames):
                page.append(i)

            else:
                j = predictPage(pgSample, pgNo, page, i + 1)
                page[j] = pgSample[i]

        # Print the results
        counter += 1
        print(f"Step {counter}: Page fault ({counter}) - Page Table: {page}, Frames: [{len(page)}], Faults: {faults}")
        print(f"Total faults: {faults}")

    print("\n")

# Function that will help us find the predicted page
# in the Optimal ALgorithm
def predictPage(pgSample, pgNo, page, index):
    # Define constants
    res = -1
    farPage = index

    # Find out which page will not be accessed further into the
    # future and then replace that with a new page.
    for i in range(len(page)):

        j = index
        for j in range(pgNo):
            if (page[i] == pgSample[j]):
                if (j > farPage):
                    farPage = j
                    res = i
                break

        # Return the page if it never being referenced in the future
        if (j == pgNo):
            return i

    if (res == -1):
        return 0
    else:
        return res

# Define FIFO Algorithm
def fifoAlgorithm(frames, pgSample, pgNo):
    # Define constants
    faults, counter = 0, 0
    page = set()
    pgQueue = Queue()

    # Check for faults in memory
    for i in range(pgNo):
        # Iterate through the sample pages that we gave
        # and check if sample page is in the page list.
        # If not, check if the page size capacity is full
        # or not and based on that perform the action.
        if (len(page) < frames):
            # If capacity is not full, then just add the
            # sample page to the page set and at the same time
            # add it to the queue. This queue helps us to perform
            # FIFO operation. 
            if (pgSample[i] not in page):
                page.add(pgSample[i])
                faults += 1
                pgQueue.put(pgSample[i])

        # If it is full and the sample page is present we do nothing.
        # If the sample page is not present, remove the first value
        # from the queue and replace it with a new page.        
        else:
            if (pgSample[i] not in page):
                val = pgQueue.queue[0]
                pgQueue.get()
                page.remove(val)
                page.add(pgSample[i])
                pgQueue.put(pgSample[i])
                faults += 1

        # Print the results
        counter += 1
        print(f"Step {counter}: Page fault ({counter}) - Page Table: {printQueue(pgQueue)}, Frames: [{pgQueue.qsize()}], Faults: {faults}")
        print(f"Total faults: {faults}")

    print("\n")

# Function to display elements in a queue
def printQueue(q):
    qList = []
    tempQ = Queue()

    # Iterate through the queue and add it to the list which will
    # be displayed. We also use a temp queue because we need to
    # restore the original queue back to how it was. Popping the
    # values from a queue empties up the queue.
    while not q.empty():
        qItem = q.get()
        qList.append(qItem)
        tempQ.put(qItem)

    # We add all the elements from the temp queue back to the
    # original queue.
    while not tempQ.empty():
        q.put(tempQ.get())

    return qList

# Define main function
def main():
    while True:
        try:
            # Take input of values
            # pgSample = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
            sampleInput = input("Enter sample values w/o commas (q to quit): ")

            if sampleInput == 'q':
                quit()

            pgSample = sampleInput.split()
            pgSample = [int(i) for i in pgSample]

            frames = int(input("Enter no of frames: "))
            pgNo = len(pgSample)

            print("\n")

            # Call LRU algorithm
            print("LRU Algorithm: \n")
            lruAlgorithm(frames, pgSample)

            # Call Optimal algorithm
            print("Optimal Algorithm: \n")
            optAlgorithm(frames, pgSample, pgNo)

            # Call FIFO algorithm
            print("FIFO Algorithm: \n")
            fifoAlgorithm(frames, pgSample, pgNo)
        
        except ValueError:
            print("Invalid input! Only numbers only!")

if __name__ == "__main__":
    main()