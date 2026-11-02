
def read_from_file(filename):
    flowers = []

    with open(filename, "r") as file:
        store_name = file.readline().strip()

        for line in file:
            data = line.strip().split(", ")

            name = data[0]
            color = data[1]
            height = int(data[2])
            price = float(data[3])

            flowers.append([name, color, height, price])

    return store_name, flowers


def count_tallest(flowers):
    tallest = flowers[0]

    for flower in flowers:
        if flower[2] > tallest[2]:
            tallest = flower

    return tallest[0]


def count_red(flowers1, flowers2):
    count = 0

    for flower in flowers1 + flowers2:
        if flower[1].lower() == "red":
            count += 1

    return count


def print_results(filename, store1, flowers1, store2, flowers2):
    with open(filename, "w") as file:
        file.write("Flower Store Results\n")
        file.write("--------------------\n")

        file.write(store1 + "\n")
        file.write("Tallest flower: " + count_tallest(flowers1) + "\n\n")

        file.write(store2 + "\n")
        file.write("Tallest flower: " + count_tallest(flowers2) + "\n\n")

        file.write(
            "Total number of red flowers: "
            + str(count_red(flowers1, flowers2))
            + "\n"
        )



store1, flowers1 = read_from_file("flowers1.txt")
store2, flowers2 = read_from_file("flowers2.txt")


print_results("results.txt", store1, flowers1, store2, flowers2)


print("Program completed successfully!")
print("Check results.txt for the answers.")
