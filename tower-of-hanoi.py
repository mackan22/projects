# Move a disk from a source peg to a destination peg, using an auxillary peg
def move(n, src, dst, aux):
    # Base case
    if n == 1:
        print("Move disk 1 from source", src, "to destination", dst)
    # Recursive case
    elif n > 1:
        move(n - 1, src, aux, dst)
        print("Move disk", n, "from source", src,"to destination", dst)
        move(n - 1, aux, dst, src)

# Move a tower of n disks from peg A to peg B
def hanoi(n):
    move(n, "A", "B", "C")
    
hanoi(4)