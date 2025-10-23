def make_logger(prefix):
    def log(message):
        print(f"[{prefix}] {message}")
    return log

app = make_logger("App")
db = make_logger("Database")

app("Starting Caffe Bot!")
db("Connecting with the Database...")
app("Shutting Down...")