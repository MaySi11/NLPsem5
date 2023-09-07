sample1="""Game playing: IBM’s DEEP BLUE became the first computer program to defeat the
world champion in a chess match when it bested Garry Kasparov by a score of 3.5 to 2.5 in
an exhibition match (Goodman and Keene, 1997). Kasparov said that he felt a “new kind of
intelligence” across the board from him. Newsweek magazine described the match as “The
brain’s last stand.” The value of IBM’s stock increased by $18 billion. Human champions
studied Kasparov’s loss and were able to draw a few matches in subsequent years, but the
most recent human-computer matches have been won convincingly by the computer.
Spam fighting: Each day, learning algorithms classify over a billion messages as spam,
saving the recipient from having to waste time deleting what, for many users, could comprise
80% or 90% of all messages, if not classified away by algorithms. Because the spammers are
continually updating their tactics, it is difficult for a static programmed approach to keep up,
and learning algorithms work best (Sahami et al., 1998; Goodman and Heckerman, 2004).
Logistics planning: During the Persian Gulf crisis of 1991"""


sample2="""16.1 (Adapted from David Heckerman.) This exercise concerns the Almanac Game, which
is used by decision analysts to calibrate numeric estimation. For each of the questions that
follow, give your best guess of the answer, that is, a number that you think is as likely to be
too high as it is to be too low. Also give your guess at a 25th percentile estimate, that is, a
number that you think has a 25% chance of being too high, and a 75% chance of being too
low. Do the same for the 75th percentile. (Thus, you should give three estimates in all—low,
median, and high—for each question.)
a. Number of passengers who flew between New York and Los Angeles in 1989.
b. Population of Warsaw in 1992.
c. Year in which Coronado discovered the Mississippi River.
d. Number of votes received by Jimmy Carter in the 1976 presidential election.
e. Age of the oldest living tree, as of 2002.
"""

sample3="""Unfortunately, this approach is rather dangerous because there is no guarantee that the best
move will not be pruned away.
The P ROB C UT, or probabilistic cut, algorithm (Buro, 1995) is a forward-pruning version of alpha–beta search that uses statistics gained from prior experience to lessen the chance
that the best move will be pruned. Alpha–beta search prunes any node that is provably outside the current (α, β) window. P ROB C UT also prunes nodes that are probably outside the
window. It computes this probability by doing a shallow search to compute the backed-up
value v of a node and then using past experience to estimate how likely it is that a score of v
at depth d in the tree would be outside (α, β). Buro applied this technique to his Othello program, L OGISTELLO , and found that a version of his program with P ROB C UT beat the regular
version 64% of the time, even when the regular version was given twice as much time.
Combining all the techniques described here results in a program that can play creditable chess (or other games). Let us assume we have implemented an evaluation function for
chess, a reasonable cutoff test with a quiescence search, and a large transposition table. Let
us also assume that, after months of tedious bit-bashing, we can generate and evaluate around
a million nodes per second on the latest PC, allowing us to search roughly 200 million nodes
per move under standard time controls (three minutes per move). The branching factor for
chess is about 35, on average, and 355 is about 50 million, so if we used minimax search,
we could look ahead only about five plies. Though not incompetent, such a program can be
fooled easily by an average human chess player, who can occasionally plan six or eight plies
ahead. With alpha–beta search we get to about 10 plies, which results in an expert level of
play. Section 5.8 describes additional pruning techniques that can extend the effective search
depth to roughly 14 plies. To reach grandmaster status we would need an extensively tuned
evaluation function and a large database of optimal opening and endgame moves."""

sample4="""The next step is to modify A LPHA -B ETA -S EARCH so that it will call the heuristic E VAL
function when it is appropriate to cut off the search. We replace the two lines in Figure 5.7
that mention T ERMINAL-T EST with the following line:
if C UTOFF -T EST (state, depth) then return E VAL(state)
We also must arrange for some bookkeeping so that the current depth is incremented on each
recursive call. The most straightforward approach to controlling the amount of search is to set
a fixed depth limit so that C UTOFF -T EST (state, depth) returns true for all depth greater than
some fixed depth d. (It must also return true for all terminal states, just as T ERMINAL-T EST
did.) The depth d is chosen so that a move is selected within the allocated time. A more
robust approach is to apply iterative deepening. (See Chapter 3.) When time runs out, the
program returns the move selected by the deepest completed search. As a bonus, iterative
deepening also helps with move ordering."""

sample5="""This strategy prefers to do resolutions where one of the sentences is a single
literal (also known as a unit clause). The idea behind the strategy is that we are trying to
produce an empty clause, so it might be a good idea to prefer inferences that produce shorter
clauses. Resolving a unit sentence (such as P ) with any other sentence (such as ¬P ∨¬Q∨R)
always yields a clause (in this case, ¬Q ∨ R) that is shorter than the other clause. When
the unit preference strategy was first tried for propositional inference in 1964, it led to a
dramatic speedup, making it feasible to prove theorems that could not be handled without the
preference. Unit resolution is a restricted form of resolution in which every resolution step
must involve a unit clause. Unit resolution is incomplete in general, but complete for Horn
clauses. Unit resolution proofs on Horn clauses resemble forward chaining.
The OTTER theorem prover (Organized Techniques for Theorem-proving and Effective
Research, McCune, 1992), uses a form of best-first search. Its heuristic function measures
the “weight” of each clause, where lighter clauses are preferred. The exact choice of heuristic
is up to the user, but generally, the weight of a clause should be correlated with its size or
difficulty. Unit clauses are treated as light; the search can thus be seen as a generalization of
the unit preference strategy."""

mergeds = [sample1,sample2,sample3,sample4,sample5]