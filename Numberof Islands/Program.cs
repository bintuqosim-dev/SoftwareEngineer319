using System;

class Program
{
    static void Main(string[] args)
    {
        char[,] grid = {
            {'1', '1', '0', '0', '0'},
            {'1', '1', '0', '0', '0'},
            {'0', '0', '1', '0', '0'},
            {'0', '0', '0', '1', '1'}
        };

        Console.WriteLine("Number of Islands: " + NumIslands(grid));
    }

    public static int NumIslands(char[,] grid)
    {
        if (grid == null || grid.GetLength(0) == 0)
            return 0;

        int numIslands = 0;
        int rows = grid.GetLength(0);
        int cols = grid.GetLength(1);

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (grid[i, j] == '1')
                {
                    numIslands++;
                    DFS(grid, i, j);
                }
            }
        }

        return numIslands;
    }

    private static void DFS(char[,] grid, int i, int j)
    {
        int rows = grid.GetLength(0);
        int cols = grid.GetLength(1);

        if (i < 0 || i >= rows || j < 0 || j >= cols || grid[i, j] == '0')
            return;

        grid[i, j] = '0'; // Mark as visited

        DFS(grid, i - 1, j); // Up
        DFS(grid, i + 1, j); // Down
        DFS(grid, i, j - 1); // Left
        DFS(grid, i, j + 1); // Right
    }
}
