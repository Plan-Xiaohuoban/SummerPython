def write_txt(filename):

    with open(filename, "w", encoding="utf-8") as f:
        for i in range(5):
            info = "Number " + str(i) + " is good.\n"
            f.write(info)

    print("Write file done.")


if __name__ == "__main__":
    write_txt("test.txt")
