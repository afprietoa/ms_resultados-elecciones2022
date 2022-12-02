from models.political_party import PoliticalParty
from repositories.political_party_repository import PoliticalPartyRepository


class PoliticalPartyController:

    def __init__(self):
        """
        This is the constructor of the PoliticalPartyController class
        """
        print("Political Party Controller ready")
        self.political_party_repository = PoliticalPartyRepository()

    #  Equivalent to 'all'
    def index(self) -> list:
        """

        :return:
        """
        print("return all political parties")
        return self.political_party_repository.find_all()

    # Equivalent to 'one by id'
    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one political party")
        political_party = self.political_party_repository.find_by_id(id_)
        return political_party

    # Equivalent to 'insert'
    def create(self, political_party_: dict) -> dict:
        """

        :param political_party_:
        :return:
        """
        print("insert an political party")
        political_party = PoliticalParty(political_party_)
        political_party = self.political_party_repository.save(political_party)
        return political_party

    # Equivalent to 'update'
    def update(self, id_: str, political_party_: dict) -> dict:
        """

        :param id_:
        :param political_party_:
        :return:
        """
        print("update an political party")
        political_party = PoliticalParty(political_party_)
        political_party = self.political_party_repository.update(id_, political_party)
        return political_party

    # Equivalent to 'delete'
    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete an political party")
        return self.political_party_repository.delete(id_)
