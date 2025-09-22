# Usign Loops
def count_frequency(arr):
    n = len(arr)
    visited = [False] * n

    highest_freq = 0
    lowest_freq = float("inf")
    highest_elem = None
    lowest_elem = None

    for i in range(n):
        if visited[i]:
            continue

        count = 1
        visited[i] = True

        for j in range(i+1, n):
            if arr[i] == arr[j] and not visited[j]:
                visited[j] = True
                count += 1

        print(f"{arr[i]} occurs {count} times")

        # Track highest
        if count > highest_freq:
            highest_freq = count
            highest_elem = arr[i]

        # Track lowest
        if count < lowest_freq:
            lowest_freq = count
            lowest_elem = arr[i]

    print("\nHighest frequency element:", highest_elem, f"({highest_freq} times)")
    print("Lowest frequency element:", lowest_elem, f"({lowest_freq} times)")


arr = [10, 5, 10, 15, 10, 5]
count_frequency(arr)

# Using Dictionary

def count_frequency(arr):
    freq = {}

    # Count frequencies
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Print all frequencies
    for num, count in freq.items():
        print(f"{num} occurs {count} times")

    # Highest and lowest frequency
    highest_elem = max(freq, key=freq.get)
    lowest_elem = min(freq, key=freq.get)

    print("\nHighest frequency element:", highest_elem, f"({freq[highest_elem]} times)")
    print("Lowest frequency element:", lowest_elem, f"({freq[lowest_elem]} times)")


arr = [10, 5, 10, 15, 10, 5]
count_frequency(arr)
