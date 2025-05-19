def sponge_case(sentence):
    result = []

    for word in sentence.split():
        new_word = ''
    
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].lower()
            else:
                new_word += word[i].upper()

        result.append(new_word)

    return ' '.join(result)

# Test cases
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")