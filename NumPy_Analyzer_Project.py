import numpy as np


class DataAnalytics:
    def __init__(self):
        self.arr = None

    @staticmethod
    def show_array(arr):
        print("\nArray:")
        print(arr)
        print("Shape:", arr.shape)
        print("Dimensions:", arr.ndim)
        print("Size:", arr.size)

    def create_array(self):
        print("\nCreate NumPy Array")
        print("1. One-dimensional array")
        print("2. Two-dimensional array")
        print("3. Three-dimensional array")

        choice = input("Choose array type (1-3): ").strip()

        try:
            if choice == "1":
                values = input("Enter numbers separated by spaces: ").split()
                self.arr = np.array([float(x) for x in values])
            elif choice == "2":
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))
                values = input(
                    f"Enter {rows * cols} numbers separated by spaces: "
                ).split()
                if len(values) != rows * cols:
                    print("Error: You entered the wrong number of values.")
                    return
                self.arr = np.array([float(x) for x in values]).reshape(rows, cols)
            elif choice == "3":
                layers = int(input("Enter number of layers: "))
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))
                total = layers * rows * cols
                values = input(f"Enter {total} numbers separated by spaces: ").split()
                if len(values) != total:
                    print("Error: You entered the wrong number of values.")
                    return
                self.arr = np.array([float(x) for x in values]).reshape(
                    layers, rows, cols
                )
            else:
                print("Invalid choice.")
                return

            self.show_array(self.arr)
        except ValueError:
            print("Please enter valid numbers and positive dimensions.")
        except Exception as error:
            print("Could not create array:", error)

    def check_array(self):
        if self.arr is None:
            print("Please create an array first.")
            return False
        return True

    def indexing_slicing(self):
        if not self.check_array():
            return

        print("\nCurrent array:")
        print(self.arr)
        print("Use comma-separated indexes for multiple dimensions.")
        raw = input("Enter index (example: 0 or 0,1): ").strip()

        try:
            indexes = tuple(int(x.strip()) for x in raw.split(","))
            print("Selected value:", self.arr[indexes])
        except (ValueError, IndexError):
            print("Invalid index.")

        if self.arr.ndim == 1:
            raw_slice = input("Enter slice start:stop (example: 1:4): ").strip()
            try:
                start_text, stop_text = raw_slice.split(":")
                start = int(start_text) if start_text else None
                stop = int(stop_text) if stop_text else None
                print("Sliced array:", self.arr[start:stop])
            except ValueError:
                print("Invalid slice format.")

    def mathematical_operations(self):
        if not self.check_array():
            return

        print("\nMathematical Operations")
        print("1. Add a number")
        print("2. Subtract a number")
        print("3. Multiply by a number")
        print("4. Divide by a number")
        print("5. Dot product (1D arrays)")
        print("6. Matrix multiplication (2D arrays)")
        choice = input("Choose operation (1-6): ").strip()

        try:
            if choice in {"1", "2", "3", "4"}:
                value = float(input("Enter a number: "))
                if choice == "1":
                    result = self.arr + value
                elif choice == "2":
                    result = self.arr - value
                elif choice == "3":
                    result = self.arr * value
                else:
                    if value == 0:
                        print("Cannot divide by zero.")
                        return
                    result = self.arr / value
                print("Result:\n", result)
            elif choice == "5":
                if self.arr.ndim != 1:
                    print("Dot product requires a one-dimensional current array.")
                    return
                other = np.array(
                    [float(x) for x in input("Enter second array values: ").split()]
                )
                if other.ndim != 1 or len(other) != len(self.arr):
                    print("Both arrays must have the same length.")
                    return
                print("Dot product:", np.dot(self.arr, other))
            elif choice == "6":
                if self.arr.ndim != 2:
                    print("Matrix multiplication requires a 2D current array.")
                    return
                rows = int(input("Enter rows of second matrix: "))
                cols = int(input("Enter columns of second matrix: "))
                values = [
                    float(x)
                    for x in input(f"Enter {rows * cols} values: ").split()
                ]
                if len(values) != rows * cols:
                    print("Wrong number of values.")
                    return
                other = np.array(values).reshape(rows, cols)
                print("Result:\n", np.matmul(self.arr, other))
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter valid numbers.")
        except Exception as error:
            print("Operation failed:", error)

    def combine_split(self):
        if not self.check_array():
            return

        print("\nCombine or Split Arrays")
        print("1. Combine with another 1D array")
        print("2. Split current 1D array into two parts")
        choice = input("Choose (1-2): ").strip()

        try:
            if choice == "1":
                if self.arr.ndim != 1:
                    print("Combining is available here for 1D arrays only.")
                    return
                values = input("Enter other array values separated by spaces: ").split()
                other = np.array([float(x) for x in values])
                self.arr = np.concatenate((self.arr, other))
                self.show_array(self.arr)
            elif choice == "2":
                if self.arr.ndim != 1 or len(self.arr) < 2:
                    print("Splitting requires a 1D array with at least two values.")
                    return
                middle = int(input("Split position: "))
                if not 0 < middle < len(self.arr):
                    print("Split position must be between 1 and array size - 1.")
                    return
                first, second = np.split(self.arr, [middle])
                print("First part:", first)
                print("Second part:", second)
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter valid values.")
        except Exception as error:
            print("Operation failed:", error)

    def search_sort_filter(self):
        if not self.check_array():
            return

        print("\nSearch, Sort, or Filter")
        print("1. Search for a value")
        print("2. Sort array")
        print("3. Filter values greater than a number")
        choice = input("Choose (1-3): ").strip()

        try:
            if choice == "1":
                value = float(input("Enter value to search: "))
                positions = np.argwhere(self.arr == value)
                if positions.size:
                    print("Found at index/indices:", positions.tolist())
                else:
                    print("Value not found.")
            elif choice == "2":
                self.arr = np.sort(self.arr, axis=None).reshape(self.arr.shape)
                self.show_array(self.arr)
            elif choice == "3":
                value = float(input("Show values greater than: "))
                print(self.arr[self.arr > value])
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")
        except Exception as error:
            print("Operation failed:", error)

    def statistics(self):
        if not self.check_array():
            return

        print("\nArray Statistics")
        print("Sum:", np.sum(self.arr))
        print("Mean:", np.mean(self.arr))
        print("Median:", np.median(self.arr))
        print("Standard deviation:", np.std(self.arr))
        print("Variance:", np.var(self.arr))
        print("Minimum:", np.min(self.arr))
        print("Maximum:", np.max(self.arr))
        percentile = float(input("Enter percentile (0-100): "))
        if 0 <= percentile <= 100:
            print(f"{percentile:g}th percentile:", np.percentile(self.arr, percentile))
        else:
            print("Percentile must be between 0 and 100.")

        if self.arr.ndim == 1 and len(self.arr) >= 2:
            print("Correlation needs a second array.")
            answer = input("Calculate correlation? (y/n): ").strip().lower()
            if answer == "y":
                try:
                    values = [
                        float(x)
                        for x in input("Enter same number of values: ").split()
                    ]
                    other = np.array(values)
                    if len(other) != len(self.arr):
                        print("The arrays must have the same length.")
                    else:
                        print("Correlation matrix:\n", np.corrcoef(self.arr, other))
                except ValueError:
                    print("Please enter valid numbers.")

    def run(self):
        while True:
            print("\n========== NUMPY ANALYZER ==========")
            print("1. Create a NumPy Array")
            print("2. Indexing and Slicing")
            print("3. Mathematical Operations")
            print("4. Combine or Split Arrays")
            print("5. Search, Sort, or Filter")
            print("6. Aggregates and Statistics")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ").strip()

            if choice == "1":
                self.create_array()
            elif choice == "2":
                self.indexing_slicing()
            elif choice == "3":
                self.mathematical_operations()
            elif choice == "4":
                self.combine_split()
            elif choice == "5":
                self.search_sort_filter()
            elif choice == "6":
                try:
                    self.statistics()
                except ValueError:
                    print("Please enter a valid number.")
                except Exception as error:
                    print("Could not calculate statistics:", error)
            elif choice == "7":
                print("Thank you for using NumPy Analyzer!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    app = DataAnalytics()
    app.run()
