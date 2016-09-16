def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any", kind, "?")
    print("--I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-"*40)
    keys = sorted(keywords.keys())
    for kw in keys:
            print(kw, ":", keywords[kw])
"""cheeseshop('limburger', 'it is very runny, sir',
            "it is reall",
            shopkeeper = "NM",
            client = "wm",
            sketch = "fdf")"""
d = {"kind":"limburger", "arguments" : ["it is very runny, sir", "it is really"]}
cheeseshop(d,*d,shopkeeper = "NM",
client = "wm",
sketch = "fdf")
