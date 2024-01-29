"""create_t_work_records_table

Revision ID: 583418c86774
Revises: 32db66416ec9
Create Date: 2024-01-24 13:38:52.935341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = '4dc65d069737'
down_revision: Union[str, None] = '26ebd28674f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "t_work_records",
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("user_id", sa.BigInteger, sa.ForeignKey("t_users.id"), nullable=False),
        sa.Column("work_type", sa.BigInteger, sa.ForeignKey("m_work_types.id"), nullable=True),
        sa.Column("user_work_type", sa.BigInteger, sa.ForeignKey("t_user_work_types.id"), nullable=True),
        sa.Column("work_name", sa.String(255), nullable=False),
        sa.Column("work_description", sa.Text(), nullable=True),
        sa.Column("started_at", sa.DateTime, default=datetime.now, nullable=False),
        sa.Column("finished_at", sa.DateTime, nullable=True),
        sa.Column("deleted_flag", sa.Boolean, default=False, nullable=False),
        sa.Column("created_at", sa.DateTime, default=datetime.now, nullable=False),
        sa.Column("updated_at", sa.DateTime, default=datetime.now, nullable=False),
        sa.Column("deleted_at", sa.DateTime, nullable=True)
    )


def downgrade() -> None:
    pass
