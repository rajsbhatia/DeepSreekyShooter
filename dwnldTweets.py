import twint

# configure
c = twint.Config()
c.Username = "sreekyshooter"
c.Store_json = True
c.Profile_full = True # in case of shadow ban

twint.run.Search(c)

# if __name__ == "__main__":
# 	twint.run.Search(c)
