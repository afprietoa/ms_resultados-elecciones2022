from models.candidate import Candidate
from models.political_party import PoliticalParty
from repositories.candidate_repository import CandidateRepository
from repositories.political_party_repository import PoliticalPartyRepository


class CandidateController:

    def __init__(self):
        """
        This is the constructor of the CandidateController class
        """
        print("Candidate Controller ready")
        self.candidate_repository = CandidateRepository()
        self.political_party_repository = PoliticalPartyRepository()

    def assign_political_party(self, candidate_id: str, political_party_id: str):
        """

        :param candidate_id:
        :param political_party_id:
        :return:
        """
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate = Candidate(candidate_dict)
        political_party_dict = self.political_party_repository.find_by_id(political_party_id)
        political_party = PoliticalParty(political_party_dict)
        candidate.political_party = political_party
        return self.candidate_repository.save(candidate)

    #  Equivalent to 'all'
    def index(self) -> list:
        """

        :return:
        """
        print("return all candidates")
        return self.candidate_repository.find_all()

    # Equivalent to 'one by id'
    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one candidate")
        candidate = self.candidate_repository.find_by_id(id_)
        return candidate

    # Equivalent to 'insert'
    def create(self, candidate_: dict) -> dict:
        """

        :param candidate_:
        :return:
        """
        print("insert an candidate")
        candidate = Candidate(candidate_)
        candidate = self.candidate_repository.save(candidate)
        return candidate

    # Equivalent to 'update'
    def update(self, id_: str, candidate_: dict) -> dict:
        """

        :param id_:
        :param candidate_:
        :return:
        """
        print("update an candidate")
        candidate = Candidate(candidate_)
        candidate = self.candidate_repository.update(id_, candidate)
        return candidate

    # Equivalent to 'delete'
    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete an candidate")
        return self.candidate_repository.delete(id_)
