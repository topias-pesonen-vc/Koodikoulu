# https://dmoj.ca/problem/wc16c1j1 - A Spooky Season
def spooky():
    n = int(input())
    spookers = n*"o"
    print(f"sp{spookers}ky")

#spooky()


# https://dmoj.ca/problem/wc15c2j1 - A New Hope
def faraway():
    n = int(input())
    #far_string = " ".join(["far, "]*(n-1))
    #far_string = far_string + "far"
    far_string = ", ".join(["far"]*n)

    print(f"A long time ago in a galaxy {far_string} away...")
#faraway()

# https://dmoj.ca/problem/ccc13j1 - Next in Line
def age_diff():
   f = int(input())
   s = int(input())

   diff = s - f 

   print(s + diff)

#age_diff()

# https://dmoj.ca/problem/wc17c1j2 - How's the Weather?
def freedom_temp():
    C = int(input())

    # C = 5 / 9 * (F - 32)
    # F = (C * 9) / 5 + 32
    F = (C * 9) / 5 + 32
    print(int(F)) 

#freedom_temp()

# https://dmoj.ca/problem/wc18c3j1 - An Honest Day's Work
def pokedollars():
    P = int(input())
    B = int(input())
    D = int(input())

    badges_crafted =  P // B
    leftover_paint = P - badges_crafted * B

    badge_profit = badges_crafted * D

    print(badge_profit + leftover_paint)
#pokedollars()

# https://dmoj.ca/problem/ccc06j1 - Canadian Calorie Counting
def calories():
    burgers = {1:461, 2: 431, 3:420, 4:0}
    sides = {1:100, 2: 57, 3:70, 4:0}
    drinks = {1:130, 2: 160, 3:118, 4:0}
    desserts = {1:167, 2: 266, 3:75, 4:0}

    b = int(input())
    s = int(input())
    d = int(input())
    de = int(input())
    print(f"Your total Calorie count is {burgers[b] + sides[s] + drinks[d] + desserts[de]}.")

#calories()
# https://dmoj.ca/problem/ccc15j1 - Special Day
def special_day():
    first = int(input())
    second = int(input())

    if first == 1 or (first == 2 and second < 18):
        print("Before")
    elif first == 2 and second == 18:
        print("Special")
    else:
        print("After")

special_day()    

# https://dmoj.ca/problem/ccc15j2 - Happy or Sad
# https://dmoj.ca/problem/dmopc16c1p0 - C.C. and Cheese-kun
# https://dmoj.ca/problem/ccc07j1 - Who is in the Middle

# https://dmoj.ca/problem/wc17c3j3 - Uncrackable
# https://dmoj.ca/problem/coci18c3p1 - Magnus
# https://dmoj.ca/problem/ccc11s1 - English or French
# https://dmoj.ca/problem/ccc11s2 - Multiple Choice
# https://dmoj.ca/problem/coci12c5p1 - Ljestvica
# https://dmoj.ca/problem/coci13c3p1 - Rijeci
# https://dmoj.ca/problem/coci18c4p1 - Elder

# https://dmoj.ca/problem/ccc20j2 - Epidemiology
# https://dmoj.ca/problem/coci08c1p2 - Ptice
# https://dmoj.ca/problem/ccc02j2 - AmeriCanadian
# https://dmoj.ca/problem/ecoo13r1p1 - Take a Number
# https://dmoj.ca/problem/ecoo15r1p1 - When You Eat Your Smarties
# https://dmoj.ca/problem/ccc19j3 - Cold Compress

# https://dmoj.ca/problem/ccc07j3 - Deal or No Deal Calculator
# https://dmoj.ca/problem/coci17c1p1 - Cezar
# https://dmoj.ca/problem/coci18c2p1 - Preokret
# https://dmoj.ca/problem/ccc00s2 - Babbling Brooks
# https://dmoj.ca/problem/ecoo18r1p1 - Willow's Wild Ride
# https://dmoj.ca/problem/ecoo19r1p1 - Free Shirts
# https://dmoj.ca/problem/dmopc14c7p2 - Tides
# https://dmoj.ca/problem/wac3p3 - Wesley Plays DDR
# https://dmoj.ca/problem/ecoo18r1p2 - Rue's Rings
# https://dmoj.ca/problem/coci19c5p1 - Emacs
# https://dmoj.ca/problem/coci20c2p1 - Crtanje
# https://dmoj.ca/problem/dmopc19c5p2 - Charlie's Crazy Conquest

# https://dmoj.ca/problem/ccc13s1 - From 1987 to 2013
# https://dmoj.ca/problem/ccc18j3 - Are we there yet?
# https://dmoj.ca/problem/ecoo12r1p2 - Decoding DNA
# https://dmoj.ca/problem/crci07p1 - Platforme
# https://dmoj.ca/problem/coci13c2p2 - Misa

# http://www.usaco.org/index.php?page=viewproblem2&cpid=855 - Mixing Milk
# http://www.usaco.org/index.php?page=viewproblem2&cpid=711 - Why Did the Cow Cross the Road
# http://www.usaco.org/index.php?page=viewproblem2&cpid=735 - The Lost Cow
# http://www.usaco.org/index.php?page=viewproblem2&cpid=963 - Cow Gymnastics
# http://www.usaco.org/index.php?page=viewproblem2&cpid=736 - Bovine Genomics
# http://www.usaco.org/index.php?page=viewproblem2&cpid=831 - Team Tic Tac Toe
# http://www.usaco.org/index.php?page=viewproblem2&cpid=918 - Sleepy Cow Herding

# https://dmoj.ca/problem/crci06p1 - Bard
# https://dmoj.ca/problem/dmopc19c5p1 - Conspicuous Cryptic Checklist
# https://dmoj.ca/problem/coci15c2p1 - Marko
# https://dmoj.ca/problem/ccc06s2 - Attack of the CipherTexts
# https://dmoj.ca/problem/dmopc19c3p1 - Mode Finding
# https://dmoj.ca/problem/coci14c2p2 - Utrka
# https://dmoj.ca/problem/coci17c2p2 - ZigZag

# http://www.usaco.org/index.php?page=viewproblem2&cpid=891 - Shell Game
# http://www.usaco.org/index.php?page=viewproblem2&cpid=639 - Diamond Collector
# https://dmoj.ca/problem/coci20c1p1 - Patkice
# https://dmoj.ca/problem/ccc09j2 - Old Fishin' Hole
# https://dmoj.ca/problem/ecoo16r1p2 - Spindie
# https://dmoj.ca/problem/cco96p2 - SafeBreaker
# http://www.usaco.org/index.php?page=viewproblem2&cpid=964 - Where Am I
# http://www.usaco.org/index.php?page=viewproblem2&cpid=592 - Angry Cows
# http://www.usaco.org/index.php?page=viewproblem2&cpid=666 - Counting Haybales
# https://dmoj.ca/problem/crci06p3 - Firefly