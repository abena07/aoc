# advent of code

this repo is where i track my advent of code progress starting from 2025. the goal is to get better at problem solving and learn new languages while having fun with these puzzles.

## project structure

```
AOC/
├── 2024/
│   └── day{n}/
├── 2025/
│   └── day{n}/
│       ├── py/
│       │   ├── part1.py
│       │   ├── part2.py
│       │   └── config.py
│       ├── input.txt
│       ├── sample.txt
│       └── question.md
└── README.md
```

each day contains the input, sample test cases, problem description, and my solutions.

## my approach

for 2025, i’m solving everything in python first and then rewriting it in c++. converting between the two helps me fully understand the logic instead of relying on whatever happens to work.

eventually, i want to solve directly in c++ and port the solution to another language the following year.

## how to run my solutions

i keep things simple.

### python

go into the year and day folder, then run the file:

```
cd 2025/day1/py
python3 part1.py
python3 part2.py
```

or, if i ever add a combined runner:

```
python3 run.py
```

### c++

once i start pushing c++ versions:

```
cd 2025/day1/cpp
g++ part1.cpp -o part1
./part1
```

### inputs

every folder has:

* `input.txt` → the real puzzle input
* `sample.txt` → the example from the problem
* the scripts read from these by default

so i don’t need to paste stuff every time.

## how i work

i try not to depend on ai for the solutions themselves. when i get stuck, i ask friends on discord. if i use ai, it is to clarify concepts or help me think through something the way an interviewer would.

## accountability

this repo keeps me honest. it helps me track my daily progress, see how my thinking evolves, and compare my python and c++ solutions side by side.

## license

mit license
