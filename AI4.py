""" Python3 program to solve N Queen Problem
using Branch or Bound """

N = 8

""" A utility function to print solution """
def printSolution(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j], end = " ")
		print()

""" A Optimized function to check if
a queen can be placed on board[row][col] """
def isSafe(row, col, slashCode, backslashCode,
		rowLookup, slashCodeLookup,
					backslashCodeLookup):
	if (slashCodeLookup[slashCode[row][col]] or
		backslashCodeLookup[backslashCode[row][col]] or
		rowLookup[row]):
		return False
	return True

""" A recursive utility function
to solve N Queen problem """
def solveNQueensUtil(board, col, slashCode, backslashCode,
					rowLookup, slashCodeLookup,
					backslashCodeLookup):
						
	""" base case: If all queens are
	placed then return True """
	if(col >= N):
		return True
	for i in range(N):
		if(isSafe(i, col, slashCode, backslashCode,
				rowLookup, slashCodeLookup,
				backslashCodeLookup)):
					
			""" Place this queen in board[i][col] """
			board[i][col] = 1
			rowLookup[i] = True
			slashCodeLookup[slashCode[i][col]] = True
			backslashCodeLookup[backslashCode[i][col]] = True
			
			""" recur to place rest of the queens """
			if(solveNQueensUtil(board, col + 1,
								slashCode, backslashCode,
								rowLookup, slashCodeLookup,
								backslashCodeLookup)):
				return True
			
			""" If placing queen in board[i][col]
			doesn't lead to a solution,then backtrack """
			
			""" Remove queen from board[i][col] """
			board[i][col] = 0
			rowLookup[i] = False
			slashCodeLookup[slashCode[i][col]] = False
			backslashCodeLookup[backslashCode[i][col]] = False
			
	""" If queen can not be place in any row in
	this column col then return False """
	return False

""" This function solves the N Queen problem using
Branch or Bound. It mainly uses solveNQueensUtil()to
solve the problem. It returns False if queens
cannot be placed,otherwise return True or
prints placement of queens in the form of 1s.
Please note that there may be more than one
solutions,this function prints one of the
feasible solutions."""
def solveNQueens():
	board = [[0 for i in range(N)]
				for j in range(N)]
	
	# helper matrices
	slashCode = [[0 for i in range(N)]
					for j in range(N)]
	backslashCode = [[0 for i in range(N)]
						for j in range(N)]
	
	# arrays to tell us which rows are occupied
	rowLookup = [False] * N
	
	# keep two arrays to tell us
	# which diagonals are occupied
	x = 2 * N - 1
	slashCodeLookup = [False] * x
	backslashCodeLookup = [False] * x
	
	# initialize helper matrices
	for rr in range(N):
		for cc in range(N):
			slashCode[rr][cc] = rr + cc
			backslashCode[rr][cc] = rr - cc + 7
	
	if(solveNQueensUtil(board, 0, slashCode, backslashCode,
						rowLookup, slashCodeLookup,
						backslashCodeLookup) == False):
		print("Solution does not exist")
		return False
		
	# solution found
	printSolution(board)
	return True

# Driver Code
solveNQueens()

# This code is contributed by SHUBHAMSINGH10

"""
// Java program to solve N Queen Problem
// using Branch and Bound
import java.io.*;
import java.util.Arrays;
 
class GFG{
 
static int N = 8;
 
// A utility function to print solution
static void printSolution(int board[][])
{
    int N = board.length;
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
            System.out.printf("%2d ", board[i][j]);
             
        System.out.printf("\n");
    }
}
 
// A Optimized function to check if a queen
// can be placed on board[row][col]
static boolean isSafe(int row, int col,
                      int slashCode[][],
                      int backslashCode[][],
                      boolean rowLookup[],
                      boolean slashCodeLookup[],
                      boolean backslashCodeLookup[])
{
    if (slashCodeLookup[slashCode[row][col]] ||
        backslashCodeLookup[backslashCode[row][col]] ||
        rowLookup[row])
        return false;
 
    return true;
}
 
// A recursive utility function to
// solve N Queen problem
static boolean solveNQueensUtil(
    int board[][], int col, int slashCode[][],
    int backslashCode[][], boolean rowLookup[],
    boolean slashCodeLookup[],
    boolean backslashCodeLookup[])
{
     
    // Base case: If all queens are placed
    // then return true
    int N = board.length;
     
    if (col >= N)
        return true;
 
    // Consider this column and try placing
    // this queen in all rows one by one
    for(int i = 0; i < N; i++)
    {
        // Check if queen can be placed on board[i][col]
        if (isSafe(i, col, slashCode, backslashCode,
                   rowLookup, slashCodeLookup,
                   backslashCodeLookup))
        {
             
            // Place this queen in board[i][col]
            board[i][col] = 1;
            rowLookup[i] = true;
            slashCodeLookup[slashCode[i][col]] = true;
            backslashCodeLookup[backslashCode[i][col]] = true;
 
            // recur to place rest of the queens
            if (solveNQueensUtil(
                    board, col + 1, slashCode,
                    backslashCode, rowLookup,
                    slashCodeLookup,
                    backslashCodeLookup))
                return true;
 
            // If placing queen in board[i][col] doesn't
            // lead to a solution, then backtrack
 
            // Remove queen from board[i][col]
            board[i][col] = 0;
            rowLookup[i] = false;
            slashCodeLookup[slashCode[i][col]] = false;
            backslashCodeLookup[backslashCode[i][col]] = false;
        }
    }
 
    // If queen can not be place in any row
    // in this column col then return false
    return false;
}
 
/*
 * This function solves the N Queen problem using Branch
 * and Bound. It mainly uses solveNQueensUtil() to solve
 * the problem. It returns false if queens cannot be
 * placed, otherwise return true and prints placement of
 * queens in the form of 1s. Please note that there may
 * be more than one solutions, this function prints one
 * of the feasible solutions.
 */
static boolean solveNQueens()
{
    int board[][] = new int[N][N];
     
    // Helper matrices
    int slashCode[][] = new int[N][N];
    int backslashCode[][] = new int[N][N];
 
    // Arrays to tell us which rows are occupied
    boolean[] rowLookup = new boolean[N];
 
    // Keep two arrays to tell us
    // which diagonals are occupied
    boolean slashCodeLookup[] = new boolean[2 * N - 1];
    boolean backslashCodeLookup[] = new boolean[2 * N - 1];
 
    // Initialize helper matrices
    for(int r = 0; r < N; r++)
        for(int c = 0; c < N; c++)
        {
            slashCode[r] = r + c;
            backslashCode[r] = r - c + 7;
        }
 
    if (solveNQueensUtil(board, 0, slashCode,
                         backslashCode, rowLookup,
                         slashCodeLookup,
                         backslashCodeLookup) == false)
    {
        System.out.printf("Solution does not exist");
        return false;
    }
     
    // Solution found
    printSolution(board);
    return true;
}
 
// Driver code
public static void main(String[] args)
{
    solveNQueens();
}
}
 
// This code is contributed by sujitmeshram
"""