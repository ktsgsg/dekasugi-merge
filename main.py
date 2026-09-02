def main():
    print("Hello from dekasugi-merge!")
    with open("oh_my_biggest_file.txt","a") as f:
        for i in range(999):
            for j in range(9999):
                f.write("dodge")
            f.write("\n")


if __name__ == "__main__":
    main()
