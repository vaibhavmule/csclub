from orator.migrations import Migration


class CreateEmploymentTypesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('employment_types') as table:
            table.increments('id')
            table.string('title', 100)
            table.string('value', 50)
            table.string('slug')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('employment_types')
