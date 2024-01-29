"""create_t_user_work_types_table

Revision ID: 26ebd28674f3
Revises: 0278be52a9f5
Create Date: 2024-01-24 13:40:57.712923

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = '26ebd28674f3'
down_revision: Union[str, None] = '0278be52a9f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "t_user_work_types",
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("user_id", sa.BigInteger, sa.ForeignKey("t_users.id"), nullable=False),
        sa.Column("work_type_name", sa.String(255), nullable=False),
        sa.Column("deleted_flag", sa.Boolean, default=False, nullable=False),
        sa.Column("created_at", sa.DateTime, default=datetime.now, nullable=False),
        sa.Column("updated_at", sa.DateTime, default=datetime.now, nullable=False),
        sa.Column("deleted_at", sa.DateTime, nullable=True),
    )


def downgrade() -> None:
    op.drop_table("t_user_work_types")
