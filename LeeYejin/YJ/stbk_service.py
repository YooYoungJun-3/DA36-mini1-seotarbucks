from stbk_repository import StarBucks_Repository

class StarBucks_Service:
    def __init__(self):
        self.stbk_repository = StarBucks_Repository()
    def find_all(self):
        return self.stbk_repository.find_all()
    def push(self, stbks):
        return self.stbk_repository.push(stbks)

    def coffee_menu(self):
        return self.stbk_repository.coffee_menu()

    def blended_menu(self):
        return self.stbk_repository.blended_menu()

    def noncoffee_menu(self):
        return self.stbk_repository.noncoffee_menu()