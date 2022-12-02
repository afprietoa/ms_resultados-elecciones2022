from flask import Blueprint
from flask import request
from controllers.candidate_controller import CandidateController

candidate_blueprints = Blueprint('candidate_blueprints', __name__)
candidate_controller = CandidateController()


@candidate_blueprints.route("/candidate/all", methods=['GET'])
def get_candidates():
    response = candidate_controller.index()
    return response, 200


@candidate_blueprints.route("/candidate/<string:id_>", methods=['GET'])
def get_candidate_by_id(id_):
    response = candidate_controller.show(id_)
    return response, 200


@candidate_blueprints.route("/candidate/insert", methods=['POST'])
def insert_candidate():
    candidate = request.get_json()
    response = candidate_controller.create(candidate)
    return response, 201


@candidate_blueprints.route("/candidate/update/<string:id_>", methods=['PATCH'])
def update_candidate(id_):
    candidate = request.get_json()
    response = candidate_controller.update(id_, candidate)
    return response, 201


@candidate_blueprints.route('/candidate/<string:id_>/political_party/<string:political_party_id>', methods=['PUT'])
def update_political_party_ref(id_, political_party_id):
    response = candidate_controller.assign_political_party(id_, political_party_id)
    return response, 201


@candidate_blueprints.route("/candidate/delete/<string:id_>", methods=['DELETE'])
def delete_candidate(id_):
    response = candidate_controller.delete(id_)
    return response, 204