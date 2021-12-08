"""CreateMealsTable Migration."""

from masoniteorm.migrations import Migration


class CreateMealsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("meals") as table:
            table.increments("id")
            table.string("days")
            table.string("subject")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("meals")
