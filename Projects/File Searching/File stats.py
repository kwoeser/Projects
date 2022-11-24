# Author: Karma Woeser
# word stats lab

# Variables
count = 0
A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
G = 0
H = 0
I = 0
J = 0
K = 0
L = 0
M = 0
N = 0
O = 0
P = 0
Q = 0
R = 0
S = 0
T = 0
U = 0
V = 0
W = 0
X = 0
Y = 0
Z = 0
other = 0
palindromes = 0
longest_word = ''
shortest_word = ''
short = 101

while True:
    open_file = open('words_alpha.txt')
    

    for line in open_file:
        line = line.strip()
        count += 1

        # Finds the longest word
        if len(line) > len(longest_word):
            longest_word = line

        # Finds the shortest word
        if len(line) < short:
            short = len(line)
            shortest_word = line


       # Reverse each line and checks if they are palindromes
        reverse = line[::-1]
        if line == reverse:
            palindromes += 1


        # If the letter is the letter in the line it will add 1 to it's variable
        if 'a' in line[0]:
            A += 1
        elif 'b' in line[0]:
            B += 1
        elif 'c' in line[0]:
            C += 1
        elif 'd' in line[0]:
            D += 1
        elif 'e' in line[0]:
            E += 1
        elif 'f' in line[0]:
            F += 1
        elif 'g' in line[0]:
            G += 1
        elif 'h' in line[0]:
            H += 1
        elif 'i' in line[0]:
            I += 1
        elif 'j' in line[0]:
            J += 1
        elif 'k' in line[0]:
            K += 1
        elif 'l' in line[0]:
            L += 1
        elif 'm' in line[0]:
            M += 1
        elif 'n' in line[0]:
            N += 1
        elif 'o' in line[0]:
            O += 1
        elif 'p' in line[0]:
            P += 1
        elif 'q' in line[0]:
            Q += 1
        elif 'r' in line[0]:
            R += 1
        elif 's' in line[0]:
            S += 1
        elif 't' in line[0]:
            T += 1
        elif 'u' in line[0]:
            U += 1
        elif 'v' in line[0]:
            V += 1
        elif 'w' in line[0]:
            W += 1
        elif 'x' in line[0]:
            X += 1
        elif 'y' in line[0]:
            Y += 1
        elif 'z' in line[0]:
            Z += 1
        
        else:
            other += 1
            
    open_file.close()

    # Finds the percentages and rounds them by 2
    A_percentage = round((A / count) * 100, 2)
    B_percentage = round((B / count) * 100, 2)
    C_percentage = round((C / count) * 100, 2)
    D_percentage = round((D / count) * 100, 2)
    E_percentage = round((E / count) * 100, 2)
    F_percentage = round((F / count) * 100, 2)
    G_percentage = round((G / count) * 100, 2)
    H_percentage = round((H / count) * 100, 2)
    I_percentage = round((I / count) * 100, 2)
    J_percentage = round((J / count) * 100, 2)
    K_percentage = round((K / count) * 100, 2)
    L_percentage = round((L / count) * 100, 2)
    M_percentage = round((M / count) * 100, 2)
    N_percentage = round((N / count) * 100, 2)
    O_percentage = round((O / count) * 100, 2)
    P_percentage = round((P / count) * 100, 2)
    Q_percentage = round((Q / count) * 100, 2)
    R_percentage = round((R / count) * 100, 2)
    S_percentage = round((S / count) * 100, 2)
    T_percentage = round((T / count) * 100, 2)
    U_percentage = round((U / count) * 100, 2)
    V_percentage = round((V / count) * 100, 2)
    W_percentage = round((W / count) * 100, 2)
    X_percentage = round((X / count) * 100, 2)
    Y_percentage = round((Y / count) * 100, 2)
    Z_percentage = round((Z / count) * 100, 2)
    other_percentage = round((other / count) * 100, 2)
    palindromes_percentage = round((palindromes / count) * 100, 2)



    # Prints everything using .format then ends the while loop
    print("Count:", count)
    print("Longest word is", longest_word, '({})'.format(len(longest_word)))
    print("Shortest word is", shortest_word,'({})'.format(len(shortest_word)))
    print("Palindromes:", palindromes, '({}%)'.format(palindromes_percentage))
    print("First Letter Counts")
    print("A:", A, "({}%)".format(A_percentage))
    print("B:", B, "({}%)".format(B_percentage))
    print("C:", C, "({}%)".format(C_percentage))
    print("D:", D, "({}%)".format(D_percentage))
    print("E:", E, "({}%)".format(E_percentage))
    print("F:", F, "({}%)".format(F_percentage))
    print("G:", G, "({}%)".format(G_percentage))
    print("H:", H, "({}%)".format(H_percentage))
    print("I:", I, "({}%)".format(I_percentage))
    print("J:", J, "({}%)".format(J_percentage))
    print("K:", K, "({}%)".format(K_percentage))
    print("L:", L, "({}%)".format(L_percentage))
    print("M:", M, "({}%)".format(M_percentage))
    print("N:", N, "({}%)".format(N_percentage))
    print("O:", O, "({}%)".format(O_percentage))
    print("P:", P, "({}%)".format(P_percentage))
    print("Q:", Q, "({}%)".format(Q_percentage))
    print("R:", R, "({}%)".format(R_percentage))
    print("S:", S, "({}%)".format(S_percentage))
    print("T:", T, "({}%)".format(T_percentage))
    print("U:", U, "({}%)".format(U_percentage))
    print("V:", V, "({}%)".format(V_percentage))
    print("W:", W, "({}%)".format(W_percentage))
    print("X:", X, "({}%)".format(X_percentage))
    print("Y:", Y, "({}%)".format(Y_percentage))
    print("Z:", Z, "({}%)".format(Z_percentage))
    print("Other:", other, "({}%)".format(other_percentage))
    break


