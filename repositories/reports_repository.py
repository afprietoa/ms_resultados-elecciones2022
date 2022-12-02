from bson import ObjectId
from models.vote import Vote
from repositories.interface_repository import InterfaceRepository


class ReportsRepository(InterfaceRepository[Vote]):

    def get_table_votes(self) -> list:
        """
        :param limit:
        :param id_:
        :return:
        """
        # Equivalent to make a INNER JOIN
        query_lookup = {
            '$lookup': {
                'from': 'table',
                'localField': 'table.$id',
                'foreignField': '_id',
                'as': '_table'
            }
        }
        query_unwind = {
            "$unwind": "$_table"
        }
        # Equivalent to GROUP BY
        query_group = {
            '$group': {
                '_id': '$_table',
                'votes': {
                    '$sum': 1
                }
            }
        }
        # Clean the response, using equivalent to ALIAS and ORDER BY
        query_add_fields = {
            '$addFields': {
                'table': '$_id.number',
                '_id': '$_id._id'
            }
        }
        query_sort = {
            "$sort": {
                "votes": -1
            }
        }

        pipeline = [query_lookup,
                    query_unwind,
                    query_group,
                    query_add_fields,
                    query_sort]
        return self.query_aggregation(pipeline)

    def get_candidate_votes(self) -> list:
        """
        :param id_:
        :return:
        """
        # Equivalent to make a INNER JOIN
        query_lookup = {
            '$lookup': {
                'from': 'candidate',
                'localField': 'candidate.$id',
                'foreignField': '_id',
                'as': '_candidate'
            }
        }
        query_unwind = {
            "$unwind": "$_candidate"
        }
        # Equivalent to GROUP BY
        query_group = {
            '$group': {
                '_id': '$_candidate',
                'votes': {
                    '$sum': 1
                }
            }
        }
        # Clean the response, using equivalent to ALIAS and ORDER BY DESC
        query_add_fields = {
            '$addFields': {
                'name': '$_id.name',
                'document': '$_id.personal_id',
                '_id': '$_id._id'
            }
        }
        query_sort = {
            "$sort": {
                "votes": -1
            }
        }
        pipeline = [query_lookup,
                    query_unwind,
                    query_group,
                    query_add_fields,
                    query_sort]
        return self.query_aggregation(pipeline)

    def get_political_party_votes(self) -> list:
        """
        :return:
        """
        # Equivalent to make an INNER JOIN courses
        query_preprocess_candidates = {
            '$lookup': {
                'from': 'candidate',
                'localField': 'candidate.$id',
                'foreignField': '_id',
                'as': '_candidate'
            }
        }
        query_unwind_candidates = {
            "$unwind": "$_candidate"
        }
        # Equivalent to make a GROUP BY courses
        query_group_candidates = {
            '$group': {
                '_id': '$_candidate',
                'count': {
                    '$sum': 1
                }
            }
        }
        query_add_fields_political_parties = {
            "$addFields": {
                'party': '$_id.political_party'
            }
        }
        # Equivalent to make an INNER JOIN departments
        query_process_political_parties = {
            '$lookup': {
                'from': 'politicalparty',
                'localField': 'party.$id',
                'foreignField': '_id',
                'as': '_party'
            }

        }
        query_unwind_political_parties = {
            "$unwind": "$_party"
        }
        # Equivalent to make GROUP BY and ORDER BY departments
        query_group_political_parties = {
            '$group': {
                '_id': '$_party',
                'votes': {
                    '$sum': '$count'
                }
            }
        }
        query_add_fields = {
            '$addFields': {
                'name': '$_id.name',
                '_id': '$_id._id'
            }
        }
        pipeline = [query_preprocess_candidates,
                    query_unwind_candidates,
                    query_group_candidates,
                    query_add_fields_political_parties,
                    query_process_political_parties,
                    query_unwind_political_parties,
                    query_group_political_parties,
                    query_add_fields]
        return self.query_aggregation(pipeline)

    def get_political_party_distribution(self) -> list:
        """
        :return:
        """
        winners = 15
        # Equivalent to make an INNER JOIN courses
        query_preprocess_candidates = {
            '$lookup': {
                'from': 'candidate',
                'localField': 'candidate.$id',
                'foreignField': '_id',
                'as': '_candidate'
            }
        }
        query_unwind_candidates = {
            "$unwind": "$_candidate"
        }
        # Equivalent to make a GROUP BY courses
        query_group_candidates = {
            '$group': {
                '_id': '$_candidate',
                'count': {
                    '$sum': 1
                }
            }
        }
        query_sort = {
            "$sort": {
                "votes": -1
            }
        }
        query_add_fields_political_parties = {
            "$addFields": {
                'party': '$_id.political_party'
            }
        }
        # Equivalent to make an INNER JOIN departments
        query_process_political_parties = {
            '$lookup': {
                'from': 'politicalparty',
                'localField': 'party.$id',
                'foreignField': '_id',
                'as': '_party'
            }
        }
        query_unwind_political_parties = {
            "$unwind": "$_party"
        }
        # Equivalent to make GROUP BY and ORDER BY departments
        query_group_political_parties = {
            '$group': {
                '_id': None,
                'total': {
                    '$sum': '$count'
                },
                'data': {
                    '$push': '$$ROOT'
                }
            }
        }
        query_unwind_data = {
            "$unwind": "$data"
        }
        query_project_data = {
            '$project': {
                'name': '$data._party.name',
                '_id': '$data._id._id',
                'percentage': {
                    '$multiply': [
                        100, {
                            '$divide': [
                                '$data.count', {
                                    '$sum': '$total'
                                }
                            ]
                        }
                    ]
                }
            }
        }
        pipeline = [query_preprocess_candidates,
                    query_unwind_candidates,
                    query_group_candidates,
                    query_sort,
                    query_add_fields_political_parties,
                    query_process_political_parties,
                    query_unwind_political_parties,
                    query_group_political_parties,
                    query_unwind_data,
                    query_project_data]
        return self.query_aggregation(pipeline)




