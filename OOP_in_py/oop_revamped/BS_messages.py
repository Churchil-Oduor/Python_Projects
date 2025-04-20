
class Msg:
    def __init__(self, names):
        self.names = names

    def messages(self):
        for person in names:
            print(f"Hello {person}😃...\n Hope you're good...My name is Churchil Okech your BS co-ordinator, for this semester...just wanted to say Hi and also to psyche you up for Todays BS.\n I wish you the best experience as you bond with your new family and hoping you grow together\n..In case of anything please feel free to reach out to me.\n\n")



names = ["Beryl", "Jane", "Terry", "Henry", "Maurine"]

msg = Msg(names)
msg.messages()
