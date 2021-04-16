import twint
import pandas as pd

#Used twint to collect data
c = twint.Config()

#collecting only mentions and username, not the tweet itself.
c.Username = "username"
c.Custom["tweet"] = ["username",'tweet']

#storing the output in a csv file
c.Store_csv = True
c.Output = 'username.csv'
c.Since = '2020-01-01'

twint.run.Search(c)