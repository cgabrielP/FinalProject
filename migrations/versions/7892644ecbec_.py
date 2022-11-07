"""empty message

Revision ID: 7892644ecbec
Revises: 
Create Date: 2022-11-07 18:03:17.627716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7892644ecbec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articulo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('precio', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=200), nullable=False),
    sa.Column('imagen', sa.String(length=200), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('fecha_publicacion', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('apellido', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('tipo', sa.String(length=120), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('cotizaciones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('direccion', sa.String(length=300), nullable=False),
    sa.Column('region', sa.String(length=50), nullable=False),
    sa.Column('telefono', sa.String(length=120), nullable=False),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pedidos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('estatus', sa.Integer(), nullable=False),
    sa.Column('fecha_pedido', sa.DateTime(), nullable=False),
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pedidos')
    op.drop_table('cotizaciones')
    op.drop_table('users')
    op.drop_table('articulo')
    # ### end Alembic commands ###
