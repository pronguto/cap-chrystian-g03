"""tabelas1 ok

Revision ID: ee6b2d7e08bb
Revises: 8682508b39b2
Create Date: 2022-04-21 18:56:03.220466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee6b2d7e08bb'
down_revision = '8682508b39b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredients',
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_name', sa.String(), nullable=False),
    sa.Column('measurement_unit', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('ingredient_id'),
    sa.UniqueConstraint('ingredient_name')
    )
    op.create_table('productions',
    sa.Column('production_id', sa.Integer(), nullable=False),
    sa.Column('production_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('production_id')
    )
    op.create_table('purchases',
    sa.Column('purchase_id', sa.Integer(), nullable=False),
    sa.Column('purchase_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('purchase_id')
    )
    op.create_table('recipes',
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('recipe_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('recipe_id'),
    sa.UniqueConstraint('recipe_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipes')
    op.drop_table('purchases')
    op.drop_table('productions')
    op.drop_table('ingredients')
    # ### end Alembic commands ###
