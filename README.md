Coding challenge - Solving Maze problem

This is a challenge that requires you to construct a program that will complete a maze. Your program may access each step of the maze from a URL which returns information encoded in JSON format. This information includes the following:

letter: the letter corresponding to this step within the maze
adjacent: an array of objects encoding x and y coordinates for steps that are immediately adjacent to this step
end: if the current step is the end, this value will be true. Otherwise it is false.
The URL is located at /step and has the following parameters:

x: the x coordinate of the step
y: the y coordinate of the step
s: the maze identifier, this parameter should be kept constant between step requests for the same maze
/start will redirect your program to the (0, 0) coordinate of a new random maze.

Your goal is to write a program that begins at the /start URL and traverse the maze until you reach the step where end is true. You should record each letter at each step in the path and print the resulting string at the end of your program.

You may check your solution by calling /check with s set to the maze identifier and guess set to the string your program thinks is a potential solution.

For example: pqkefzvymrbtfqntnqkrdipik is a solution for maze identifier 123456.5. The check endpoint returns a successful response for: /check?s=123456.5&guess=pqkefzvymrbtfqntnqkrdipik. Note that another, shorter solution is also possible for this identifer pqkefzvymrbtfqkrdik.

Notes
1. There is more than one path to the end of each maze, so there is more than one potential solution.
2. If your program backtracks, it must include letters contained on the backtracking path in the output solution. For example, consider two steps of a maze where (1,1) is set to a and (1,2) is set to b, if your program traverses from (1,1) to (1,2) then back (1,1), the solution string should contain aba for that segment.
3. No maze will contain loops.
4. Mazes are always square but their dimensions may vary.
5. You may use any language to write the program, the only caveat is that it must be buildable and runnable on common, modern operating systems. We don’t accept pseudo-code.
