MIN_H = 2800
MAX_H = 2852

content = open("quetions.txt").read()

question_height = content.split("\n")
list_qh = [(key, int(float(value))) for key, value in [q_h.split(" ") for q_h in question_height]]
list_qh.sort(key=lambda x: x[1], reverse=True)

QUESTION_ID = [x[0] for x in list_qh]
HEIGHTS = [x[1] for x in list_qh]
QUESTION_COUNT = len(QUESTION_ID)

# print(HEIGHTS)

# print(QUESTION_COUNT)

page = []
page_count = 1000
line_count = page_count * MAX_H

current_page = []
current_line_left = []


def solve(index):
    # print("Run", index)
    global page, page_count, line_count
    global current_page, current_line_left


    queue = []

    if index == QUESTION_COUNT:
        if max(current_line_left) <= 52:
            if len(current_page) < page_count:
                page = [p.copy() for p in current_page]
                page_count = len(current_page)
                line_count = sum(current_line_left)
                print(current_line_left)
            elif len(current_page) == page_count and sum(current_line_left) < line_count:
                page = [p.copy for p in current_page]
                page_count = len(current_page)
                line_count = sum(current_line_left)
                print(current_line_left)

        return 0

    i = 0
    while i < index and i < len(current_page):
        if HEIGHTS[index] < current_line_left[i]:
            queue.append(i)
        i += 1
    if not queue:
        queue.append(i)
    while queue:
        choice = queue.pop(0)

        if choice + 1 > len(current_page):
            current_page.append([index])
            current_line_left.append(2852 - HEIGHTS[index])
        elif choice + 1 <= len(current_page):
            current_page[choice].append(index)
            current_line_left[choice] -= HEIGHTS[index]

        solve(index + 1)

        if page:
            return 0

        current_page[choice].pop(-1)
        current_line_left[choice] += HEIGHTS[index]

        if not current_page[choice]:
            current_page.pop(choice)
            current_line_left.pop(choice)
    return 0

solve(0)
print(page)
print(page_count)
print(line_count)


