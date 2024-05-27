# Clinicer Sukkasaippua koodikoulu

Steps to get started.

- Create an account at: https://dmoj.ca/
- Create github account and fork the repo. Then clone it locally and push your changes to the master. We will go over your solutions in your own repo. If you need help with this hit me up.
- Start with part 1 of the koodingschool.

## Format of answers:

For each submission have one function with all the necessary logic.

```python
def spooky_season(inp=None):
    if inp:
        inputti = inp
    else:
        inputti = int(input())
    print(f"sp{inputti * 'o'}ky")


spooky_season(5)

```
With this you can just copy the solution to the dmoj website and call it with different test inputs on your local environment.
When finished comment out the function call.

### Catching input:

for one line its just inputti = input()

For 4 lines input.
```python
inputti = [input() for x in range(4)]
```

Then you can destructure
```python
months, days, years, players = inputti
```

## Part 1: Learning to code by solving problems.

There will be python modules with urls to DMOJ competitive programming problems. You're job is to solve those problems and then we will go through the solutions together.

## Favela-GPT rules:
 - Never ever include the actual problem in the question.

## Allowed questions:
 - "With python how to get 3rd element from list"
 - "How to get all unique elements from a list"


## Python environments, virtual environments, imports, dependency handling and packaging. 
 - Will do in future.


## Data-Engineering concepts.
 - Future

## Python and Fabric
 - Future