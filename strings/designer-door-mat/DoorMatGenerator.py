# Enter your code here. Read input from STDIN. Print output to STDOUT
def generate_door_mat(mat_size, mat_width):
    rows_above_welcome = (mat_size - 1) // 2
    for i in range(rows_above_welcome):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(mat_width, '-'))
    welcome_line = 'WELCOME'.center(mat_width, '-')
    print(welcome_line)
    for i in range(rows_above_welcome - 1, -1, -1):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(mat_width, '-'))

mat_size, mat_width = map(int, input().split())
generate_door_mat(mat_size, mat_width)
