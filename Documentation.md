## Variables
- A: *Reserved as a cache variable to store various values*
- B: Beginning of current chunk
- C: Chunk limit X
- D: Chunk limit Y
- E: *Cache 1 (item type)*
- F: *Cache 2 (item count)*
- G: *Cache for needed item in the current mission/story*
- H: Player height level limit
- I: *Reserved for loops*
- J: *Reserved for loops*
- K: Currently pressed key
- L: *Reserved for calculating list positions*
- M: *Reserved for current tile in list for rendering*
- N: *Reserved for current NPC x position to render later on* **to be removed**
- O: *Reserved for current NPC y position to render later on* **to be removed**
- P: Position of player in the (floor) list
- Q: Boolean if player is currently rendering / has to be
- R: Boolean if world is currently rendering / has to be
- S: *Reserved for coming story, see interpretation below*
- T: Current tile
- U: Water state for animation
- V: Previous player X position
- W: Previous player Y position
- X: Player X position
- Y: Player Y position
- Z: Player height level

## Lists
- 1: Floor 1 (Z=1)
- 2: Floor 2
- 3: Floor 3
- 4: Floor 4
- 5: NPC positions
- 6: Story progess (0=not started, 1=active, 2=finished)
- 7: Inventory (two values representing the item type and the count of it, {Type,Count})
- 8: *Reserved*
- 9: *Reserved*

## Strings
- 1-7: World-rendering (lines 1-7)
- 8: Temporary line of world for faster rendering
- 10: Current NPC conversation text

## Misc
### Tiles
- 0: Air
- 1..: Blocks
- 90..: Water
- 100: NPC
- 201..: *see items below*

### Items
- 1: Cake
- 2: Sword

### Variable interpretation
#### S:
Represents the current id of the NPC we're talking to. It goes through the NPC list (List 5)

### List interpretation
#### List 5
Every odd value is the X-position of an NPC, every even position stands for each Y-position.

### TODO / Notes / Comments
- Use MOD() only when really needed to. This operation is very slow!
- Create fluids. Maybe create a new list for fluids and generate a string for each "fluid block" in the position list and then Locate xy each string for efficiency (and a smooth animation)
- Make the text in the conversation scrollable to allow texts > len 45 (9*5) maybe make the bottom open when the user can scroll
- \[check\] Render NPCs (go through the whole List 5 so it doesn't need to be sorted by chunks)
- \[check\]I can reuse the code for getting the NPC id for the inventory because it's based on the same system
- \[check\]Make items collectable (I think somewhere after the player moves when checking T=100 for the NPC)

=       =
~~      _#E6B1_
~       _#E6B5_
===     _#E6B2_
~==     _#E6B4_

'ProgramMode:RUN
"=_#E6B1__#E6B5__#E6B2__#E6B4_"->Str 1
"   _#E6C4_"->Str 2
" ___#E6D7___"->Str 3
"_#E699_  _#E6D7_  _#E696_"->Str 4
"| _#E6B1__#E6D7__#E6B1_ |"->Str 5
"| _#E6B1__#E6B1__#E6B1_ |"->Str 6
"_#E698_______#E697_"->Str 7
