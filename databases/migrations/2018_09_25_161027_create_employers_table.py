from orator.migrations import Migration


class CreateEmployersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('employers') as table:
            table.increments('id')
            table.string('title', 150)
            table.string('slug', 150)
            table.string('website').nullable()
            table.string('logo').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('employers')
