import IB


# Instagram
username = "Твій логін"
password = "Твій пароль"
follower = ['explore/people/suggested']

ig = IB.InstagramBot(username, password, *follower)
ig.login()
ig.unsubscribe()










