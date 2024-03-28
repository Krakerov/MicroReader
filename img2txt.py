class RefCycleExample:
    def __init__(self):
        self.myself = self

    def __del__(self):
        print("deleting")

obj = RefCycleExample()
del obj