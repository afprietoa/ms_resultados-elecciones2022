from repositories.reports_repository import ReportsRepository


class ReportsController:

    def __init__(self):
        self.report_repository = ReportsRepository()

        # Equivalent to: count votes per tables
    def report_table_votes(self) -> list:
        """
        :param id_:
        :return:
        """
        return self.report_repository.get_table_votes()

    # Equivalent to: count votes per candidate
    def report_candidate_votes(self) -> list:
        """
        :param id_:
        :return:
        """
        return self.report_repository.get_candidate_votes()

    # Equivalent to: count votes per political party
    def report_political_party_votes(self) -> list:
        """
        :return:
        """
        return self.report_repository.get_political_party_votes()

    # Equivalent to: percentual distribution of political party winners
    def report_political_party_distribution(self) -> list:
        """
        :return:
        """
        return self.report_repository.get_political_party_distribution()