# Python Learning

A simple four-week path for learning Python by writing small programs. Use only this course, VS Code, Python, and GitHub for now. Aim for 20–30 minutes a session. It is fine if a week takes longer than a week.

## Your setup

- **Watch lessons:** [Python for Everybody video lessons](https://www.py4e.com/lessons). Open the linked lesson page and use its Videos section.
- **Write code:** In VS Code, open this `python-learning` folder. Save each practice file in `exercises` with the filename listed below.
- **Run code:** Open the file, then click the triangle ▶ in the top-right. Type any answer the program asks for in the Terminal panel.
- **Save your progress:** VS Code can save automatically with **File → Auto Save**. Git commits are checkpoints you can return to.

For each session: watch only the assigned video (pause when useful), type the example yourself, then do the small practice task without copying the answer. If you get stuck, try for 10 minutes, reread the error, and make one small change. It is okay to look up an explanation after trying.

## Four-week plan

### Week 1 — Understand programs

1. Watch [Why Program? Part 1](https://www.py4e.com/lessons/intro), then change and run `projects/first_program.py` again.
2. Watch **Why Program? Part 2** on the same lesson page. Make `exercises/day02_print.py` print three things you like.
3. Watch **Why Program? Part 3**. Make `exercises/day03_input.py` ask for a favorite food and print a reply.
4. Watch **Why Program? Part 4**. In `exercises/day04_math.py`, print the answers to two sums you choose.
5. In `exercises/day05_review.py`, combine `input()` and `print()` to ask a question and reply. Run it twice with different answers.

### Week 2 — Variables and text

Use [Variables, Expressions and Statements](https://www.py4e.com/lessons/memory).

6. Watch Part 1. In `exercises/day06_variables.py`, store your name in a variable and print it.
7. Watch Part 2. In `exercises/day07_math.py`, ask for two numbers and add them. (Use `int(input(...))` to turn the answer into a whole number.)
8. Watch **Worked Exercise 2.2**. Try the exercise yourself in `exercises/day08_exercise.py` before watching the solution.
9. Watch **Worked Exercise 2.3**. Try it yourself in `exercises/day09_exercise.py` first.
10. Make `exercises/day10_tip.py`: ask for a bill amount and tip percent, then print the tip. Ask someone to try it.

### Week 3 — Decisions and reusable code

Use [Conditional Execution](https://www.py4e.com/lessons/logic) and [Functions](https://www.py4e.com/lessons/functions). Both pages have short videos and worked exercises.

11. Watch Conditional Execution Part 1. In `exercises/day11_compare.py`, ask for a number and say whether it is positive.
12. Watch Conditional Execution Part 2. In `exercises/day12_age.py`, ask for an age and respond differently based on the answer.
13. Watch **Worked Exercise 3.1**. Try it first in `exercises/day13_conditionals.py`.
14. Watch Functions Part 1. In `exercises/day14_greeting.py`, write a function that greets someone by name.
15. Watch Functions Part 2. In `exercises/day15_temperature.py`, write a function that converts Celsius to Fahrenheit.

### Week 4 — Loops and your first project

Use [Loops and Iterations](https://www.py4e.com/lessons/loops).

16. Watch Loops Part 1. In `exercises/day16_for_loop.py`, print the numbers 1 to 10 with a loop.
17. Watch Loops Part 2. In `exercises/day17_total.py`, use a loop to add three numbers.
18. Watch Loops Part 3. In `exercises/day18_guess.py`, make a number guessing game. Start with a fixed secret number like `7`.
19. Watch Loops Part 4. Improve the guessing game so it repeats until the guess is right.
20. Use `projects/first_project.py` to make your own small quiz or guessing game. Add instructions at the top as comments and explain the program to someone.

If a session feels hard, repeat it the next time. Finishing slowly is still finishing.

## Put your project on GitHub

GitHub is an online place to keep a backup of your code. You can wait until you have done a few exercises; no rush.

1. Go to [github.com](https://github.com) and create an account or sign in.
2. Click **New repository**. Name it `python-learning`, select **Private** (only you can see it), and leave **Add a README** unchecked. Click **Create repository**.
3. In VS Code, choose **Terminal → New Terminal**. The terminal should be in this `python-learning` folder. If not, open the folder again with **File → Open Folder**.
4. Run each command below one at a time. Replace `YOUR-USERNAME` with your GitHub username:

```powershell
git add .
git commit -m "Start Python learning"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/python-learning.git
git push -u origin main
```

If Git says it needs your name or email, set them with the commands below (use your own name and the email on your GitHub account), then repeat the commit command:

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

GitHub may open a browser to sign you in. For future sessions, after finishing an exercise, run:

```powershell
git add .
git commit -m "Practice loops"
git push
```

Change the commit message to describe what you practiced. The files remain on your computer even if you have not uploaded them yet.

## Keep learning simple

- Main course: [Python for Everybody](https://www.py4e.com/lessons). Follow only the videos assigned above.
- VS Code help, if you need it: [Getting started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial).
- GitHub help, if you need it: [GitHub Skills](https://skills.github.com/).

You can learn on your own with this plan. Ask for help whenever you want; include the file, the error message, and what you expected to happen.
