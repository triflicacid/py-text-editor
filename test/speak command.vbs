Dim message, sapi
message=InputBox("Enter speach","speak command")
Set sapi=CreateObject("sapi.spvoice")
sapi.Speak message