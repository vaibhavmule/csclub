from orator.migrations import Migration


class CreateRedirectsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('redirects') as table:
            table.increments('id')
            table.string('old_path')
            table.string('new_path')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('redirects')
