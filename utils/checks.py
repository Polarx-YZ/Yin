def authorized_user(ctx):
    whitelist = [
        332300933327355905, # Rin
        478266960505995274, # Mudai
        821371512187387914, # Alam
        1088149438540812448, # Asahi
        706410897429495819, # Yoshi
        820354251640799343, # Yaru
        ]
    if ctx.author.id in whitelist:
        return True
    return False
