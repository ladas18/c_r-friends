from cr_friends import app
from cr_friends.config import routes
app.secret_key = "venom"



if __name__=="__main__":
    app.run(debug=True)
