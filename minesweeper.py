def mine_sweeper(bombs , n_rows , n_cols):
    fields = [[0 for i in range (n_cols)] for j in range (n_rows)]

    for bomb_loc in bombs:
        (b_rows , b_cols) = bomb_loc
        fields[b_rows][b_cols] = -1

        r_range = range (b_rows - 1 , b_rows + 2)
        c_range = range (b_cols - 1 , b_cols + 2)

        for i in (r_range):
            for j in (c_range):
                if( 0 <= i < n_rows and 0 <= j < n_cols and fields[i][j] != -1):
                    fields[i][j] += 1
    return fields

print(mine_sweeper([[0,0] , [1,2]], 3, 4))