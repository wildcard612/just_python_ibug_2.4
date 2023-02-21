def main():
    just_list = (2 ** x for x in range(1, 21))
    return list(just_list)

if __name__ == '__main__':
    main()