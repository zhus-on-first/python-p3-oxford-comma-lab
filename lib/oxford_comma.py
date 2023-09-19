def oxford_comma(items):
    if len(items) == 2:
        string = " and ".join(items)
    elif len(items) == 3:
        string = items[0] + ", " + items[1] + ", and " + items[-1]
    elif len(items) > 3:
        string = ", ".join(items[:-1]) + ", and " + items[-1]
    else:
        string = items[0]
    return string

    # string = " ".join(items)

    # for 2 items:
    #     item1 and item2

    # for items == 3:
    #     item1, item2, and item3
 