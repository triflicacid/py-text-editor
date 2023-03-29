favColor = InputBox("What is your favorite color?", "Favorite color")
	
  if favColor = "" then
  MsgBox "You did not specify your favorite color!",0+16,"ERROR!"

  else
  MsgBox "Your favorite color is " & favColor,0+64,"Fav Colour"
	
  end if

