def playback (s):
    s = s.replace(" ", "...")
    return s

input_str = input()
print(playback(input_str))