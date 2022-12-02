from bson import ObjectId

from models.vote import Vote
from repositories.interface_repository import InterfaceRepository


class VoteRepository(InterfaceRepository[Vote]):
    def get_table_by_candidate(self, candidate_id):
        query = {"candidate.$id": ObjectId(candidate_id)}
        return self.query(query)
