import numpy as np

def play_game(boards, masks, draws):
    for i, draw in enumerate(draws):
        masks[np.where(boards == draw)] = True
        if np.all(masks, axis = 1).any() == True:
            winning_board = np.where(np.all(masks, axis=1) ==True )[0][0]
            winning_mask = np.squeeze(np.invert(masks[winning_board]))
            winning_sum = boards[winning_board,winning_mask].sum(dtype = np.int)
            winning_draw = draw
            print(f'winner after {i} draws with number {draw} on board {winning_board}')
            boards = np.delete(boards, winning_board, axis = 0)
            masks = np.delete(masks, winning_board, axis = 0)
            return(winning_sum * winning_draw, boards, masks, draws[i:])
        if np.all(masks, axis = 2).any() == True:
            winning_board = np.where(np.all(masks, axis=2) ==True )[0][0]
            winning_mask = np.squeeze(np.invert(masks[winning_board]))
            winning_sum = boards[winning_board,winning_mask].sum(dtype = np.int)
            winning_draw = draw
            print(f'winner after {i} draws with number {draw} on board {winning_board}')
            boards = np.delete(boards, winning_board, axis = 0)
            masks = np.delete(masks, winning_board, axis = 0)
            return(winning_sum * winning_draw, boards, masks, draws[i:])


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
print(sum)
while len(boards) != 0:
    sum, boards, masks, draws= play_game(boards, masks, draws)

print(sum)

