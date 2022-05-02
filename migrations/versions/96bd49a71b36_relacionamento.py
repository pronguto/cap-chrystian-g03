"""relacionamento

Revision ID: 96bd49a71b36
Revises: 3d88ba222821
Create Date: 2022-04-28 15:38:33.238060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96bd49a71b36'
down_revision = '3d88ba222821'
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