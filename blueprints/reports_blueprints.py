from flask import Blueprint
from controllers.reports_controller import ReportsController

reports_blueprints = Blueprint('reports_blueprints', __name__)
reports_controller = ReportsController()


@reports_blueprints.route("/reports/table_votes/all", methods=['GET'])
def report_table_votes():
    response = reports_controller.report_table_votes()
    return response, 200


@reports_blueprints.route("/reports/candidate_votes/all", methods=['GET'])
def report_candidate_votes():
    response = reports_controller.report_candidate_votes()
    return response, 200


@reports_blueprints.route("/reports/party_votes/all", methods=['GET'])
def report_political_party_enrollments():
    response = reports_controller.report_political_party_votes()
    return response, 200


@reports_blueprints.route("/reports/general_distribution", methods=['GET'])
def report_political_party_distribution():
    response = reports_controller.report_political_party_distribution()
    return response, 200