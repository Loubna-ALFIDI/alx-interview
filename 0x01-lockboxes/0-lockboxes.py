#!/usr/bin/python3
""" lockboxes """


def canUnlockAll(boxes):
    """
    Function that determines if all the boxes in a list
    can be opened.
    """
    if not boxes:
        return False

    n = len(boxes)
    unlocked_boxes = [False] * n
    unlocked_boxes[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if 0 <= key < n and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)
