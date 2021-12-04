import numpy as np

def play_game(boards, masks, draws):
    for i, draw in enumerate(draws):
        win_axs = 0
        masks[np.where(boards == draw)] = True
        if np.all(masks, axis = 1).any() == True:
            win_axs = 1
        elif np.all(masks, axis = 2).any() == True:
            win_axs = 2
        if win_axs !=0:
            winning_board = np.where(np.all(masks, axis=win_axs) ==True )[0][0]
            winning_mask = np.squeeze(np.invert(masks[winning_board]))
            winning_sum = boards[winning_board,winning_mask].sum(dtype = np.int)
            # print(f'winner with draw {draw} and sum {winning_sum*winning_draw}')
            boards = np.delete(boards, winning_board, axis = 0)
            masks = np.delete(masks, winning_board, axis = 0)
            return(winning_sum * draw, boards, masks, draws[i:])


boards = np.zeros((500,5))

with open('input.txt', 'r') as file:
    draws = file.readline().rstrip()
    draws = draws.split(',')
    draws = np.array(draws, dtype = np.int)
    lines = filter(None, (line.rstrip() for line in file))
    for i, line in enumerate(lines):
        line = line.rstrip()
        a = line.split(' ')
        while '' in a:
            a.remove('')
        boards[i, :] = np.array(a, dtype = np.int)

boards = boards.reshape(100,5,5)
masks = np.zeros((100,5,5), dtype = np.bool)

sum, boards, masks, draws = play_game(boards, masks, draws)
print(f'first winning sum {sum}')
while len(boards) != 0:
    sum, boards, masks, draws= play_game(boards, masks, draws)
print(f'last winning sum: {sum}')

