## Variables:
A:
B:
C: Current chunk X
D: Current chunk Y
E: Maximum chunk X (constant)
F: Maximum chunk Y (constant)
G: *Reserved*
H: Player height level limit
I: *Reserved*
J: *Reserved*
K: Currently pressed key
L: *Reserved*
M: *Reserved*
N:
O:
P:
Q: Boolean if player is currently rendering / has to be
R: Boolean if world is currently rendering / has to be
S:
T:
U:
V: Previous player X position
W: Previous player Y position
X: Player X position
Y: Player Y position
Z: Player height level

## Lists:
1: Floor 1 (Z=1)
2: Floor 2
3: Floor 3
4: Floor 4
5: *Reserved*
6: *Reserved*
7: *Reserved*
8: Map assignment (rectangular world, see int values below)
9: *Reserved*
**9: Assigned numbers to tiles (i.e. No. 0 = Char / Tile 5)**

## Misc:
### Map assignment:
0: Empty chunk
1: Used chunk
2: End of current row (X)
3: End of map (column or Y)
