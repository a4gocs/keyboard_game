# keyboard_game
simple console application

- have characters list maybe made from 
  - unmodified keys
  - shift keys
  - ~~altgr keys (empty)~~

 main menu:

  1. play if list not empty
  2. add unmod to list
  3. add shift to list
  4. add altgr to list - does nothing
  5. reset
  6. quit

play:
- loop while list not empty:
  - shuffle list 
  - ask for first char in list, 
  - if correct remove from list,
  - else if input is quit then exit
  - everything else incorrect, back to shuffle
