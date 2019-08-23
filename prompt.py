def argtest(*args, **keywords):
    for arg in args:
        print(arg)

    for key in keywords:
        print(keywords['fourth'])

argtest("asdf", "second", "Third", fourth="Fourth")