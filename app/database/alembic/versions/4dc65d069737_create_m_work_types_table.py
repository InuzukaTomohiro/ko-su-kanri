"""create_m_work_types_table

Revision ID: 4dc65d069737
Revises: 26ebd28674f3
Create Date: 2024-01-24 13:41:04.904806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0278be52a9f5'
down_revision: Union[str, None] = '32db66416ec9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "m_work_types",
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("work_type", sa.String(255), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("m_work_types")
