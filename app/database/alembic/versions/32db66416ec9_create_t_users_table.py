"""create_t_users_table

Revision ID: 32db66416ec9
Revises: 
Create Date: 2024-01-24 13:37:54.282941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = '32db66416ec9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "t_users",
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("deleted_flag", sa.Boolean, default=False, nullable=False),
        sa.Column("created_at", sa.DateTime, default=datetime.now, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=True),
        sa.Column("deleted_at", sa.DateTime, nullable=True),
    )


def downgrade() -> None:
    op.drop_table("t_users")
