from orator.migrations import Migration


class CreatePostsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('posts') as table:
            table.increments('id')
            table.string('title')
            table.string('slug')

            table.integer('author_id').unsigned()
            table.foreign('author_id').references('id').on('users')

            table.string('text')
            table.timestamp('published_date')
    
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('posts')
