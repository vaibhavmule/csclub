from orator.migrations import Migration


class AddIsAdminToUsers(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('users') as table:
            table.integer('is_admin').nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('users') as table:
            pass
