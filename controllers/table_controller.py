from models.table import Table
from repositories.table_repository import TableRepository


class TableController:

    def __init__(self):
        """
        This is the constructor of the TableController class
        """
        print("Table Controller ready")
        self.table_repository = TableRepository()

    #  Equivalent to 'all'
    def index(self) -> list:
        """
        This method returns all tables persisted in the db
        :return: table list
        """
        print("return all tables")
        return self.table_repository.find_all()

    # Equivalent to 'one by id'
    def show(self, id_: str) -> dict:
        """
        This method returns a table persisted in the db
        :param id_:
        :return: table
        """
        print("return one table")
        table = self.table_repository.find_by_id(id_)
        return table

    # Equivalent to 'insert'
    def create(self, table_: dict) -> dict:
        """
        This method return a table that was created in the db
        :param table_:
        :return: table
        """
        print("insert an table")
        table = Table(table_)
        table = self.table_repository.save(table)
        return table

    # Equivalent to 'update'
    def update(self, id_: str, table_: dict) -> dict:
        """
        This method return a table that was updated in the db
        :param id_:
        :param table_:
        :return:
        """
        print("update a student")
        table = Table(table_)
        table = self.table_repository.update(id_, table)
        return table

    # Equivalent to 'delete'
    def delete(self, id_: str) -> dict:
        """
        This method return delete count of a table that was deleted in the db
        :param id_:
        :return:
        """
        print("delete a table " + id_)
        return self.table_repository.delete(id_)
