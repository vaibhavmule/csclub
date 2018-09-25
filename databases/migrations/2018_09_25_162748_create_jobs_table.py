from orator.migrations import Migration


class CreateJobsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('jobs') as table:
            table.increments('id')
            table.string('title', 50)
            table.string('slug')
            table.timestamp('date_posted')
            table.long_text('description')
            table.string('location')
            table.datetime('expiry_date')
            table.decimal('salary', 7, 2)
            table.enum('salary_unit', ['Month', 'Year']).nullable()
            table.string('apply_link').nullable()
            table.string('apply_email').nullable()

            table.integer('employer_id').unassined()
            table.foreign('employer_id').references('id').on('employers')

            table.integer('employment_type_id').unassined()
            table.foreign('employment_type_id').references('id').on('employment_types')

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('jobs')