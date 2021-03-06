"""relacionamento

Revision ID: 2f5c4686c8d1
Revises: 96bd49a71b36
Create Date: 2022-04-28 15:39:42.458783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f5c4686c8d1'
down_revision = '96bd49a71b36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ingredients_purchase', 'purchase_quantity',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=False)
    op.alter_column('production_recipes', 'recipe_quantity',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=False)
    op.alter_column('recipe_ingredients', 'quantity',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('recipe_ingredients', 'quantity',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=False)
    op.alter_column('production_recipes', 'recipe_quantity',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=False)
    op.alter_column('ingredients_purchase', 'purchase_quantity',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=False)
    # ### end Alembic commands ###
