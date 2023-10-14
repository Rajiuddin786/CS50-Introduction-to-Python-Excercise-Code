play=input()
playback=""
for i in play:
    if i == " ":
        playback+="..."
    else:
        playback+=i

print(playback)