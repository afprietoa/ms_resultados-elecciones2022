

from models.candidate import Candidate
from models.vote import Vote
from models.table import Table
from repositories.candidate_repository import  CandidateRepository
from repositories.vote_repository import VoteRepository
from repositories.table_repository import TableRepository


class VoteController:

    def __init__(self):
        """
        This is the constructor of the VoteController class
        """
        print("Vote Controller ready")
        self.vote_repository = VoteRepository()
        self.candidate_repository = CandidateRepository()
        self.table_repository = TableRepository()

    #  Equivalent to 'all'
    def index(self) -> list:
        """

        :return:
        """
        print("return all votes")
        return self.vote_repository.find_all()

    # Equivalent to 'one by id'
    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one vote")
        vote = self.vote_repository.find_by_id(id_)
        return vote

    # Equivalent to 'insert'
    def create(self, vote_: dict, table_id: str, candidate_id: str) -> dict:
        """

        :param candidate_id:
        :param table_id:
        :param vote_:
        :return:
        """
        print("insert an vote")
        vote = Vote(vote_)
        table_dict = self.table_repository.find_by_id(table_id)
        table_obj = Table(table_dict)
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)
        vote.table = table_obj
        vote.candidate = candidate_obj
        return self.vote_repository.save(vote)

    # Equivalent to 'update'
    def update(self, id_: str, vote_: dict) -> dict:
        """

        :param id_:
        :param vote_:
        :return:
        """
        print("update an vote")
        vote = Vote(vote_)
        vote = self.vote_repository.update(id_, vote)
        return vote

    # Equivalent to 'delete'
    def delete(self, id_):
        """

        :param id_:
        :return:
        """
        print("delete an vote")
        return self.vote_repository.delete(id_)

    def list_table_by_candidate(self, candidate_id):
        return self.vote_repository.get_table_by_candidate(candidate_id)
