from datetime import datetime
import os.path

class Session:
    def __init__(self, logpath):
        ft = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")
        self.logfile = open(os.path.join(logpath, ft), "w")
    def __enter__(self):
        print("[{t}] Session started".format(t=datetime.now()), file=self.logfile)
        return self
    def __exit__(self, exception_type, exception_value, traceback):
        print("[{t}] Session ended".format(t=datetime.now()), file=self.logfile)
        self.logfile.close()
    def write_to_log(self, text):
        print("[{t}] {text}".format(t=datetime.now(), text=text), file=self.logfile)

if __name__ == '__main__':
    with Session(logpath = "assets/log/") as session:
        session.write_to_log("smth")
