"""Initial migration

Revision ID: 21b694fbc2f7
Revises: 
Create Date: 2024-08-10 17:59:00.011253

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '21b694fbc2f7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_jogadores_id', table_name='jogadores')
    op.drop_index('ix_jogadores_nome', table_name='jogadores')
    op.drop_index('ix_jogadores_token', table_name='jogadores')
    op.drop_table('jogadores')
    op.drop_table('baralho_cartas')
    op.drop_index('ix_personagens_id', table_name='personagens')
    op.drop_table('personagens')
    op.drop_index('ix_habilidades_id', table_name='habilidades')
    op.drop_index('ix_habilidades_nome', table_name='habilidades')
    op.drop_table('habilidades')
    op.drop_index('ix_cartas_foto', table_name='cartas')
    op.drop_index('ix_cartas_id', table_name='cartas')
    op.drop_table('cartas')
    op.drop_index('ix_baralhos_id', table_name='baralhos')
    op.drop_index('ix_baralhos_nome', table_name='baralhos')
    op.drop_table('baralhos')
    op.drop_index('ix_personagem_modelos_foto', table_name='personagem_modelos')
    op.drop_index('ix_personagem_modelos_id', table_name='personagem_modelos')
    op.drop_index('ix_personagem_modelos_nome', table_name='personagem_modelos')
    op.drop_table('personagem_modelos')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personagem_modelos',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nome', sa.VARCHAR(), nullable=True),
    sa.Column('foto', sa.VARCHAR(), nullable=True),
    sa.Column('descricao', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_personagem_modelos_nome', 'personagem_modelos', ['nome'], unique=False)
    op.create_index('ix_personagem_modelos_id', 'personagem_modelos', ['id'], unique=False)
    op.create_index('ix_personagem_modelos_foto', 'personagem_modelos', ['foto'], unique=False)
    op.create_table('baralhos',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nome', sa.VARCHAR(), nullable=True),
    sa.Column('descricao', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_baralhos_nome', 'baralhos', ['nome'], unique=False)
    op.create_index('ix_baralhos_id', 'baralhos', ['id'], unique=False)
    op.create_table('cartas',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('foto', sa.VARCHAR(), nullable=True),
    sa.Column('tipo', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_cartas_id', 'cartas', ['id'], unique=False)
    op.create_index('ix_cartas_foto', 'cartas', ['foto'], unique=False)
    op.create_table('habilidades',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nome', sa.VARCHAR(), nullable=True),
    sa.Column('descricao', sa.VARCHAR(), nullable=True),
    sa.Column('nivel', sa.INTEGER(), nullable=True),
    sa.Column('personagem_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['personagem_id'], ['personagens.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_habilidades_nome', 'habilidades', ['nome'], unique=False)
    op.create_index('ix_habilidades_id', 'habilidades', ['id'], unique=False)
    op.create_table('personagens',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('pontos_de_vida', sa.INTEGER(), nullable=True),
    sa.Column('nivel', sa.INTEGER(), nullable=True),
    sa.Column('pontos_de_experiencia', sa.INTEGER(), nullable=True),
    sa.Column('jogador_id', sa.INTEGER(), nullable=True),
    sa.Column('modelo_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['jogador_id'], ['jogadores.id'], ),
    sa.ForeignKeyConstraint(['modelo_id'], ['personagem_modelos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_personagens_id', 'personagens', ['id'], unique=False)
    op.create_table('baralho_cartas',
    sa.Column('baralho_id', sa.INTEGER(), nullable=False),
    sa.Column('carta_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['baralho_id'], ['baralhos.id'], ),
    sa.ForeignKeyConstraint(['carta_id'], ['cartas.id'], ),
    sa.PrimaryKeyConstraint('baralho_id', 'carta_id')
    )
    op.create_table('jogadores',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nome', sa.VARCHAR(), nullable=True),
    sa.Column('token', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_jogadores_token', 'jogadores', ['token'], unique=1)
    op.create_index('ix_jogadores_nome', 'jogadores', ['nome'], unique=False)
    op.create_index('ix_jogadores_id', 'jogadores', ['id'], unique=False)
    # ### end Alembic commands ###
