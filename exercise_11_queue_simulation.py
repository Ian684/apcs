def solve(operations):
    queue = []
    output = []
    for operation in operations:
        if operation[0] == "push": queue.append(operation[1])
        elif queue: output.append(queue.pop(0))
    return output

if __name__ == "__main__":
    print("Exercise: 11_queue_simulation")
