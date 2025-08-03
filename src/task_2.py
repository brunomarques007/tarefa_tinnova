from rich import print


class BubbleSort:
    """Bubble Sort Algorithm Implementation"""

    def __init__(self, arr: list[int]):
        self.original = arr.copy()
        self.sorted_arr = []

    def sort(self) -> list[int]:
        """
        Sorts the array using the Bubble Sort algorithm with visual feedback.
        """
        arr = self.original
        n = len(arr)

        for i in range(n - 1):
            print(f'\n--- Iteration {i + 1} ---')
            swapped = False

            for j in range(n - 1 - i):
                print(f'Comparing ({arr[j]} {arr[j + 1]})', end=' ')
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    print('→ swapped')
                else:
                    print('→ kept')

                print('Current state:', arr)

            unsorted_part = arr[: n - 1 - i]
            sorted_part = [f'[{x}]' for x in arr[n - 1 - i :]]
            print('After iteration:', unsorted_part + sorted_part)

            if not swapped:
                break

        self.sorted_arr = arr
        return self.sorted_arr
